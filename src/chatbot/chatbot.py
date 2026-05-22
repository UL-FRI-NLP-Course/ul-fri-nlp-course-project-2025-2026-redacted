import re
import argparse

import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer

from rag import RAGRetriever

SYSTEM_PROMPT = """You are a helpful tech assistant. You provide general \
computer information, specialized in providing help with choosing a processor/CPU or graphics card/GPU \
using context retrieved from various online reviews both of specific products and general articles.

GUIDELINES:
PRIORITIZE the provided context. If the context does not contain relevant \
information, say so honestly — do not invent processors of graphics cards or speculate beyond what the \
sources say. Do not mention the context explicitly, simply say that you do not have the \
required information or knowledge to answer the question."""

REWRITE_PROMPT = """Given the conversation history, if present, and a new user question, rewrite the question \
into a standalone search query that captures everything needed to find relevant info about what the user is looking for. \
Only output the rewritten query, nothing else. If the user changes topics, prioritize that information, rather than the history.

Conversation history:
{history}

New question: {question}

Standalone search query:"""


def load_llm(model_name: str):
    print(f"Loading LLM: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="cuda",
    )
    model.eval()
    return model, tokenizer


def generate(model, tokenizer, messages, max_new_tokens=512, temperature=0.7):
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    sample = temperature > 0
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=sample,
            temperature=temperature if sample else None,
            pad_token_id=tokenizer.eos_token_id,
        )

    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def rewrite_query(prompt, model, tokenizer, question: str, history: list) -> str:
    history_text = "\n".join(f"{m['role']}: {m['content']}" for m in history)
    rewrite_input = prompt.format(history=history_text, question=question)
    messages = [{"role": "user", "content": rewrite_input}]
    rewritten = generate(model, tokenizer, messages, max_new_tokens=100, temperature=0.0)
    return rewritten or question


def build_messages(system_prompt: str, history: list, context: str, question: str):
    user_turn = f"""Use the following context to answer the question. Remember to cite \
sources inline as "Source N" when you use information from them. If the context is completely \
irrelevant to the question, ignore it and tell the user politely that you cannot help them with \
their query and explain what you're designed to answer. 

Context:
{context}

Question: {question}"""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_turn})
    return messages


def rag_lookup(search_query, retriever, top_k, show_sources):
    results = retriever.retrieve(search_query, k=top_k, min_score=0.500)

    if show_sources:
        print(f"\n['{retriever.id}' search query: {search_query}]")
        for i, r in enumerate(results, 1):
            print(f"  retrieved [{i}] {r['source']} (score={r['score']:.3f})")

    if not results:
        return "No relevant context found."
    else:
        parts = []
        for i, r in enumerate(results, 1):
            parts.append(f"- {r['text']}")
        return "\n\n".join(parts)


def route_query(rag_model, rag_retrievers, user_query: str, threshold: float = 0.3) -> list[RAGRetriever]:
    query_emb = rag_model.encode(user_query)

    scores = {}
    for key, retriever in rag_retrievers.items():
        # Cosine similarity
        score = np.dot(query_emb, retriever.keywords) / (
                np.linalg.norm(query_emb) * np.linalg.norm(retriever.keywords)
        )
        scores[key] = score
        print(f"Routing score for '{key}': {score}")

    # Return indexes above threshold, or just the top-1 if none pass
    selected = [rag_retrievers[k] for k, s in scores.items() if s >= threshold]
    return selected if selected else [rag_retrievers[max(scores, key=scores.get)]]


def chat_loop(model, tokenizer, rag_model, rag_retrievers, top_k=4, max_history_turns=6, show_sources=False):
    history = []

    print("\nMedical info chatbot ready.")
    print("This bot provides general information, not medical advice.")
    print("Type 'quit' to exit, 'reset' to clear history.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not question:
            continue
        if question.lower() in {"quit", "exit"}:
            break
        if question.lower() == "reset":
            history = []
            print("[history cleared]\n")
            continue

        search_query = rewrite_query(REWRITE_PROMPT, model, tokenizer, question, history)
        rags = route_query(rag_model, rag_retrievers, search_query, 0.4)
        context = ""
        for rag in rags:
            context += "\n"
            context += rag_lookup(search_query, rag, top_k, show_sources)

        # answer
        messages = build_messages(SYSTEM_PROMPT, history, context, question)
        response = generate(model, tokenizer, messages)

        print(f"\nBot: {response}\n")

        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": response})

        if len(history) > max_history_turns * 2:
            history = history[-max_history_turns * 2:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--index-dir", default="./rag_index")
    parser.add_argument("--model", default="mistralai/Mistral-7B-Instruct-v0.3")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--show-sources", action="store_true", default=True, help="Print retrieved chunks (debug)")

    args = parser.parse_args()

    model, tokenizer = load_llm(args.model)
    rag_model = SentenceTransformer("all-MiniLM-L6-v2")
    rag_retrievers = {
        "cpu": RAGRetriever("cpu", "rag_index/cpu",
                            rag_model.encode("processor CPU cores threads clock speed compute tasks gaming workloads")),
        "gpu": RAGRetriever("gpu", "rag_index/gpu",
                            rag_model.encode("graphics card GPU gaming performance VRAM ray tracing rendering frames")),
    }
    chat_loop(model, tokenizer, rag_model, rag_retrievers, top_k=args.top_k, show_sources=args.show_sources)


if __name__ == "__main__":
    main()
