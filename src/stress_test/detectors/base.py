"""Detector interface and the threshold-transfer protocol.

Detectors emit raw scores (higher = more machine-like), NOT probabilities.
The deployment-realistic protocol: calibrate a threshold ONCE on clean human
text at a target FPR (default 1%), then evaluate every transformed condition
at that same threshold. Re-tuning per condition overstates robustness.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np


class Detector(ABC):
    name: str = "detector"

    @abstractmethod
    def score(self, texts: list[str]) -> np.ndarray:
        """Raw scores, higher = more likely machine-generated."""

    def fit(self, texts: list[str], labels: np.ndarray) -> "Detector":
        """Trainable detectors override; zero-shot detectors are no-ops.
        Training uses CLEAN data only, matching deployment."""
        return self

    def predict_proba(self, texts: list[str]) -> np.ndarray | None:
        """P(machine) if the detector is probabilistic (needed for ECE/AURC);
        None otherwise."""
        return None


def calibrate_threshold(clean_human_scores: np.ndarray, target_fpr: float = 0.01) -> float:
    """Smallest threshold t with P(score > t | clean human) <= target_fpr."""
    scores = np.asarray(clean_human_scores, dtype=float)
    if scores.size == 0:
        raise ValueError("need clean human scores to calibrate")
    return float(np.quantile(scores, 1.0 - target_fpr, method="higher"))


def evaluate_at_threshold(scores: np.ndarray, labels: np.ndarray, threshold: float) -> dict:
    """labels: 1 = machine, 0 = human."""
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    pred = (scores > threshold).astype(int)
    machine, human = labels == 1, labels == 0
    return {
        "threshold": threshold,
        "accuracy": float((pred == labels).mean()),
        "tpr": float(pred[machine].mean()) if machine.any() else float("nan"),
        "fpr": float(pred[human].mean()) if human.any() else float("nan"),
        "n": int(labels.size),
    }
