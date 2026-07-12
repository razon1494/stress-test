"""GPTZero-style detector: hand-crafted stylometric features + gradient
boosting. Reproduces the deployed commercial paradigm (burstiness + perplexity
heuristics) without a paid API.

Perplexity-derived features are passed in precomputed (from the perplexity
cache) so this stays CPU-only and never double-computes model forwards.
"""

from __future__ import annotations

import re

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

from stress_test.detectors.base import Detector

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def stylometric_features(text: str) -> np.ndarray:
    sentences = [s for s in _SENT_SPLIT.split(text.strip()) if s]
    words = text.split()
    sent_lens = np.asarray([len(s.split()) for s in sentences] or [0], dtype=float)
    word_lens = np.asarray([len(w) for w in words] or [0], dtype=float)
    n_words = max(len(words), 1)
    unique_ratio = len({w.lower() for w in words}) / n_words
    punct_density = sum(text.count(c) for c in ",;:—-()") / max(len(text), 1)
    return np.asarray(
        [
            sent_lens.mean(),
            sent_lens.std(ddof=0),  # burstiness: humans vary sentence length more
            sent_lens.max() - sent_lens.min() if len(sent_lens) > 1 else 0.0,
            word_lens.mean(),
            unique_ratio,
            punct_density,
            len(sentences),
        ]
    )


class StylometricDetector(Detector):
    name = "stylometric_gbm"

    def __init__(self, seed: int = 0):
        self._model = GradientBoostingClassifier(random_state=seed)
        self._fitted = False

    def _features(self, texts: list[str]) -> np.ndarray:
        return np.stack([stylometric_features(t) for t in texts])

    def fit(self, texts: list[str], labels: np.ndarray) -> "StylometricDetector":
        self._model.fit(self._features(texts), np.asarray(labels, dtype=int))
        self._fitted = True
        return self

    def score(self, texts: list[str]) -> np.ndarray:
        if not self._fitted:
            raise RuntimeError("call fit() on clean training data first")
        return self._model.predict_proba(self._features(texts))[:, 1]

    def predict_proba(self, texts: list[str]) -> np.ndarray:
        return self.score(texts)
