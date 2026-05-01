import os
import torch
import numpy as np
import faiss
import pickle
from os.path import exists
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

# EMBED_MODEL_ID = "all-MiniLM-L6-v2"
EMBED_MODEL_ID = "all-mpnet-base-v2"
# GEN_MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
GEN_MODEL_ID = "microsoft/Phi-4-mini-instruct"
# GEN_MODEL_ID = "Qwen/Qwen3-4B-Instruct"
TOP_K = 3
MAX_NEW_TOKENS = 256

print("[1/3] Preparing FAISS index...")
embedder = SentenceTransformer(EMBED_MODEL_ID)

index_loaded = False
if exists("rag_index.faiss") and exists("sentences.pkl"):
    print("Index files exist, attempting to load...")
    try:
        index = faiss.read_index("rag_index.faiss")
        with open("sentences.pkl", "rb") as f:
            sentences = pickle.load(f)
        index_loaded = True
        print(f"Restored {index.ntotal} sentences from disk index")
    except Exception as e:
        print(f"Failed loading index from disc!\n{e}")
    finally:
        pass
else:
    print("Index files missing, will generate index...")

if not index_loaded:
    print("Generating index from sources...")

    sentences = []
    file_count = 0
    for e in os.scandir("prepared_data"):
        if e.is_file():
            print(f"Loading sentences from {e.path}")
            with open(e.path, "r") as f:
                sentences.extend(f.readlines())
                file_count += 1

    print(f"Loaded {len(sentences)} sentences from {file_count} files")

    embeddings = embedder.encode(sentences, batch_size=32, show_progress_bar=True)
    embeddings = np.array(embeddings, dtype="float32")
    faiss.normalize_L2(embeddings)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    print(f"Indexed {index.ntotal} sentences (dim={dim})")

    faiss.write_index(index, "rag_index.faiss")
    with open("sentences.pkl", "wb") as f:
        pickle.dump(sentences, f)
    print(f"Saved index to disk!")

print(f"\n[2/3] Loading generative model: {GEN_MODEL_ID}")

tokenizer = AutoTokenizer.from_pretrained(GEN_MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    GEN_MODEL_ID,
    dtype=torch.bfloat16,  # use torch.float32 if on CPU only
    device_map="auto",  # auto-selects MPS (Apple), CUDA, or CPU
)
model.eval()
print(f"    Model loaded on: {next(model.parameters()).device}")


def retrieve(query: str, top_k: int = TOP_K) -> list[str]:
    """Embed the query and return top-k matching sentences."""
    q_vec = embedder.encode([query], convert_to_numpy=True).astype("float32")
    faiss.normalize_L2(q_vec)
    _, indices = index.search(q_vec, top_k)
    return [sentences[i] for i in indices[0] if i >= 0]


def generate(query: str, context_chunks: list[str]) -> str:
    """Build a chat-templated prompt and generate an answer."""
    context = "\n".join(f"- {c}" for c in context_chunks)
    print(context)
    messages = [
        {
            "role": "system",
            "content": (
                    "You are a helpful assistant. Answer the user's question using "
                    "ONLY the context provided. If the context doesn't contain the "
                    "answer, say you don't know.\n\nContext:\n" + context
            ),
        },
        {"role": "user", "content": query},
    ]

    # apply_chat_template correctly formats the prompt for TinyLlama
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            temperature=0.3,
            do_sample=True,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
        )

    # Decode only the newly generated tokens (skip the prompt)
    new_tokens = output_ids[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def ask(question: str) -> str:
    """Full RAG pipeline: retrieve → augment → generate."""
    context = retrieve(question)
    return generate(question, context)


print("\n[3/3] Ready. Type 'quit' to exit.\n" + "─" * 40)
while True:
    try:
        user_input = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        break

    if not user_input:
        continue
    if user_input.lower() in {"quit", "exit", "q"}:
        print("Goodbye.")
        break

    answer = ask(user_input)
    print(f"Bot: {answer}\n")
