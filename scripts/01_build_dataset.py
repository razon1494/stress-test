"""Stage 1: pull free corpora into the canonical schema + split manifest.

Usage: python scripts/01_build_dataset.py --out data/processed --hc3-per-domain 500
"""

import argparse
from pathlib import Path

from stress_test.data import build_manifest, save_manifest
from stress_test.data.non_native import load_liang_toefl
from stress_test.data.sources import load_hc3, write_jsonl


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/processed")
    parser.add_argument("--hc3-per-domain", type=int, default=500)
    parser.add_argument("--min-words", type=int, default=50)
    parser.add_argument("--holdout-generators", nargs="*", default=[])
    parser.add_argument("--holdout-domains", nargs="*", default=[])
    parser.add_argument("--include-fairness-subset", action="store_true",
                        help="add the Liang et al. TOEFL/native-essay corpus (fairness/FAR analysis)")
    args = parser.parse_args()

    records = list(load_hc3(max_per_domain=args.hc3_per_domain))
    if args.include_fairness_subset:
        records += list(load_liang_toefl())
    # drop the WHOLE pair if either side is too short: detection on tiny texts
    # is noise, and asymmetric filtering would break the matched-pair design
    too_short = {r.doc_id for r in records if len(r.text.split()) < args.min_words}
    records = [r for r in records if r.doc_id not in too_short]
    # TODO(week 2): add MAGE / RAID-sample / ICNALE loaders here
    out = Path(args.out)
    n = write_jsonl(records, out / "clean.jsonl")
    # the curated fairness subset is small and unpaired; never train on it —
    # force it entirely into a dedicated test slice like any other OOD holdout
    holdout_domains = set(args.holdout_domains)
    if args.include_fairness_subset:
        holdout_domains |= {"toefl", "student_essay"}
    manifest = build_manifest(
        records,
        holdout_generators=tuple(args.holdout_generators),
        holdout_domains=tuple(holdout_domains),
    )
    save_manifest(manifest, out / "split_manifest.json")
    print(f"wrote {n} records, {len(manifest)} docs -> {out}")


if __name__ == "__main__":
    main()
