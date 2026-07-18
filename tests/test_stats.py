import numpy as np
import pytest

from stress_test.stats import (
    clustered_bootstrap_ci,
    holm_bonferroni,
    mcnemar_exact,
    paired_permutation_test,
)


def test_clustered_bootstrap_contains_point_estimate():
    rng = np.random.default_rng(0)
    values = rng.normal(0.7, 0.1, size=400)
    clusters = np.repeat(np.arange(100), 4)
    r = clustered_bootstrap_ci(values, clusters, n_boot=500, seed=1)
    assert r["ci_low"] <= r["point"] <= r["ci_high"]
    assert r["n_clusters"] == 100


def test_clustered_ci_wider_than_iid_when_clusters_correlated():
    rng = np.random.default_rng(0)
    cluster_effects = rng.normal(0.5, 0.2, size=50)
    values = np.repeat(cluster_effects, 8) + rng.normal(0, 0.01, size=400)
    clustered = clustered_bootstrap_ci(values, np.repeat(np.arange(50), 8), n_boot=500, seed=1)
    iid = clustered_bootstrap_ci(values, np.arange(400), n_boot=500, seed=1)
    width = lambda r: r["ci_high"] - r["ci_low"]  # noqa: E731
    assert width(clustered) > width(iid)


def test_clustered_bootstrap_empty_input_returns_nan():
    r = clustered_bootstrap_ci([], [], n_boot=100)
    assert np.isnan(r["point"]) and np.isnan(r["ci_low"]) and r["n_clusters"] == 0


def test_permutation_test_detects_real_difference():
    a = np.ones(200, dtype=bool)
    b = np.zeros(200, dtype=bool)
    assert paired_permutation_test(a, b, n_perm=2000)["p_value"] < 0.01


def test_permutation_test_null_when_identical():
    a = np.array([True, False] * 100)
    assert paired_permutation_test(a, a, n_perm=500)["p_value"] == pytest.approx(1.0)


def test_mcnemar_counts_and_symmetry():
    a = np.array([True, True, False, False, True])
    b = np.array([True, False, True, False, False])
    r = mcnemar_exact(a, b)
    assert r["only_a"] == 2 and r["only_b"] == 1
    assert 0 < r["p_value"] <= 1


def test_holm_known_answers_with_monotone_tie():
    adjusted = holm_bonferroni({"a": 0.01, "b": 0.04, "c": 0.03, "d": 0.9})
    assert adjusted["a"] == pytest.approx(0.04)  # (4-0) * 0.01
    assert adjusted["c"] == pytest.approx(0.09)  # (4-1) * 0.03
    # b's raw step value (4-2)*0.04 = 0.08 is lifted to 0.09 by monotonicity
    assert adjusted["b"] == pytest.approx(0.09)
    assert adjusted["d"] == pytest.approx(0.9)
    assert all(p <= 1.0 for p in adjusted.values())
