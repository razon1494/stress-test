"""Hardness aggregation H(x) = sum_k w_k * h_k(x), plus weight fitting and the
validation that makes the score defensible:

1. Weights are fit on a HELD-OUT slice by predicting committee errors, then
   FROZEN before any benchmark evaluation.
2. Validate by showing detector accuracy decreases monotonically across
   H-quintiles (see metrics.hardness_collapse_index for the reporting side).
"""

from __future__ import annotations

import numpy as np

SIGNAL_NAMES = (
    "perplexity_closeness",
    "readability_normality",
    "semantic_consistency",
    "lexical_diversity",
    "committee_margin",
)


class HardnessScorer:
    def __init__(self, weights: dict[str, float] | None = None):
        if weights is None:
            weights = {name: 1.0 / len(SIGNAL_NAMES) for name in SIGNAL_NAMES}
        missing = set(SIGNAL_NAMES) - set(weights)
        if missing:
            raise ValueError(f"missing signal weights: {sorted(missing)}")
        total = sum(weights[n] for n in SIGNAL_NAMES)
        self.weights = {n: weights[n] / total for n in SIGNAL_NAMES}

    def score(self, signals: dict[str, np.ndarray]) -> np.ndarray:
        cols = [np.asarray(signals[n], dtype=float) * self.weights[n] for n in SIGNAL_NAMES]
        return np.sum(cols, axis=0)


def fit_weights(signals: dict[str, np.ndarray], committee_error: np.ndarray) -> dict[str, float]:
    """Logistic regression: which signals predict that the held-out committee
    errs on an example? Absolute coefficients, normalized, become weights."""
    from sklearn.linear_model import LogisticRegression

    x = np.column_stack([np.asarray(signals[n], dtype=float) for n in SIGNAL_NAMES])
    y = np.asarray(committee_error, dtype=int)
    clf = LogisticRegression(max_iter=2000).fit(x, y)
    coefs = np.abs(clf.coef_[0])
    if coefs.sum() == 0:
        coefs = np.ones_like(coefs)
    coefs = coefs / coefs.sum()
    return dict(zip(SIGNAL_NAMES, coefs.tolist()))
