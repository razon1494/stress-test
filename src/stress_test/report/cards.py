"""Reliability cards that summarize multiple detector behavior metrics."""

from __future__ import annotations


def make_reliability_card(detector: str, results: dict) -> str:
    """results keys: clean_tpr, rs, ts, wcp, worst_pipeline, far_clean,
    far_worst, far_worst_transform, hci, ece_clean, ece_shift, qaes_mean.
    Missing keys render as 'n/a' so partial runs still produce cards."""

    def fmt(key: str, pct: bool = False) -> str:
        value = results.get(key)
        if value is None:
            return "n/a"
        return f"{value:.1%}" if pct else f"{value:.3f}"

    return f"""## Reliability Card — {detector}

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | {fmt('clean_tpr', pct=True)} | sensitivity on the clean evaluation records |
| Robustness Score (RS) | {fmt('rs')} | mean retained performance across transforms |
| Transformation Stability (TS) | {fmt('ts')} | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | {fmt('wcp', pct=True)} | minimum observed TPR, on `{results.get('worst_pipeline', 'n/a')}` |
| False-Accusation Rate, clean | {fmt('far_clean', pct=True)} | FPR on clean human text |
| False-Accusation Rate, worst | {fmt('far_worst', pct=True)} | maximum observed human-text FPR, on `{results.get('far_worst_transform', 'n/a')}` |
| Hardness Collapse (HCI) | {fmt('hci')} | larger = stronger collapse; negative = higher hard-bin accuracy |
| ECE clean → shifted | {fmt('ece_clean')} → {fmt('ece_shift')} | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | {fmt('qaes_mean', pct=True)} | evasion among transforms passing the automated similarity filter |
"""


def leaderboard_table(cards: dict[str, dict]) -> str:
    header = (
        "| Detector | Clean TPR | RS | WCP | FAR (worst) | HCI |\n"
        "|---|---|---|---|---|---|\n"
    )
    rows = []
    # Sort by observed worst-case performance for a consistent presentation.
    for name, r in sorted(cards.items(), key=lambda kv: -(kv[1].get("wcp") or 0)):
        rows.append(
            f"| {name} | {r.get('clean_tpr', float('nan')):.1%} | "
            f"{r.get('rs', float('nan')):.3f} | {r.get('wcp', float('nan')):.1%} | "
            f"{r.get('far_worst', float('nan')):.1%} | {r.get('hci', float('nan')):.3f} |"
        )
    return header + "\n".join(rows) + "\n"
