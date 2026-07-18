# Hardness-Aware Evaluation

*601 test examples with paraphrase-similarity signal (others lack semantic_consistency and are excluded). Hardness weights fit once per detector on `paraphrase_t5`, then frozen and reused below.*

| Detector | Condition | HCI | Acc by hardness quintile (easy -> hard) |
|---|---|---|---|
| binoculars_lite | clean | -0.017 | 98% -> 100% -> 100% -> 100% -> 99% |
| binoculars_lite | paraphrase_t5 | 0.034 | 98% -> 98% -> 98% -> 95% -> 94% |
| deberta_hc3_ft | clean | -0.026 | 98% -> 99% -> 98% -> 100% -> 100% |
| deberta_hc3_ft | paraphrase_t5 | -0.036 | 93% -> 96% -> 99% -> 98% -> 97% |
| fast_detect_gpt | clean | -0.017 | 98% -> 99% -> 100% -> 100% -> 100% |
| fast_detect_gpt | paraphrase_t5 | -0.018 | 96% -> 96% -> 95% -> 98% -> 98% |
| perplexity | clean | -0.026 | 97% -> 99% -> 98% -> 99% -> 99% |
| perplexity | paraphrase_t5 | 0.008 | 98% -> 98% -> 98% -> 97% -> 98% |
| roberta_openai | clean | -0.026 | 97% -> 98% -> 99% -> 100% -> 99% |
| roberta_openai | paraphrase_t5 | -0.206 | 73% -> 81% -> 85% -> 82% -> 88% |
| stylometric_gbm | clean | -0.008 | 99% -> 98% -> 98% -> 100% -> 100% |
| stylometric_gbm | paraphrase_t5 | -0.043 | 96% -> 98% -> 99% -> 99% -> 100% |
| tfidf_logreg | clean | -0.008 | 99% -> 100% -> 100% -> 100% -> 100% |
| tfidf_logreg | paraphrase_t5 | -0.073 | 92% -> 95% -> 97% -> 99% -> 98% |
