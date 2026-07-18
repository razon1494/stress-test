"""Non-native-writer fairness subset (see docs/related_work.md, claim 6).

Liang et al.'s public release (github.com/Weixin-Liang/ChatGPT-Detector-Bias)
gives us, for free and with no registration: 91 real non-native TOEFL essays,
91 GPT-4-"enhanced" versions of the same essays, and native-speaker baselines
(88 Hewlett student essays, 70 college essays). Their data.json in each folder
is a plain [{"document": text}, ...] list with no detector scores attached.

ICNALE (registration required, password-gated, license PROHIBITS
redistribution) is the larger-scale complement: 5,600 essays across 10
countries and 4 CEFR proficiency bands, with matched native-speaker reference
data. Both sources are read from data/external/ and must stay out of git
(see .gitignore) — never commit raw text from either corpus.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator

from stress_test.data.schema import Record, make_doc_id


def load_liang_toefl(
    root: str | Path = "data/external/liang_toefl_src/Data_and_Results/Human_Data",
) -> Iterator[Record]:
    """label=0 (human) for all folders; ``meta.native`` marks the fairness axis.
    TOEFL_gpt4polished_91 is GPT-4-edited TOEFL text, not machine-generated
    from scratch — kept human-labeled with a transform tag, not label=1."""
    root = Path(root)
    folders = {
        "TOEFL_real_91": {"native": False, "transform": "clean"},
        "TOEFL_gpt4polished_91": {"native": False, "transform": "gpt4_polish"},
        "HewlettStudentEssay_real_88": {"native": True, "transform": "clean"},
        "CollegeEssay_real_70": {"native": True, "transform": "clean"},
    }
    for folder, meta in folders.items():
        path = root / folder / "data.json"
        if not path.exists():
            continue
        docs = json.loads(path.read_text(encoding="utf-8"))
        for row in docs:
            text = row["document"].strip()
            if not text:
                continue
            yield Record(
                text=text,
                label=0,
                doc_id=make_doc_id(text, f"liang_{folder}"),
                domain="toefl" if "TOEFL" in folder else "student_essay",
                generator="human",
                source_dataset="liang_toefl_bias",
                transform=meta["transform"],
                meta={"native": meta["native"]},
            )


def load_wi_locness(
    root: str | Path = "data/external/wi+locness/json",
    per_band: int | None = None,
) -> Iterator[Record]:
    """W&I+LOCNESS v2.1 (BEA-2019, immediately downloadable, non-commercial):
    CEFR-graded non-native essays (bands A/B/C) + native LOCNESS essays (N).

    Each record's meta carries the gold character-offset edits so
    build_human_edit_records() can produce the REAL human-corrected version —
    the one transformation we refused to fake with a model."""
    root = Path(root)
    files = {
        "A": ["A.train.json", "A.dev.json"],
        "B": ["B.train.json", "B.dev.json"],
        "C": ["C.train.json", "C.dev.json"],
        "N": ["N.dev.json"],
    }
    for band, names in files.items():
        count = 0
        for name in names:
            path = root / name
            if not path.exists():
                continue
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    if per_band is not None and count >= per_band:
                        break
                    row = json.loads(line)
                    text = row["text"].strip()
                    if not text:
                        continue
                    count += 1
                    native = band == "N"
                    yield Record(
                        text=text,
                        label=0,
                        doc_id=make_doc_id(text, f"wi_locness_{row['id']}"),
                        domain="locness" if native else "wi_learner",
                        generator="human",
                        source_dataset="wi_locness",
                        transform="clean",
                        meta={
                            "native": native,
                            "cefr": row.get("cefr") or ("N" if native else ""),
                            "edits": row.get("edits") or [],
                        },
                    )


def apply_gold_edits(text: str, edits: list) -> str:
    """Applies the first annotator's character-offset edits (right-to-left so
    earlier offsets stay valid). Detection-only edits (None correction) are
    skipped."""
    if not edits:
        return text
    spans = [e for e in edits[0][1] if e[2] is not None]
    for start, end, replacement in sorted(spans, key=lambda e: e[0], reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def build_human_edit_records(records: list[Record]) -> list[Record]:
    """The 'human_edit' condition: each W&I/LOCNESS text as its own annotator
    actually corrected it. Same doc_id as the clean record, so the paired
    FAR-drift analysis works unchanged."""
    out = []
    for record in records:
        corrected = apply_gold_edits(record.text, record.meta.get("edits") or [])
        meta = {k: v for k, v in record.meta.items() if k != "edits"}
        out.append(
            Record(
                text=corrected,
                label=record.label,
                doc_id=record.doc_id,
                domain=record.domain,
                generator=record.generator,
                source_dataset=record.source_dataset,
                transform="human_edit",
                meta=meta,
            )
        )
    return out


def load_icnale_written_essays(
    root: str | Path = "data/external/icnale",
) -> Iterator[Record]:
    """Parses ICNALE's file-naming convention:
    WE_<Region>_<Task>_<StudentID>_<CEFR>.txt (native speakers use region 'ENS').
    Adjust the glob/parse below once you've unzipped the real archive and can
    confirm the exact folder layout (Merged/Plain_Text vs Unmerged/Classified)."""
    root = Path(root)
    if not root.exists():
        raise FileNotFoundError(
            f"{root} not found — unzip the password-protected ICNALE WE archive here first"
        )
    for path in sorted(root.rglob("*.txt")):
        parts = path.stem.split("_")
        if len(parts) < 5:
            continue
        _, region, _task, student_id, *cefr = parts
        text = path.read_text(encoding="utf-8-sig").strip()
        if not text:
            continue
        native = region.upper() in {"ENS", "ENL"}  # ICNALE's native-speaker code
        yield Record(
            text=text,
            label=0,
            doc_id=make_doc_id(text, f"icnale_{path.stem}"),
            domain="icnale_essay",
            generator="human",
            source_dataset="icnale_we",
            transform="clean",
            meta={"native": native, "region": region, "cefr": "_".join(cefr), "student_id": student_id},
        )
