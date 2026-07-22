# Per-Domain Calibration Sensitivity Analysis

> **Interpretation note.** Thresholds are estimated and evaluated on records from the same dataset slices. This analysis measures sensitivity to the calibration strategy; it is not an independently held-out estimate.

*One threshold per (detector, domain), calibrated at 1% FPR on that domain's clean human text; domains with <30 human docs fall back to the pooled threshold. Same cached scores as the pooled analysis.*

## Headline (per-domain calibrated)

| Detector | Clean TPR | Clean FPR | RS | WCP (worst pipeline) | FAR grammar | FAR human-edit |
|---|---|---|---|---|---|---|
| binoculars_lite | 96.9% | 0.8% | 0.634 | 44.0% (launder_lite) | 4.1% | 7.4% |
| deberta_hc3_ft | 93.1% | 0.8% | 0.829 | 78.7% (launder_lite) | 4.0% | 8.0% |
| fast_detect_gpt | 97.7% | 0.8% | 0.727 | 46.7% (launder_lite) | 2.6% | 3.4% |
| perplexity | 93.1% | 0.8% | 0.642 | 62.0% (launder_lite) | 5.7% | 6.4% |
| roberta_openai | 85.9% | 0.8% | 0.554 | 53.3% (launder_lite) | 6.0% | 6.7% |
| stylometric_gbm | 55.7% | 0.7% | 0.915 | 50.7% (launder_lite) | 0.8% | 1.2% |
| tfidf_logreg | 79.4% | 0.8% | 0.961 | 63.3% (launder_lite) | 1.9% | 1.1% |

## Per-condition TPR/FPR (per-domain calibrated)

