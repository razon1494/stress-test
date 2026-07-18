# Fairness Analysis: Native vs Non-Native False-Accusation Rate

*Liang et al. (Patterns 2023) found 61.22% FPR on clean non-native TOEFL essays with commercial detectors. n_native=158, n_non_native=181.*

| Detector | Condition | Native FAR [95% CI] (n) | Non-native FAR [95% CI] (n) | Gap |
|---|---|---|---|---|
| tfidf_logreg | clean | 0.6% [0.0%, 1.9%] (158) | 2.2% [0.5%, 4.4%] (182) | +1.6% |
| tfidf_logreg | grammar_correct | 0.6% [0.0%, 1.9%] (158) | 1.1% [0.0%, 2.8%] (182) | +0.5% |
| stylometric_gbm | clean | 0.0% [0.0%, 0.0%] (158) | 1.1% [0.0%, 2.8%] (182) | +1.1% |
| stylometric_gbm | grammar_correct | 0.0% [0.0%, 0.0%] (158) | 1.6% [0.0%, 3.8%] (182) | +1.6% |
| perplexity | clean | 0.0% [0.0%, 0.0%] (158) | 1.6% [0.0%, 3.8%] (182) | +1.6% |
| perplexity | grammar_correct | 2.5% [0.6%, 5.1%] (158) | 5.5% [2.7%, 8.8%] (182) | +3.0% |
| fast_detect_gpt | clean | 1.9% [0.0%, 4.4%] (158) | 1.1% [0.0%, 2.8%] (182) | -0.8% |
| fast_detect_gpt | grammar_correct | 4.4% [1.3%, 8.2%] (158) | 4.4% [1.6%, 7.2%] (182) | -0.0% |
| binoculars_lite | clean | 0.0% [0.0%, 0.0%] (158) | 2.7% [0.5%, 5.5%] (182) | +2.7% |
| binoculars_lite | grammar_correct | 0.0% [0.0%, 0.0%] (158) | 7.7% [3.9%, 11.6%] (182) | +7.7% |
| roberta_openai | clean | 0.0% [0.0%, 0.0%] (158) | 3.3% [1.1%, 6.0%] (182) | +3.3% |
| roberta_openai | grammar_correct | 5.7% [2.5%, 9.5%] (158) | 6.6% [3.3%, 10.4%] (182) | +0.9% |
| deberta_hc3_ft | clean | 0.0% [0.0%, 0.0%] (158) | 3.3% [1.1%, 6.1%] (182) | +3.3% |
| deberta_hc3_ft | grammar_correct | 1.9% [0.0%, 4.4%] (158) | 3.3% [1.1%, 6.0%] (182) | +1.4% |
