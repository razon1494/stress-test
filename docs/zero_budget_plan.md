# Execution roadmap and current status

The project is designed for open-weight models and consumer-GPU or free-tier
compute. This document distinguishes what is implemented from what remains on
the research roadmap.

## Implemented

- HC3-based paired human/ChatGPT core with deterministic document-level splits
- Thirteen transformed conditions, including character perturbations,
  paraphrasing, translation, grammar correction, gold/professional human edits,
  and named composed pipelines
- Seven detector families: TF-IDF, stylometric GBM, GPT-2 perplexity,
  Fast-DetectGPT, Binoculars-lite, OpenAI RoBERTa, and a DeBERTa HC3 fine-tune
- Pooled and per-domain threshold sensitivity analyses
- Reliability, false-accusation, quality-adjusted evasion, hardness, and
  clustered-inference code
- W&I+LOCNESS and ICNALE fairness/register loaders
- Annotation materials for semantic-preservation validation
- Unit tests and GitHub Actions for the research logic and LaTeX manuscript

## Required before a credible preprint

1. **Independent calibration.** Reserve calibration documents before inspecting
   test results and regenerate every headline, subgroup, and manuscript table.
2. **Human semantic validation.** Complete the planned three-annotator study,
   report agreement, and select or revise the semantic-similarity cutoff.
3. **Generator diversity.** Add an unseen-generator evaluation using a permitted
   MAGE, RAID, or comparable source.
4. **Repeated training.** Run the DeBERTa fine-tune with multiple seeds and
   report variation.
5. **Uncertainty for slices.** Add confidence intervals and minimum-cell rules
   for CEFR and region comparisons.
6. **Normalization ablation.** Measure detector performance with a documented
   preprocessing defense instead of inferring its effect from transform tests.
7. **Release manifest.** Record package versions, hardware, seeds, dataset
   checksums, model revisions, and permitted score artifacts for the final run.

## Optional extensions

- Full-size Binoculars model pair
- Multilingual source text and transformations
- Watermark detectors and watermarked generations
- CoCoOp-style or alternative transformation-quality judges
- Risk-coverage and abstention analyses after score calibration is finalized
- A small commercial-detector external-validity study, subject to budget and
  terms of service

## Resource plan

| Workload | Expected environment |
|---|---|
| Unit tests, TF-IDF, stylometric detector, reports | CPU laptop |
| T5 paraphrasing, CoEdIT, translation | Consumer GPU, Colab, or Kaggle |
| Transformer detector scoring | Consumer GPU or free-tier GPU |
| DeBERTa fine-tuning across seeds | Several GPU sessions |
| Human validation | Three annotators using the released blinded batches |

No paid API is required for the current design. Free-tier quotas and model-hosting
availability can change, so the final paper should report the actual compute and
software environment rather than promise a fixed dollar cost.

## Release rule

A result is ready for the README or abstract only when its generating script,
structured output, sample definition, calibration regime, and limitations are
all committed and consistent. See [result provenance](result_provenance.md) for
the artifact map.
