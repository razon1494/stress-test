"""Publication-grade statistical inference.

Key design decision: bootstrap resampling is CLUSTERED by source document,
because a human text and its machine/transformed counterparts share a cluster —
i.i.d. resampling would understate variance and produce too-narrow intervals.
"""

from __future__ import annotations

from typing import Callable, Mapping, Sequence

import numpy as np
from scipy import stats as sps


def clustered_bootstrap_ci(
    values: Sequence[float],
    clusters: Sequence,
    stat: Callable[[np.ndarray], float] = np.mean,
    n_boot: int = 2000,
    alpha: float = 0.05,
    seed: int = 0,
) -> dict:
    """Percentile bootstrap CI with cluster resampling (resample clusters with
    replacement, keep all members of a chosen cluster)."""
    vals = np.asarray(values, dtype=float)
    cl = np.asarray(clusters)
    if vals.shape[0] != cl.shape[0]:
        raise ValueError("values and clusters must be the same length")
    if vals.size == 0:
        # single-class conditions (e.g. human-only human_edit) have no rows
        # for the other class's rate — report NaN rather than crashing
        nan = float("nan")
        return {"point": nan, "ci_low": nan, "ci_high": nan, "n_clusters": 0, "n_boot": n_boot}
    unique = np.unique(cl)
    members = {c: np.flatnonzero(cl == c) for c in unique}
    rng = np.random.default_rng(seed)
    boot = np.empty(n_boot)
    for i in range(n_boot):
        chosen = rng.choice(unique, size=len(unique), replace=True)
        idx = np.concatenate([members[c] for c in chosen])
        boot[i] = stat(vals[idx])
    lo, hi = np.quantile(boot, [alpha / 2, 1 - alpha / 2])
    return {
        "point": float(stat(vals)),
        "ci_low": float(lo),
        "ci_high": float(hi),
        "n_clusters": int(len(unique)),
        "n_boot": n_boot,
    }


def paired_permutation_test(
    a_correct: Sequence[bool],
    b_correct: Sequence[bool],
    n_perm: int = 10000,
    seed: int = 0,
) -> dict:
    """Two-sided sign-flip permutation test on per-example accuracy differences
    between two detectors evaluated on the SAME examples."""
    a = np.asarray(a_correct, dtype=float)
    b = np.asarray(b_correct, dtype=float)
    if a.shape != b.shape:
        raise ValueError("a_correct and b_correct must be the same length")
    d = a - b
    observed = d.mean()
    rng = np.random.default_rng(seed)
    signs = rng.choice([-1.0, 1.0], size=(n_perm, d.size))
    perm_means = (signs * d).mean(axis=1)
    # add-one smoothing gives a valid p-value under the permutation null
    p = (np.sum(np.abs(perm_means) >= abs(observed)) + 1) / (n_perm + 1)
    return {"mean_diff": float(observed), "p_value": float(p), "n": int(d.size)}


def mcnemar_exact(a_correct: Sequence[bool], b_correct: Sequence[bool]) -> dict:
    """Exact McNemar test (binomial on discordant pairs) for two classifiers
    on the same examples."""
    a = np.asarray(a_correct, dtype=bool)
    b = np.asarray(b_correct, dtype=bool)
    only_a = int(np.sum(a & ~b))
    only_b = int(np.sum(~a & b))
    n_disc = only_a + only_b
    p = 1.0 if n_disc == 0 else sps.binomtest(only_a, n_disc, 0.5).pvalue
    return {"only_a": only_a, "only_b": only_b, "p_value": float(p)}


def holm_bonferroni(p_values: Mapping[str, float]) -> dict[str, float]:
    """Holm step-down correction across the many detector x transform
    comparisons. Returns adjusted p-values, capped at 1 and monotone."""
    items = sorted(p_values.items(), key=lambda kv: kv[1])
    m = len(items)
    adjusted: dict[str, float] = {}
    running_max = 0.0
    for i, (name, p) in enumerate(items):
        adj = min(1.0, (m - i) * p)
        running_max = max(running_max, adj)
        adjusted[name] = running_max
    return {name: adjusted[name] for name in p_values}
