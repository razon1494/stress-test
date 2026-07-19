"""Stage 12: paper figures.

Figure 1 — GPT-2 log-perplexity distributions by corpus group. Substantiates
the register-mediation account (paper Sec. 'The register twist'): non-native
TOEFL essays AND native topic-controlled prompt essays both sit closer to the
machine-text region than open-register human writing does.

Usage: python scripts/12_make_figures.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

from stress_test.data.sources import load_jsonl

GROUPS = [
    # (key, human-readable row label) — assignment function below
    ("hc3_machine", "ChatGPT (HC3)"),
    ("hc3_human", "Human, open register (HC3)"),
    ("toefl", "Non-native TOEFL essays"),
    ("student_essay", "Native student essays"),
    ("wi_learner", "Learner essays (W&I)"),
    ("locness", "Native essays (LOCNESS)"),
    ("icnale_learner", "Learner prompt essays (ICNALE)"),
    ("icnale_native", "NATIVE prompt essays (ICNALE)"),
]

MACHINE_COLOR = "#4269D0"
HUMAN_COLOR = "#9CA3AF"


def group_of(record) -> str | None:
    if record.source_dataset == "hc3":
        return "hc3_machine" if record.label == 1 else "hc3_human"
    if record.domain in {"toefl", "student_essay", "wi_learner", "locness",
                         "icnale_learner", "icnale_native"}:
        # only the untouched originals; gpt4-polished TOEFL variants excluded
        return record.domain if record.transform == "clean" else None
    return None


def main() -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    scores = pd.read_csv("results/cache/perplexity__clean.csv").drop_duplicates(
        subset=["doc_id", "label"]
    )
    # perplexity detector score = -mean token NLL; flip so low = predictable
    score_map = {(row.doc_id, row.label): -row.score for row in scores.itertuples()}

    values: dict[str, list[float]] = {key: [] for key, _ in GROUPS}
    for record in load_jsonl("data/processed/clean.jsonl"):
        group = group_of(record)
        if group in values and (record.doc_id, record.label) in score_map:
            values[group].append(score_map[(record.doc_id, record.label)])

    rows = [(key, label, values[key]) for key, label in GROUPS if len(values[key]) >= 20]
    rows.sort(key=lambda r: float(np.median(r[2])))

    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    positions = np.arange(len(rows))
    for pos, (key, label, vals) in zip(positions, rows):
        color = MACHINE_COLOR if key == "hc3_machine" else HUMAN_COLOR
        box = ax.boxplot(
            [vals], positions=[pos], vert=False, widths=0.62, patch_artist=True,
            showfliers=False, whis=(5, 95),
            boxprops=dict(facecolor=color, edgecolor="none", alpha=0.85),
            whiskerprops=dict(color="#4B5563", linewidth=1),
            capprops=dict(color="#4B5563", linewidth=1),
            medianprops=dict(color="white", linewidth=1.6),
        )
        ax.text(-0.012, pos, f"{label}  (n={len(vals)})", transform=ax.get_yaxis_transform(),
                ha="right", va="center", fontsize=8.5, color="#111827")

    ax.set_yticks([])
    for spine in ("left", "top", "right"):
        ax.spines[spine].set_visible(False)
    ax.set_xlabel("GPT-2 mean token negative log-likelihood  (lower = more predictable)",
                  fontsize=9, color="#374151")
    ax.tick_params(axis="x", labelsize=8.5, colors="#374151")
    ax.set_xlim(left=max(0.0, ax.get_xlim()[0]))
    ax.grid(axis="x", color="#E5E7EB", linewidth=0.7)
    ax.set_axisbelow(True)
    fig.suptitle(
        "Predictable registers sit near the machine-text region — regardless of nativeness",
        fontsize=10, x=0.985, ha="right", y=0.98,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))

    out = Path("paper/figures")
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / "perplexity_by_corpus.pdf")
    fig.savefig(out / "perplexity_by_corpus.png", dpi=200)
    print(f"wrote {out / 'perplexity_by_corpus.pdf'} (+.png)")
    for key, label, vals in rows:
        print(f"  {label:38s} median {np.median(vals):.3f}")


if __name__ == "__main__":
    main()
