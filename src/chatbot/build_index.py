import os
import json
import argparse
import pickle
from pathlib import Path
from typing import List, Dict

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


def load_chunks(data_dir: str) -> List[Dict]:
    chunks: List[Dict] = []
    data_path = Path(data_dir)

    files = sorted(data_path.rglob("*.jsonl"))

    if not files:
        raise FileNotFoundError(f"No .jsonl files found at {data_dir}?")

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"  warning: skipping bad JSON at {file_path}:{line_no} ({e})")
                    continue

                text = (entry.get("text") or "").strip()
                if not text:
                    continue

                # samo linki in nič stavkov, počisti data
                if text.count("http") >= 5 and text.count(". ") < 3:
                    continue

                topic = entry.get("topic_title", "")
                source_title = entry.get("source_title", "")

                prefix_parts = [p for p in [topic, source_title] if p]
                prefix = f"[{' | '.join(prefix_parts)}] " if prefix_parts else ""
                embed_text = prefix + text

                # for display
                display_source = " — ".join(prefix_parts) or entry.get("source_url") or "unknown"

                chunks.append({
                    "text": text,
                    "embed_text": embed_text,
                    "source": display_source,
                    "topic_title": topic,
                    "topic_url": entry.get("topic_url", ""),
                    "source_title": source_title,
                    "source_url": entry.get("source_url", ""),
                    "chunk_id": entry.get("chunk_id", ""),
                    "chunk_index": entry.get("chunk_index"),
                    "groups": entry.get("groups", []),
                    "also_called": entry.get("also_called", []),
                    "mesh_headings": entry.get("mesh_headings", []),
                    "information_categories": entry.get("information_categories", []),
                    "organization": entry.get("organization", ""),
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

    # Drop embed_text from saved metadata — only the embedder needed it,
    # and we don't want it cluttering retrieval results.
    metadata = [{k: v for k, v in c.items() if k != "embed_text"} for c in chunks]
    return index, metadata


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True, help="Chunked jsonl")
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
