# STRESS-Test Statistics

> **Interpretation note.** Preliminary sensitivity analysis. Thresholds are estimated at 1% FPR from clean human records in the evaluation pool, not from an independent held-out calibration set.

*95% document-clustered bootstrap confidence intervals.*

## Rates with confidence intervals

| Detector | Condition | TPR [95% CI] | FPR [95% CI] |
|---|---|---|---|
| binoculars_lite | case_noise | 5.3% [2.7%, 8.0%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | clean | 99.6% [98.9%, 100.0%] | 1.0% [0.6%, 1.3%] |
| binoculars_lite | contraction_expand | 99.6% [98.9%, 100.0%] | 0.8% [0.0%, 1.9%] |
| binoculars_lite | esl_student | 82.7% [76.0%, 88.7%] | 2.7% [0.7%, 5.3%] |
| binoculars_lite | grammar_correct | 98.9% [97.3%, 100.0%] | 2.4% [1.8%, 3.0%] |
| binoculars_lite | homoglyph | 48.9% [42.4%, 55.0%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | human_edit | nan% [nan%, nan%] | 3.3% [2.2%, 4.3%] |
| binoculars_lite | launder_lite | 49.3% [41.3%, 57.3%] | 3.3% [0.7%, 6.7%] |
| binoculars_lite | light_human_edit | 99.3% [98.0%, 100.0%] | 4.7% [1.3%, 8.0%] |
| binoculars_lite | paraphrase_t5 | 69.5% [63.7%, 74.8%] | 7.8% [5.7%, 10.0%] |
| binoculars_lite | roundtrip_fr | 82.7% [76.7%, 88.7%] | 2.7% [0.7%, 5.3%] |
| binoculars_lite | typo | 42.4% [36.6%, 48.5%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | whitespace_noise | 89.3% [85.5%, 92.7%] | 0.4% [0.0%, 1.1%] |
| binoculars_lite | zero_width | 29.4% [23.7%, 34.7%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | case_noise | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | clean | 72.1% [66.8%, 77.9%] | 1.0% [0.7%, 1.4%] |
| deberta_hc3_ft | contraction_expand | 72.5% [67.2%, 78.2%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | esl_student | 67.3% [59.3%, 74.0%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | grammar_correct | 73.3% [67.9%, 78.6%] | 2.8% [2.2%, 3.4%] |
| deberta_hc3_ft | homoglyph | 3.1% [1.1%, 5.3%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | human_edit | nan% [nan%, nan%] | 5.7% [4.4%, 7.1%] |
| deberta_hc3_ft | launder_lite | 56.7% [48.7%, 64.7%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | light_human_edit | 73.3% [66.0%, 80.0%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | paraphrase_t5 | 79.4% [74.4%, 84.4%] | 0.5% [0.0%, 1.2%] |
| deberta_hc3_ft | roundtrip_fr | 66.0% [58.7%, 73.3%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | typo | 15.3% [11.1%, 19.8%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | whitespace_noise | 72.1% [66.8%, 77.9%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | zero_width | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | case_noise | 18.7% [14.1%, 23.7%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | clean | 95.0% [92.4%, 97.3%] | 1.0% [0.6%, 1.4%] |
| fast_detect_gpt | contraction_expand | 95.4% [92.7%, 97.7%] | 0.4% [0.0%, 1.1%] |
| fast_detect_gpt | esl_student | 68.7% [61.3%, 76.0%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | grammar_correct | 93.5% [90.5%, 96.2%] | 2.7% [2.1%, 3.3%] |
| fast_detect_gpt | homoglyph | 51.9% [45.8%, 58.0%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | human_edit | nan% [nan%, nan%] | 2.6% [1.7%, 3.5%] |
| fast_detect_gpt | launder_lite | 29.3% [22.0%, 36.7%] | 0.7% [0.0%, 2.0%] |
| fast_detect_gpt | light_human_edit | 95.3% [92.0%, 98.0%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | paraphrase_t5 | 55.0% [48.9%, 61.1%] | 5.0% [3.3%, 6.8%] |
| fast_detect_gpt | roundtrip_fr | 67.3% [60.0%, 74.7%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | typo | 47.3% [41.2%, 53.8%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | whitespace_noise | 69.5% [63.7%, 75.2%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | zero_width | 16.4% [11.8%, 21.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | case_noise | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | clean | 88.2% [84.0%, 92.0%] | 1.0% [0.7%, 1.4%] |
| perplexity | contraction_expand | 88.5% [84.7%, 92.4%] | 0.0% [0.0%, 0.0%] |
| perplexity | esl_student | 64.7% [56.7%, 72.0%] | 1.3% [0.0%, 3.3%] |
| perplexity | grammar_correct | 91.2% [87.8%, 94.3%] | 3.0% [2.4%, 3.7%] |
| perplexity | homoglyph | 0.8% [0.0%, 1.9%] | 0.0% [0.0%, 0.0%] |
| perplexity | human_edit | nan% [nan%, nan%] | 3.0% [2.0%, 4.2%] |
| perplexity | launder_lite | 30.0% [22.7%, 37.3%] | 0.0% [0.0%, 0.0%] |
| perplexity | light_human_edit | 92.7% [88.0%, 96.7%] | 0.7% [0.0%, 2.0%] |
| perplexity | paraphrase_t5 | 38.2% [32.4%, 43.9%] | 0.5% [0.0%, 1.2%] |
| perplexity | roundtrip_fr | 60.7% [52.7%, 68.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | typo | 6.9% [3.8%, 9.9%] | 0.0% [0.0%, 0.0%] |
| perplexity | whitespace_noise | 48.1% [42.4%, 54.2%] | 0.0% [0.0%, 0.0%] |
| perplexity | zero_width | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | case_noise | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | clean | 51.9% [45.8%, 57.6%] | 1.0% [0.6%, 1.4%] |
| roberta_openai | contraction_expand | 52.7% [46.2%, 58.4%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | esl_student | 38.0% [30.7%, 46.0%] | 1.3% [0.0%, 3.3%] |
| roberta_openai | grammar_correct | 47.7% [41.6%, 53.8%] | 4.6% [3.8%, 5.4%] |
| roberta_openai | homoglyph | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | human_edit | nan% [nan%, nan%] | 4.6% [3.4%, 5.9%] |
| roberta_openai | launder_lite | 20.0% [14.0%, 26.7%] | 8.0% [4.0%, 12.7%] |
| roberta_openai | light_human_edit | 46.7% [38.7%, 55.3%] | 0.7% [0.0%, 2.0%] |
| roberta_openai | paraphrase_t5 | 27.1% [21.8%, 32.8%] | 8.1% [6.0%, 10.3%] |
| roberta_openai | roundtrip_fr | 32.0% [24.7%, 39.3%] | 0.7% [0.0%, 2.0%] |
| roberta_openai | typo | 0.4% [0.0%, 1.1%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | whitespace_noise | 18.7% [14.1%, 23.3%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | zero_width | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | case_noise | 24.4% [19.5%, 29.8%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | clean | 24.4% [19.5%, 29.8%] | 1.0% [0.6%, 1.3%] |
| stylometric_gbm | contraction_expand | 24.8% [19.8%, 30.2%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | esl_student | 16.7% [10.7%, 22.7%] | 0.7% [0.0%, 2.0%] |
| stylometric_gbm | grammar_correct | 26.3% [21.0%, 31.7%] | 1.0% [0.7%, 1.4%] |
| stylometric_gbm | homoglyph | 12.2% [8.4%, 16.4%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | human_edit | nan% [nan%, nan%] | 1.1% [0.6%, 1.8%] |
| stylometric_gbm | launder_lite | 16.0% [10.0%, 22.0%] | 0.7% [0.0%, 2.0%] |
| stylometric_gbm | light_human_edit | 21.3% [14.7%, 28.0%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | paraphrase_t5 | 15.3% [11.1%, 19.5%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | roundtrip_fr | 16.0% [10.7%, 22.0%] | 0.7% [0.0%, 2.0%] |
| stylometric_gbm | typo | 16.4% [11.8%, 21.0%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | whitespace_noise | 24.8% [19.8%, 30.2%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | zero_width | 6.9% [3.8%, 9.9%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | case_noise | 57.3% [51.5%, 63.0%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | clean | 57.3% [51.5%, 63.0%] | 1.0% [0.7%, 1.4%] |
| tfidf_logreg | contraction_expand | 57.3% [51.5%, 63.0%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | esl_student | 52.0% [43.3%, 60.7%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | grammar_correct | 56.5% [50.8%, 62.2%] | 1.0% [0.7%, 1.4%] |
| tfidf_logreg | homoglyph | 58.0% [52.3%, 63.7%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | human_edit | nan% [nan%, nan%] | 0.9% [0.4%, 1.5%] |
| tfidf_logreg | launder_lite | 34.7% [27.3%, 42.7%] | 2.7% [0.0%, 5.3%] |
| tfidf_logreg | light_human_edit | 56.0% [48.0%, 64.0%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | paraphrase_t5 | 29.0% [23.7%, 34.4%] | 1.5% [0.7%, 2.5%] |
| tfidf_logreg | roundtrip_fr | 54.0% [46.0%, 62.0%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | typo | 57.3% [51.5%, 63.0%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | whitespace_noise | 57.3% [51.5%, 63.0%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | zero_width | 56.5% [50.8%, 62.2%] | 0.0% [0.0%, 0.0%] |

## Paired detector comparisons (per-example accuracy)

### binoculars_lite vs deberta_hc3_ft

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +2.7% | 14 / 0 | 0.0001 | 0.0014 * |
| clean | +2.4% | 96 / 23 | 0.0001 | 0.0014 * |
| contraction_expand | +13.2% | 71 / 2 | 0.0001 | 0.0014 * |
| esl_student | +6.3% | 36 / 17 | 0.0137 | 0.0274 * |
| grammar_correct | +2.5% | 138 / 60 | 0.0001 | 0.0014 * |
| homoglyph | +22.9% | 120 / 0 | 0.0001 | 0.0014 * |
| human_edit | +2.5% | 64 / 36 | 0.0056 | 0.0224 * |
| launder_lite | -5.3% | 24 / 40 | 0.0560 | 0.0560 |
| light_human_edit | +10.7% | 39 / 7 | 0.0001 | 0.0014 * |
| paraphrase_t5 | -8.1% | 35 / 105 | 0.0001 | 0.0014 * |
| roundtrip_fr | +7.0% | 39 / 18 | 0.0080 | 0.0240 * |
| typo | +13.5% | 96 / 25 | 0.0001 | 0.0014 * |
| whitespace_noise | +8.4% | 62 / 18 | 0.0001 | 0.0014 * |
| zero_width | +14.7% | 77 / 0 | 0.0001 | 0.0014 * |

### binoculars_lite vs fast_detect_gpt

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -6.7% | 11 / 46 | 0.0001 | 0.0014 * |
| clean | +0.4% | 31 / 19 | 0.1155 | 0.5774 |
| contraction_expand | +1.9% | 11 / 1 | 0.0063 | 0.0567 |
| esl_student | +5.7% | 28 / 11 | 0.0091 | 0.0728 |
| grammar_correct | +0.7% | 63 / 40 | 0.0302 | 0.2114 |
| homoglyph | -1.5% | 49 / 57 | 0.5046 | 1.0000 |
| human_edit | -0.7% | 19 / 27 | 0.2987 | 0.8960 |
| launder_lite | +8.7% | 42 / 16 | 0.0009 | 0.0099 * |
| light_human_edit | -0.3% | 6 / 7 | 1.0000 | 1.0000 |
| paraphrase_t5 | +2.4% | 78 / 57 | 0.0864 | 0.5183 |
| roundtrip_fr | +6.3% | 30 / 11 | 0.0052 | 0.0520 |
| typo | -2.5% | 39 / 52 | 0.2074 | 0.8295 |
| whitespace_noise | +9.7% | 59 / 8 | 0.0001 | 0.0014 * |
| zero_width | +6.5% | 53 / 19 | 0.0002 | 0.0024 * |

### binoculars_lite vs perplexity

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +2.7% | 14 / 0 | 0.0001 | 0.0014 * |
| clean | +1.0% | 49 / 19 | 0.0003 | 0.0021 * |
| contraction_expand | +5.2% | 29 / 2 | 0.0001 | 0.0014 * |
| esl_student | +8.3% | 35 / 10 | 0.0003 | 0.0021 * |
| grammar_correct | +1.2% | 89 / 52 | 0.0018 | 0.0090 * |
| homoglyph | +24.0% | 126 / 0 | 0.0001 | 0.0014 * |
| human_edit | -0.3% | 30 / 33 | 0.7974 | 0.9123 |
| launder_lite | +8.0% | 42 / 18 | 0.0030 | 0.0090 * |
| light_human_edit | +1.3% | 10 / 6 | 0.4562 | 0.9123 |
| paraphrase_t5 | +4.4% | 92 / 54 | 0.0018 | 0.0090 * |
| roundtrip_fr | +9.7% | 41 / 12 | 0.0002 | 0.0016 * |
| typo | +17.7% | 100 / 7 | 0.0001 | 0.0014 * |
| whitespace_noise | +20.4% | 114 / 7 | 0.0001 | 0.0014 * |
| zero_width | +14.7% | 77 / 0 | 0.0001 | 0.0014 * |

### binoculars_lite vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +2.7% | 14 / 0 | 0.0001 | 0.0014 * |
| clean | +4.0% | 147 / 22 | 0.0001 | 0.0014 * |
| contraction_expand | +23.1% | 123 / 2 | 0.0001 | 0.0014 * |
| esl_student | +21.7% | 73 / 8 | 0.0001 | 0.0014 * |
| grammar_correct | +6.3% | 250 / 55 | 0.0001 | 0.0014 * |
| homoglyph | +24.4% | 128 / 0 | 0.0001 | 0.0014 * |
| human_edit | +1.3% | 49 / 34 | 0.1259 | 0.1259 |
| launder_lite | +17.0% | 71 / 20 | 0.0001 | 0.0014 * |
| light_human_edit | +24.3% | 80 / 7 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +13.0% | 170 / 57 | 0.0001 | 0.0014 * |
| roundtrip_fr | +24.3% | 80 / 7 | 0.0001 | 0.0014 * |
| typo | +21.0% | 110 / 0 | 0.0001 | 0.0014 * |
| whitespace_noise | +35.1% | 187 / 3 | 0.0001 | 0.0014 * |
| zero_width | +14.7% | 77 / 0 | 0.0001 | 0.0014 * |

### binoculars_lite vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -9.5% | 10 / 60 | 0.0001 | 0.0014 * |
| clean | +6.4% | 226 / 29 | 0.0001 | 0.0014 * |
| contraction_expand | +37.0% | 197 / 3 | 0.0001 | 0.0014 * |
| esl_student | +32.0% | 103 / 7 | 0.0001 | 0.0014 * |
| grammar_correct | +4.8% | 221 / 71 | 0.0001 | 0.0014 * |
| homoglyph | +18.3% | 111 / 15 | 0.0001 | 0.0014 * |
| human_edit | -2.1% | 12 / 36 | 0.0004 | 0.0014 * |
| launder_lite | +15.3% | 57 / 11 | 0.0001 | 0.0014 * |
| light_human_edit | +36.7% | 118 / 8 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +11.0% | 150 / 55 | 0.0001 | 0.0014 * |
| roundtrip_fr | +32.3% | 105 / 8 | 0.0001 | 0.0014 * |
| typo | +13.0% | 90 / 22 | 0.0001 | 0.0014 * |
| whitespace_noise | +32.1% | 176 / 8 | 0.0001 | 0.0014 * |
| zero_width | +11.3% | 68 / 9 | 0.0001 | 0.0014 * |

### binoculars_lite vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -26.0% | 4 / 140 | 0.0001 | 0.0014 * |
| clean | +3.6% | 139 / 28 | 0.0001 | 0.0014 * |
| contraction_expand | +20.8% | 111 / 2 | 0.0001 | 0.0014 * |
| esl_student | +14.0% | 55 / 13 | 0.0001 | 0.0014 * |
| grammar_correct | +2.3% | 141 / 69 | 0.0001 | 0.0014 * |
| homoglyph | -4.6% | 48 / 72 | 0.0378 | 0.0602 |
| human_edit | -2.4% | 10 / 37 | 0.0002 | 0.0014 * |
| launder_lite | +7.0% | 55 / 34 | 0.0301 | 0.0602 |
| light_human_edit | +19.3% | 65 / 7 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +7.9% | 135 / 67 | 0.0001 | 0.0014 * |
| roundtrip_fr | +13.0% | 55 / 16 | 0.0001 | 0.0014 * |
| typo | -7.4% | 43 / 82 | 0.0007 | 0.0021 * |
| whitespace_noise | +15.8% | 94 / 11 | 0.0001 | 0.0014 * |
| zero_width | -13.5% | 34 / 105 | 0.0001 | 0.0014 * |

### deberta_hc3_ft vs fast_detect_gpt

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -9.4% | 0 / 49 | 0.0001 | 0.0014 * |
| clean | -2.0% | 32 / 93 | 0.0001 | 0.0014 * |
| contraction_expand | -11.3% | 9 / 68 | 0.0001 | 0.0014 * |
| esl_student | -0.7% | 33 / 35 | 0.9042 | 1.0000 |
| grammar_correct | -1.8% | 75 / 130 | 0.0002 | 0.0014 * |
| homoglyph | -24.4% | 3 / 131 | 0.0001 | 0.0014 * |
| human_edit | -3.2% | 21 / 57 | 0.0002 | 0.0014 * |
| launder_lite | +14.0% | 58 / 16 | 0.0001 | 0.0014 * |
| light_human_edit | -11.0% | 3 / 36 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +10.5% | 118 / 27 | 0.0001 | 0.0014 * |
| roundtrip_fr | -0.7% | 32 / 34 | 0.9022 | 1.0000 |
| typo | -16.0% | 19 / 103 | 0.0001 | 0.0014 * |
| whitespace_noise | +1.3% | 51 / 44 | 0.5330 | 1.0000 |
| zero_width | -8.2% | 0 / 43 | 0.0001 | 0.0014 * |

### deberta_hc3_ft vs perplexity

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.0% | 0 / 0 | 1.0000 | 1.0000 |
| clean | -1.4% | 34 / 77 | 0.0001 | 0.0014 * |
| contraction_expand | -8.0% | 17 / 59 | 0.0001 | 0.0014 * |
| esl_student | +2.0% | 27 / 21 | 0.4675 | 1.0000 |
| grammar_correct | -1.3% | 66 / 107 | 0.0023 | 0.0161 * |
| homoglyph | +1.1% | 8 / 2 | 0.1103 | 0.5514 |
| human_edit | -2.7% | 16 / 47 | 0.0002 | 0.0018 * |
| launder_lite | +13.3% | 49 / 9 | 0.0001 | 0.0014 * |
| light_human_edit | -9.3% | 5 / 33 | 0.0002 | 0.0018 * |
| paraphrase_t5 | +12.5% | 127 / 19 | 0.0001 | 0.0014 * |
| roundtrip_fr | +2.7% | 25 / 17 | 0.2805 | 1.0000 |
| typo | +4.2% | 36 / 14 | 0.0033 | 0.0198 * |
| whitespace_noise | +12.0% | 92 / 29 | 0.0001 | 0.0014 * |
| zero_width | +0.0% | 0 / 0 | 1.0000 | 1.0000 |

### deberta_hc3_ft vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.0% | 0 / 0 | 1.0000 | 1.0000 |
| clean | +1.7% | 117 / 65 | 0.0001 | 0.0014 * |
| contraction_expand | +9.9% | 93 / 41 | 0.0001 | 0.0014 * |
| esl_student | +15.3% | 61 / 15 | 0.0001 | 0.0014 * |
| grammar_correct | +3.8% | 219 / 102 | 0.0001 | 0.0014 * |
| homoglyph | +1.5% | 8 / 0 | 0.0068 | 0.0272 * |
| human_edit | -1.1% | 37 / 50 | 0.1958 | 0.5873 |
| launder_lite | +22.3% | 78 / 11 | 0.0001 | 0.0014 * |
| light_human_edit | +13.7% | 60 / 19 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +21.1% | 198 / 15 | 0.0001 | 0.0014 * |
| roundtrip_fr | +17.3% | 66 / 14 | 0.0001 | 0.0014 * |
| typo | +7.4% | 40 / 1 | 0.0001 | 0.0014 * |
| whitespace_noise | +26.7% | 154 / 14 | 0.0001 | 0.0014 * |
| zero_width | +0.0% | 0 / 0 | 1.0000 | 1.0000 |

### deberta_hc3_ft vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -12.2% | 0 / 64 | 0.0001 | 0.0014 * |
| clean | +4.0% | 166 / 42 | 0.0001 | 0.0014 * |
| contraction_expand | +23.9% | 140 / 15 | 0.0001 | 0.0014 * |
| esl_student | +25.7% | 86 / 9 | 0.0001 | 0.0014 * |
| grammar_correct | +2.3% | 164 / 92 | 0.0002 | 0.0014 * |
| homoglyph | -4.6% | 8 / 32 | 0.0001 | 0.0014 * |
| human_edit | -4.6% | 11 / 63 | 0.0001 | 0.0014 * |
| launder_lite | +20.7% | 72 / 10 | 0.0001 | 0.0014 * |
| light_human_edit | +26.0% | 88 / 10 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +19.1% | 170 / 5 | 0.0001 | 0.0014 * |
| roundtrip_fr | +25.3% | 82 / 6 | 0.0001 | 0.0014 * |
| typo | -0.6% | 34 / 37 | 0.8115 | 0.8115 |
| whitespace_noise | +23.7% | 139 / 15 | 0.0001 | 0.0014 * |
| zero_width | -3.4% | 0 / 18 | 0.0001 | 0.0014 * |

### deberta_hc3_ft vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -28.6% | 0 / 150 | 0.0001 | 0.0014 * |
| clean | +1.2% | 108 / 70 | 0.0050 | 0.0150 * |
| contraction_expand | +7.6% | 81 / 41 | 0.0005 | 0.0035 * |
| esl_student | +7.7% | 41 / 18 | 0.0032 | 0.0128 * |
| grammar_correct | -0.2% | 111 / 117 | 0.7419 | 0.7419 |
| homoglyph | -27.5% | 2 / 146 | 0.0001 | 0.0014 * |
| human_edit | -4.9% | 9 / 64 | 0.0001 | 0.0014 * |
| launder_lite | +12.3% | 48 / 11 | 0.0001 | 0.0014 * |
| light_human_edit | +8.7% | 46 / 20 | 0.0016 | 0.0080 * |
| paraphrase_t5 | +15.9% | 143 / 5 | 0.0001 | 0.0014 * |
| roundtrip_fr | +6.0% | 39 / 21 | 0.0258 | 0.0516 |
| typo | -21.0% | 9 / 119 | 0.0001 | 0.0014 * |
| whitespace_noise | +7.4% | 81 / 42 | 0.0005 | 0.0035 * |
| zero_width | -28.2% | 0 / 148 | 0.0001 | 0.0014 * |

### fast_detect_gpt vs perplexity

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +9.4% | 49 / 0 | 0.0001 | 0.0014 * |
| clean | +0.6% | 45 / 27 | 0.0478 | 0.3824 |
| contraction_expand | +3.2% | 25 / 8 | 0.0040 | 0.0360 * |
| esl_student | +2.7% | 33 / 25 | 0.3573 | 1.0000 |
| grammar_correct | +0.5% | 82 / 68 | 0.2848 | 1.0000 |
| homoglyph | +25.6% | 135 / 1 | 0.0001 | 0.0014 * |
| human_edit | +0.4% | 27 / 22 | 0.5692 | 1.0000 |
| launder_lite | -0.7% | 28 / 30 | 0.8992 | 1.0000 |
| light_human_edit | +1.7% | 8 / 3 | 0.2205 | 1.0000 |
| paraphrase_t5 | +2.0% | 78 / 61 | 0.1749 | 1.0000 |
| roundtrip_fr | +3.3% | 33 / 23 | 0.2255 | 1.0000 |
| typo | +20.2% | 112 / 6 | 0.0001 | 0.0014 * |
| whitespace_noise | +10.7% | 84 / 28 | 0.0001 | 0.0014 * |
| zero_width | +8.2% | 43 / 0 | 0.0001 | 0.0014 * |

### fast_detect_gpt vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +9.4% | 49 / 0 | 0.0001 | 0.0014 * |
| clean | +3.6% | 141 / 28 | 0.0001 | 0.0014 * |
| contraction_expand | +21.2% | 115 / 4 | 0.0001 | 0.0014 * |
| esl_student | +16.0% | 58 / 10 | 0.0001 | 0.0014 * |
| grammar_correct | +5.6% | 229 / 57 | 0.0001 | 0.0014 * |
| homoglyph | +26.0% | 136 / 0 | 0.0001 | 0.0014 * |
| human_edit | +2.0% | 44 / 21 | 0.0064 | 0.0064 * |
| launder_lite | +8.3% | 43 / 18 | 0.0018 | 0.0036 * |
| light_human_edit | +24.7% | 74 / 0 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +10.6% | 130 / 38 | 0.0001 | 0.0014 * |
| roundtrip_fr | +18.0% | 63 / 9 | 0.0001 | 0.0014 * |
| typo | +23.5% | 123 / 0 | 0.0001 | 0.0014 * |
| whitespace_noise | +25.4% | 139 / 6 | 0.0001 | 0.0014 * |
| zero_width | +8.2% | 43 / 0 | 0.0001 | 0.0014 * |

### fast_detect_gpt vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -2.9% | 32 / 47 | 0.1142 | 0.1142 |
| clean | +6.0% | 214 / 29 | 0.0001 | 0.0014 * |
| contraction_expand | +35.1% | 186 / 2 | 0.0001 | 0.0014 * |
| esl_student | +26.3% | 82 / 3 | 0.0001 | 0.0014 * |
| grammar_correct | +4.1% | 208 / 81 | 0.0001 | 0.0014 * |
| homoglyph | +19.8% | 113 / 9 | 0.0001 | 0.0014 * |
| human_edit | -1.4% | 13 / 29 | 0.0211 | 0.0422 * |
| launder_lite | +6.7% | 29 / 9 | 0.0022 | 0.0066 * |
| light_human_edit | +37.0% | 112 / 1 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +8.5% | 112 / 38 | 0.0001 | 0.0014 * |
| roundtrip_fr | +26.0% | 84 / 6 | 0.0001 | 0.0014 * |
| typo | +15.5% | 99 / 18 | 0.0001 | 0.0014 * |
| whitespace_noise | +22.3% | 131 / 14 | 0.0001 | 0.0014 * |
| zero_width | +4.8% | 36 / 11 | 0.0006 | 0.0024 * |

### fast_detect_gpt vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -19.3% | 15 / 116 | 0.0001 | 0.0014 * |
| clean | +3.2% | 134 / 35 | 0.0001 | 0.0014 * |
| contraction_expand | +18.9% | 106 / 7 | 0.0001 | 0.0014 * |
| esl_student | +8.3% | 50 / 25 | 0.0039 | 0.0234 * |
| grammar_correct | +1.6% | 136 / 87 | 0.0013 | 0.0104 * |
| homoglyph | -3.1% | 57 / 73 | 0.1889 | 0.3778 |
| human_edit | -1.7% | 10 / 29 | 0.0030 | 0.0210 * |
| launder_lite | -1.7% | 30 / 35 | 0.6216 | 0.6216 |
| light_human_edit | +19.7% | 63 / 4 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +5.4% | 115 / 68 | 0.0003 | 0.0027 * |
| roundtrip_fr | +6.7% | 47 / 27 | 0.0242 | 0.0968 |
| typo | -5.0% | 51 / 77 | 0.0270 | 0.0968 |
| whitespace_noise | +6.1% | 83 / 51 | 0.0057 | 0.0285 * |
| zero_width | -20.0% | 17 / 122 | 0.0001 | 0.0014 * |

### perplexity vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.0% | 0 / 0 | 1.0000 | 1.0000 |
| clean | +3.1% | 121 / 26 | 0.0001 | 0.0014 * |
| contraction_expand | +17.9% | 103 / 9 | 0.0001 | 0.0014 * |
| esl_student | +13.3% | 54 / 14 | 0.0001 | 0.0014 * |
| grammar_correct | +5.1% | 224 / 66 | 0.0001 | 0.0014 * |
| homoglyph | +0.4% | 2 / 0 | 0.5023 | 1.0000 |
| human_edit | +1.6% | 47 / 29 | 0.0511 | 0.2044 |
| launder_lite | +9.0% | 44 / 17 | 0.0007 | 0.0035 * |
| light_human_edit | +23.0% | 73 / 4 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +8.7% | 113 / 38 | 0.0001 | 0.0014 * |
| roundtrip_fr | +14.7% | 55 / 11 | 0.0001 | 0.0014 * |
| typo | +3.2% | 18 / 1 | 0.0001 | 0.0014 * |
| whitespace_noise | +14.7% | 94 / 17 | 0.0001 | 0.0014 * |
| zero_width | +0.0% | 0 / 0 | 1.0000 | 1.0000 |

### perplexity vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -12.2% | 0 / 64 | 0.0001 | 0.0014 * |
| clean | +5.4% | 201 / 34 | 0.0001 | 0.0014 * |
| contraction_expand | +31.9% | 174 / 7 | 0.0001 | 0.0014 * |
| esl_student | +23.7% | 82 / 11 | 0.0001 | 0.0014 * |
| grammar_correct | +3.6% | 198 / 85 | 0.0001 | 0.0014 * |
| homoglyph | -5.7% | 2 / 32 | 0.0001 | 0.0014 * |
| human_edit | -1.9% | 12 / 33 | 0.0025 | 0.0050 * |
| launder_lite | +7.3% | 40 / 18 | 0.0061 | 0.0061 * |
| light_human_edit | +35.3% | 110 / 4 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +6.6% | 85 / 28 | 0.0001 | 0.0014 * |
| roundtrip_fr | +22.7% | 79 / 11 | 0.0001 | 0.0014 * |
| typo | -4.8% | 15 / 40 | 0.0007 | 0.0021 * |
| whitespace_noise | +11.6% | 92 / 31 | 0.0001 | 0.0014 * |
| zero_width | -3.4% | 0 / 18 | 0.0001 | 0.0014 * |

### perplexity vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -28.6% | 0 / 150 | 0.0001 | 0.0014 * |
| clean | +2.6% | 124 / 43 | 0.0001 | 0.0014 * |
| contraction_expand | +15.6% | 96 / 14 | 0.0001 | 0.0014 * |
| esl_student | +5.7% | 43 / 26 | 0.0526 | 0.1852 |
| grammar_correct | +1.1% | 130 / 95 | 0.0219 | 0.1095 |
| homoglyph | -28.6% | 1 / 151 | 0.0001 | 0.0014 * |
| human_edit | -2.1% | 10 / 34 | 0.0003 | 0.0021 * |
| launder_lite | -1.0% | 35 / 38 | 0.8138 | 0.8138 |
| light_human_edit | +18.0% | 60 / 6 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +3.5% | 77 / 47 | 0.0093 | 0.0558 |
| roundtrip_fr | +3.3% | 39 / 29 | 0.2724 | 0.5447 |
| typo | -25.2% | 9 / 141 | 0.0001 | 0.0014 * |
| whitespace_noise | -4.6% | 55 / 79 | 0.0463 | 0.1852 |
| zero_width | -28.2% | 0 / 148 | 0.0001 | 0.0014 * |

### roberta_openai vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -12.2% | 0 / 64 | 0.0001 | 0.0014 * |
| clean | +2.3% | 129 / 57 | 0.0001 | 0.0014 * |
| contraction_expand | +13.9% | 102 / 29 | 0.0001 | 0.0014 * |
| esl_student | +10.3% | 47 / 16 | 0.0005 | 0.0030 * |
| grammar_correct | -1.5% | 119 / 164 | 0.0095 | 0.0380 * |
| homoglyph | -6.1% | 0 / 32 | 0.0001 | 0.0014 * |
| human_edit | -3.4% | 12 / 51 | 0.0001 | 0.0014 * |
| launder_lite | -1.7% | 22 / 27 | 0.5664 | 0.5664 |
| light_human_edit | +12.3% | 53 / 16 | 0.0001 | 0.0014 * |
| paraphrase_t5 | -2.1% | 57 / 75 | 0.1424 | 0.2848 |
| roundtrip_fr | +8.0% | 39 / 15 | 0.0021 | 0.0105 * |
| typo | -8.0% | 1 / 43 | 0.0001 | 0.0014 * |
| whitespace_noise | -3.1% | 31 / 47 | 0.0872 | 0.2616 |
| zero_width | -3.4% | 0 / 18 | 0.0001 | 0.0014 * |

### roberta_openai vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -28.6% | 0 / 150 | 0.0001 | 0.0014 * |
| clean | -0.5% | 83 / 97 | 0.3303 | 0.6391 |
| contraction_expand | -2.3% | 57 / 69 | 0.3196 | 0.6391 |
| esl_student | -7.7% | 26 / 49 | 0.0113 | 0.0452 * |
| grammar_correct | -4.0% | 79 / 202 | 0.0001 | 0.0014 * |
| homoglyph | -29.0% | 0 / 152 | 0.0001 | 0.0014 * |
| human_edit | -3.7% | 10 / 52 | 0.0001 | 0.0014 * |
| launder_lite | -10.0% | 21 / 51 | 0.0002 | 0.0014 * |
| light_human_edit | -5.0% | 31 / 46 | 0.1070 | 0.3210 |
| paraphrase_t5 | -5.2% | 49 / 94 | 0.0002 | 0.0014 * |
| roundtrip_fr | -11.3% | 24 / 58 | 0.0004 | 0.0020 * |
| typo | -28.4% | 0 / 149 | 0.0001 | 0.0014 * |
| whitespace_noise | -19.3% | 24 / 125 | 0.0001 | 0.0014 * |
| zero_width | -28.2% | 0 / 148 | 0.0001 | 0.0014 * |

### stylometric_gbm vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -16.4% | 32 / 118 | 0.0001 | 0.0014 * |
| clean | -2.8% | 59 / 145 | 0.0001 | 0.0014 * |
| contraction_expand | -16.2% | 33 / 118 | 0.0001 | 0.0014 * |
| esl_student | -18.0% | 15 / 69 | 0.0001 | 0.0014 * |
| grammar_correct | -2.5% | 61 / 139 | 0.0001 | 0.0014 * |
| homoglyph | -22.9% | 17 / 137 | 0.0001 | 0.0014 * |
| human_edit | -0.3% | 10 / 13 | 0.6769 | 0.6769 |
| launder_lite | -8.3% | 23 / 48 | 0.0041 | 0.0123 * |
| light_human_edit | -17.3% | 16 / 68 | 0.0001 | 0.0014 * |
| paraphrase_t5 | -3.1% | 41 / 68 | 0.0103 | 0.0206 * |
| roundtrip_fr | -19.3% | 13 / 71 | 0.0001 | 0.0014 * |
| typo | -20.4% | 21 / 128 | 0.0001 | 0.0014 * |
| whitespace_noise | -16.2% | 33 / 118 | 0.0001 | 0.0014 * |
| zero_width | -24.8% | 11 / 141 | 0.0001 | 0.0014 * |

