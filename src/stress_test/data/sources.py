"""Free corpus loaders (zero-budget: reuse public generation corpora instead of
paying to generate — see docs/zero_budget_plan.md).

Each loader yields Records in the canonical schema. ``datasets`` is an optional
dependency; loaders raise a clear error if it is missing.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator

from stress_test.data.schema import Record, make_doc_id


def _require_datasets():
    try:
        import datasets  # noqa: F401

        return datasets
    except ImportError as err:
        raise ImportError("pip install 'stress-test[data]' to use HF corpus loaders") from err


def load_hc3(max_per_domain: int | None = None) -> Iterator[Record]:
    """HC3: paired human/ChatGPT answers to the same questions — exactly the
    matched-pair structure our protocol needs."""
    datasets = _require_datasets()
    ds = datasets.load_dataset("Hello-SimpleAI/HC3", "all", split="train")
    counts: dict[str, int] = {}
    for row in ds:
        domain = row.get("source", "unknown")
        if max_per_domain is not None and counts.get(domain, 0) >= max_per_domain:
            continue
        human = (row.get("human_answers") or [None])[0]
        machine = (row.get("chatgpt_answers") or [None])[0]
        if not human or not machine:
            continue
        counts[domain] = counts.get(domain, 0) + 1
        doc_id = make_doc_id(row["question"], "hc3")
        yield Record(human.strip(), 0, doc_id, domain, "human", "hc3")
        yield Record(machine.strip(), 1, doc_id, domain, "chatgpt", "hc3")


def load_mage(split: str = "test", max_records: int | None = None) -> Iterator[Record]:
    """MAGE: 27 generators, 10 domains; brings generator diversity we do not
    pay for. Column names verified against yaful/MAGE at implementation time —
    re-check on first run."""
    datasets = _require_datasets()
    ds = datasets.load_dataset("yaful/MAGE", split=split)
    for i, row in enumerate(ds):
        if max_records is not None and i >= max_records:
            break
        label = int(row["label"])
        src = str(row.get("src", "unknown"))
        # MAGE encodes "<domain>_<generator>" in src; humans have generator 'human'
        domain, _, generator = src.partition("_")
        yield Record(
            row["text"].strip(),
            label,
            make_doc_id(row["text"], "mage"),
            domain or "unknown",
            generator or ("human" if label == 0 else "unknown"),
            "mage",
        )


def load_jsonl(path: str | Path) -> Iterator[Record]:
    """Local corpora (student essays, non-native subset, watermarked subset)
    stored as one canonical-schema JSON object per line."""
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield Record(**json.loads(line))


def write_jsonl(records: Iterator[Record] | list[Record], path: str | Path) -> int:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with open(path, "w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record.to_dict(), ensure_ascii=False) + "\n")
            n += 1
    return n
