"""Stage 6: native vs non-native False-Accusation Rate under transformation.

The core fairness experiment (docs/related_work.md claim 6): does grammar
correction move FAR differently for non-native writers than for native ones?
Liang et al. showed non-native TOEFL essays get 61.22% FPR on CLEAN text with
commercial detectors; here we test whether a benign transform widens or closes
that gap for our own detectors, at their frozen 1%-FPR-on-HC3 threshold.

Usage: python scripts/06_fairness_analysis.py --cache results/cache --out results
"""

import argparse
import json
from pathlib import Path

import pandas as pd

from stress_test.data.sources import load_jsonl
from stress_test.stats import clustered_bootstrap_ci


def far_by_group(scores_df: pd.DataFrame, doc_native: dict, threshold: float) -> dict:
    scores_df = scores_df[scores_df["doc_id"].isin(doc_native)].copy()
    scores_df["native"] = scores_df["doc_id"].map(doc_native)
    out = {}
    for native, label in [(True, "native"), (False, "non_native")]:
        subset = scores_df[scores_df["native"] == native]
        if subset.empty:
            continue
        flagged = (subset["score"] > threshold).to_numpy(dtype=float)
        out[label] = clustered_bootstrap_ci(flagged, subset["doc_id"].to_numpy())
        out[label]["n"] = int(len(subset))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="results/cache")
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--out", default="results")
    parser.add_argument("--conditions", nargs="*", default=["clean", "grammar_correct"])
    args = parser.parse_args()

    cache = Path(args.cache)
    summary = json.loads((cache / "summary.json").read_text())
    fairness_records = [
        r for r in load_jsonl(Path(args.data) / "clean.jsonl")
        if r.domain in ("toefl", "student_essay")
    ]
    doc_native = {r.doc_id: bool(r.meta["native"]) for r in fairness_records}
    if not doc_native:
        raise SystemExit(
            "no toefl/student_essay records in data/processed/clean.jsonl — "
            "rerun scripts/01_build_dataset.py with --include-fairness-subset"
        )

    lines = ["# Fairness Analysis: Native vs Non-Native False-Accusation Rate", "",
              f"*Liang et al. (Patterns 2023) found 61.22% FPR on clean non-native TOEFL essays "
              f"with commercial detectors. n_native={sum(doc_native.values())}, "
              f"n_non_native={sum(not v for v in doc_native.values())}.*", "",
              "| Detector | Condition | Native FAR [95% CI] (n) | Non-native FAR [95% CI] (n) | Gap |",
              "|---|---|---|---|---|"]
    payload = {}

    for detector, det_payload in summary.items():
        threshold = det_payload["threshold"]
        for condition in args.conditions:
            path = cache / f"{detector}__{condition}.csv"
            if not path.exists():
                continue
            groups = far_by_group(pd.read_csv(path), doc_native, threshold)
            if "native" not in groups or "non_native" not in groups:
                continue
            nat, non = groups["native"], groups["non_native"]
            gap = non["point"] - nat["point"]
            payload[f"{detector}__{condition}"] = groups
            lines.append(
                f"| {detector} | {condition} "
                f"| {nat['point']:.1%} [{nat['ci_low']:.1%}, {nat['ci_high']:.1%}] ({nat['n']}) "
                f"| {non['point']:.1%} [{non['ci_low']:.1%}, {non['ci_high']:.1%}] ({non['n']}) "
                f"| {gap:+.1%} |"
            )

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "FAIRNESS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "fairness.json").write_text(json.dumps(payload, indent=2, default=float), encoding="utf-8")
    print(f"wrote {out / 'FAIRNESS.md'}")


if __name__ == "__main__":
    main()
