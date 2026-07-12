"""Stage 5: publication-grade statistics over the stage-3 score caches.

- TPR/FPR per (detector, condition) with 95% document-clustered bootstrap CIs
  (a human text and its machine pair share a cluster).
- Detector-vs-detector paired sign-flip permutation tests per condition on
  per-example accuracy, Holm-Bonferroni corrected across conditions, with
  McNemar discordant counts for transparency.

Usage: python scripts/05_stats.py --cache results/cache --out results
"""

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import pandas as pd

from stress_test.stats import (
    clustered_bootstrap_ci,
    holm_bonferroni,
    mcnemar_exact,
    paired_permutation_test,
)


def rate_ci(df: pd.DataFrame, threshold: float, label: int, n_boot: int = 2000) -> dict:
    rows = df[df["label"] == label]
    flagged = (rows["score"] > threshold).to_numpy(dtype=float)
    return clustered_bootstrap_ci(flagged, rows["doc_id"].to_numpy(), n_boot=n_boot)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="results/cache")
    parser.add_argument("--out", default="results")
    parser.add_argument("--n-boot", type=int, default=2000)
    args = parser.parse_args()

    cache = Path(args.cache)
    summary = json.loads((cache / "summary.json").read_text())
    detectors = sorted(summary)
    conditions = sorted(
        {p.stem.split("__", 1)[1] for p in cache.glob("*__*.csv")}
    )

    lines = ["# STRESS-Test Statistics", "",
             "*95% document-clustered bootstrap CIs; thresholds frozen at 1% FPR on clean human text.*",
             "", "## Rates with confidence intervals", "",
             "| Detector | Condition | TPR [95% CI] | FPR [95% CI] |", "|---|---|---|---|"]
    payload: dict = {"rates": {}, "paired_tests": {}}

    for detector in detectors:
        threshold = summary[detector]["threshold"]
        for condition in conditions:
            path = cache / f"{detector}__{condition}.csv"
            if not path.exists():
                continue
            df = pd.read_csv(path)
            tpr = rate_ci(df, threshold, label=1, n_boot=args.n_boot)
            fpr = rate_ci(df, threshold, label=0, n_boot=args.n_boot)
            payload["rates"][f"{detector}__{condition}"] = {"tpr": tpr, "fpr": fpr}
            lines.append(
                f"| {detector} | {condition} "
                f"| {tpr['point']:.1%} [{tpr['ci_low']:.1%}, {tpr['ci_high']:.1%}] "
                f"| {fpr['point']:.1%} [{fpr['ci_low']:.1%}, {fpr['ci_high']:.1%}] |"
            )

    lines += ["", "## Paired detector comparisons (per-example accuracy)", ""]
    for det_a, det_b in itertools.combinations(detectors, 2):
        raw_p: dict[str, float] = {}
        results: dict[str, dict] = {}
        for condition in conditions:
            path_a, path_b = cache / f"{det_a}__{condition}.csv", cache / f"{det_b}__{condition}.csv"
            if not (path_a.exists() and path_b.exists()):
                continue
            a = pd.read_csv(path_a)
            b = pd.read_csv(path_b)
            merged = a.merge(b, on=["doc_id", "label"], suffixes=("_a", "_b"))
            thr_a, thr_b = summary[det_a]["threshold"], summary[det_b]["threshold"]
            correct_a = ((merged["score_a"] > thr_a).astype(int) == merged["label"]).to_numpy()
            correct_b = ((merged["score_b"] > thr_b).astype(int) == merged["label"]).to_numpy()
            perm = paired_permutation_test(correct_a, correct_b)
            results[condition] = {**perm, "mcnemar": mcnemar_exact(correct_a, correct_b)}
            raw_p[condition] = perm["p_value"]
        adjusted = holm_bonferroni(raw_p)
        lines += [f"### {det_a} vs {det_b}", "",
                  "| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |",
                  "|---|---|---|---|---|"]
        for condition, r in results.items():
            mc = r["mcnemar"]
            star = " *" if adjusted[condition] < 0.05 else ""
            lines.append(
                f"| {condition} | {r['mean_diff']:+.1%} | {mc['only_a']} / {mc['only_b']} "
                f"| {r['p_value']:.4f} | {adjusted[condition]:.4f}{star} |"
            )
        lines.append("")
        payload["paired_tests"][f"{det_a}__vs__{det_b}"] = {
            "conditions": results, "holm_adjusted": adjusted,
        }

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "STATS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "stats.json").write_text(json.dumps(payload, indent=2, default=float), encoding="utf-8")
    print(f"wrote {out / 'STATS.md'}")


if __name__ == "__main__":
    main()
