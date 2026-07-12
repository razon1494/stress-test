import numpy as np
import pytest

from stress_test.detectors import (
    StylometricDetector,
    TfidfLogReg,
    calibrate_threshold,
    evaluate_at_threshold,
)


def _toy_corpus(n=60, seed=0):
    rng = np.random.default_rng(seed)
    human_vocab = ["river", "granddad", "stumbled", "porch", "kettle", "mud", "laughter"]
    machine_vocab = ["furthermore", "leverage", "delve", "comprehensive", "pivotal", "landscape"]
    texts, labels = [], []
    for _ in range(n):
        texts.append(" ".join(rng.choice(human_vocab, size=25)) + ".")
        labels.append(0)
        texts.append(" ".join(rng.choice(machine_vocab, size=25)) + ".")
        labels.append(1)
    return texts, np.asarray(labels)


def test_tfidf_detector_separates_toy_classes():
    texts, labels = _toy_corpus()
    det = TfidfLogReg().fit(texts, labels)
    test_texts, test_labels = _toy_corpus(n=20, seed=1)
    scores = det.score(test_texts)
    assert scores[test_labels == 1].mean() > scores[test_labels == 0].mean()


def test_tfidf_requires_fit():
    with pytest.raises(RuntimeError):
        TfidfLogReg().score(["hello"])


def test_stylometric_features_do_not_crash_on_edge_cases():
    det = StylometricDetector()
    for text in ["", "word", "One sentence only."]:
        assert det._features([text]).shape == (1, 7)


def test_calibrate_threshold_respects_target_fpr():
    rng = np.random.default_rng(0)
    human_scores = rng.normal(0, 1, size=5000)
    t = calibrate_threshold(human_scores, target_fpr=0.01)
    assert (human_scores > t).mean() <= 0.01


def test_evaluate_at_threshold_reports_both_classes():
    scores = np.array([0.1, 0.2, 0.8, 0.9])
    labels = np.array([0, 0, 1, 1])
    r = evaluate_at_threshold(scores, labels, threshold=0.5)
    assert r["tpr"] == 1.0 and r["fpr"] == 0.0 and r["accuracy"] == 1.0
