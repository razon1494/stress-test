"""Stage 11: build the human-annotation batch for QAES validation.

Draws a stratified sample of (original, transformed) pairs across the semantic
transforms, shuffles them with the condition HIDDEN from annotators, and writes
one CSV per annotator: everyone rates the same overlap block (for Krippendorff
alpha), then disjoint blocks of the remainder.

  python scripts/11_make_annotation_batch.py --annotators 3          # build
  python scripts/11_make_annotation_batch.py --score sheets/*.csv    # agreement

Ratings: same_meaning in {0,1}; fluency in 1-5. See docs/annotation_guidelines.md.
"""

import argparse
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd

from stress_test.data.sources import load_jsonl

CONDITIONS = ["paraphrase_t5", "roundtrip_fr", "launder_lite", "grammar_correct", "human_edit"]


def build(args) -> None:
    clean = {(r.doc_id, r.label): r.text for r in load_jsonl(Path(args.data) / "clean.jsonl")}
    pairs = []
    for condition in CONDITIONS:
        path = Path(args.transformed) / f"{condition}.jsonl"
        if not path.exists():
            continue
        rows = [r for r in load_jsonl(path) if (r.doc_id, r.label) in clean]
        # deterministic per-condition subsample, stable across machines
        rows.sort(key=lambda r: hashlib.sha256(f"{condition}:{r.doc_id}:{r.label}".encode()).hexdigest())
        for r in rows[: args.per_condition]:
            pairs.append({
                "pair_id": hashlib.sha256(f"{condition}:{r.doc_id}:{r.label}".encode()).hexdigest()[:10],
                "condition": condition,  # stripped from annotator sheets
                "original": clean[(r.doc_id, r.label)],
                "transformed": r.text,
            })

    rng = np.random.default_rng(0)
    rng.shuffle(pairs)
    overlap, rest = pairs[: args.overlap], pairs[args.overlap :]
    chunks = np.array_split(np.array(rest, dtype=object), args.annotators)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(pairs).to_csv(out / "answer_key.csv", index=False)  # keep private
    for i in range(args.annotators):
        sheet = pd.DataFrame(overlap + list(chunks[i]))[["pair_id", "original", "transformed"]]
        sheet["same_meaning_0or1"] = ""
        sheet["fluency_1to5"] = ""
        sheet["comments"] = ""
        sheet.to_csv(out / f"annotator_{i + 1}.csv", index=False)
        print(f"annotator_{i + 1}.csv: {len(sheet)} pairs ({args.overlap} shared)")
    print(f"total unique pairs: {len(pairs)}; answer key (with conditions) -> {out / 'answer_key.csv'}")


def krippendorff_alpha_binary(ratings: pd.DataFrame) -> float:
    """Krippendorff's alpha for binary same_meaning ratings; rows = pair_id,
    columns = annotators, NaN = missing."""
    values = ratings.to_numpy(dtype=float)
    pairable = [row[~np.isnan(row)] for row in values if (~np.isnan(row)).sum() >= 2]
    n_pairable = sum(len(row) for row in pairable)
    if n_pairable == 0:
        return float("nan")
    disagreement_obs = 0.0
    denom = 0
    for row in pairable:
        m = len(row)
        disagreement_obs += (row.sum() * (m - row.sum())) / (m - 1)
        denom += m
    d_o = 2 * disagreement_obs / denom
    p = np.concatenate(pairable).mean()
    d_e = 2 * p * (1 - p) * denom / (denom - 1)
    return float(1 - d_o / d_e) if d_e > 0 else float("nan")


def score(args) -> None:
    frames = []
    for i, path in enumerate(args.score):
        df = pd.read_csv(path)[["pair_id", "same_meaning_0or1"]]
        df = df.rename(columns={"same_meaning_0or1": f"a{i}"})
        frames.append(df.set_index("pair_id"))
    merged = pd.concat(frames, axis=1)
    alpha = krippendorff_alpha_binary(merged)
    print(f"Krippendorff alpha (binary same_meaning, {len(args.score)} annotators): {alpha:.3f}")

    key = pd.read_csv(Path(args.out) / "answer_key.csv").set_index("pair_id")
    merged["human_same"] = merged.mean(axis=1) >= 0.5
    joined = key.join(merged["human_same"], how="inner")
    print("\nHuman-judged meaning preservation by condition:")
    print(joined.groupby("condition")["human_same"].agg(["mean", "count"]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--transformed", default="data/transformed")
    parser.add_argument("--out", default="annotation")
    parser.add_argument("--per-condition", type=int, default=120)
    parser.add_argument("--overlap", type=int, default=200)
    parser.add_argument("--annotators", type=int, default=3)
    parser.add_argument("--score", nargs="*", default=None,
                        help="filled annotator sheets: compute agreement + per-condition rates")
    args = parser.parse_args()
    if args.score:
        score(args)
    else:
        build(args)


if __name__ == "__main__":
    main()
