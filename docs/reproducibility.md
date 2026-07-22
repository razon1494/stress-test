# Reproducibility guide

This document separates the lightweight software check from the full research
pipeline. The latter requires model downloads, GPU time, and access to corpora
that cannot be redistributed here.

## 1. Verify the research code

Use Python 3.10 or newer in a clean environment:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest -q
```

The test suite covers document-level splits, reliability metrics, clustered
statistics, detector interfaces, transformation determinism, normalization,
hardness scoring, and fairness-corpus parsers.

## 2. Install the full experiment environment

```bash
python -m pip install -e ".[models,data,dev]"
```

All implemented model-backed components use downloadable open-weight models.
Model and dataset terms still apply independently of this repository's MIT
license.

## 3. Obtain the data

The loaders expect external corpora below `data/external/`. This directory is
ignored by Git.

| Source | Purpose | Redistribution status |
|---|---|---|
| HC3 | Paired human/ChatGPT core benchmark | Loaded through Hugging Face Datasets |
| Liang et al. detector-bias release | TOEFL and native comparison essays | Download from the authors' public repository |
| W&I+LOCNESS v2.1 | CEFR-stratified learner/native essays and gold corrections | Download under the dataset's non-commercial terms |
| ICNALE Written/Edited Essays | Region-stratified essays and professional edits | Registration required; redistribution prohibited |

The exact paths expected by each loader are documented in
[`src/stress_test/data/non_native.py`](../src/stress_test/data/non_native.py).
Do not commit raw text from these corpora.

## 4. Build the current dataset configuration

The committed manuscript reports the following configuration:

```bash
python scripts/01_build_dataset.py \
  --hc3-per-domain 500 \
  --min-words 50 \
  --include-fairness-subset \
  --wi-locness-per-band 1000 \
  --icnale-per-region 180 \
  --include-icnale-ee
```

This produces `data/processed/clean.jsonl` and a checksum-bearing,
document-level split manifest. Review the printed record counts before
continuing; missing external corpora can otherwise yield an incomplete run.

## 5. Generate transformations

Cheap perturbations can be generated on CPU. Model-backed transformations and
semantic-similarity scoring require the `models` dependencies.

```bash
python scripts/02_apply_transforms.py \
  --transforms case_noise contraction_expand homoglyph typo whitespace_noise zero_width

python scripts/02_apply_transforms.py \
  --transforms paraphrase_t5 grammar_correct roundtrip_fr \
  --pipelines esl_student light_human_edit launder_lite \
  --limit 150

python scripts/09_build_human_edit.py
```

The `--limit` option selects documents deterministically and keeps human/machine
pairs together.

## 6. Run detectors and analyses

```bash
python scripts/08_finetune_deberta.py --seed 0
python scripts/03_run_detectors.py
python scripts/04_make_report.py
python scripts/05_stats.py
python scripts/06_fairness_analysis.py
python scripts/07_hardness.py
python scripts/10_per_domain_calibration.py
python scripts/12_make_figures.py
```

Score caches and fine-tuned weights are intentionally ignored because of their
size. Keep the run logs, package versions, hardware details, and random seeds
with any result release.

## 7. Human validation

The semantic-preservation cutoff is provisional. The released annotation
materials support the planned three-annotator study:

```bash
python scripts/11_make_annotation_batch.py
python scripts/11_make_annotation_batch.py --score annotation/annotator_*.csv
```

Do not describe QAES as human-validated until this study has been completed and
the agreement and threshold-selection results have been added to the repository.

## Known protocol limitation

The current committed score summaries estimate pooled and per-domain thresholds
from clean human records in the evaluation pool. They are useful for exploratory
sensitivity analysis, but they are not independent held-out estimates. The next
full experimental release should reserve a separate calibration set, freeze each
threshold there, and evaluate all headline and subgroup metrics only on untouched
test documents.
