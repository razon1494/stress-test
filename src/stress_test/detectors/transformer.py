"""Supervised neural detectors: pretrained RoBERTa detector for inference, and
notes for the DeBERTa-v3 fine-tune (train on Kaggle, ~2 GPU-h; training data
must be CLEAN text only, split by source document — see data/splits.py).
"""

from __future__ import annotations

from functools import lru_cache

import numpy as np

from stress_test.detectors.base import Detector


@lru_cache(maxsize=2)
def _clf_pipeline(model_name: str):
    from transformers import pipeline

    return pipeline("text-classification", model=model_name, truncation=True, top_k=None)


class TransformerDetector(Detector):
    """Wraps any HF text-classification detector checkpoint. ``machine_label``
    is the class name that means 'machine-generated' for that checkpoint
    (the OpenAI RoBERTa detector uses 'Fake')."""

    name = "roberta_openai"

    def __init__(
        self,
        model_name: str = "openai-community/roberta-base-openai-detector",
        machine_label: str = "Fake",
    ):
        self.model_name = model_name
        self.machine_label = machine_label

    def score(self, texts: list[str]) -> np.ndarray:
        pipe = _clf_pipeline(self.model_name)
        results = pipe(texts, batch_size=16)
        out = []
        for scores in results:
            by_label = {r["label"]: r["score"] for r in scores}
            if self.machine_label not in by_label:
                raise ValueError(
                    f"label '{self.machine_label}' not in {sorted(by_label)}; "
                    f"set machine_label for {self.model_name}"
                )
            out.append(by_label[self.machine_label])
        return np.asarray(out)

    def predict_proba(self, texts: list[str]) -> np.ndarray:
        return self.score(texts)
