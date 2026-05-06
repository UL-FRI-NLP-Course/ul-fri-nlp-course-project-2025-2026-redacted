"""
build_index.py
Builds a FAISS index from text files containing facts about computer components.
Each line in each file is treated as an individual fact.
"""

import os
import pickle
import argparse
from pathlib import Path

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def load_facts(data_dir: str) -> list[str]:
    """Read all lines from all files in the given directory. Each line is a fact."""
    facts = []
    data_path = Path(data_dir)

    if not data_path.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    files = [f for f in data_path.iterdir() if f.is_file()]
    print(f"Found {len(files)} file(s) in {data_dir}")

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:  # skip empty lines
                        facts.append(line)
        except Exception as e:
            print(f"Skipping {file_path.name}: {e}")

    print(f"Loaded {len(facts)} facts total")
    return facts


def build_index(facts: list[str], model: SentenceTransformer) -> faiss.Index:
    """Embed facts and build a FAISS index using cosine similarity (via inner product)."""
    print(f"Embedding {len(facts)} facts...")
    embeddings = model.encode(
        facts,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,  # so inner product == cosine similarity
    )
    embeddings = embeddings.astype(np.float32)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # inner product index, fine for small/medium datasets
    index.add(embeddings)
    print(f"Built FAISS index with {index.ntotal} vectors of dimension {dim}")
    return index


def main():
    parser = argparse.ArgumentParser(description="Build a RAG index from fact files.")
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Directory containing .txt files with one fact per line (default: data)",
    )
    parser.add_argument(
        "--out-dir",
        default="index",
        help="Output directory for the index and facts (default: index)",
    )
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    facts = load_facts(args.data_dir)
    if not facts:
        print("No facts found. Aborting.")
        return

    print(f"Loading embedding model: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)

    index = build_index(facts, model)

    index_path = os.path.join(args.out_dir, "facts.faiss")
    facts_path = os.path.join(args.out_dir, "facts.pkl")

    faiss.write_index(index, index_path)
    with open(facts_path, "wb") as f:
        pickle.dump(facts, f)

    print(f"\nSaved index to {index_path}")
    print(f"Saved facts to {facts_path}")
    print("Done.")


if __name__ == "__main__":
    main()
