"""Semantic-preservation scoring between original and transformed text.

Embedding cosine (all-MiniLM-L6-v2, free, runs on any GPU/CPU) is the
large-scale scorer; it must be validated against the human annotation sample
(Week 6) before QAES thresholds are trusted. Default tau=0.85 is provisional
until that validation.
"""

from __future__ import annotations

from functools import lru_cache

import numpy as np

QAES_SEM_THRESHOLD = 0.85  # provisional; revisit after human validation


@lru_cache(maxsize=1)
def _embedder(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(model_name)


def semantic_similarity(originals: list[str], transformed: list[str]) -> np.ndarray:
    """Cosine similarity per (original, transformed) pair, in [-1, 1]."""
    if len(originals) != len(transformed):
        raise ValueError("originals and transformed must be the same length")
    model = _embedder()
    a = model.encode(originals, batch_size=64, convert_to_numpy=True, normalize_embeddings=True)
    b = model.encode(transformed, batch_size=64, convert_to_numpy=True, normalize_embeddings=True)
    return np.sum(a * b, axis=1)
