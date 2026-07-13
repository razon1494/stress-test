# Fairness Analysis: Native vs Non-Native False-Accusation Rate

*Liang et al. (Patterns 2023) found 61.22% FPR on clean non-native TOEFL essays with commercial detectors. n_native=158, n_non_native=181.*

| Detector | Condition | Native FAR [95% CI] (n) | Non-native FAR [95% CI] (n) | Gap |
|---|---|---|---|---|
| tfidf_logreg | clean | 0.6% [0.0%, 1.9%] (158) | 2.2% [0.5%, 4.4%] (182) | +1.6% |
| tfidf_logreg | grammar_correct | 0.6% [0.0%, 1.9%] (158) | 1.1% [0.0%, 2.8%] (182) | +0.5% |
| perplexity | clean | 0.0% [0.0%, 0.0%] (158) | 1.6% [0.0%, 3.8%] (182) | +1.6% |
| perplexity | grammar_correct | 2.5% [0.6%, 5.1%] (158) | 5.5% [2.7%, 8.8%] (182) | +3.0% |
