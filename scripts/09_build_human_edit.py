"""Stage 9: the human_edit condition from W&I+LOCNESS gold annotations.

Applies each essay's REAL annotator corrections (character-offset gold edits)
to produce the human-corrected version — genuine human editing, not a model's
imitation of it. Written as a standard transformed-condition jsonl (same
doc_ids, meta.semsim included) so stages 3/6 consume it unchanged.

Usage: python scripts/09_build_human_edit.py
"""

import argparse
from pathlib import Path

from stress_test.data.non_native import build_human_edit_records
from stress_test.data.sources import load_jsonl, write_jsonl


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--out", default="data/transformed")
    args = parser.parse_args()

    source = [
        r for r in load_jsonl(Path(args.data) / "clean.jsonl")
        if r.source_dataset == "wi_locness"
    ]
    if not source:
        raise SystemExit(
            "no wi_locness records in clean.jsonl — rerun scripts/01_build_dataset.py "
            "with --wi-locness-per-band N"
        )
    edited = build_human_edit_records(source)

    from stress_test.semantics import semantic_similarity

    sims = semantic_similarity([r.text for r in source], [r.text for r in edited])
    changed = 0
    for original, record, sim in zip(source, edited, sims):
        record.meta["semsim"] = round(float(sim), 4)
        changed += record.text != original.text
    n = write_jsonl(edited, Path(args.out) / "human_edit.jsonl")
    print(f"human_edit: {n} records ({changed} actually changed by their annotator)")


if __name__ == "__main__":
    main()
