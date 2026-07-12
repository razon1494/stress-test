"""Stage 4: reliability cards + leaderboard from stage-3 summaries.

Usage: python scripts/04_make_report.py --cache results/cache --out results
"""

import argparse
import json
from pathlib import Path

from stress_test.metrics import robustness_score, transformation_stability, worst_case_performance
from stress_test.report import leaderboard_table, make_reliability_card
from stress_test.transforms.compose import NAMED_PIPELINES


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="results/cache")
    parser.add_argument("--out", default="results")
    args = parser.parse_args()

    summary = json.loads((Path(args.cache) / "summary.json").read_text())
    cards = {}
    for detector, payload in summary.items():
        conditions = payload["conditions"]
        clean = conditions["clean"]
        transformed_tpr = {
            name: c["tpr"] for name, c in conditions.items() if name != "clean"
        }
        results = {"clean_tpr": clean["tpr"], "far_clean": clean["fpr"]}
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
    (out / "REPORT.md").write_text(report, encoding="utf-8")
    print(f"wrote {out / 'REPORT.md'}")


if __name__ == "__main__":
    main()
