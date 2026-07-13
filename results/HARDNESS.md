# Hardness-Aware Evaluation

*601 test examples with paraphrase-similarity signal (others lack semantic_consistency and are excluded). Hardness weights fit once per detector on `paraphrase_t5`, then frozen and reused below.*

| Detector | Condition | HCI | Acc by hardness quintile (easy -> hard) |
|---|---|---|---|
| binoculars_lite | clean | -0.026 | 97% -> 99% -> 100% -> 100% -> 99% |
| binoculars_lite | paraphrase_t5 | 0.060 | 97% -> 98% -> 96% -> 92% -> 91% |
| fast_detect_gpt | clean | -0.026 | 98% -> 98% -> 98% -> 100% -> 100% |
| fast_detect_gpt | paraphrase_t5 | 0.025 | 97% -> 91% -> 89% -> 87% -> 94% |
| perplexity | clean | -0.017 | 98% -> 98% -> 99% -> 99% -> 100% |
| perplexity | paraphrase_t5 | 0.008 | 100% -> 100% -> 98% -> 96% -> 99% |
| roberta_openai | clean | -0.026 | 97% -> 99% -> 99% -> 100% -> 99% |
| roberta_openai | paraphrase_t5 | -0.105 | 80% -> 83% -> 82% -> 92% -> 88% |
| stylometric_gbm | clean | -0.026 | 98% -> 99% -> 98% -> 100% -> 100% |
| stylometric_gbm | paraphrase_t5 | -0.044 | 95% -> 98% -> 97% -> 100% -> 99% |
| tfidf_logreg | clean | -0.017 | 98% -> 98% -> 99% -> 100% -> 100% |
| tfidf_logreg | paraphrase_t5 | -0.056 | 90% -> 88% -> 92% -> 94% -> 95% |
