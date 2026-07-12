import numpy as np

from stress_test.data import Record, build_manifest, make_doc_id
from stress_test.hardness import (
    HardnessScorer,
    committee_margin,
    fit_weights,
    grouped_zscore,
    mtld,
)


def _records():
    out = []
    for i in range(300):
        doc_id = make_doc_id(f"source text {i}", "test")
        domain = ["news", "essay", "wiki"][i % 3]
        generator = ["gpt4", "llama", "human"][i % 3]
        out.append(Record(f"human {i}", 0, doc_id, domain, "human", "test"))
        out.append(Record(f"machine {i}", 1, doc_id, domain, generator, "test"))
    return out


def test_paired_records_never_straddle_splits():
    records = _records()
    manifest = build_manifest(records)
    for record in records:
        assert record.doc_id in manifest  # every doc assigned exactly one split


def test_manifest_is_deterministic():
    records = _records()
    assert build_manifest(records) == build_manifest(records)


def test_ood_holdouts_go_to_dedicated_slices():
    records = _records()
    manifest = build_manifest(records, holdout_generators=("llama",), holdout_domains=("wiki",))
    llama_docs = {r.doc_id for r in records if r.generator == "llama"}
    assert all(manifest[d] == "test_ood_generator" for d in llama_docs)


def test_split_proportions_roughly_correct():
    manifest = build_manifest(_records())
    values = list(manifest.values())
    train_frac = values.count("train") / len(values)
    assert 0.6 < train_frac < 0.8


def test_grouped_zscore_centers_within_group():
    values = np.array([1.0, 2.0, 3.0, 10.0, 20.0, 30.0])
    groups = np.array(["a", "a", "a", "b", "b", "b"])
    z = grouped_zscore(values, groups)
    assert abs(z[:3].mean()) < 1e-9 and abs(z[3:].mean()) < 1e-9


def test_committee_margin_peaks_at_uncertainty():
    margins = committee_margin(np.array([0.0, 0.5, 1.0]))
    assert margins[1] == 1.0 and margins[0] == 0.0 and margins[2] == 0.0


def test_mtld_repetitive_text_scores_lower():
    diverse = "the quick brown fox jumps over a lazy dog near riverbanks daily".split() * 3
    repetitive = ["word"] * 36
    assert mtld(diverse) > mtld(repetitive)


def test_hardness_scorer_uniform_weights_average_signals():
    signals = {name: np.array([0.0, 1.0]) for name in HardnessScorer().weights}
    scores = HardnessScorer().score(signals)
    assert scores[0] == 0.0 and abs(scores[1] - 1.0) < 1e-9


def test_fit_weights_finds_predictive_signal():
    rng = np.random.default_rng(0)
    n = 500
    predictive = rng.random(n)
    committee_error = (predictive > 0.5).astype(int)
    signals = {name: rng.random(n) for name in HardnessScorer().weights}
    signals["committee_margin"] = predictive
    weights = fit_weights(signals, committee_error)
    assert weights["committee_margin"] == max(weights.values())
    assert abs(sum(weights.values()) - 1.0) < 1e-9
