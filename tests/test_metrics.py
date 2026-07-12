import numpy as np
import pytest

from stress_test.metrics import (
    aurc,
    expected_calibration_error,
    false_accusation_rate,
    hardness_collapse_index,
    qaes,
    robustness_score,
    semantic_preservation_gap,
    transformation_stability,
    worst_case_performance,
)


def test_robustness_score_known_answer():
    r = robustness_score(clean=0.9, transformed={"a": 0.9, "b": 0.45})
    assert r["rs"] == pytest.approx(0.75)
    assert r["per_transform"]["b"] == pytest.approx(0.5)


def test_robustness_score_rejects_zero_clean():
    with pytest.raises(ValueError):
        robustness_score(0.0, {"a": 0.5})


def test_transformation_stability_uniform_is_one():
    assert transformation_stability({"a": 0.8, "b": 0.8, "c": 0.8}) == pytest.approx(1.0)


def test_transformation_stability_fragile_is_lower():
    uniform = transformation_stability({"a": 0.6, "b": 0.6})
    fragile = transformation_stability({"a": 0.9, "b": 0.3})
    assert fragile < uniform


def test_qaes_filters_meaning_destroying_evasions():
    # 4 evasions, but 2 destroyed the meaning: raw=1.0, qaes computed on valid only
    r = qaes(
        evaded=[True, True, True, True],
        semantic_similarity=[0.95, 0.9, 0.2, 0.1],
        sem_threshold=0.85,
    )
    assert r["raw_evasion"] == 1.0
    assert r["qaes"] == 1.0
    assert r["n_valid"] == 2
    # now the valid ones did NOT evade: honest number drops to 0
    r2 = qaes([False, False, True, True], [0.95, 0.9, 0.2, 0.1])
    assert r2["raw_evasion"] == 0.5
    assert r2["qaes"] == 0.0


def test_spg_is_raw_minus_qaes():
    gap = semantic_preservation_gap([False, True], [0.95, 0.1])
    assert gap == pytest.approx(0.5 - 0.0)


def test_hci_detects_collapse():
    hardness = np.linspace(0, 1, 100)
    collapsing = hardness < 0.8  # perfect on easy, fails hardest quintile
    r = hardness_collapse_index(collapsing, hardness)
    assert r["hci"] == pytest.approx(1.0)
    uniform = np.ones(100, dtype=bool)
    assert hardness_collapse_index(uniform, hardness)["hci"] == pytest.approx(0.0)


def test_wcp_names_the_worst_pipeline():
    r = worst_case_performance({"esl_student": 0.7, "content_launderer": 0.2})
    assert r["wcp"] == pytest.approx(0.2)
    assert r["worst_pipeline"] == "content_launderer"


def test_far_at_threshold():
    assert false_accusation_rate([0.1, 0.2, 0.9, 0.95], threshold=0.5) == pytest.approx(0.5)


def test_ece_perfectly_calibrated_bins_are_zero():
    # bin at p=0.75 containing 75% positives -> zero ECE contribution
    probs = [0.75] * 4
    labels = [1, 1, 1, 0]
    assert expected_calibration_error(probs, labels, n_bins=10) == pytest.approx(0.0)


def test_ece_overconfident_is_positive():
    assert expected_calibration_error([0.95] * 4, [1, 0, 0, 0]) > 0.5


def test_aurc_confident_and_correct_beats_confident_and_wrong():
    good = aurc(confidence=[0.9, 0.8, 0.6, 0.5], correct=[True, True, True, False])
    bad = aurc(confidence=[0.9, 0.8, 0.6, 0.5], correct=[False, True, True, True])
    assert good["aurc"] < bad["aurc"]
