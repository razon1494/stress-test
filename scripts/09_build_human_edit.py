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

    clean = list(load_jsonl(Path(args.data) / "clean.jsonl"))

    wi_source = [r for r in clean if r.source_dataset == "wi_locness"]
    source, edited = list(wi_source), build_human_edit_records(wi_source)

    # ICNALE EE: professionally edited counterparts, paired by doc_id with the
    # EE originals that stage 1 put into clean.jsonl
    ee_clean_ids = {r.doc_id for r in clean if r.source_dataset == "icnale_ee"}
    if ee_clean_ids:
        from stress_test.data.non_native import load_icnale_edited_pairs

        ee_orig, ee_edit = load_icnale_edited_pairs()
        for orig, edit in zip(ee_orig, ee_edit):
            if orig.doc_id in ee_clean_ids:
                source.append(orig)
                edited.append(edit)

    if not source:
        raise SystemExit(
            "no wi_locness or icnale_ee records in clean.jsonl — rerun "
            "scripts/01_build_dataset.py with --wi-locness-per-band N / --include-icnale-ee"
        )

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
