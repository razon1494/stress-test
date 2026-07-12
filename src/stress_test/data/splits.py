"""Contamination-safe splitting.

Rules (any violation invalidates the benchmark — tests enforce rule 1):
1. Split by doc_id: a source document and ALL its machine/transformed
   counterparts land in exactly one split.
2. Assignment is a deterministic hash of doc_id — stable across runs and
   machines, no RNG state to lose.
3. OOD slices additionally hold out entire generators / domains.
4. Transformed variants exist ONLY in test; detector training sees clean
   train-split data only.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

SPLITS = ("train", "val", "test")


def assign_split(doc_id: str, train: float = 0.7, val: float = 0.1) -> str:
    bucket = int(hashlib.sha256(doc_id.encode()).hexdigest(), 16) % 10_000 / 10_000
    if bucket < train:
        return "train"
    if bucket < train + val:
        return "val"
    return "test"


def build_manifest(
    records: list,
    holdout_generators: tuple[str, ...] = (),
    holdout_domains: tuple[str, ...] = (),
) -> dict:
    """doc_id -> split. OOD holdouts go to dedicated test slices regardless of
    their hash bucket."""
    manifest: dict[str, str] = {}
    for record in records:
        if record.generator in holdout_generators:
            manifest[record.doc_id] = "test_ood_generator"
        elif record.domain in holdout_domains:
            manifest[record.doc_id] = "test_ood_domain"
        else:
            manifest.setdefault(record.doc_id, assign_split(record.doc_id))
    return manifest


def save_manifest(manifest: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "n_docs": len(manifest),
        "checksum": hashlib.sha256(
            json.dumps(manifest, sort_keys=True).encode()
        ).hexdigest(),
        "assignments": manifest,
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_manifest(path: str | Path) -> dict:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return payload["assignments"]
