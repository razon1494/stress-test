# STRESS-Test

[![tests](https://github.com/razon1494/stress-test/actions/workflows/ci.yml/badge.svg)](https://github.com/razon1494/stress-test/actions/workflows/ci.yml)
[![paper](https://github.com/razon1494/stress-test/actions/workflows/paper.yml/badge.svg)](https://github.com/razon1494/stress-test/actions/workflows/paper.yml)
[![license](https://img.shields.io/badge/license-MIT-5b8c85.svg)](LICENSE)

**S**emantic-preserving **T**ransformations for **R**obust **E**valuation of
**S**ynthetic-text **S**creening

STRESS-Test is a research framework for evaluating whether AI-text detectors
remain reliable after paraphrasing, translation, grammar correction, human
editing, and character-level perturbations. Transformations are evaluated on
both machine and human text at a fixed decision threshold, making evasion and
false-accusation risk part of the same protocol.

**Research status:** active, pre-submission work. The current results are
preliminary sensitivity analyses, not a finalized benchmark. Semantic-preservation
thresholds still require the planned human-validation study, and the present
per-domain calibration analysis estimates thresholds from the same clean domain
slices used for evaluation. These limitations are stated here because they affect
how the numbers should be interpreted.

[Paper draft](paper/main.tex) · [Generated results](results/) ·
[Reproducibility guide](docs/reproducibility.md) ·
[Result provenance](docs/result_provenance.md)

## Research questions

1. Do clean-text accuracy and robustness rank detectors differently?
2. How do realistic transformation pipelines affect detection at a frozen
   operating threshold?
3. Do benign edits to human writing increase false-accusation rates for
   particular registers or writer groups?
4. Which conclusions change when results are stratified by text difficulty,
   domain, and detector mechanism?

## Preliminary results

The table below is generated from the current per-domain calibration sensitivity
analysis at a target 1% false-positive rate. Robustness Score (RS) is the mean
retained TPR across transformed conditions; worst-case is the minimum TPR among
the named transformation pipelines.

| Detector | Clean TPR | RS | Worst-case pipeline TPR | FAR after human editing |
|---|---:|---:|---:|---:|
| Fast-DetectGPT | **97.7%** | 0.727 | 46.7% | 3.4% |
| Binoculars-lite | 96.9% | 0.634 | 44.0% | 7.4% |
| DeBERTa-v3, HC3 fine-tune | 93.1% | 0.829 | **78.7%** | 8.0% |
| GPT-2 perplexity | 93.1% | 0.642 | 62.0% | 6.4% |
| OpenAI RoBERTa detector | 85.9% | 0.554 | 53.3% | 6.7% |
| TF-IDF + logistic regression | 79.4% | **0.961** | 63.3% | 1.1% |
| Stylometric GBM | 55.7% | 0.915 | 50.7% | 1.2% |

What the current analysis suggests:

- Strong clean performance does not guarantee transformation robustness. The two
  strongest clean detectors fall to 44–47% TPR under the depth-2 laundering
  pipeline.
- The supervised DeBERTa model retains the highest worst-case pipeline TPR, while
  TF-IDF has the highest relative robustness at a lower clean TPR.
- False-accusation rates vary substantially by detector, transformation, and
  writing register. The slice results do not support a simple “native versus
  non-native” explanation.
- Quality-adjusted evasion results are provisional until the semantic-similarity
  cutoff has been checked against human judgments.

Full generated tables are available in
[PER_DOMAIN.md](results/PER_DOMAIN.md), [REPORT.md](results/REPORT.md),
[FAIRNESS.md](results/FAIRNESS.md), [HARDNESS.md](results/HARDNESS.md), and
[STATS.md](results/STATS.md).

## Evaluation design

- **Symmetric transformations:** apply each transformation to human and machine
  text.
- **Clean-only training:** trainable detectors do not see transformed text during
  training.
- **Frozen thresholds:** select a target operating point once and do not retune it
  for each transformation.
- **Document-level grouping:** keep a source document and all of its variants in
  the same split.
- **Reliability metrics:** report RS, worst-case performance, false-accusation
  rate, calibration drift, quality-adjusted evasion, and hardness collapse.
- **Cluster-aware inference:** resample source documents rather than individual
  rows and correct paired comparisons for multiple testing.

The current draft contains both pooled-threshold and per-domain sensitivity
analyses. A separate held-out calibration set is required before the reported
operating-point estimates should be treated as final.

## Quickstart

The lightweight installation runs the metric, statistics, split, detector, and
transformation tests without downloading model weights:

```bash
git clone https://github.com/razon1494/stress-test.git
cd stress-test
python -m pip install -e ".[dev]"
python -m pytest -q
```

For the complete pipeline:

```bash
python -m pip install -e ".[models,data,dev]"
python scripts/01_build_dataset.py --help
python scripts/02_apply_transforms.py --help
python scripts/03_run_detectors.py --help
python scripts/04_make_report.py --help
```

Some fairness corpora require separate downloads and cannot be redistributed in
this repository. See the [reproducibility guide](docs/reproducibility.md) before
attempting a full run.

## Repository map

| Path | Purpose |
|---|---|
| [`src/stress_test/`](src/stress_test/) | Transformations, detectors, metrics, statistics, data utilities, and report generation |
| [`scripts/`](scripts/) | Numbered experiment and analysis stages |
| [`tests/`](tests/) | Unit tests for core research logic |
| [`results/`](results/) | Committed generated summaries and structured outputs |
| [`paper/`](paper/) | LaTeX manuscript draft and generated figure |
| [`docs/`](docs/) | Reproduction instructions, annotation protocol, and related-work notes |

## Current limitations

- The machine-text core currently uses one generator family and one broad source
  dataset (HC3).
- Threshold calibration and final evaluation are not yet separated in the
  committed result set.
- Semantic preservation is currently embedding-scored; the planned three-annotator
  validation has not been completed.
- The DeBERTa fine-tune uses one training seed, and Binoculars-lite is not the
  original Falcon-7B model pair.
- Several subgroup estimates have wide uncertainty because the cells are small.
- Raw licensed corpora, model weights, and score caches are intentionally not
  committed.

## Citation

Until a preprint is released, cite the software repository:

```bibtex
@software{rahman2026stresstest,
  author = {Rahman, Mohammad Arifur},
  title  = {STRESS-Test: Semantic-preserving Transformations for Robust
            Evaluation of Synthetic-text Screening},
  year   = {2026},
  url    = {https://github.com/razon1494/stress-test}
}
```

## Author and license

Mohammad Arifur Rahman · rahman.arif.cse@gmail.com ·
[Portfolio](https://ari-fur.com/)

The framework code is released under the [MIT License](LICENSE). External
datasets and pretrained models remain subject to their original licenses and
terms of use.
