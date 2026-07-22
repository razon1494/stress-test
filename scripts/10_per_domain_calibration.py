"""Stage 10: per-domain calibration reanalysis (RAID-style), from cached scores.

The pooled 1%-FPR threshold is dominated by whichever human register fills the
calibration pool (Sec. 'Calibration-pool sensitivity' in the paper). Here each
detector gets one threshold PER DOMAIN, calibrated on that domain's clean human
scores (falling back to the pooled threshold when a domain has too few human
docs), and every cached condition is re-evaluated at each record's own domain
threshold. No model forwards — everything comes from results/cache/*.csv.

Usage: python scripts/10_per_domain_calibration.py
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from stress_test.data.sources import load_jsonl
from stress_test.metrics import robustness_score, worst_case_performance
from stress_test.transforms.compose import NAMED_PIPELINES


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="results/cache")
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--out", default="results")
    parser.add_argument("--target-fpr", type=float, default=0.01)
    parser.add_argument("--min-human-docs", type=int, default=30)
    args = parser.parse_args()

    cache = Path(args.cache)
    summary = json.loads((cache / "summary.json").read_text())
    records = list(load_jsonl(Path(args.data) / "clean.jsonl"))
    doc_domain = {r.doc_id: r.domain for r in records}

    conditions = sorted({p.stem.split("__", 1)[1] for p in cache.glob("*__*.csv")})
    lines = ["# Per-Domain Calibration Sensitivity Analysis", "",
             "> **Interpretation note.** Thresholds are estimated and evaluated on records "
             "from the same dataset slices. This analysis measures sensitivity to the "
             "calibration strategy; it is not an independently held-out estimate.", "",
             f"*One threshold per (detector, domain), calibrated at {args.target_fpr:.0%} FPR "
             f"on that domain's clean human text; domains with <{args.min_human_docs} human "
             "docs fall back to the pooled threshold. Same cached scores as the pooled analysis.*",
             "", "## Headline (per-domain calibrated)", "",
             "| Detector | Clean TPR | Clean FPR | RS | WCP (worst pipeline) | FAR grammar | FAR human-edit |",
             "|---|---|---|---|---|---|---|"]
    payload = {}

    for detector in sorted(summary):
        clean_df = pd.read_csv(cache / f"{detector}__clean.csv").drop_duplicates(subset=["doc_id", "label"])
        clean_df["domain"] = clean_df["doc_id"].map(doc_domain)
        pooled_threshold = summary[detector]["threshold"]

        thresholds = {}
        for domain, group in clean_df[clean_df["label"] == 0].groupby("domain"):
            if len(group) >= args.min_human_docs:
                thresholds[domain] = float(
                    np.quantile(group["score"], 1 - args.target_fpr, method="higher")
                )

        def evaluate(df: pd.DataFrame) -> dict:
            df = df.copy()
            df["domain"] = df["doc_id"].map(doc_domain)
            df["thr"] = df["domain"].map(thresholds).fillna(pooled_threshold)
            flagged = df["score"] > df["thr"]
            machine, human = df["label"] == 1, df["label"] == 0
            return {
                "tpr": float(flagged[machine].mean()) if machine.any() else float("nan"),
                "fpr": float(flagged[human].mean()) if human.any() else float("nan"),
                "n": int(len(df)),
            }

        results = {}
        for condition in conditions:
            path = cache / f"{detector}__{condition}.csv"
            if path.exists():
                results[condition] = evaluate(pd.read_csv(path).drop_duplicates(subset=["doc_id", "label"]))

        clean = results["clean"]
        transformed_tpr = {
            c: r["tpr"] for c, r in results.items()
            if c != "clean" and not np.isnan(r["tpr"])
        }
        rs = robustness_score(clean["tpr"], transformed_tpr)["rs"] if clean["tpr"] > 0 else float("nan")
        pipelines = {c: v for c, v in transformed_tpr.items() if c in NAMED_PIPELINES}
        wcp = worst_case_performance(pipelines or transformed_tpr)
        far_grammar = results.get("grammar_correct", {}).get("fpr", float("nan"))
        far_edit = results.get("human_edit", {}).get("fpr", float("nan"))

        payload[detector] = {"thresholds": thresholds, "pooled_threshold": pooled_threshold,
                             "conditions": results, "rs": rs, "wcp": wcp}
        lines.append(
            f"| {detector} | {clean['tpr']:.1%} | {clean['fpr']:.1%} | {rs:.3f} "
            f"| {wcp['wcp']:.1%} ({wcp['worst_pipeline']}) | {far_grammar:.1%} | {far_edit:.1%} |"
        )

    lines += ["", "## Per-condition TPR/FPR (per-domain calibrated)", "",
              "| Detector | Condition | TPR | FPR |", "|---|---|---|---|"]
    for detector, p in payload.items():
        for condition, r in p["conditions"].items():
            lines.append(f"| {detector} | {condition} | {r['tpr']:.1%} | {r['fpr']:.1%} |")

    out = Path(args.out)
    (out / "PER_DOMAIN.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "per_domain.json").write_text(json.dumps(payload, indent=2, default=float), encoding="utf-8")
    print(f"wrote {out / 'PER_DOMAIN.md'}")


if __name__ == "__main__":
    main()
