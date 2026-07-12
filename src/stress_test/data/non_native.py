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
