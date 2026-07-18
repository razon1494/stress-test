"""Stage 8: fine-tune DeBERTa-v3-base as our supervised neural detector.

Protocol (same rules as every other detector in the suite):
- trains on the CLEAN train split only, model-selects on the val split;
- the test splits (incl. the OOD fairness slice) are never touched here;
- after training, stage 3 scores it at the frozen 1%-FPR threshold like
  everyone else: python scripts/03_run_detectors.py --only deberta_hc3_ft

Sized for a 6GB laptop GPU: 184M params, fp16, batch 8 x grad-accum 2,
max_length 256 (median doc is ~140 words). ~5 min/epoch on an RTX 4050.

Usage: python scripts/08_finetune_deberta.py --epochs 3
"""

import argparse
from pathlib import Path

import numpy as np

from stress_test.data import load_manifest
from stress_test.data.sources import load_jsonl


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    parser.add_argument("--out", default="models/deberta_hc3")
    parser.add_argument("--model", default="microsoft/deberta-v3-base")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch", type=int, default=8)
    parser.add_argument("--max-length", type=int, default=256)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    import torch
    from transformers import (
        AutoModelForSequenceClassification,
        AutoTokenizer,
        DataCollatorWithPadding,
        Trainer,
        TrainingArguments,
        set_seed,
    )

    set_seed(args.seed)
    manifest = load_manifest(Path(args.data) / "split_manifest.json")
    records = list(load_jsonl(Path(args.data) / "clean.jsonl"))
    train = [r for r in records if manifest.get(r.doc_id) == "train"]
    val = [r for r in records if manifest.get(r.doc_id) == "val"]
    print(f"train: {len(train)} records, val: {len(val)} records")

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForSequenceClassification.from_pretrained(
        args.model,
        num_labels=2,
        id2label={0: "human", 1: "machine"},
        label2id={"human": 0, "machine": 1},
    ).float()  # master weights must be fp32; mixed precision is handled by Trainer

    class DetectionDataset(torch.utils.data.Dataset):
        def __init__(self, recs):
            self.encodings = tokenizer(
                [r.text for r in recs], truncation=True, max_length=args.max_length
            )
            self.labels = [r.label for r in recs]

        def __len__(self):
            return len(self.labels)

        def __getitem__(self, idx):
            item = {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
            item["labels"] = torch.tensor(self.labels[idx])
            return item

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        preds = np.argmax(logits, axis=-1)
        return {"accuracy": float((preds == labels).mean())}

    training_args = TrainingArguments(
        output_dir=str(Path(args.out) / "checkpoints"),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch,
        per_device_eval_batch_size=args.batch * 4,
        gradient_accumulation_steps=2,
        learning_rate=args.lr,
        # bf16 needs no grad scaler (avoids the fp16 unscale crash) and is
        # supported on Ada-generation GPUs like the RTX 4050
        bf16=torch.cuda.is_available() and torch.cuda.is_bf16_supported(),
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        save_total_limit=1,
        logging_steps=50,
        seed=args.seed,
        report_to=[],
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=DetectionDataset(train),
        eval_dataset=DetectionDataset(val),
        data_collator=DataCollatorWithPadding(tokenizer),
        compute_metrics=compute_metrics,
    )
    trainer.train()
    print("final val metrics:", trainer.evaluate())

    out = Path(args.out)
    trainer.save_model(str(out))
    tokenizer.save_pretrained(str(out))
    print(f"saved fine-tuned model -> {out}")


if __name__ == "__main__":
    main()
