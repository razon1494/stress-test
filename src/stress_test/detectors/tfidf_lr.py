"""Classical baseline: TF-IDF (word + char n-grams) + logistic regression.

The sanity floor. If this survives a transformation that breaks the neural
detectors, that asymmetry is itself a finding worth a paragraph.
"""

from __future__ import annotations

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion, Pipeline as SkPipeline

from stress_test.detectors.base import Detector


class TfidfLogReg(Detector):
    name = "tfidf_logreg"

    def __init__(self, max_features: int = 50000, seed: int = 0):
        self._model = SkPipeline(
            [
                (
                    "features",
                    FeatureUnion(
                        [
                            ("word", TfidfVectorizer(ngram_range=(1, 2), max_features=max_features)),
                            (
                                "char",
                                TfidfVectorizer(
                                    analyzer="char_wb", ngram_range=(2, 4), max_features=max_features
                                ),
                            ),
                        ]
                    ),
                ),
                ("clf", LogisticRegression(max_iter=2000, C=1.0, random_state=seed)),
            ]
        )
        self._fitted = False

    def fit(self, texts: list[str], labels: np.ndarray) -> "TfidfLogReg":
        self._model.fit(texts, np.asarray(labels, dtype=int))
        self._fitted = True
        return self

    def score(self, texts: list[str]) -> np.ndarray:
        if not self._fitted:
            raise RuntimeError("call fit() on clean training data first")
        return self._model.predict_proba(texts)[:, 1]

    def predict_proba(self, texts: list[str]) -> np.ndarray:
        return self.score(texts)
