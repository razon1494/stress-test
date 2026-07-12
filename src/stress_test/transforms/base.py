"""Transformations as metamorphic relations.

Every transformation is a LABEL-PRESERVING metamorphic relation: applying it
must not change the gold provenance label (human stays human, machine stays
machine). Detector reliability = violation rate of these relations. This
constraint is what makes composition and symmetric (human-side) evaluation valid.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import numpy as np


@dataclass
class TransformResult:
    text: str
    transform: str
    category: str
    params: dict = field(default_factory=dict)


class MetamorphicRelation(ABC):
    name: str = "identity"
    category: str = "none"
    label_preserving: bool = True
    # semantics_lossy marks transforms (e.g. summarization) expected to alter
    # content; they exist to stress the QAES machinery and must be flagged.
    semantics_lossy: bool = False

    @abstractmethod
    def apply(self, text: str, rng: np.random.Generator) -> str: ...

    def __call__(self, text: str, seed: int = 0) -> TransformResult:
        rng = np.random.default_rng(seed)
        return TransformResult(
            text=self.apply(text, rng),
            transform=self.name,
            category=self.category,
            params=self.params(),
        )

    def params(self) -> dict:
        return {}


REGISTRY: dict[str, type[MetamorphicRelation]] = {}


def register(cls: type[MetamorphicRelation]) -> type[MetamorphicRelation]:
    if cls.name in REGISTRY:
        raise ValueError(f"duplicate transform name: {cls.name}")
    REGISTRY[cls.name] = cls
    return cls


class Identity(MetamorphicRelation):
    name = "identity"
    category = "none"

    def apply(self, text: str, rng: np.random.Generator) -> str:
        return text


register(Identity)
