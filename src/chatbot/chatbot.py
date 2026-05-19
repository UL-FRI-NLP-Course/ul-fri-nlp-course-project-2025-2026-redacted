import re
import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from rag import RAGRetriever

SYSTEM_PROMPT = """You are a helpful medical information assistant. You provide general \
health information drawn from context retrieved from trusted medical sources (such as \
the CDC, NIH, and MedlinePlus). You are NOT a doctor, and you do not diagnose conditions.

GUIDELINES:
1. Answer using ONLY the provided context. If the context does not contain relevant \
information, say so honestly — do not invent medical facts or speculate beyond what the \
sources say. Do not mention the context explicitly, simply say that you do not have the \
required information or knowledge to answer the question. 
2. CITE YOUR SOURCES INLINE. When you use information from the context, reference it as \
"Source 1", "Source 2", etc., matching the numbers in the provided context. Only cite \
sources you actually used.
3. RECOMMEND PROFESSIONAL CARE for anything serious: severe, persistent, or worsening \
symptoms; potential emergencies (chest pain, difficulty breathing, severe bleeding, signs \
of stroke); pregnancy-related concerns; mental health crises; questions about specific \
medications, dosages, or treatment plans. For emergencies, advise calling local emergency \
services or going to the nearest emergency department.
4. DO NOT DIAGNOSE. You may describe what a condition involves, but never tell a user \
they have it. Use phrasing like "this could be consistent with..." or "a healthcare \
provider can determine...".
5. Be empathetic and clear. Acknowledge the user's concern, share the relevant \
information, and point them toward appropriate care.

If a user describes symptoms that could indicate an emergency, lead your response with \
the recommendation to seek immediate medical care before anything else."""

SYSTEM_PROMPT_NO_RAG = """You are a helpful medical information assistant. You provide general \
health information from trusted medical sources (such as \
the CDC, NIH, and MedlinePlus). You are NOT a doctor, and you do not diagnose conditions.

GUIDELINES:
1. RECOMMEND PROFESSIONAL CARE for anything serious: severe, persistent, or worsening \
symptoms; potential emergencies (chest pain, difficulty breathing, severe bleeding, signs \
of stroke); pregnancy-related concerns; mental health crises; questions about specific \
medications, dosages, or treatment plans. For emergencies, advise calling local emergency \
services or going to the nearest emergency department.
2. DO NOT DIAGNOSE. You may describe what a condition involves, but never tell a user \
they have it. Use phrasing like "this could be consistent with..." or "a healthcare \
provider can determine...".
3. Be empathetic and clear. Acknowledge the user's concern, share the relevant \
information, and point them toward appropriate care.

If a user describes symptoms that could indicate an emergency, lead your response with \
the recommendation to seek immediate medical care before anything else."""

REWRITE_PROMPT = """Given the conversation history and a new user question, rewrite the question \
into a standalone search query that captures everything needed to find relevant info. \
Only output the rewritten query, nothing else. If the user changes topics, prioritize that \
information, rather than the history.

Conversation history:
{history}

New question: {question}

Standalone search query:"""

CITATION_PATTERN = re.compile(r'[Ss]ources?\s*(\d+(?:\s*(?:,|and)\s*\d+)*)')


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


def rewrite_query(model, tokenizer, question: str, history: list) -> str:
    if not history:
        return question

    history_text = "\n".join(f"{m['role']}: {m['content']}" for m in history)
    rewrite_input = REWRITE_PROMPT.format(history=history_text, question=question)
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


def build_messages_no_rag(system_prompt: str, history: list, question: str):
    user_turn = f"""Question: {question}"""
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_turn})
    return messages


def extract_cited_indices(response: str, num_sources: int) -> list:
    seen = []
    for match in CITATION_PATTERN.finditer(response):
        for num_str in re.findall(r'\d+', match.group(1)):
            idx = int(num_str) - 1
            if 0 <= idx < num_sources and idx not in seen:
                seen.append(idx)
    return seen


def build_sources_block(results: list, cited_indices: list) -> str:
    if not cited_indices:
        return ""

    # group by url
    by_url: dict = {}  # url -> {"label": str, "nums": [int, ...]}
    no_url = []  # (display_num, label) for chunks with no URL

    for idx in cited_indices:
        r = results[idx]
        display_num = idx + 1
        url = r.get("source_url") or r.get("topic_url") or ""
        label = r.get("source", "source")

        if url:
            if url not in by_url:
                by_url[url] = {"label": label, "nums": []}
            by_url[url]["nums"].append(display_num)
        else:
            no_url.append((display_num, label))

    lines = ["", "Sources:"]
    for url, info in by_url.items():
        nums = info["nums"]
        prefix = f"Source {nums[0]}" if len(nums) == 1 \
            else f"Sources {', '.join(str(n) for n in nums)}"
        lines.append(f"  [{prefix}] {info['label']} — {url}")
    for num, label in no_url:
        lines.append(f"  [Source {num}] {label}")

    return "\n".join(lines)


def chat_loop(model, tokenizer, retriever, top_k=4, max_history_turns=6, show_sources=False, show_ragless_answer=False):
    history = []
    history_no_rag = []

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
            history_no_rag = []
            print("[history cleared]\n")
            continue

        # raq lookup
        search_query = rewrite_query(model, tokenizer, question, history)

        results = retriever.retrieve(search_query, k=top_k, min_score=0.580)
        if not results:
            context = "No relevant context found."
        else:
            parts = []
            for i, r in enumerate(results, 1):
                parts.append(f"[Source {i}: {r['source']}]\n{r['text']}")
            context = "\n\n".join(parts)

        if show_sources:
            print(f"\n[search query: {search_query}]")
            for i, r in enumerate(results, 1):
                print(f"  retrieved [{i}] {r['source']} (score={r['score']:.3f})")

        # answer
        messages = build_messages(SYSTEM_PROMPT, history, context, question)
        response = generate(model, tokenizer, messages)

        # citations
        cited = extract_cited_indices(response, len(results))
        sources_block = build_sources_block(results, cited)
        display_response = response + ("\n" + sources_block if sources_block else "")

        print(f"\nBot: {display_response}\n")

        # dodamo samo stvari brez sources itd.
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": response})

        if len(history) > max_history_turns * 2:
            history = history[-max_history_turns * 2:]

        if show_ragless_answer:

            # answer
            messages = build_messages_no_rag(SYSTEM_PROMPT_NO_RAG, history_no_rag, question)
            response = generate(model, tokenizer, messages)

            print(f"\nBot (NO RAG): {response}\n")

            history_no_rag.append({"role": "user", "content": question})
            history_no_rag.append({"role": "assistant", "content": response})

            if len(history_no_rag) > max_history_turns * 2:
                history_no_rag = history_no_rag[-max_history_turns * 2:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--index-dir", default="./rag_index")
    parser.add_argument("--model", default="mistralai/Mistral-7B-Instruct-v0.3")
    parser.add_argument("--top-k", type=int, default=4)
    parser.add_argument("--show-sources", action="store_true", default=True, help="Print retrieved chunks (debug)")
    parser.add_argument("--show-ragless-answer", action="store_true", default=True,
                        help="Print answer without using rag (debug)")
    args = parser.parse_args()

    model, tokenizer = load_llm(args.model)
    retriever = RAGRetriever(args.index_dir)
    chat_loop(model, tokenizer, retriever, top_k=args.top_k, show_sources=args.show_sources,
              show_ragless_answer=args.show_ragless_answer)


if __name__ == "__main__":
    main()
