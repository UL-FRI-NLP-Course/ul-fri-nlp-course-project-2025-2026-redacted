import argparse
import os
import pickle
import re
from typing import List, Dict

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


def load_chunks(data_dir: str) -> List[Dict]:
    chunks: List[Dict] = []

    for fname in sorted(os.listdir(data_dir)):
        if not fname.endswith(".md"):
            continue

        fpath = os.path.join(data_dir, fname)
        source = f"{data_dir}/{fname}"

        with open(fpath, encoding="utf-8") as f:
            raw = f.read()

        title_match = re.search(r"^# (.+)", raw, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else fname

        # Split on H2 headings; odd indices = heading, even = body
        parts = re.split(r"^(## .+)$", raw, flags=re.MULTILINE)

        for i in range(1, len(parts), 2):
            heading = parts[i][3:].strip()
            body = parts[i + 1].strip() if i + 1 < len(parts) else ""
            body = re.sub(r"\[Image:[^\]]*\]\n?", "", body).strip()

            if len(body) < 80:
                continue

            text = f"[{title}] {heading}\n{body}"
            chunks.append({
                "embed_text": text,
                "text": text,
                "source": source,
                "section": heading,
                "category": data_dir,
            })

    return chunks


def build_index(chunks: List[Dict], embedding_model: SentenceTransformer):
    if not chunks:
        raise ValueError("No chunks to index.")

    # noinspection PyTypeChecker
    texts_to_embed: list[str] = [c.get("embed_text") for c in chunks]

    print(f"Embedding {len(texts_to_embed)} chunks...")
    embeddings = embedding_model.encode(
        texts_to_embed,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype(np.float32))

    # Drop embed_text from saved metadata ? only the embedder needed it,
    # and we don't want it cluttering retrieval results.
    metadata = [{k: v for k, v in c.items() if k != "embed_text"} for c in chunks]
    return index, metadata


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True)
    parser.add_argument("--output-dir", default="./rag_index")
    parser.add_argument("--embedding-model", default="BAAI/bge-base-en-v1.5")
    args = parser.parse_args()

    print(f"Loading embedding model: {args.embedding_model}")
    embedding_model = SentenceTransformer(args.embedding_model, device='cuda')

    print(f"Loading chunks from: {args.data_dir}")
    chunks = load_chunks(args.data_dir)

    if not chunks:
        raise SystemExit("No chunks?? oops")

    # sanity check
    print(f"Loaded {len(chunks)} chunks. Sample sources:")
    seen = []
    for c in chunks:
        if c["source"] not in seen:
            seen.append(c["source"])
            if len(seen) >= 5:
                break
    for s in seen:
        print(f"  - {s}")

    print("Building index...")
    index, metadata = build_index(chunks, embedding_model)

    os.makedirs(args.output_dir, exist_ok=True)
    faiss.write_index(index, os.path.join(args.output_dir, "index.faiss"))
    with open(os.path.join(args.output_dir, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)
    with open(os.path.join(args.output_dir, "config.pkl"), "wb") as f:
        pickle.dump({
            "embedding_model": args.embedding_model,
        }, f)

    print(f"\nSaved index to: {args.output_dir}")
    print(f"Total chunks indexed: {len(metadata)}")


if __name__ == "__main__":
    main()
