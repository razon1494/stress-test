# Hardness-Aware Evaluation

*601 test examples with paraphrase-similarity signal (others lack semantic_consistency and are excluded). Hardness weights fit once per detector on `paraphrase_t5`, then frozen and reused below.*

| Detector | Condition | HCI | Acc by hardness quintile (easy -> hard) |
|---|---|---|---|
| binoculars_lite | clean | -0.054 | 93% -> 99% -> 99% -> 99% -> 98% |
| binoculars_lite | paraphrase_t5 | 0.149 | 94% -> 97% -> 95% -> 95% -> 80% |
| deberta_hc3_ft | clean | -0.017 | 98% -> 100% -> 100% -> 100% -> 100% |
| deberta_hc3_ft | paraphrase_t5 | -0.017 | 98% -> 99% -> 100% -> 100% -> 100% |
| fast_detect_gpt | clean | -0.034 | 97% -> 99% -> 100% -> 100% -> 100% |
| fast_detect_gpt | paraphrase_t5 | 0.008 | 97% -> 95% -> 92% -> 95% -> 96% |
| perplexity | clean | -0.026 | 98% -> 100% -> 100% -> 100% -> 100% |
| perplexity | paraphrase_t5 | 0.000 | 100% -> 99% -> 98% -> 100% -> 100% |
| roberta_openai | clean | -0.017 | 98% -> 100% -> 100% -> 100% -> 100% |
| roberta_openai | paraphrase_t5 | -0.039 | 87% -> 94% -> 93% -> 95% -> 90% |
| stylometric_gbm | clean | 0.000 | 100% -> 100% -> 100% -> 100% -> 100% |
| stylometric_gbm | paraphrase_t5 | 0.000 | 100% -> 100% -> 100% -> 100% -> 100% |
| tfidf_logreg | clean | 0.000 | 100% -> 100% -> 99% -> 100% -> 100% |
| tfidf_logreg | paraphrase_t5 | -0.017 | 98% -> 98% -> 96% -> 100% -> 100% |
