"""Per-example hardness signals. Each returns values in [0, 1], higher = harder.

Signals that need model outputs (perplexity, committee probabilities, semantic
similarity) take PRECOMPUTED arrays so heavy forwards run once, in the cached
pipeline stage — never inside the scorer.

All z-scoring is done WITHIN (domain, length-bucket) groups so hardness does
not silently become a length or domain proxy.
"""

from __future__ import annotations

import numpy as np


def grouped_zscore(values: np.ndarray, groups: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    groups = np.asarray(groups)
    z = np.empty_like(values)
    for g in np.unique(groups):
        mask = groups == g
        std = values[mask].std(ddof=0)
        z[mask] = (values[mask] - values[mask].mean()) / (std if std > 0 else 1.0)
    return z


def _band_hardness(z: np.ndarray, cap: float = 3.0) -> np.ndarray:
    """Examples near their group's typical value (|z| small) are hard to tell
    apart; extremes are easy tells. Maps |z| in [0, cap] -> hardness [1, 0]."""
    return 1.0 - np.minimum(np.abs(z), cap) / cap


def perplexity_closeness(log_ppl: np.ndarray, groups: np.ndarray) -> np.ndarray:
    return _band_hardness(grouped_zscore(log_ppl, groups))


def readability_normality(fkgl: np.ndarray, groups: np.ndarray) -> np.ndarray:
    return _band_hardness(grouped_zscore(fkgl, groups))


def lexical_diversity_normality(mtld_values: np.ndarray, groups: np.ndarray) -> np.ndarray:
    return _band_hardness(grouped_zscore(mtld_values, groups))


def semantic_consistency(paraphrase_similarity: np.ndarray) -> np.ndarray:
    """cos(E(x), E(paraphrase(x))), already in ~[0,1]: text whose meaning
    survives paraphrase cleanly is harder to disrupt."""
    return np.clip(np.asarray(paraphrase_similarity, dtype=float), 0.0, 1.0)


def committee_margin(committee_probs: np.ndarray) -> np.ndarray:
    """1 - |2p - 1| from a held-out detector committee. MUST be leave-one-out:
    never include the detector being evaluated, or the score is circular."""
    p = np.asarray(committee_probs, dtype=float)
    return 1.0 - np.abs(2.0 * p - 1.0)


def mtld(tokens: list[str], ttr_threshold: float = 0.72) -> float:
    """Measure of Textual Lexical Diversity (McCarthy & Jarvis 2010),
    bidirectional mean. Pure Python — no extra dependency."""
    if len(tokens) < 10:
        return float(len(tokens))

    def one_pass(seq: list[str]) -> float:
        factors = 0.0
        types: set[str] = set()
        count = 0
        for tok in seq:
            count += 1
            types.add(tok.lower())
            if len(types) / count <= ttr_threshold:
                factors += 1.0
                types = set()
                count = 0
        if count:
            ttr = len(types) / count
            factors += (1.0 - ttr) / (1.0 - ttr_threshold)
        return len(seq) / factors if factors > 0 else float(len(seq))

    return (one_pass(tokens) + one_pass(tokens[::-1])) / 2.0
