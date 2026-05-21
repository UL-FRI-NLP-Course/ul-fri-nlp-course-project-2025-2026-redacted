import os
import pickle
from typing import List, Dict

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from torch import Tensor


class RAGRetriever:

    def __init__(self, id:str, index_dir: str, keywords: Tensor):
        self.id = id,
        self.index = faiss.read_index(os.path.join(index_dir, "index.faiss"))
        self.keywords = keywords

        with open(os.path.join(index_dir, "metadata.pkl"), "rb") as f:
            self.metadata = pickle.load(f)

        with open(os.path.join(index_dir, "config.pkl"), "rb") as f:
            config = pickle.load(f)

        self.embedding_model = SentenceTransformer(config["embedding_model"], device="cuda")

    def retrieve(self, query: str, k: int, min_score: float = 0.0) -> List[Dict]:
        query_emb = self.embedding_model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True,
        ).astype(np.float32)

        scores, indices = self.index.search(query_emb, k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            # -1 ko je manj kot k rez.
            if idx == -1:
                continue
            if float(score) < min_score:
                continue
            chunk = dict(self.metadata[idx])
            chunk["score"] = float(score)
            results.append(chunk)
        return results
