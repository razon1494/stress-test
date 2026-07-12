"""Reliability metrics for detector evaluation.

Conventions:
- ``accuracy`` values are performance at a FIXED threshold calibrated once on
  clean human text (threshold-transfer protocol) — typically TPR@1%FPR.
- ``transformed`` maps transformation/pipeline name -> performance under it.
- Label convention: 1 = machine-generated, 0 = human-written.
"""

from __future__ import annotations

from typing import Mapping, Sequence

import numpy as np


def robustness_score(clean: float, transformed: Mapping[str, float]) -> dict:
    """RS(d) = mean_t A(d,t) / A(d,0): mean retained performance across transforms."""
    if clean <= 0:
        raise ValueError("clean performance must be positive to form retention ratios")
    per_transform = {t: a / clean for t, a in transformed.items()}
    return {
        "rs": float(np.mean(list(per_transform.values()))),
        "per_transform": per_transform,
        "clean": clean,
    }


def transformation_stability(transformed: Mapping[str, float]) -> float:
    """TS(d) = 1 - CV of performance across transforms. 1 = uniform, low = fragile
    to specific transforms even if the mean is high."""
    vals = np.asarray(list(transformed.values()), dtype=float)
    mean = vals.mean()
    if mean <= 0:
        return float("nan")
    return float(1.0 - vals.std(ddof=0) / mean)


def qaes(
    evaded: Sequence[bool],
    semantic_similarity: Sequence[float],
    sem_threshold: float = 0.85,
    fluency_ok: Sequence[bool] | None = None,
) -> dict:
    """Quality-Adjusted Evasion Success: evasion rate restricted to transformed
    examples whose meaning survived (and, optionally, that remain fluent).

    Raw evasion rates conflate "fooled the detector" with "destroyed the text";
    QAES is the honest number.
    """
    evaded_arr = np.asarray(evaded, dtype=bool)
    sim = np.asarray(semantic_similarity, dtype=float)
    if evaded_arr.shape != sim.shape:
        raise ValueError("evaded and semantic_similarity must be the same length")
    valid = sim >= sem_threshold
    if fluency_ok is not None:
        valid &= np.asarray(fluency_ok, dtype=bool)
    return {
        "raw_evasion": float(evaded_arr.mean()) if evaded_arr.size else float("nan"),
        "qaes": float(evaded_arr[valid].mean()) if valid.any() else float("nan"),
        "valid_fraction": float(valid.mean()) if valid.size else float("nan"),
        "n": int(evaded_arr.size),
        "n_valid": int(valid.sum()),
    }


def semantic_preservation_gap(
    evaded: Sequence[bool],
    semantic_similarity: Sequence[float],
    sem_threshold: float = 0.85,
) -> float:
    """SPG = raw evasion - QAES: the share of apparent attack success that is
    actually attributable to meaning destruction rather than detector weakness."""
    r = qaes(evaded, semantic_similarity, sem_threshold)
    return float(r["raw_evasion"] - r["qaes"])


def hardness_collapse_index(
    correct: Sequence[bool],
    hardness: Sequence[float],
    n_quantiles: int = 5,
) -> dict:
    """HCI = (A_easiest - A_hardest) / A_easiest over hardness quantile bins.

    0 = performance uniform across difficulty; -> 1 = detector collapses on the
    hard examples that aggregate metrics hide.
    """
    correct_arr = np.asarray(correct, dtype=float)
    h = np.asarray(hardness, dtype=float)
    if correct_arr.shape != h.shape:
        raise ValueError("correct and hardness must be the same length")
    edges = np.quantile(h, np.linspace(0, 1, n_quantiles + 1))
    # searchsorted handles ties in quantile edges more gracefully than digitize
    bins = np.clip(np.searchsorted(edges[1:-1], h, side="right"), 0, n_quantiles - 1)
    acc_by_bin = [
        float(correct_arr[bins == b].mean()) if (bins == b).any() else float("nan")
        for b in range(n_quantiles)
    ]
    a_easy, a_hard = acc_by_bin[0], acc_by_bin[-1]
    hci = float((a_easy - a_hard) / a_easy) if a_easy and not np.isnan(a_easy) else float("nan")
    return {"hci": hci, "acc_by_quantile": acc_by_bin}


def worst_case_performance(pipeline_performance: Mapping[str, float]) -> dict:
    """WCP = min performance over the NAMED realistic pipelines (restrict inputs
    to QAES-valid conditions upstream so this is not dominated by garbage text)."""
    if not pipeline_performance:
        raise ValueError("no pipelines given")
    worst = min(pipeline_performance, key=pipeline_performance.get)  # type: ignore[arg-type]
    return {"wcp": float(pipeline_performance[worst]), "worst_pipeline": worst}


def false_accusation_rate(human_scores: Sequence[float], threshold: float) -> float:
    """FAR(d, t) = FPR on (transformed) HUMAN text at the clean-calibrated
    threshold — the symmetric, socially-costly failure mode."""
    scores = np.asarray(human_scores, dtype=float)
    return float((scores > threshold).mean()) if scores.size else float("nan")


def expected_calibration_error(
    probs: Sequence[float],
    labels: Sequence[int],
    n_bins: int = 10,
) -> float:
    """Standard equal-width-bin ECE on P(machine). Report clean vs transformed
    (delta-ECE) to measure calibration drift under shift."""
    p = np.asarray(probs, dtype=float)
    y = np.asarray(labels, dtype=float)
    if p.shape != y.shape:
        raise ValueError("probs and labels must be the same length")
    bins = np.clip((p * n_bins).astype(int), 0, n_bins - 1)
    ece = 0.0
    for b in range(n_bins):
        mask = bins == b
        if mask.any():
            ece += mask.mean() * abs(p[mask].mean() - y[mask].mean())
    return float(ece)


def aurc(confidence: Sequence[float], correct: Sequence[bool]) -> dict:
    """Area under the risk-coverage curve (selective prediction). Lower is
    better; supports the 'abstain and flag for human review' deployment mode."""
    conf = np.asarray(confidence, dtype=float)
    corr = np.asarray(correct, dtype=float)
    if conf.shape != corr.shape:
        raise ValueError("confidence and correct must be the same length")
    order = np.argsort(-conf, kind="stable")
    risks = np.cumsum(1.0 - corr[order]) / np.arange(1, len(corr) + 1)
    coverage = np.arange(1, len(corr) + 1) / len(corr)
    return {
        "aurc": float(risks.mean()),
        "risk_at_full_coverage": float(risks[-1]),
        "coverage": coverage,
        "risk": risks,
    }
