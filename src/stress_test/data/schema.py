"""Canonical record schema shared by every pipeline stage.

label: 0 = human-written, 1 = machine-generated (never changed by transforms —
the metamorphic invariant). ``doc_id`` groups a source document with all of its
machine counterparts and transformed variants: splits and bootstrap clustering
both key on it.
"""

from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field


@dataclass
class Record:
    text: str
    label: int
    doc_id: str
    domain: str
    generator: str = "human"
    source_dataset: str = ""
    transform: str = "clean"
    meta: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


def make_doc_id(source_text: str, source_dataset: str) -> str:
    digest = hashlib.sha256(f"{source_dataset}::{source_text}".encode()).hexdigest()
    return digest[:16]
