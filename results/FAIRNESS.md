# Fairness Analysis: Native vs Non-Native False-Accusation Rate

*Liang et al. (Patterns 2023) found 61.22% FPR on clean non-native TOEFL essays with commercial detectors. n_native=208, n_non_native=608.*

| Detector | Condition | Native FAR [95% CI] (n) | Non-native FAR [95% CI] (n) | Gap |
|---|---|---|---|---|
| tfidf_logreg | clean | 0.5% [0.0%, 1.4%] (208) | 1.5% [0.7%, 2.5%] (609) | +1.0% |
| tfidf_logreg | grammar_correct | 0.0% [0.0%, 0.0%] (208) | 2.0% [1.0%, 3.1%] (609) | +2.0% |
| tfidf_logreg | human_edit | 2.0% [0.0%, 6.0%] (50) | 1.9% [0.7%, 3.3%] (427) | -0.1% |
| stylometric_gbm | clean | 0.5% [0.0%, 1.4%] (208) | 1.0% [0.3%, 1.8%] (609) | +0.5% |
| stylometric_gbm | grammar_correct | 0.5% [0.0%, 1.4%] (208) | 1.1% [0.3%, 2.0%] (609) | +0.7% |
| stylometric_gbm | human_edit | 2.0% [0.0%, 6.0%] (50) | 1.4% [0.5%, 2.6%] (427) | -0.6% |
| perplexity | clean | 0.0% [0.0%, 0.0%] (208) | 1.0% [0.3%, 1.8%] (609) | +1.0% |
| perplexity | grammar_correct | 2.4% [0.5%, 4.8%] (208) | 6.2% [4.4%, 8.2%] (609) | +3.8% |
| perplexity | human_edit | 2.0% [0.0%, 6.0%] (50) | 3.0% [1.6%, 4.7%] (427) | +1.0% |
| fast_detect_gpt | clean | 0.5% [0.0%, 1.4%] (208) | 1.3% [0.5%, 2.3%] (609) | +0.8% |
| fast_detect_gpt | grammar_correct | 1.0% [0.0%, 2.4%] (208) | 3.4% [2.1%, 5.1%] (609) | +2.5% |
| fast_detect_gpt | human_edit | 2.0% [0.0%, 6.0%] (50) | 3.0% [1.6%, 4.7%] (427) | +1.0% |
| binoculars_lite | clean | 0.0% [0.0%, 0.0%] (208) | 1.5% [0.7%, 2.5%] (609) | +1.5% |
| binoculars_lite | grammar_correct | 0.0% [0.0%, 0.0%] (208) | 2.8% [1.5%, 4.1%] (609) | +2.8% |
| binoculars_lite | human_edit | 0.0% [0.0%, 0.0%] (50) | 3.3% [1.9%, 5.2%] (427) | +3.3% |
| roberta_openai | clean | 0.0% [0.0%, 0.0%] (208) | 1.5% [0.7%, 2.5%] (609) | +1.5% |
| roberta_openai | grammar_correct | 4.8% [1.9%, 7.7%] (208) | 10.0% [7.6%, 12.3%] (609) | +5.2% |
| roberta_openai | human_edit | 2.0% [0.0%, 6.0%] (50) | 6.8% [4.4%, 9.1%] (427) | +4.8% |
| deberta_hc3_ft | clean | 0.0% [0.0%, 0.0%] (208) | 1.5% [0.7%, 2.5%] (609) | +1.5% |
| deberta_hc3_ft | grammar_correct | 1.4% [0.0%, 3.4%] (208) | 4.4% [2.9%, 6.1%] (609) | +3.0% |
| deberta_hc3_ft | human_edit | 0.0% [0.0%, 0.0%] (50) | 3.5% [1.9%, 5.4%] (427) | +3.5% |

## FAR by CEFR proficiency band (W&I+LOCNESS; N = native)

| Detector | Condition | A | B | C | N |
|---|---|---|---|---|---|
| tfidf_logreg | clean | 2.3% (128) | 1.3% (150) | 2.0% (149) | 2.0% (50) |
| tfidf_logreg | grammar_correct | 2.3% (128) | 1.3% (150) | 3.4% (149) | 0.0% (50) |
| tfidf_logreg | human_edit | 2.3% (128) | 1.3% (150) | 2.0% (149) | 2.0% (50) |
| stylometric_gbm | clean | 0.0% (128) | 1.3% (150) | 1.3% (149) | 2.0% (50) |
| stylometric_gbm | grammar_correct | 0.8% (128) | 2.0% (150) | 1.3% (149) | 2.0% (50) |
| stylometric_gbm | human_edit | 0.8% (128) | 2.0% (150) | 1.3% (149) | 2.0% (50) |
| perplexity | clean | 0.0% (128) | 0.0% (150) | 0.7% (149) | 0.0% (50) |
| perplexity | grammar_correct | 4.7% (128) | 6.7% (150) | 7.4% (149) | 0.0% (50) |
| perplexity | human_edit | 1.6% (128) | 2.7% (150) | 4.7% (149) | 2.0% (50) |
| fast_detect_gpt | clean | 0.0% (128) | 2.0% (150) | 2.7% (149) | 0.0% (50) |
| fast_detect_gpt | grammar_correct | 1.6% (128) | 7.3% (150) | 4.0% (149) | 2.0% (50) |
| fast_detect_gpt | human_edit | 1.6% (128) | 5.3% (150) | 2.0% (149) | 2.0% (50) |
| binoculars_lite | clean | 0.8% (128) | 2.0% (150) | 1.3% (149) | 0.0% (50) |
| binoculars_lite | grammar_correct | 3.1% (128) | 0.7% (150) | 1.3% (149) | 0.0% (50) |
| binoculars_lite | human_edit | 3.1% (128) | 4.0% (150) | 2.7% (149) | 0.0% (50) |
| roberta_openai | clean | 0.0% (128) | 0.7% (150) | 0.7% (149) | 0.0% (50) |
| roberta_openai | grammar_correct | 10.2% (128) | 15.3% (150) | 6.7% (149) | 0.0% (50) |
| roberta_openai | human_edit | 7.8% (128) | 6.0% (150) | 6.7% (149) | 2.0% (50) |
| deberta_hc3_ft | clean | 0.0% (128) | 0.0% (150) | 2.0% (149) | 0.0% (50) |
| deberta_hc3_ft | grammar_correct | 0.0% (128) | 3.3% (150) | 8.1% (149) | 0.0% (50) |
| deberta_hc3_ft | human_edit | 1.6% (128) | 2.0% (150) | 6.7% (149) | 0.0% (50) |
