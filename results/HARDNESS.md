# Hardness-Aware Evaluation

*150 test examples with paraphrase-similarity signal (others lack semantic_consistency and are excluded). Hardness weights fit once per detector on `paraphrase_t5`, then frozen and reused below.*

| Detector | Condition | HCI | Acc by hardness quintile (easy -> hard) |
|---|---|---|---|
| binoculars_lite | clean | 0.000 | 100% -> 100% -> 100% -> 100% -> 100% |
| binoculars_lite | paraphrase_t5 | 0.000 | 100% -> 100% -> 93% -> 90% -> 100% |
| fast_detect_gpt | clean | 0.000 | 100% -> 100% -> 97% -> 100% -> 100% |
| fast_detect_gpt | paraphrase_t5 | 0.067 | 100% -> 93% -> 100% -> 100% -> 93% |
| perplexity | clean | 0.000 | 100% -> 100% -> 100% -> 97% -> 100% |
| perplexity | paraphrase_t5 | 0.000 | 100% -> 100% -> 100% -> 100% -> 100% |
| roberta_openai | clean | 0.033 | 100% -> 100% -> 100% -> 100% -> 97% |
| roberta_openai | paraphrase_t5 | 0.000 | 87% -> 93% -> 93% -> 93% -> 87% |
| stylometric_gbm | clean | -0.034 | 97% -> 97% -> 97% -> 100% -> 100% |
| stylometric_gbm | paraphrase_t5 | -0.154 | 87% -> 97% -> 97% -> 97% -> 100% |
| tfidf_logreg | clean | 0.000 | 100% -> 100% -> 100% -> 100% -> 100% |
| tfidf_logreg | paraphrase_t5 | -0.077 | 87% -> 97% -> 97% -> 93% -> 93% |
