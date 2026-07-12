"""Stage 1: pull free corpora into the canonical schema + split manifest.

Usage: python scripts/01_build_dataset.py --out data/processed --hc3-per-domain 500
"""

import argparse
from pathlib import Path

from stress_test.data import build_manifest, save_manifest
from stress_test.data.sources import load_hc3, write_jsonl


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/processed")
    parser.add_argument("--hc3-per-domain", type=int, default=500)
    parser.add_argument("--holdout-generators", nargs="*", default=[])
    parser.add_argument("--holdout-domains", nargs="*", default=[])
    args = parser.parse_args()

    records = list(load_hc3(max_per_domain=args.hc3_per_domain))
    # TODO(week 2): add MAGE / RAID-sample / essay / non-native loaders here
    out = Path(args.out)
    n = write_jsonl(records, out / "clean.jsonl")
    manifest = build_manifest(
        records,
        holdout_generators=tuple(args.holdout_generators),
        holdout_domains=tuple(args.holdout_domains),
    )
    save_manifest(manifest, out / "split_manifest.json")
    print(f"wrote {n} records, {len(manifest)} docs -> {out}")


if __name__ == "__main__":
    main()
