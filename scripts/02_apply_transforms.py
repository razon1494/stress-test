"""Stage 2: apply transforms/pipelines to TEST-split records (both classes —
the symmetric protocol). Emits one jsonl per condition; each output row keeps
its doc_id so downstream stages can cluster and pair.

Usage:
  python scripts/02_apply_transforms.py --data data/processed --out data/transformed \
      --transforms contraction_expand homoglyph --pipelines innocent_grammar_user
Model-backed transforms need: pip install 'stress-test[models]'
"""

import argparse
from pathlib import Path

from tqdm import tqdm

from stress_test.data import load_manifest
from stress_test.data.sources import load_jsonl, write_jsonl
from stress_test.transforms import REGISTRY, build_pipeline


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--out", default="data/transformed")
    parser.add_argument("--transforms", nargs="*", default=["contraction_expand"])
    parser.add_argument("--pipelines", nargs="*", default=[])
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if any(REGISTRY.get(t) is None for t in args.transforms) or args.pipelines:
        import stress_test.transforms.model_backed  # noqa: F401  (registers model transforms)

    manifest = load_manifest(Path(args.data) / "split_manifest.json")
    test_records = [
        r for r in load_jsonl(Path(args.data) / "clean.jsonl")
        if manifest.get(r.doc_id, "").startswith("test")
    ]
    conditions = [REGISTRY[name]() for name in args.transforms]
    conditions += [build_pipeline(name) for name in args.pipelines]

    for condition in conditions:
        out_records = []
        for record in tqdm(test_records, desc=condition.name):
            result = condition(record.text, seed=args.seed)
            transformed = type(record)(**{**record.to_dict(), "text": result.text,
                                          "transform": condition.name,
                                          "meta": {**record.meta, **result.params}})
            out_records.append(transformed)
        n = write_jsonl(out_records, Path(args.out) / f"{condition.name}.jsonl")
        print(f"{condition.name}: {n} records")


if __name__ == "__main__":
    main()
