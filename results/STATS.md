# STRESS-Test Statistics

*95% document-clustered bootstrap CIs; thresholds frozen at 1% FPR on clean human text.*

## Rates with confidence intervals

| Detector | Condition | TPR [95% CI] | FPR [95% CI] |
|---|---|---|---|
| binoculars_lite | case_noise | 3.4% [1.5%, 5.7%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | clean | 98.9% [97.3%, 100.0%] | 1.0% [0.3%, 1.8%] |
| binoculars_lite | contraction_expand | 99.2% [98.1%, 100.0%] | 0.4% [0.0%, 1.1%] |
| binoculars_lite | esl_student | 76.0% [69.3%, 82.7%] | 2.0% [0.0%, 4.7%] |
| binoculars_lite | grammar_correct | 97.3% [95.4%, 99.2%] | 3.2% [1.8%, 4.6%] |
| binoculars_lite | homoglyph | 37.0% [30.9%, 42.7%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | launder_lite | 38.0% [30.7%, 45.3%] | 2.0% [0.0%, 4.7%] |
| binoculars_lite | light_human_edit | 99.3% [98.0%, 100.0%] | 2.0% [0.0%, 4.7%] |
| binoculars_lite | paraphrase_t5 | 58.0% [52.3%, 63.7%] | 5.3% [3.5%, 7.1%] |
| binoculars_lite | roundtrip_fr | 75.3% [68.7%, 82.0%] | 2.0% [0.0%, 4.7%] |
| binoculars_lite | typo | 31.3% [25.6%, 37.0%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | whitespace_noise | 82.8% [78.2%, 87.4%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | zero_width | 17.2% [12.6%, 22.1%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | case_noise | 29.4% [24.0%, 35.1%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | clean | 96.6% [94.3%, 98.5%] | 1.2% [0.3%, 2.2%] |
| fast_detect_gpt | contraction_expand | 96.9% [94.7%, 98.9%] | 0.8% [0.0%, 1.9%] |
| fast_detect_gpt | esl_student | 75.3% [68.7%, 82.0%] | 0.7% [0.0%, 2.0%] |
| fast_detect_gpt | grammar_correct | 95.0% [92.4%, 97.3%] | 3.3% [2.0%, 4.8%] |
| fast_detect_gpt | homoglyph | 64.1% [58.0%, 69.8%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | launder_lite | 38.7% [31.3%, 46.7%] | 2.7% [0.7%, 5.3%] |
| fast_detect_gpt | light_human_edit | 96.0% [92.7%, 98.7%] | 3.3% [0.7%, 6.7%] |
| fast_detect_gpt | paraphrase_t5 | 66.0% [60.3%, 71.8%] | 8.5% [6.3%, 10.8%] |
| fast_detect_gpt | roundtrip_fr | 75.3% [68.0%, 82.0%] | 0.7% [0.0%, 2.0%] |
| fast_detect_gpt | typo | 60.7% [54.6%, 66.8%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | whitespace_noise | 79.4% [74.4%, 84.4%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | zero_width | 26.3% [21.0%, 31.7%] | 0.0% [0.0%, 0.0%] |
| perplexity | case_noise | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | clean | 94.3% [91.2%, 96.9%] | 1.0% [0.3%, 1.8%] |
| perplexity | contraction_expand | 94.7% [91.6%, 97.3%] | 1.1% [0.0%, 2.7%] |
| perplexity | esl_student | 80.7% [74.0%, 86.7%] | 2.7% [0.7%, 5.3%] |
| perplexity | grammar_correct | 94.7% [92.0%, 97.0%] | 3.2% [1.8%, 4.5%] |
| perplexity | homoglyph | 1.5% [0.4%, 3.1%] | 0.0% [0.0%, 0.0%] |
| perplexity | launder_lite | 49.3% [41.3%, 56.7%] | 0.0% [0.0%, 0.0%] |
| perplexity | light_human_edit | 95.3% [91.3%, 98.7%] | 0.7% [0.0%, 2.0%] |
| perplexity | paraphrase_t5 | 59.9% [54.6%, 65.6%] | 1.5% [0.7%, 2.5%] |
| perplexity | roundtrip_fr | 77.3% [70.0%, 83.3%] | 1.3% [0.0%, 3.3%] |
| perplexity | typo | 12.2% [8.4%, 16.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | whitespace_noise | 69.5% [63.7%, 74.8%] | 0.4% [0.0%, 1.1%] |
| perplexity | zero_width | 0.4% [0.0%, 1.1%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | case_noise | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | clean | 78.6% [73.3%, 83.2%] | 1.2% [0.3%, 2.0%] |
| roberta_openai | contraction_expand | 79.4% [74.4%, 84.4%] | 0.4% [0.0%, 1.1%] |
| roberta_openai | esl_student | 62.0% [54.7%, 70.0%] | 3.3% [0.7%, 6.7%] |
| roberta_openai | grammar_correct | 73.3% [67.6%, 78.3%] | 4.0% [2.5%, 5.6%] |
| roberta_openai | homoglyph | 0.4% [0.0%, 1.1%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | launder_lite | 34.7% [27.3%, 42.7%] | 16.0% [10.7%, 22.0%] |
| roberta_openai | light_human_edit | 70.7% [63.3%, 78.0%] | 2.0% [0.0%, 4.7%] |
| roberta_openai | paraphrase_t5 | 44.7% [38.5%, 51.1%] | 14.8% [12.1%, 17.7%] |
| roberta_openai | roundtrip_fr | 47.3% [38.7%, 55.3%] | 2.0% [0.0%, 4.7%] |
| roberta_openai | typo | 0.8% [0.0%, 1.9%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | whitespace_noise | 32.1% [26.3%, 37.8%] | 0.4% [0.0%, 1.1%] |
| roberta_openai | zero_width | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | case_noise | 65.3% [59.2%, 70.6%] | 1.5% [0.4%, 3.1%] |
| stylometric_gbm | clean | 65.3% [59.2%, 70.6%] | 1.0% [0.3%, 1.8%] |
| stylometric_gbm | contraction_expand | 65.6% [59.2%, 71.4%] | 1.5% [0.4%, 3.1%] |
| stylometric_gbm | esl_student | 56.7% [48.7%, 64.7%] | 4.0% [1.3%, 7.3%] |
| stylometric_gbm | grammar_correct | 64.1% [58.0%, 69.8%] | 1.0% [0.3%, 1.8%] |
| stylometric_gbm | homoglyph | 49.6% [43.5%, 55.7%] | 0.4% [0.0%, 1.1%] |
| stylometric_gbm | launder_lite | 49.3% [41.3%, 57.3%] | 5.3% [2.0%, 9.3%] |
| stylometric_gbm | light_human_edit | 65.3% [58.0%, 73.3%] | 2.7% [0.7%, 5.3%] |
| stylometric_gbm | paraphrase_t5 | 50.4% [44.3%, 56.1%] | 2.3% [1.2%, 3.7%] |
| stylometric_gbm | roundtrip_fr | 56.7% [48.7%, 64.7%] | 2.7% [0.7%, 5.3%] |
| stylometric_gbm | typo | 58.4% [52.3%, 64.1%] | 0.8% [0.0%, 1.9%] |
| stylometric_gbm | whitespace_noise | 65.3% [59.2%, 70.6%] | 1.5% [0.4%, 3.1%] |
| stylometric_gbm | zero_width | 38.9% [33.2%, 45.0%] | 0.4% [0.0%, 1.1%] |
| tfidf_logreg | case_noise | 79.4% [74.8%, 84.0%] | 0.4% [0.0%, 1.1%] |
| tfidf_logreg | clean | 79.4% [74.8%, 84.0%] | 1.0% [0.3%, 1.8%] |
| tfidf_logreg | contraction_expand | 79.8% [74.8%, 84.4%] | 0.4% [0.0%, 1.1%] |
| tfidf_logreg | esl_student | 75.3% [68.7%, 82.0%] | 2.0% [0.0%, 4.7%] |
| tfidf_logreg | grammar_correct | 77.9% [72.9%, 82.8%] | 0.8% [0.2%, 1.7%] |
| tfidf_logreg | homoglyph | 80.9% [76.3%, 85.5%] | 0.4% [0.0%, 1.1%] |
| tfidf_logreg | launder_lite | 58.0% [50.0%, 66.0%] | 9.3% [4.7%, 14.7%] |
| tfidf_logreg | light_human_edit | 77.3% [70.7%, 84.0%] | 0.7% [0.0%, 2.0%] |
| tfidf_logreg | paraphrase_t5 | 55.0% [48.5%, 61.1%] | 8.3% [6.3%, 10.6%] |
| tfidf_logreg | roundtrip_fr | 74.7% [68.0%, 81.3%] | 1.3% [0.0%, 3.3%] |
| tfidf_logreg | typo | 80.2% [75.6%, 84.7%] | 0.8% [0.0%, 1.9%] |
| tfidf_logreg | whitespace_noise | 79.4% [74.8%, 84.0%] | 0.4% [0.0%, 1.1%] |
| tfidf_logreg | zero_width | 79.4% [74.4%, 84.0%] | 1.1% [0.0%, 2.7%] |

## Paired detector comparisons (per-example accuracy)

### binoculars_lite vs fast_detect_gpt

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -13.0% | 5 / 73 | 0.0001 | 0.0013 * |
| clean | +0.8% | 13 / 6 | 0.1616 | 1.0000 |
| contraction_expand | +1.3% | 9 / 2 | 0.0660 | 0.5279 |
| esl_student | -0.3% | 15 / 16 | 1.0000 | 1.0000 |
| grammar_correct | +0.8% | 21 / 14 | 0.3090 | 1.0000 |
| homoglyph | -13.5% | 23 / 94 | 0.0001 | 0.0013 * |
| launder_lite | +0.0% | 26 / 26 | 1.0000 | 1.0000 |
| light_human_edit | +2.3% | 8 / 1 | 0.0392 | 0.3528 |
| paraphrase_t5 | -0.2% | 70 / 72 | 0.9358 | 1.0000 |
| roundtrip_fr | -0.7% | 19 / 21 | 0.8720 | 1.0000 |
| typo | -14.7% | 15 / 92 | 0.0001 | 0.0013 * |
| whitespace_noise | +1.7% | 33 / 24 | 0.2901 | 1.0000 |
| zero_width | -4.6% | 26 / 50 | 0.0076 | 0.0760 |

### binoculars_lite vs perplexity

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +1.7% | 9 / 0 | 0.0029 | 0.0234 * |
| clean | +1.4% | 15 / 3 | 0.0056 | 0.0392 * |
| contraction_expand | +2.7% | 16 / 2 | 0.0026 | 0.0234 * |
| esl_student | -2.0% | 14 / 20 | 0.3886 | 1.0000 |
| grammar_correct | +0.8% | 19 / 12 | 0.2781 | 1.0000 |
| homoglyph | +17.7% | 93 / 0 | 0.0001 | 0.0013 * |
| launder_lite | -6.7% | 19 / 39 | 0.0141 | 0.0705 |
| light_human_edit | +1.3% | 7 / 3 | 0.3418 | 1.0000 |
| paraphrase_t5 | -3.2% | 36 / 64 | 0.0065 | 0.0392 * |
| roundtrip_fr | -1.3% | 18 / 22 | 0.6297 | 1.0000 |
| typo | +9.5% | 59 / 9 | 0.0001 | 0.0013 * |
| whitespace_noise | +6.9% | 52 / 16 | 0.0001 | 0.0013 * |
| zero_width | +8.4% | 44 / 0 | 0.0001 | 0.0013 * |

### binoculars_lite vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +1.7% | 9 / 0 | 0.0029 | 0.0058 * |
| clean | +6.2% | 58 / 4 | 0.0001 | 0.0013 * |
| contraction_expand | +9.9% | 53 / 1 | 0.0001 | 0.0013 * |
| esl_student | +7.7% | 38 / 15 | 0.0018 | 0.0054 * |
| grammar_correct | +7.9% | 82 / 14 | 0.0001 | 0.0013 * |
| homoglyph | +18.3% | 96 / 0 | 0.0001 | 0.0013 * |
| launder_lite | +8.7% | 59 / 33 | 0.0088 | 0.0088 * |
| light_human_edit | +14.3% | 46 / 3 | 0.0001 | 0.0013 * |
| paraphrase_t5 | +10.6% | 156 / 64 | 0.0001 | 0.0013 * |
| roundtrip_fr | +14.0% | 53 / 11 | 0.0001 | 0.0013 * |
| typo | +15.3% | 80 / 0 | 0.0001 | 0.0013 * |
| whitespace_noise | +25.6% | 146 / 12 | 0.0001 | 0.0013 * |
| zero_width | +8.6% | 45 / 0 | 0.0001 | 0.0013 * |

### binoculars_lite vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -30.2% | 7 / 165 | 0.0001 | 0.0013 * |
| clean | +10.2% | 96 / 8 | 0.0001 | 0.0013 * |
| contraction_expand | +17.4% | 94 / 3 | 0.0001 | 0.0013 * |
| esl_student | +10.7% | 48 / 16 | 0.0002 | 0.0013 * |
| grammar_correct | +8.5% | 98 / 24 | 0.0001 | 0.0013 * |
| homoglyph | -6.1% | 47 / 79 | 0.0066 | 0.0198 * |
| launder_lite | -4.0% | 29 / 41 | 0.1874 | 0.3748 |
| light_human_edit | +17.3% | 56 / 4 | 0.0001 | 0.0013 * |
| paraphrase_t5 | +0.2% | 88 / 86 | 0.9411 | 0.9411 |
| roundtrip_fr | +9.7% | 44 / 15 | 0.0002 | 0.0013 * |
| typo | -13.2% | 32 / 101 | 0.0001 | 0.0013 * |
| whitespace_noise | +9.5% | 72 / 22 | 0.0001 | 0.0013 * |
| zero_width | -10.7% | 23 / 79 | 0.0001 | 0.0013 * |

### binoculars_lite vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -37.8% | 4 / 202 | 0.0001 | 0.0013 * |
| clean | +5.9% | 58 / 7 | 0.0001 | 0.0013 * |
| contraction_expand | +9.7% | 53 / 2 | 0.0001 | 0.0013 * |
| esl_student | +0.3% | 24 / 23 | 1.0000 | 1.0000 |
| grammar_correct | +4.3% | 60 / 23 | 0.0002 | 0.0013 * |
| homoglyph | -21.8% | 17 / 131 | 0.0001 | 0.0013 * |
| launder_lite | -6.3% | 40 / 59 | 0.0712 | 0.3560 |
| light_human_edit | +10.3% | 34 / 3 | 0.0001 | 0.0013 * |
| paraphrase_t5 | +3.0% | 116 / 90 | 0.0801 | 0.3560 |
| roundtrip_fr | +0.0% | 24 / 24 | 1.0000 | 1.0000 |
| typo | -24.0% | 13 / 139 | 0.0001 | 0.0013 * |
| whitespace_noise | +1.9% | 41 / 31 | 0.2835 | 0.8504 |
| zero_width | -30.5% | 11 / 171 | 0.0001 | 0.0013 * |

### fast_detect_gpt vs perplexity

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +14.7% | 77 / 0 | 0.0001 | 0.0013 * |
| clean | +0.6% | 15 / 10 | 0.4172 | 1.0000 |
| contraction_expand | +1.3% | 12 / 5 | 0.1461 | 0.8765 |
| esl_student | -1.7% | 20 / 25 | 0.5407 | 1.0000 |
| grammar_correct | +0.0% | 24 / 24 | 1.0000 | 1.0000 |
| homoglyph | +31.3% | 165 / 1 | 0.0001 | 0.0013 * |
| launder_lite | -6.7% | 25 / 45 | 0.0204 | 0.1632 |
| light_human_edit | -1.0% | 6 / 9 | 0.6034 | 1.0000 |
| paraphrase_t5 | -3.0% | 64 / 90 | 0.0474 | 0.3318 |
| roundtrip_fr | -0.7% | 25 / 27 | 0.8904 | 1.0000 |
| typo | +24.2% | 136 / 9 | 0.0001 | 0.0013 * |
| whitespace_noise | +5.2% | 56 / 29 | 0.0050 | 0.0450 * |
| zero_width | +13.0% | 68 / 0 | 0.0001 | 0.0013 * |

### fast_detect_gpt vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +14.7% | 77 / 0 | 0.0001 | 0.0013 * |
| clean | +5.4% | 56 / 9 | 0.0001 | 0.0013 * |
| contraction_expand | +8.6% | 49 / 4 | 0.0001 | 0.0013 * |
| esl_student | +8.0% | 38 / 14 | 0.0020 | 0.0040 * |
| grammar_correct | +7.0% | 80 / 19 | 0.0001 | 0.0013 * |
| homoglyph | +31.9% | 167 / 0 | 0.0001 | 0.0013 * |
| launder_lite | +8.7% | 55 / 29 | 0.0063 | 0.0063 * |
| light_human_edit | +12.0% | 41 / 5 | 0.0001 | 0.0013 * |
| paraphrase_t5 | +10.9% | 144 / 50 | 0.0001 | 0.0013 * |
| roundtrip_fr | +14.7% | 53 / 9 | 0.0001 | 0.0013 * |
| typo | +30.0% | 157 / 0 | 0.0001 | 0.0013 * |
| whitespace_noise | +23.9% | 132 / 7 | 0.0001 | 0.0013 * |
| zero_width | +13.2% | 69 / 0 | 0.0001 | 0.0013 * |

### fast_detect_gpt vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -17.2% | 23 / 113 | 0.0001 | 0.0013 * |
| clean | +9.4% | 92 / 11 | 0.0001 | 0.0013 * |
| contraction_expand | +16.0% | 90 / 6 | 0.0001 | 0.0013 * |
| esl_student | +11.0% | 48 / 15 | 0.0002 | 0.0013 * |
| grammar_correct | +7.7% | 89 / 22 | 0.0001 | 0.0013 * |
| homoglyph | +7.4% | 73 / 34 | 0.0001 | 0.0013 * |
| launder_lite | -4.0% | 26 / 38 | 0.1716 | 0.5147 |
| light_human_edit | +15.0% | 51 / 6 | 0.0001 | 0.0013 * |
| paraphrase_t5 | +0.5% | 85 / 81 | 0.8118 | 1.0000 |
| roundtrip_fr | +10.3% | 48 / 17 | 0.0002 | 0.0013 * |
| typo | +1.5% | 69 / 61 | 0.5352 | 1.0000 |
| whitespace_noise | +7.8% | 68 / 27 | 0.0001 | 0.0013 * |
| zero_width | -6.1% | 33 / 65 | 0.0020 | 0.0080 * |

### fast_detect_gpt vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -24.8% | 14 / 144 | 0.0001 | 0.0013 * |
| clean | +5.1% | 57 / 13 | 0.0001 | 0.0013 * |
| contraction_expand | +8.4% | 51 / 7 | 0.0001 | 0.0013 * |
| esl_student | +0.7% | 26 / 24 | 0.8888 | 1.0000 |
| grammar_correct | +3.5% | 57 / 27 | 0.0014 | 0.0084 * |
| homoglyph | -8.2% | 29 / 72 | 0.0001 | 0.0013 * |
| launder_lite | -6.3% | 36 / 55 | 0.0595 | 0.2975 |
| light_human_edit | +8.0% | 33 / 9 | 0.0003 | 0.0021 * |
| paraphrase_t5 | +3.2% | 118 / 90 | 0.0619 | 0.2975 |
| roundtrip_fr | +0.7% | 29 / 27 | 0.8944 | 1.0000 |
| typo | -9.4% | 28 / 77 | 0.0001 | 0.0013 * |
| whitespace_noise | +0.2% | 40 / 39 | 1.0000 | 1.0000 |
| zero_width | -26.0% | 16 / 152 | 0.0001 | 0.0013 * |

### perplexity vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.0% | 0 / 0 | 1.0000 | 1.0000 |
| clean | +4.8% | 49 / 7 | 0.0001 | 0.0013 * |
| contraction_expand | +7.3% | 44 / 6 | 0.0001 | 0.0013 * |
| esl_student | +9.7% | 43 / 14 | 0.0004 | 0.0016 * |
| grammar_correct | +7.0% | 75 / 14 | 0.0001 | 0.0013 * |
| homoglyph | +0.6% | 3 / 0 | 0.2508 | 0.7523 |
| launder_lite | +15.3% | 69 / 23 | 0.0001 | 0.0013 * |
| light_human_edit | +13.0% | 42 / 3 | 0.0001 | 0.0013 * |
| paraphrase_t5 | +13.9% | 163 / 43 | 0.0001 | 0.0013 * |
| roundtrip_fr | +15.3% | 54 / 8 | 0.0001 | 0.0013 * |
| typo | +5.7% | 32 / 2 | 0.0001 | 0.0013 * |
| whitespace_noise | +18.7% | 120 / 22 | 0.0001 | 0.0013 * |
| zero_width | +0.2% | 1 / 0 | 1.0000 | 1.0000 |

### perplexity vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -31.9% | 4 / 171 | 0.0001 | 0.0013 * |
| clean | +8.8% | 86 / 10 | 0.0001 | 0.0013 * |
| contraction_expand | +14.7% | 83 / 6 | 0.0001 | 0.0013 * |
| esl_student | +12.7% | 53 / 15 | 0.0001 | 0.0013 * |
| grammar_correct | +7.7% | 89 / 22 | 0.0001 | 0.0013 * |
| homoglyph | -23.9% | 3 / 128 | 0.0001 | 0.0013 * |
| launder_lite | +2.7% | 40 / 32 | 0.4011 | 0.4011 |
| light_human_edit | +16.0% | 51 / 3 | 0.0001 | 0.0013 * |
| paraphrase_t5 | +3.5% | 83 / 53 | 0.0124 | 0.0372 * |
| roundtrip_fr | +11.0% | 48 / 15 | 0.0002 | 0.0013 * |
| typo | -22.7% | 9 / 128 | 0.0001 | 0.0013 * |
| whitespace_noise | +2.7% | 56 / 42 | 0.1889 | 0.3778 |
| zero_width | -19.1% | 1 / 101 | 0.0001 | 0.0013 * |

### perplexity vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -39.5% | 1 / 208 | 0.0001 | 0.0013 * |
| clean | +4.5% | 54 / 15 | 0.0001 | 0.0013 * |
| contraction_expand | +7.1% | 48 / 11 | 0.0001 | 0.0013 * |
| esl_student | +2.3% | 30 / 23 | 0.4074 | 1.0000 |
| grammar_correct | +3.5% | 58 / 28 | 0.0018 | 0.0090 * |
| homoglyph | -39.5% | 3 / 210 | 0.0001 | 0.0013 * |
| launder_lite | +0.3% | 45 / 44 | 1.0000 | 1.0000 |
| light_human_edit | +9.0% | 33 / 6 | 0.0001 | 0.0013 * |
| paraphrase_t5 | +6.2% | 122 / 68 | 0.0004 | 0.0024 * |
| roundtrip_fr | +1.3% | 30 / 26 | 0.6850 | 1.0000 |
| typo | -33.6% | 9 / 185 | 0.0001 | 0.0013 * |
| whitespace_noise | -5.0% | 39 / 65 | 0.0131 | 0.0524 |
| zero_width | -38.9% | 4 / 208 | 0.0001 | 0.0013 * |

### roberta_openai vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -31.9% | 4 / 171 | 0.0001 | 0.0013 * |
| clean | +3.9% | 66 / 32 | 0.0007 | 0.0035 * |
| contraction_expand | +7.4% | 64 / 25 | 0.0001 | 0.0013 * |
| esl_student | +3.0% | 37 / 28 | 0.3293 | 0.9356 |
| grammar_correct | +0.7% | 68 / 62 | 0.6690 | 0.9356 |
| homoglyph | -24.4% | 1 / 129 | 0.0001 | 0.0013 * |
| launder_lite | -12.7% | 27 / 65 | 0.0001 | 0.0013 * |
| light_human_edit | +3.0% | 36 / 27 | 0.3119 | 0.9356 |
| paraphrase_t5 | -10.4% | 60 / 150 | 0.0001 | 0.0013 * |
| roundtrip_fr | -4.3% | 28 / 41 | 0.1500 | 0.5999 |
| typo | -28.4% | 3 / 152 | 0.0001 | 0.0013 * |
| whitespace_noise | -16.0% | 29 / 113 | 0.0001 | 0.0013 * |
| zero_width | -19.3% | 1 / 102 | 0.0001 | 0.0013 * |

### roberta_openai vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -39.5% | 1 / 208 | 0.0001 | 0.0013 * |
| clean | -0.3% | 47 / 50 | 0.8410 | 1.0000 |
| contraction_expand | -0.2% | 41 / 42 | 1.0000 | 1.0000 |
| esl_student | -7.3% | 22 / 44 | 0.0093 | 0.0372 * |
| grammar_correct | -3.6% | 45 / 76 | 0.0059 | 0.0295 * |
| homoglyph | -40.1% | 2 / 212 | 0.0001 | 0.0013 * |
| launder_lite | -15.0% | 32 / 77 | 0.0002 | 0.0014 * |
| light_human_edit | -4.0% | 25 / 37 | 0.1571 | 0.4713 |
| paraphrase_t5 | -7.6% | 82 / 148 | 0.0002 | 0.0014 * |
| roundtrip_fr | -14.0% | 18 / 60 | 0.0001 | 0.0013 * |
| typo | -39.3% | 2 / 208 | 0.0001 | 0.0013 * |
| whitespace_noise | -23.7% | 21 / 145 | 0.0001 | 0.0013 * |
| zero_width | -39.1% | 3 / 208 | 0.0001 | 0.0013 * |

### stylometric_gbm vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -7.6% | 33 / 73 | 0.0002 | 0.0020 * |
| clean | -4.3% | 36 / 73 | 0.0006 | 0.0036 * |
| contraction_expand | -7.6% | 32 / 72 | 0.0002 | 0.0020 * |
| esl_student | -10.3% | 21 / 52 | 0.0004 | 0.0028 * |
| grammar_correct | -4.3% | 39 / 76 | 0.0010 | 0.0045 * |
| homoglyph | -15.6% | 25 / 107 | 0.0001 | 0.0013 * |
| launder_lite | -2.3% | 42 / 49 | 0.5317 | 0.5317 |
| light_human_edit | -7.0% | 21 / 42 | 0.0113 | 0.0339 * |
| paraphrase_t5 | +2.8% | 104 / 80 | 0.0889 | 0.1778 |
| roundtrip_fr | -9.7% | 22 / 51 | 0.0009 | 0.0045 * |
| typo | -10.9% | 30 / 87 | 0.0001 | 0.0013 * |
| whitespace_noise | -7.6% | 33 / 73 | 0.0002 | 0.0020 * |
| zero_width | -19.8% | 27 / 131 | 0.0001 | 0.0013 * |

