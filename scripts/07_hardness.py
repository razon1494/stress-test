"""Stage 7: hardness scoring on clean test examples + Hardness Collapse Index.

Builds the 5 signals per docs/design (perplexity closeness, readability
normality, semantic consistency, lexical diversity, committee margin), fits
weights against a LEAVE-ONE-OUT committee (never includes the detector being
scored for HCI), and reports HCI per detector alongside the reliability cards.

Perplexity reuses the cached perplexity-detector score (already -mean NLL);
semantic consistency reuses meta.semsim from the paraphrase_t5 condition
(already computed in stage 2, so no extra forward passes needed).

Usage: python scripts/07_hardness.py --cache results/cache --data data/processed --out results
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import textstat

from stress_test.data.sources import load_jsonl
from stress_test.hardness import (
    HardnessScorer,
    committee_margin,
    fit_weights,
    lexical_diversity_normality,
    mtld,
    perplexity_closeness,
    readability_normality,
    semantic_consistency,
)
from stress_test.metrics import hardness_collapse_index


def build_signals(records: list, cache: Path, summary: dict) -> tuple[np.ndarray, dict, np.ndarray]:
    """Returns (doc_ids array, signals dict, domain-groups array) aligned to `records`."""
    doc_ids = np.array([r.doc_id for r in records])
    domains = np.array([r.domain for r in records])
    id_to_idx = {d: i for i, d in enumerate(doc_ids)}

    fkgl = np.array([textstat.flesch_kincaid_grade(r.text) if r.text.strip() else 0.0 for r in records])
    mtld_vals = np.array([mtld(r.text.split()) for r in records])

    ppl_path = cache / "perplexity__clean.csv"
    log_ppl = np.zeros(len(records))
    if ppl_path.exists():
        ppl_df = pd.read_csv(ppl_path)
        for _, row in ppl_df.iterrows():
            if row["doc_id"] in id_to_idx:
                log_ppl[id_to_idx[row["doc_id"]]] = -row["score"]  # score = -mean NLL

    para_path = Path("data/transformed/paraphrase_t5.jsonl")
    semsim = np.full(len(records), np.nan)
    if para_path.exists():
        for row in load_jsonl(para_path):
            if row.doc_id in id_to_idx and "semsim" in row.meta:
                semsim[id_to_idx[row.doc_id]] = row.meta["semsim"]
    has_semsim = ~np.isnan(semsim)

    detector_names = sorted(summary)
    committee_probs = {}
    for name in detector_names:
        path = cache / f"{name}__clean.csv"
        if not path.exists():
            continue
        df = pd.read_csv(path).drop_duplicates(subset="doc_id").set_index("doc_id")
        raw = df["score"].reindex(doc_ids).to_numpy()
        # min-max normalize each detector's raw score to a pseudo-probability
        lo, hi = np.nanmin(raw), np.nanmax(raw)
        committee_probs[name] = (raw - lo) / (hi - lo) if hi > lo else np.full_like(raw, 0.5)

    signals_base = {
        "perplexity_closeness": perplexity_closeness(log_ppl, domains),
        "readability_normality": readability_normality(fkgl, domains),
        "lexical_diversity": lexical_diversity_normality(mtld_vals, domains),
    }
    return doc_ids, {
        "base": signals_base,
        "semsim": semsim,
        "has_semsim": has_semsim,
        "committee_probs": committee_probs,
    }, domains


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="results/cache")
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--out", default="results")
    parser.add_argument("--eval-conditions", nargs="*", default=["clean", "paraphrase_t5"],
                        help="hardness is always computed from CLEAN-text signals; accuracy "
                             "(and hence HCI) is measured on each of these conditions in turn, "
                             "since collapse-on-hard-examples is most visible post-transformation")
    args = parser.parse_args()

    cache = Path(args.cache)
    summary = json.loads((cache / "summary.json").read_text())
    from stress_test.data import load_manifest

    manifest = load_manifest(Path(args.data) / "split_manifest.json")
    all_records = list(load_jsonl(Path(args.data) / "clean.jsonl"))
    test_records = [r for r in all_records if manifest.get(r.doc_id, "").startswith("test")]
    # hardness needs a paraphrase-similarity signal, only computed for the
    # 150-doc subsample in stage 2 — restrict to examples that have it
    doc_ids, built, domains = build_signals(test_records, cache, summary)
    valid = built["has_semsim"]
    if valid.sum() < 20:
        raise SystemExit("too few examples with paraphrase semsim; run stage 2 with more --limit docs")

    # weights are fit ONCE per detector (on the condition with the most error
    # variance, so logistic regression has signal to learn from) and then
    # FROZEN — the same hardness score is reused to evaluate HCI across every
    # eval condition, per the design in hardness/score.py
    fit_condition = args.eval_conditions[-1]
    lines = ["# Hardness-Aware Evaluation", "",
              f"*{int(valid.sum())} test examples with paraphrase-similarity signal "
              f"(others lack semantic_consistency and are excluded). Hardness weights fit "
              f"once per detector on `{fit_condition}`, then frozen and reused below.*", "",
              "| Detector | Condition | HCI | Acc by hardness quintile (easy -> hard) |",
              "|---|---|---|---|"]
    payload = {}

    detector_names = sorted(summary)
    for held_out in detector_names:
        committee = [n for n in detector_names if n != held_out and n in built["committee_probs"]]
        if not committee:
            continue
        mean_prob = np.mean([built["committee_probs"][n][valid] for n in committee], axis=0)
        signals = {
            **{k: v[valid] for k, v in built["base"].items()},
            "semantic_consistency": semantic_consistency(built["semsim"][valid]),
            "committee_margin": committee_margin(mean_prob),
        }
        threshold = summary[held_out]["threshold"]

        def load_correct(condition: str) -> np.ndarray | None:
            path = cache / f"{held_out}__{condition}.csv"
            if not path.exists():
                return None
            df = (
                pd.read_csv(path).drop_duplicates(subset="doc_id")
                .set_index("doc_id").reindex(doc_ids[valid])
            )
            return ((df["score"] > threshold).astype(int) == df["label"]).to_numpy()

        fit_correct = load_correct(fit_condition)
        if fit_correct is None:
            continue
        weights = fit_weights(signals, committee_error=1 - fit_correct)
        scorer = HardnessScorer(weights)
        hardness = scorer.score(signals)

        payload[held_out] = {"weights": weights, "by_condition": {}}
        for condition in args.eval_conditions:
            correct = fit_correct if condition == fit_condition else load_correct(condition)
            if correct is None:
                continue
            hci = hardness_collapse_index(correct, hardness)
            payload[held_out]["by_condition"][condition] = hci
            acc_str = " -> ".join(
                f"{a:.0%}" if not np.isnan(a) else "n/a" for a in hci["acc_by_quantile"]
            )
            lines.append(f"| {held_out} | {condition} | {hci['hci']:.3f} | {acc_str} |")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "HARDNESS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "hardness.json").write_text(json.dumps(payload, indent=2, default=float), encoding="utf-8")
    print(f"wrote {out / 'HARDNESS.md'}")


if __name__ == "__main__":
    main()
