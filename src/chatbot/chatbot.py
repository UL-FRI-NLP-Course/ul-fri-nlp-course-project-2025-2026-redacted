"""
chatbot.py
Runs a simple RAG chatbot that retrieves relevant facts from the FAISS index
and uses a small instruction-tuned LLM to answer single-shot questions.
"""

import os

# IMPORTANT: must be set before importing torch/faiss to avoid OpenMP clashes on macOS
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
# Prevent MPS from reserving more than the high watermark of available memory.
# 0.0 disables the upper limit (use system default); set to e.g. "0.7" to cap at 70% of unified memory.
os.environ.setdefault("PYTORCH_MPS_HIGH_WATERMARK_RATIO", "0.0")

import pickle
import argparse

import numpy as np
# Import torch BEFORE faiss to avoid OpenMP/BLAS conflicts on macOS
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer
import faiss

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "Qwen/Qwen2.5-3B-Instruct"  # ~3GB, works well on Mac mini

SYSTEM_PROMPT = (
    "You are a knowledgeable assistant that helps users build computers. "
    "Answer questions about PC components using ONLY the facts provided in the context. "
    "If the context doesn't contain the answer, say you don't have that information. "
    "Be concise and accurate."
)


def get_device() -> str:
    """Pick the best available device. MPS for Apple Silicon, else CPU.
    Allow override via FORCE_CPU=1 env var if MPS causes crashes."""
    if os.environ.get("FORCE_CPU") == "1":
        return "cpu"
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def load_index(index_dir: str):
    """Load the FAISS index and the parallel list of facts."""
    index_path = os.path.join(index_dir, "facts.faiss")
    facts_path = os.path.join(index_dir, "facts.pkl")

    if not os.path.exists(index_path) or not os.path.exists(facts_path):
        raise FileNotFoundError(
            f"Index files not found in {index_dir}. Run build_index.py first."
        )

    index = faiss.read_index(index_path)
    with open(facts_path, "rb") as f:
        facts = pickle.load(f)

    print(f"Loaded index with {index.ntotal} facts")
    return index, facts


def retrieve(query: str, embedder: SentenceTransformer, index, facts, k: int = 5):
    """Embed the query and return the top-k most similar facts."""
    q_emb = embedder.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)

    scores, idxs = index.search(q_emb, k)
    results = []
    for score, idx in zip(scores[0], idxs[0]):
        if idx == -1:
            continue
        results.append((facts[idx], float(score)))
    return results


def build_prompt(question: str, retrieved: list[tuple[str, float]]) -> list[dict]:
    """Build the chat-format prompt for the LLM."""
    context = "\n".join(f"- {fact}" for fact, _ in retrieved)
    user_msg = f"Context:\n{context}\n\nQuestion: {question}"
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]


def generate_answer(messages, tokenizer, model, device: str, max_new_tokens: int = 256) -> str:
    """Generate a response from the LLM given chat-format messages."""
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    # Cap input length to keep KV cache memory bounded
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048,
    ).to(device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.2,
            pad_token_id=tokenizer.eos_token_id,
            use_cache=True,
            repetition_penalty=1.15,  # discourages the model from looping on repeated phrases
            no_repeat_ngram_size=4,   # hard block on repeating any 4-token sequence
        )

    # Slice off the prompt tokens so we only decode the new generation
    generated = output_ids[0][inputs["input_ids"].shape[1]:]
    text = tokenizer.decode(generated, skip_special_tokens=True).strip()

    # Free intermediate tensors so memory doesn't accumulate across turns
    del inputs, output_ids, generated
    if device == "mps":
        torch.mps.empty_cache()
    elif device == "cuda":
        torch.cuda.empty_cache()

    return text


def main():
    parser = argparse.ArgumentParser(description="Run the RAG chatbot.")
    parser.add_argument(
        "--index-dir",
        default="index",
        help="Directory containing the prebuilt index (default: index)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=8,
        help="Number of facts to retrieve per query (default: 8)",
    )
    parser.add_argument(
        "--show-context",
        default=True,
        action="store_true",
        help="Print the retrieved facts before each answer",
    )
    args = parser.parse_args()

    device = get_device()
    print(f"Using device: {device}")

    print("Loading index...")
    index, facts = load_index(args.index_dir)

    print(f"Loading embedding model: {EMBEDDING_MODEL}")
    embedder = SentenceTransformer(EMBEDDING_MODEL, device=device)

    print(f"Loading LLM: {LLM_MODEL} (this may take a moment on first run)")
    tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)

    # Memory/correctness tradeoff:
    # - fp16 on CUDA: fast and stable
    # - bf16 on MPS: was unstable for Qwen (caused repetition loops / garbage output)
    # - fp32 on MPS: stable but ~6GB for a 1.5B model. Acceptable on Mac mini.
    # - fp32 on CPU: stable, slow but works.
    if device == "cuda":
        dtype = torch.float16
    else:
        dtype = torch.float32

    model = AutoModelForCausalLM.from_pretrained(
        LLM_MODEL,
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
    ).to(device)
    model.eval()

    print("\nReady. Type a question (or 'quit' to exit).\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not question:
            continue
        if question.lower() in {"quit", "exit", "q"}:
            break

        retrieved = retrieve(question, embedder, index, facts, k=args.top_k)

        if args.show_context:
            print("\n--- Retrieved facts ---")
            for fact, score in retrieved:
                print(f"  [{score:.3f}] {fact}")
            print("-----------------------\n")

        messages = build_prompt(question, retrieved)
        answer = generate_answer(messages, tokenizer, model, device)
        print(f"\nBot: {answer}\n")


if __name__ == "__main__":
    main()
