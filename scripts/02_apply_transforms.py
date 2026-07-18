"""Stage 2: apply transforms/pipelines to TEST-split records (both classes —
the symmetric protocol). Emits one jsonl per condition; each row keeps its
doc_id for pairing and carries meta.semsim (similarity to the clean original)
so the metrics stage can compute quality-adjusted evasion.

Usage:
  python scripts/02_apply_transforms.py --transforms paraphrase_t5 roundtrip_fr \
      --pipelines launder_lite --limit 150
Model-backed transforms need: pip install 'stress-test[models]'
"""

import argparse
from pathlib import Path

from tqdm import tqdm

from stress_test.data import load_manifest, subsample_doc_pairs
from stress_test.data.sources import load_jsonl, write_jsonl
from stress_test.transforms import REGISTRY, build_pipeline


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--out", default="data/transformed")
    parser.add_argument("--transforms", nargs="*", default=["contraction_expand"])
    parser.add_argument("--pipelines", nargs="*", default=[])
    parser.add_argument("--limit", type=int, default=None,
                        help="cap on number of test DOCS (pairs), for laptop-scale runs")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--no-semsim", action="store_true",
                        help="skip semantic scoring (e.g. sentence-transformers unavailable)")
    args = parser.parse_args()

    if any(REGISTRY.get(t) is None for t in args.transforms) or args.pipelines:
        import stress_test.transforms.model_backed  # noqa: F401  (registers model transforms)

    manifest = load_manifest(Path(args.data) / "split_manifest.json")
    test_records = [
        r for r in load_jsonl(Path(args.data) / "clean.jsonl")
        if manifest.get(r.doc_id, "").startswith("test")
    ]
    if args.limit:
        test_records = subsample_doc_pairs(test_records, args.limit)
        print(f"subsampled to {len(test_records)} records ({args.limit} docs)")

    conditions = [REGISTRY[name]() for name in args.transforms]
    conditions += [build_pipeline(name) for name in args.pipelines]

    for condition in conditions:
        # incremental: reuse already-transformed records from a previous run of
        # this condition (keyed by doc_id+label), transform only the new ones
        out_path = Path(args.out) / f"{condition.name}.jsonl"
        cached: dict[tuple, object] = {}
        if out_path.exists():
            cached = {(r.doc_id, r.label): r for r in load_jsonl(out_path)}
        todo = [r for r in test_records if (r.doc_id, r.label) not in cached]
        print(f"{condition.name}: {len(cached)} cached, {len(todo)} to transform")

        new_records = []
        for record in tqdm(todo, desc=condition.name):
            result = condition(record.text, seed=args.seed)
            new_records.append(type(record)(**{**record.to_dict(), "text": result.text,
                                               "transform": condition.name,
                                               "meta": {**record.meta, **result.params}}))
        if new_records and not args.no_semsim:
            from stress_test.semantics import semantic_similarity

            sims = semantic_similarity([r.text for r in todo], [r.text for r in new_records])
            for record, sim in zip(new_records, sims):
                record.meta["semsim"] = round(float(sim), 4)

        # keep output aligned to the current test set: cached where available,
        # freshly transformed otherwise
        new_by_key = {(r.doc_id, r.label): r for r in new_records}
        out_records = [
            cached.get((r.doc_id, r.label)) or new_by_key[(r.doc_id, r.label)]
            for r in test_records
        ]
        n = write_jsonl(out_records, out_path)
        print(f"{condition.name}: {n} records")


if __name__ == "__main__":
    main()
