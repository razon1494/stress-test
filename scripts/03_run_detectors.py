"""Stage 3: train (clean-only), calibrate at 1% FPR on clean human text, then
score every condition at the FROZEN threshold. Caches per-(detector, condition)
scores to csv so nothing runs twice.

Usage: python scripts/03_run_detectors.py --data data/processed --transformed data/transformed
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from stress_test.data import load_manifest
from stress_test.data.sources import load_jsonl
from stress_test.detectors import (
    StylometricDetector,
    TfidfLogReg,
    calibrate_threshold,
    evaluate_at_threshold,
)


def build_detectors(only: list[str] | None = None) -> list:
    detectors = [TfidfLogReg(), StylometricDetector()]
    # torch-backed detectors are optional so the pipeline runs on any machine;
    # their imports are lazy, so probe for torch itself rather than catching
    # an ImportError that would only surface at scoring time
    import importlib.util

    if importlib.util.find_spec("torch") is not None:
        from stress_test.detectors.transformer import TransformerDetector
        from stress_test.detectors.zero_shot import BinocularsLite, FastDetectGPT, PerplexityDetector

        detectors += [PerplexityDetector(), FastDetectGPT(), BinocularsLite(), TransformerDetector()]
        finetuned = Path("models/deberta_hc3")
        if finetuned.exists():
            detectors.append(
                TransformerDetector(
                    model_name=str(finetuned), machine_label="machine", name="deberta_hc3_ft"
                )
            )
    else:
        print("torch not installed: skipping model-backed detectors")
    if only:
        detectors = [d for d in detectors if d.name in only]
    return detectors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--transformed", default="data/transformed")
    parser.add_argument("--out", default="results/cache")
    parser.add_argument("--target-fpr", type=float, default=0.01)
    parser.add_argument("--only", nargs="*", default=None,
                        help="restrict to these detector names (default: all available)")
    args = parser.parse_args()

    manifest = load_manifest(Path(args.data) / "split_manifest.json")
    records = list(load_jsonl(Path(args.data) / "clean.jsonl"))
    split_of = lambda r: manifest.get(r.doc_id, "")  # noqa: E731
    train = [r for r in records if split_of(r) == "train"]
    test_clean = [r for r in records if split_of(r).startswith("test")]

    conditions = {"clean": test_clean}
    for path in sorted(Path(args.transformed).glob("*.jsonl")):
        conditions[path.stem] = list(load_jsonl(path))

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    # merge into the existing summary so a partial rerun (--only) never wipes
    # the cached results of detectors that were not re-scored
    summary_path = out_dir / "summary.json"
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
    for detector in build_detectors(only=args.only):
        detector.fit([r.text for r in train], np.array([r.label for r in train]))
        clean_scores = detector.score([r.text for r in test_clean])
        clean_labels = np.array([r.label for r in test_clean])
        threshold = calibrate_threshold(clean_scores[clean_labels == 0], args.target_fpr)

        summary[detector.name] = {"threshold": threshold, "conditions": {}}
        for name, recs in conditions.items():
            scores = clean_scores if name == "clean" else detector.score([r.text for r in recs])
            labels = np.array([r.label for r in recs])
            pd.DataFrame({
                "doc_id": [r.doc_id for r in recs], "label": labels, "score": scores,
                "semsim": [r.meta.get("semsim") for r in recs],
            }).to_csv(out_dir / f"{detector.name}__{name}.csv", index=False)
            summary[detector.name]["conditions"][name] = evaluate_at_threshold(
                scores, labels, threshold
            )
            print(f"{detector.name} / {name}: {summary[detector.name]['conditions'][name]}")

    summary_path.write_text(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
