"""Stage 4: reliability cards + leaderboard from stage-3 caches.

Computes headline metrics from summary.json and QAES per condition from the
per-example score csvs (evaded = machine text scored below the frozen
threshold, conditioned on meta.semsim >= tau).

Usage: python scripts/04_make_report.py --cache results/cache --out results
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from stress_test.metrics import qaes, robustness_score, transformation_stability, worst_case_performance
from stress_test.report import leaderboard_table, make_reliability_card
from stress_test.semantics import QAES_SEM_THRESHOLD
from stress_test.transforms.compose import NAMED_PIPELINES


def condition_qaes(csv_path: Path, threshold: float) -> dict | None:
    df = pd.read_csv(csv_path)
    machine = df[df["label"] == 1].dropna(subset=["semsim"])
    if machine.empty:
        return None
    evaded = (machine["score"] <= threshold).to_numpy()
    return qaes(evaded, machine["semsim"].to_numpy(), sem_threshold=QAES_SEM_THRESHOLD)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="results/cache")
    parser.add_argument("--out", default="results")
    args = parser.parse_args()

    cache = Path(args.cache)
    summary = json.loads((cache / "summary.json").read_text())
    cards, qaes_rows = {}, []
    for detector, payload in summary.items():
        conditions = payload["conditions"]
        threshold = payload["threshold"]
        clean = conditions["clean"]
        transformed_tpr = {n: c["tpr"] for n, c in conditions.items() if n != "clean"}
        results = {"clean_tpr": clean["tpr"], "far_clean": clean["fpr"]}

        qaes_values = []
        for name in conditions:
            if name == "clean":
                continue
            csv_path = cache / f"{detector}__{name}.csv"
            if csv_path.exists():
                q = condition_qaes(csv_path, threshold)
                if q is not None:
                    qaes_rows.append({"detector": detector, "condition": name, **q})
                    if not np.isnan(q["qaes"]):
                        qaes_values.append(q["qaes"])
        if qaes_values:
            results["qaes_mean"] = float(np.mean(qaes_values))

        if transformed_tpr:
            results["rs"] = robustness_score(clean["tpr"], transformed_tpr)["rs"]
            results["ts"] = transformation_stability(transformed_tpr)
            pipelines = {n: v for n, v in transformed_tpr.items() if n in NAMED_PIPELINES}
            wcp = worst_case_performance(pipelines or transformed_tpr)
            results["wcp"], results["worst_pipeline"] = wcp["wcp"], wcp["worst_pipeline"]
            fars = {n: c["fpr"] for n, c in conditions.items() if n != "clean"}
            worst_far = max(fars, key=fars.get)
            results["far_worst"], results["far_worst_transform"] = fars[worst_far], worst_far
        cards[detector] = results

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    report = "# STRESS-Test Leaderboard\n\n" + leaderboard_table(cards) + "\n"
    report += "\n".join(make_reliability_card(d, r) for d, r in cards.items())
    if qaes_rows:
        report += (
            f"\n## Quality-Adjusted Evasion (machine class, semsim >= {QAES_SEM_THRESHOLD})\n\n"
            "| Detector | Condition | Raw evasion | QAES | Valid fraction | n |\n|---|---|---|---|---|---|\n"
        )
        for row in qaes_rows:
            report += (
                f"| {row['detector']} | {row['condition']} | {row['raw_evasion']:.1%} "
                f"| {row['qaes']:.1%} | {row['valid_fraction']:.1%} | {row['n']} |\n"
            )
    (out / "REPORT.md").write_text(report, encoding="utf-8")
    print(f"wrote {out / 'REPORT.md'}")


if __name__ == "__main__":
    main()
