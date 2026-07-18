# Hardness-Aware Evaluation

*601 test examples with paraphrase-similarity signal (others lack semantic_consistency and are excluded). Hardness weights fit once per detector on `paraphrase_t5`, then frozen and reused below.*

| Detector | Condition | HCI | Acc by hardness quintile (easy -> hard) |
|---|---|---|---|
| binoculars_lite | clean | -0.026 | 97% -> 99% -> 100% -> 100% -> 99% |
| binoculars_lite | paraphrase_t5 | 0.085 | 98% -> 97% -> 95% -> 95% -> 89% |
| deberta_hc3_ft | clean | -0.053 | 95% -> 100% -> 99% -> 100% -> 100% |
| deberta_hc3_ft | paraphrase_t5 | -0.017 | 98% -> 99% -> 99% -> 99% -> 99% |
| fast_detect_gpt | clean | -0.026 | 98% -> 97% -> 100% -> 100% -> 100% |
| fast_detect_gpt | paraphrase_t5 | 0.017 | 95% -> 92% -> 86% -> 92% -> 93% |
| perplexity | clean | -0.009 | 98% -> 98% -> 99% -> 100% -> 99% |
| perplexity | paraphrase_t5 | 0.025 | 100% -> 99% -> 98% -> 97% -> 98% |
| roberta_openai | clean | -0.009 | 98% -> 98% -> 100% -> 99% -> 99% |
| roberta_openai | paraphrase_t5 | -0.126 | 80% -> 82% -> 88% -> 86% -> 90% |
| stylometric_gbm | clean | -0.026 | 98% -> 98% -> 99% -> 100% -> 100% |
| stylometric_gbm | paraphrase_t5 | -0.044 | 95% -> 97% -> 98% -> 100% -> 99% |
| tfidf_logreg | clean | -0.008 | 99% -> 97% -> 100% -> 99% -> 100% |
| tfidf_logreg | paraphrase_t5 | -0.037 | 91% -> 87% -> 92% -> 95% -> 94% |