| Detector | Condition | TPR | FPR |
|---|---|---|---|
| binoculars_lite | case_noise | 13.7% | 0.0% |
| binoculars_lite | clean | 96.9% | 0.8% |
| binoculars_lite | contraction_expand | 96.9% | 0.0% |
| binoculars_lite | esl_student | 71.3% | 6.0% |
| binoculars_lite | grammar_correct | 94.3% | 4.1% |
| binoculars_lite | homoglyph | 43.1% | 0.4% |
| binoculars_lite | human_edit | nan% | 7.4% |
| binoculars_lite | launder_lite | 44.0% | 7.3% |
| binoculars_lite | light_human_edit | 93.3% | 6.0% |
| binoculars_lite | paraphrase_t5 | 59.9% | 7.0% |
| binoculars_lite | roundtrip_fr | 72.0% | 3.3% |
| binoculars_lite | typo | 41.2% | 0.0% |
| binoculars_lite | whitespace_noise | 74.4% | 0.0% |
| binoculars_lite | zero_width | 33.6% | 0.8% |
| deberta_hc3_ft | case_noise | 59.5% | 0.0% |
| deberta_hc3_ft | clean | 93.1% | 0.8% |
| deberta_hc3_ft | contraction_expand | 93.1% | 0.0% |
| deberta_hc3_ft | esl_student | 90.0% | 1.3% |
| deberta_hc3_ft | grammar_correct | 93.5% | 4.0% |
| deberta_hc3_ft | homoglyph | 67.2% | 0.0% |
| deberta_hc3_ft | human_edit | nan% | 8.0% |
| deberta_hc3_ft | launder_lite | 78.7% | 8.7% |
| deberta_hc3_ft | light_human_edit | 93.3% | 3.3% |
| deberta_hc3_ft | paraphrase_t5 | 92.4% | 8.3% |
| deberta_hc3_ft | roundtrip_fr | 89.3% | 1.3% |
| deberta_hc3_ft | typo | 75.2% | 0.0% |
| deberta_hc3_ft | whitespace_noise | 93.1% | 0.0% |
| deberta_hc3_ft | zero_width | 1.1% | 0.0% |
| fast_detect_gpt | case_noise | 36.3% | 0.8% |
| fast_detect_gpt | clean | 97.7% | 0.8% |
| fast_detect_gpt | contraction_expand | 97.7% | 0.0% |
| fast_detect_gpt | esl_student | 80.7% | 3.3% |
| fast_detect_gpt | grammar_correct | 96.9% | 2.6% |
| fast_detect_gpt | homoglyph | 69.8% | 0.4% |
| fast_detect_gpt | human_edit | nan% | 3.4% |
| fast_detect_gpt | launder_lite | 46.7% | 4.0% |
| fast_detect_gpt | light_human_edit | 97.3% | 3.3% |
| fast_detect_gpt | paraphrase_t5 | 71.4% | 5.5% |
| fast_detect_gpt | roundtrip_fr | 80.7% | 2.0% |
| fast_detect_gpt | typo | 64.9% | 0.0% |
| fast_detect_gpt | whitespace_noise | 81.7% | 0.0% |
| fast_detect_gpt | zero_width | 27.9% | 0.0% |
| perplexity | case_noise | 0.4% | 0.0% |
| perplexity | clean | 93.1% | 0.8% |
| perplexity | contraction_expand | 93.1% | 0.0% |
| perplexity | esl_student | 83.3% | 6.0% |
| perplexity | grammar_correct | 95.4% | 5.7% |
| perplexity | homoglyph | 17.2% | 0.0% |
| perplexity | human_edit | nan% | 6.4% |
| perplexity | launder_lite | 62.0% | 5.3% |
| perplexity | light_human_edit | 96.0% | 4.0% |
| perplexity | paraphrase_t5 | 72.9% | 3.5% |
| perplexity | roundtrip_fr | 78.7% | 4.0% |
| perplexity | typo | 41.2% | 0.0% |
| perplexity | whitespace_noise | 72.5% | 0.0% |
| perplexity | zero_width | 5.0% | 0.0% |
| roberta_openai | case_noise | 0.0% | 0.8% |
| roberta_openai | clean | 85.9% | 0.8% |
| roberta_openai | contraction_expand | 85.9% | 0.0% |
| roberta_openai | esl_student | 76.7% | 24.7% |
| roberta_openai | grammar_correct | 83.2% | 6.0% |
| roberta_openai | homoglyph | 0.8% | 0.4% |
| roberta_openai | human_edit | nan% | 6.7% |
| roberta_openai | launder_lite | 53.3% | 41.3% |
| roberta_openai | light_human_edit | 81.3% | 6.0% |
| roberta_openai | paraphrase_t5 | 66.0% | 25.5% |
| roberta_openai | roundtrip_fr | 63.3% | 18.7% |
| roberta_openai | typo | 4.2% | 1.5% |
| roberta_openai | whitespace_noise | 56.5% | 0.4% |
| roberta_openai | zero_width | 0.0% | 0.0% |
| stylometric_gbm | case_noise | 55.7% | 0.0% |
| stylometric_gbm | clean | 55.7% | 0.7% |
| stylometric_gbm | contraction_expand | 56.9% | 0.0% |
| stylometric_gbm | esl_student | 53.3% | 1.3% |
| stylometric_gbm | grammar_correct | 56.5% | 0.8% |
| stylometric_gbm | homoglyph | 42.4% | 0.0% |
| stylometric_gbm | human_edit | nan% | 1.2% |
| stylometric_gbm | launder_lite | 50.7% | 3.3% |
| stylometric_gbm | light_human_edit | 57.3% | 0.7% |
| stylometric_gbm | paraphrase_t5 | 48.1% | 1.3% |
| stylometric_gbm | roundtrip_fr | 49.3% | 1.3% |
| stylometric_gbm | typo | 51.1% | 0.0% |
| stylometric_gbm | whitespace_noise | 56.1% | 0.0% |
| stylometric_gbm | zero_width | 34.7% | 0.0% |
| tfidf_logreg | case_noise | 79.4% | 0.0% |
| tfidf_logreg | clean | 79.4% | 0.8% |
| tfidf_logreg | contraction_expand | 79.8% | 0.4% |
| tfidf_logreg | esl_student | 75.3% | 12.0% |
| tfidf_logreg | grammar_correct | 78.2% | 1.9% |
| tfidf_logreg | homoglyph | 81.7% | 0.8% |
| tfidf_logreg | human_edit | nan% | 1.1% |
| tfidf_logreg | launder_lite | 63.3% | 22.7% |
| tfidf_logreg | light_human_edit | 78.7% | 10.7% |
| tfidf_logreg | paraphrase_t5 | 63.0% | 13.8% |
| tfidf_logreg | roundtrip_fr | 78.0% | 12.0% |
| tfidf_logreg | typo | 80.2% | 1.5% |
| tfidf_logreg | whitespace_noise | 79.4% | 0.0% |
| tfidf_logreg | zero_width | 79.0% | 1.5% |
