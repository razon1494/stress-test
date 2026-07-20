# STRESS-Test

![tests](https://github.com/razon1494/stress-test/actions/workflows/ci.yml/badge.svg)
![paper](https://github.com/razon1494/stress-test/actions/workflows/paper.yml/badge.svg)

**S**emantic-preserving **T**ransformations for **R**obust **E**valuation of **S**ynthetic-text **S**creening

> Detector benchmarks count evasions. **We measure reliability.**
> 📄 Paper draft: [`paper/main.tex`](paper/main.tex) · Results: [`results/`](results/)

## Headline results (per-domain calibration, target 1% FPR)

| Detector | Clean TPR | Robustness | Worst-case | FAR under human editing |
|---|---|---|---|---|
| Fast-DetectGPT | **97.7%** | 0.73 | 46.7% | 3.4% |
| Binoculars-lite | 96.9% | 0.63 | 44.0% | 7.4% |
| DeBERTa-v3 (ours) | 93.1% | 0.83 | **78.7%** | 8.0% |
| TF-IDF + LR | 79.4% | **0.96** | 63.3% | 1.1% |

Three findings: **(1)** clean accuracy and reliability rank detectors in nearly
opposite orders; **(2)** at frozen deployed thresholds, grammar-correcting
*human* text multiplies false accusations 5–8× — an effect that reproduces
under *gold human editing* and lands hardest on non-native learners (up to
15.3% FAR at CEFR-B), invisible to the AUROC-only evaluation used by prior
benchmarks; **(3)** the bias tracks *text predictability*, not nativeness —
on topic-controlled prompt essays, native writers are flagged most
([figure](paper/figures/perplexity_by_corpus.png)).

AI-text detectors advertise 99% accuracy — then fail the moment text is paraphrased,
translated, or lightly edited, and falsely accuse non-native English writers. Existing
benchmarks (RAID, DetectRL) apply single atomic attacks to machine text and report
aggregate accuracy. STRESS-Test evaluates what they miss:

| Axis | Question it answers |
|---|---|
| 🔗 **Compositional robustness** | What happens under realistic *pipelines* (translate → grammar-fix → edit), not single attacks? |
| ⚖️ **Quality-adjusted evasion (QAES)** | How much "attack success" is just meaning destruction? |
| 📉 **Hardness-aware metrics** | Does the detector collapse precisely on the hard examples averages hide? |
| 🎯 **Threshold transfer** | Calibrate once at 1% FPR on clean data — what *actually* happens under shift? |
| 🚨 **False-Accusation Risk** | Every transform hits *human* text too. Who gets wrongly flagged — and does grammar correction make it worse for non-native writers? |
| 🌡️ **Calibration drift** | Is detector confidence still meaningful after transformation? (ΔECE, risk–coverage) |

Every transformation is a **label-preserving metamorphic relation**; detector
reliability is the violation rate of these relations. Output per detector is a
**reliability card** — a nutrition label, not a single leaderboard number.

## Install

```bash
pip install -e ".[dev]"          # core: metrics, stats, splits, cheap transforms (CPU-only)
pip install -e ".[models,data]"  # + open-weight transforms/detectors and HF corpus loaders
```

Zero-budget by design: all models are open-weight and sized for Colab/Kaggle free tier.
See [docs/zero_budget_plan.md](docs/zero_budget_plan.md).

## Quickstart

```bash
pytest                                             # 40+ tests on metrics/stats/transforms
python scripts/01_build_dataset.py                 # free corpora -> canonical schema + split manifest
python scripts/02_apply_transforms.py              # transforms/pipelines on BOTH classes
python scripts/03_run_detectors.py                 # train clean-only, calibrate @1% FPR, score all conditions
python scripts/04_make_report.py                   # reliability cards + leaderboard
```

## Repository map

```
src/stress_test/
├── transforms/    # metamorphic relations: perturbations (pure Python), model-backed
│   └── compose.py #   pipelines: esl_student, content_launderer, innocent_grammar_user...
├── detectors/     # TF-IDF+LR, stylometric GBM, perplexity, Fast-DetectGPT, Binoculars-lite, RoBERTa
├── hardness/      # 5-signal hardness score (leave-one-out committee, grouped z-scoring)
├── metrics/       # RS, TS, QAES/SPG, HCI, WCP, FAR, ECE, AURC — all unit-tested
├── stats/         # clustered bootstrap, permutation/McNemar, Holm–Bonferroni
├── data/          # corpus loaders, contamination-safe doc-level splits (hash-deterministic)
└── report/        # reliability cards + leaderboard
docs/              # related-work differentiation, zero-budget plan
```

## Protocol rules (what makes the numbers honest)

1. **Split by source document** — a text and all its machine/transformed counterparts
   share one split; OOD slices hold out entire generators/domains.
2. **Train clean, test shifted** — detectors never see transformed text in training.
3. **One threshold** — calibrated at 1% FPR on clean human text, never re-tuned.
4. **Clustered statistics** — bootstrap resamples source documents, not rows.
5. **Quality-controlled attacks** — evasion counts only if meaning survives (validated
   against human judgments).

## Status

🚧 Active research project (target: arXiv preprint + NeurIPS D&B / TrustNLP-style venue).
Roadmap in [docs/zero_budget_plan.md](docs/zero_budget_plan.md); week-by-week plan tracked in issues.

## Citation

```bibtex
@misc{rahman2026stresstest,
  title  = {STRESS-Test: Measuring the Reliability of AI-Text Detectors
            Under Real-World Transformations},
  author = {Rahman, Arifur},
  year   = {2026},
  note   = {arXiv preprint forthcoming},
}
```

MIT licensed. Dataset sources retain their original licenses (see docs).
