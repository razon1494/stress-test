# STRESS-Test Statistics

*95% document-clustered bootstrap CIs; thresholds frozen at 1% FPR on clean human text.*

## Rates with confidence intervals

| Detector | Condition | TPR [95% CI] | FPR [95% CI] |
|---|---|---|---|
| binoculars_lite | case_noise | 1.1% [0.0%, 2.7%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | clean | 96.2% [93.5%, 98.5%] | 0.9% [0.5%, 1.5%] |
| binoculars_lite | contraction_expand | 96.9% [94.7%, 98.9%] | 0.4% [0.0%, 1.1%] |
| binoculars_lite | esl_student | 69.3% [62.0%, 76.7%] | 1.3% [0.0%, 3.3%] |
| binoculars_lite | grammar_correct | 95.4% [92.7%, 97.7%] | 1.9% [1.1%, 2.7%] |
| binoculars_lite | homoglyph | 22.9% [17.9%, 27.9%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | human_edit | nan% [nan%, nan%] | 2.9% [1.5%, 4.4%] |
| binoculars_lite | launder_lite | 22.7% [16.0%, 29.3%] | 1.3% [0.0%, 3.3%] |
| binoculars_lite | light_human_edit | 97.3% [94.7%, 99.3%] | 0.7% [0.0%, 2.0%] |
| binoculars_lite | paraphrase_t5 | 44.7% [38.5%, 50.4%] | 3.5% [2.1%, 5.0%] |
| binoculars_lite | roundtrip_fr | 66.7% [59.3%, 74.0%] | 0.7% [0.0%, 2.0%] |
| binoculars_lite | typo | 21.0% [16.0%, 26.0%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | whitespace_noise | 73.3% [67.9%, 78.6%] | 0.0% [0.0%, 0.0%] |
| binoculars_lite | zero_width | 9.9% [6.5%, 13.7%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | case_noise | 0.4% [0.0%, 1.5%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | clean | 96.6% [94.3%, 98.5%] | 0.9% [0.5%, 1.6%] |
| deberta_hc3_ft | contraction_expand | 96.6% [94.3%, 98.5%] | 0.4% [0.0%, 1.1%] |
| deberta_hc3_ft | esl_student | 92.0% [87.3%, 96.0%] | 0.7% [0.0%, 2.0%] |
| deberta_hc3_ft | grammar_correct | 96.6% [94.3%, 98.5%] | 2.9% [1.9%, 3.9%] |
| deberta_hc3_ft | homoglyph | 19.8% [15.3%, 25.2%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | human_edit | nan% [nan%, nan%] | 3.1% [1.7%, 4.8%] |
| deberta_hc3_ft | launder_lite | 71.3% [64.0%, 78.0%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | light_human_edit | 96.7% [93.3%, 99.3%] | 0.7% [0.0%, 2.0%] |
| deberta_hc3_ft | paraphrase_t5 | 91.2% [87.8%, 94.7%] | 3.3% [2.0%, 4.8%] |
| deberta_hc3_ft | roundtrip_fr | 92.7% [88.0%, 96.7%] | 0.7% [0.0%, 2.0%] |
| deberta_hc3_ft | typo | 47.7% [42.0%, 53.4%] | 0.0% [0.0%, 0.0%] |
| deberta_hc3_ft | whitespace_noise | 96.6% [94.3%, 98.5%] | 0.4% [0.0%, 1.1%] |
| deberta_hc3_ft | zero_width | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | case_noise | 15.3% [11.1%, 19.8%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | clean | 94.7% [91.6%, 97.3%] | 0.9% [0.4%, 1.6%] |
| fast_detect_gpt | contraction_expand | 95.0% [92.4%, 97.3%] | 0.4% [0.0%, 1.1%] |
| fast_detect_gpt | esl_student | 66.0% [58.0%, 73.3%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | grammar_correct | 92.4% [88.9%, 95.4%] | 2.2% [1.4%, 3.2%] |
| fast_detect_gpt | homoglyph | 45.8% [39.7%, 52.3%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | human_edit | nan% [nan%, nan%] | 2.9% [1.5%, 4.6%] |
| fast_detect_gpt | launder_lite | 26.7% [19.3%, 34.0%] | 0.7% [0.0%, 2.0%] |
| fast_detect_gpt | light_human_edit | 94.7% [90.7%, 98.0%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | paraphrase_t5 | 48.9% [42.7%, 55.0%] | 3.5% [2.0%, 5.0%] |
| fast_detect_gpt | roundtrip_fr | 64.7% [57.3%, 72.0%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | typo | 39.3% [33.6%, 45.8%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | whitespace_noise | 64.1% [58.4%, 70.2%] | 0.0% [0.0%, 0.0%] |
| fast_detect_gpt | zero_width | 13.4% [9.5%, 17.6%] | 0.0% [0.0%, 0.0%] |
| perplexity | case_noise | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | clean | 95.0% [92.0%, 97.3%] | 0.9% [0.4%, 1.6%] |
| perplexity | contraction_expand | 95.0% [92.0%, 97.3%] | 1.5% [0.4%, 3.1%] |
| perplexity | esl_student | 83.3% [77.3%, 89.3%] | 2.7% [0.7%, 5.3%] |
| perplexity | grammar_correct | 96.2% [93.9%, 98.5%] | 4.6% [3.4%, 5.8%] |
| perplexity | homoglyph | 2.3% [0.8%, 4.2%] | 0.0% [0.0%, 0.0%] |
| perplexity | human_edit | nan% [nan%, nan%] | 2.9% [1.5%, 4.4%] |
| perplexity | launder_lite | 54.0% [46.0%, 61.3%] | 0.0% [0.0%, 0.0%] |
| perplexity | light_human_edit | 97.3% [94.7%, 99.3%] | 2.0% [0.0%, 4.7%] |
| perplexity | paraphrase_t5 | 66.0% [60.3%, 71.4%] | 2.3% [1.2%, 3.5%] |
| perplexity | roundtrip_fr | 80.0% [73.3%, 86.0%] | 2.0% [0.0%, 4.7%] |
| perplexity | typo | 16.8% [12.2%, 21.4%] | 0.0% [0.0%, 0.0%] |
| perplexity | whitespace_noise | 74.0% [68.7%, 79.4%] | 0.4% [0.0%, 1.1%] |
| perplexity | zero_width | 0.4% [0.0%, 1.1%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | case_noise | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | clean | 85.1% [80.9%, 88.9%] | 0.9% [0.4%, 1.5%] |
| roberta_openai | contraction_expand | 85.1% [80.9%, 88.9%] | 0.4% [0.0%, 1.1%] |
| roberta_openai | esl_student | 69.3% [61.3%, 76.7%] | 6.7% [2.7%, 10.7%] |
| roberta_openai | grammar_correct | 77.5% [72.1%, 82.4%] | 6.9% [5.4%, 8.3%] |
| roberta_openai | homoglyph | 0.4% [0.0%, 1.1%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | human_edit | nan% [nan%, nan%] | 6.3% [4.2%, 8.6%] |
| roberta_openai | launder_lite | 40.0% [32.7%, 48.0%] | 20.0% [14.0%, 26.7%] |
| roberta_openai | light_human_edit | 74.7% [67.3%, 82.0%] | 2.7% [0.7%, 5.3%] |
| roberta_openai | paraphrase_t5 | 50.8% [45.0%, 56.9%] | 18.1% [15.1%, 21.3%] |
| roberta_openai | roundtrip_fr | 52.7% [44.6%, 60.7%] | 3.3% [0.7%, 6.7%] |
| roberta_openai | typo | 0.8% [0.0%, 1.9%] | 0.0% [0.0%, 0.0%] |
| roberta_openai | whitespace_noise | 38.5% [32.8%, 44.3%] | 0.4% [0.0%, 1.1%] |
| roberta_openai | zero_width | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| stylometric_gbm | case_noise | 59.2% [52.7%, 64.9%] | 1.1% [0.0%, 2.7%] |
| stylometric_gbm | clean | 59.2% [52.7%, 64.9%] | 0.9% [0.4%, 1.6%] |
| stylometric_gbm | contraction_expand | 59.2% [52.7%, 64.9%] | 1.1% [0.0%, 2.7%] |
| stylometric_gbm | esl_student | 48.7% [40.7%, 56.7%] | 3.3% [0.7%, 6.0%] |
| stylometric_gbm | grammar_correct | 59.2% [53.1%, 65.3%] | 0.9% [0.4%, 1.5%] |
| stylometric_gbm | homoglyph | 40.5% [34.4%, 46.6%] | 0.4% [0.0%, 1.1%] |
| stylometric_gbm | human_edit | nan% [nan%, nan%] | 1.5% [0.4%, 2.5%] |
| stylometric_gbm | launder_lite | 42.7% [34.7%, 50.7%] | 3.3% [0.7%, 6.0%] |
| stylometric_gbm | light_human_edit | 60.0% [52.0%, 68.0%] | 1.3% [0.0%, 3.3%] |
| stylometric_gbm | paraphrase_t5 | 42.7% [37.0%, 48.5%] | 1.7% [0.8%, 2.8%] |
| stylometric_gbm | roundtrip_fr | 48.7% [40.7%, 56.7%] | 2.7% [0.7%, 5.3%] |
| stylometric_gbm | typo | 50.0% [43.9%, 56.1%] | 0.8% [0.0%, 1.9%] |
| stylometric_gbm | whitespace_noise | 58.8% [52.3%, 64.5%] | 1.1% [0.0%, 2.7%] |
| stylometric_gbm | zero_width | 29.8% [24.4%, 35.5%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | case_noise | 64.9% [59.5%, 70.6%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | clean | 64.9% [59.5%, 70.6%] | 0.9% [0.4%, 1.5%] |
| tfidf_logreg | contraction_expand | 65.3% [59.5%, 70.6%] | 0.4% [0.0%, 1.1%] |
| tfidf_logreg | esl_student | 62.0% [54.6%, 70.0%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | grammar_correct | 63.7% [58.0%, 69.1%] | 1.2% [0.6%, 1.9%] |
| tfidf_logreg | homoglyph | 67.2% [61.8%, 72.5%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | human_edit | nan% [nan%, nan%] | 1.9% [0.8%, 3.1%] |
| tfidf_logreg | launder_lite | 42.7% [34.7%, 50.7%] | 4.0% [1.3%, 7.3%] |
| tfidf_logreg | light_human_edit | 63.3% [55.3%, 71.3%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | paraphrase_t5 | 37.0% [30.9%, 42.7%] | 3.8% [2.3%, 5.5%] |
| tfidf_logreg | roundtrip_fr | 63.3% [55.3%, 71.3%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | typo | 64.5% [58.8%, 69.8%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | whitespace_noise | 64.9% [59.5%, 70.6%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | zero_width | 64.1% [58.8%, 69.8%] | 0.0% [0.0%, 0.0%] |

## Paired detector comparisons (per-example accuracy)

### binoculars_lite vs deberta_hc3_ft

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.4% | 3 / 1 | 0.6236 | 1.0000 |
| clean | -0.1% | 14 / 15 | 1.0000 | 1.0000 |
| contraction_expand | +0.2% | 8 / 7 | 1.0000 | 1.0000 |
| esl_student | -11.7% | 6 / 41 | 0.0001 | 0.0014 * |
| grammar_correct | +0.6% | 32 / 24 | 0.3533 | 1.0000 |
| homoglyph | +1.5% | 43 / 35 | 0.4189 | 1.0000 |
| human_edit | +0.2% | 15 / 14 | 1.0000 | 1.0000 |
| launder_lite | -25.0% | 5 / 80 | 0.0001 | 0.0014 * |
| light_human_edit | +0.3% | 6 / 5 | 1.0000 | 1.0000 |
| paraphrase_t5 | -14.2% | 25 / 148 | 0.0001 | 0.0014 * |
| roundtrip_fr | -13.0% | 5 / 44 | 0.0001 | 0.0014 * |
| typo | -13.4% | 27 / 97 | 0.0001 | 0.0014 * |
| whitespace_noise | -11.5% | 7 / 67 | 0.0001 | 0.0014 * |
| zero_width | +5.0% | 26 / 0 | 0.0001 | 0.0014 * |

### binoculars_lite vs fast_detect_gpt

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -7.1% | 1 / 38 | 0.0001 | 0.0014 * |
| clean | +0.3% | 16 / 12 | 0.5717 | 1.0000 |
| contraction_expand | +1.0% | 10 / 5 | 0.3066 | 1.0000 |
| esl_student | +1.0% | 24 / 21 | 0.7763 | 1.0000 |
| grammar_correct | +0.9% | 34 / 22 | 0.1401 | 1.0000 |
| homoglyph | -11.5% | 27 / 87 | 0.0001 | 0.0014 * |
| human_edit | +0.0% | 10 / 10 | 1.0000 | 1.0000 |
| launder_lite | -2.3% | 17 / 24 | 0.3450 | 1.0000 |
| light_human_edit | +1.0% | 6 / 3 | 0.5131 | 1.0000 |
| paraphrase_t5 | -1.3% | 59 / 70 | 0.3870 | 1.0000 |
| roundtrip_fr | +0.7% | 20 / 18 | 0.8689 | 1.0000 |
| typo | -9.2% | 26 / 74 | 0.0001 | 0.0014 * |
| whitespace_noise | +4.6% | 53 / 29 | 0.0115 | 0.1265 |
| zero_width | -1.7% | 17 / 26 | 0.2199 | 1.0000 |

### binoculars_lite vs perplexity

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.6% | 3 / 0 | 0.2469 | 1.0000 |
| clean | +0.2% | 16 / 13 | 0.7035 | 1.0000 |
| contraction_expand | +1.5% | 13 / 5 | 0.0972 | 0.6803 |
| esl_student | -6.3% | 11 / 30 | 0.0048 | 0.0432 * |
| grammar_correct | +2.1% | 42 / 14 | 0.0005 | 0.0050 * |
| homoglyph | +10.3% | 56 / 2 | 0.0001 | 0.0014 * |
| human_edit | +0.0% | 11 / 11 | 1.0000 | 1.0000 |
| launder_lite | -16.3% | 7 / 56 | 0.0001 | 0.0014 * |
| light_human_edit | +0.7% | 7 / 5 | 0.7839 | 1.0000 |
| paraphrase_t5 | -7.3% | 18 / 81 | 0.0001 | 0.0014 * |
| roundtrip_fr | -6.0% | 12 / 30 | 0.0076 | 0.0608 |
| typo | +2.1% | 29 / 18 | 0.1413 | 0.8477 |
| whitespace_noise | -0.2% | 33 / 34 | 1.0000 | 1.0000 |
| zero_width | +4.8% | 25 / 0 | 0.0001 | 0.0014 * |

### binoculars_lite vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.6% | 3 / 0 | 0.2469 | 0.7406 |
| clean | +2.2% | 41 / 12 | 0.0002 | 0.0014 * |
| contraction_expand | +5.9% | 35 / 4 | 0.0001 | 0.0014 * |
| esl_student | +2.7% | 31 / 23 | 0.3526 | 0.7406 |
| grammar_correct | +7.5% | 115 / 14 | 0.0001 | 0.0014 * |
| homoglyph | +11.3% | 59 / 0 | 0.0001 | 0.0014 * |
| human_edit | +3.4% | 24 / 8 | 0.0064 | 0.0256 * |
| launder_lite | +0.7% | 45 / 43 | 0.9140 | 0.9140 |
| light_human_edit | +12.3% | 39 / 2 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +8.3% | 144 / 72 | 0.0001 | 0.0014 * |
| roundtrip_fr | +8.3% | 39 / 14 | 0.0014 | 0.0070 * |
| typo | +10.1% | 53 / 0 | 0.0001 | 0.0014 * |
| whitespace_noise | +17.6% | 109 / 17 | 0.0001 | 0.0014 * |
| zero_width | +5.0% | 26 / 0 | 0.0001 | 0.0014 * |

### binoculars_lite vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -28.4% | 5 / 154 | 0.0001 | 0.0014 * |
| clean | +7.2% | 113 / 16 | 0.0001 | 0.0014 * |
| contraction_expand | +19.3% | 107 / 6 | 0.0001 | 0.0014 * |
| esl_student | +11.3% | 50 / 16 | 0.0001 | 0.0014 * |
| grammar_correct | +6.3% | 113 / 28 | 0.0001 | 0.0014 * |
| homoglyph | -8.6% | 33 / 78 | 0.0002 | 0.0014 * |
| human_edit | -1.5% | 7 / 14 | 0.1933 | 0.3866 |
| launder_lite | -9.0% | 16 / 43 | 0.0014 | 0.0042 * |
| light_human_edit | +19.0% | 61 / 4 | 0.0001 | 0.0014 * |
| paraphrase_t5 | -0.7% | 72 / 78 | 0.6836 | 0.6836 |
| roundtrip_fr | +10.0% | 44 / 14 | 0.0002 | 0.0014 * |
| typo | -14.1% | 27 / 101 | 0.0001 | 0.0014 * |
| whitespace_noise | +7.8% | 78 / 37 | 0.0004 | 0.0016 * |
| zero_width | -9.9% | 12 / 64 | 0.0001 | 0.0014 * |

### binoculars_lite vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -31.9% | 2 / 169 | 0.0001 | 0.0014 * |
| clean | +6.1% | 96 / 14 | 0.0001 | 0.0014 * |
| contraction_expand | +15.8% | 87 / 4 | 0.0001 | 0.0014 * |
| esl_student | +3.0% | 35 / 26 | 0.2995 | 0.8984 |
| grammar_correct | +5.7% | 101 / 25 | 0.0001 | 0.0014 * |
| homoglyph | -22.1% | 17 / 133 | 0.0001 | 0.0014 * |
| human_edit | -1.0% | 9 / 14 | 0.4059 | 0.8984 |
| launder_lite | -8.7% | 27 / 53 | 0.0054 | 0.0324 * |
| light_human_edit | +16.7% | 53 / 3 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +2.5% | 99 / 77 | 0.1189 | 0.4756 |
| roundtrip_fr | +1.3% | 34 / 30 | 0.7029 | 0.8984 |
| typo | -21.8% | 16 / 130 | 0.0001 | 0.0014 * |
| whitespace_noise | +4.2% | 61 / 39 | 0.0350 | 0.1750 |
| zero_width | -27.1% | 10 / 152 | 0.0001 | 0.0014 * |

### deberta_hc3_ft vs fast_detect_gpt

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -7.4% | 0 / 39 | 0.0001 | 0.0014 * |
| clean | +0.4% | 19 / 14 | 0.4892 | 1.0000 |
| contraction_expand | +0.8% | 12 / 8 | 0.4979 | 1.0000 |
| esl_student | +12.7% | 44 / 6 | 0.0001 | 0.0014 * |
| grammar_correct | +0.3% | 36 / 32 | 0.7124 | 1.0000 |
| homoglyph | -13.0% | 21 / 89 | 0.0001 | 0.0014 * |
| human_edit | -0.2% | 12 / 13 | 1.0000 | 1.0000 |
| launder_lite | +22.7% | 76 / 8 | 0.0001 | 0.0014 * |
| light_human_edit | +0.7% | 7 / 5 | 0.7735 | 1.0000 |
| paraphrase_t5 | +12.9% | 132 / 20 | 0.0001 | 0.0014 * |
| roundtrip_fr | +13.7% | 45 / 4 | 0.0001 | 0.0014 * |
| typo | +4.2% | 69 / 47 | 0.0530 | 0.3180 |
| whitespace_noise | +16.0% | 86 / 2 | 0.0001 | 0.0014 * |
| zero_width | -6.7% | 0 / 35 | 0.0001 | 0.0014 * |

### deberta_hc3_ft vs perplexity

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.2% | 1 / 0 | 1.0000 | 1.0000 |
| clean | +0.3% | 15 / 11 | 0.5687 | 1.0000 |
| contraction_expand | +1.3% | 13 / 6 | 0.1677 | 1.0000 |
| esl_student | +5.3% | 24 / 8 | 0.0075 | 0.0600 |
| grammar_correct | +1.5% | 44 / 24 | 0.0212 | 0.1484 |
| homoglyph | +8.8% | 49 / 3 | 0.0001 | 0.0014 * |
| human_edit | -0.2% | 11 / 12 | 1.0000 | 1.0000 |
| launder_lite | +8.7% | 32 / 6 | 0.0001 | 0.0014 * |
| light_human_edit | +0.3% | 5 / 4 | 1.0000 | 1.0000 |
| paraphrase_t5 | +6.9% | 85 / 25 | 0.0001 | 0.0014 * |
| roundtrip_fr | +7.0% | 27 / 6 | 0.0006 | 0.0054 * |
| typo | +15.5% | 108 / 27 | 0.0001 | 0.0014 * |
| whitespace_noise | +11.3% | 63 / 4 | 0.0001 | 0.0014 * |
| zero_width | -0.2% | 0 / 1 | 1.0000 | 1.0000 |

### deberta_hc3_ft vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.2% | 1 / 0 | 1.0000 | 1.0000 |
| clean | +2.2% | 41 / 11 | 0.0003 | 0.0014 * |
| contraction_expand | +5.7% | 35 / 5 | 0.0001 | 0.0014 * |
| esl_student | +14.3% | 50 / 7 | 0.0001 | 0.0014 * |
| grammar_correct | +6.9% | 119 / 26 | 0.0001 | 0.0014 * |
| homoglyph | +9.7% | 52 / 1 | 0.0001 | 0.0014 * |
| human_edit | +3.1% | 27 / 12 | 0.0236 | 0.0708 |
| launder_lite | +25.7% | 92 / 15 | 0.0001 | 0.0014 * |
| light_human_edit | +12.0% | 41 / 5 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +22.5% | 209 / 14 | 0.0001 | 0.0014 * |
| roundtrip_fr | +21.3% | 67 / 3 | 0.0001 | 0.0014 * |
| typo | +23.5% | 125 / 2 | 0.0001 | 0.0014 * |
| whitespace_noise | +29.0% | 154 / 2 | 0.0001 | 0.0014 * |
| zero_width | +0.0% | 0 / 0 | 1.0000 | 1.0000 |

### deberta_hc3_ft vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -28.8% | 4 / 155 | 0.0001 | 0.0014 * |
| clean | +7.3% | 108 / 10 | 0.0001 | 0.0014 * |
| contraction_expand | +19.1% | 103 / 3 | 0.0001 | 0.0014 * |
| esl_student | +23.0% | 73 / 4 | 0.0001 | 0.0014 * |
| grammar_correct | +5.7% | 106 / 29 | 0.0001 | 0.0014 * |
| homoglyph | -10.1% | 30 / 83 | 0.0001 | 0.0014 * |
| human_edit | -1.7% | 7 / 15 | 0.1319 | 0.2638 |
| launder_lite | +16.0% | 56 / 8 | 0.0001 | 0.0014 * |
| light_human_edit | +18.7% | 57 / 1 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +13.5% | 135 / 18 | 0.0001 | 0.0014 * |
| roundtrip_fr | +23.0% | 74 / 5 | 0.0001 | 0.0014 * |
| typo | -0.8% | 66 / 70 | 0.7957 | 0.7957 |
| whitespace_noise | +19.3% | 103 / 2 | 0.0001 | 0.0014 * |
| zero_width | -14.9% | 0 / 78 | 0.0001 | 0.0014 * |

### deberta_hc3_ft vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -32.3% | 0 / 169 | 0.0001 | 0.0014 * |
| clean | +6.2% | 97 / 14 | 0.0001 | 0.0014 * |
| contraction_expand | +15.6% | 87 / 5 | 0.0001 | 0.0014 * |
| esl_student | +14.7% | 49 / 5 | 0.0001 | 0.0014 * |
| grammar_correct | +5.1% | 103 / 35 | 0.0001 | 0.0014 * |
| homoglyph | -23.7% | 15 / 139 | 0.0001 | 0.0014 * |
| human_edit | -1.3% | 8 / 14 | 0.2883 | 0.2883 |
| launder_lite | +16.3% | 57 / 8 | 0.0001 | 0.0014 * |
| light_human_edit | +16.3% | 51 / 2 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +16.7% | 166 / 21 | 0.0001 | 0.0014 * |
| roundtrip_fr | +14.3% | 48 / 5 | 0.0001 | 0.0014 * |
| typo | -8.4% | 41 / 85 | 0.0001 | 0.0014 * |
| whitespace_noise | +15.6% | 87 / 5 | 0.0001 | 0.0014 * |
| zero_width | -32.1% | 0 / 168 | 0.0001 | 0.0014 * |

### fast_detect_gpt vs perplexity

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +7.6% | 40 / 0 | 0.0001 | 0.0014 * |
| clean | -0.1% | 16 / 17 | 1.0000 | 1.0000 |
| contraction_expand | +0.6% | 12 / 9 | 0.6597 | 1.0000 |
| esl_student | -7.3% | 18 / 40 | 0.0047 | 0.0376 * |
| grammar_correct | +1.2% | 44 / 28 | 0.0789 | 0.3945 |
| homoglyph | +21.8% | 118 / 4 | 0.0001 | 0.0014 * |
| human_edit | +0.0% | 9 / 9 | 1.0000 | 1.0000 |
| launder_lite | -14.0% | 17 / 59 | 0.0001 | 0.0014 * |
| light_human_edit | -0.3% | 6 / 7 | 1.0000 | 1.0000 |
| paraphrase_t5 | -6.0% | 45 / 97 | 0.0002 | 0.0018 * |
| roundtrip_fr | -6.7% | 15 / 35 | 0.0055 | 0.0385 * |
| typo | +11.3% | 82 / 23 | 0.0001 | 0.0014 * |
| whitespace_noise | -4.8% | 36 / 61 | 0.0159 | 0.0954 |
| zero_width | +6.5% | 34 / 0 | 0.0001 | 0.0014 * |

### fast_detect_gpt vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +7.6% | 40 / 0 | 0.0001 | 0.0014 * |
| clean | +1.9% | 40 / 15 | 0.0014 | 0.0070 * |
| contraction_expand | +5.0% | 31 / 5 | 0.0001 | 0.0014 * |
| esl_student | +1.7% | 32 / 27 | 0.6051 | 0.7905 |
| grammar_correct | +6.6% | 111 / 22 | 0.0001 | 0.0014 * |
| homoglyph | +22.7% | 120 / 1 | 0.0001 | 0.0014 * |
| human_edit | +3.4% | 24 / 8 | 0.0051 | 0.0153 * |
| launder_lite | +3.0% | 49 / 40 | 0.3953 | 0.7905 |
| light_human_edit | +11.3% | 35 / 1 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +9.6% | 140 / 57 | 0.0001 | 0.0014 * |
| roundtrip_fr | +7.7% | 39 / 16 | 0.0028 | 0.0112 * |
| typo | +19.3% | 102 / 1 | 0.0001 | 0.0014 * |
| whitespace_noise | +13.0% | 88 / 20 | 0.0001 | 0.0014 * |
| zero_width | +6.7% | 35 / 0 | 0.0001 | 0.0014 * |

### fast_detect_gpt vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -21.4% | 16 / 128 | 0.0001 | 0.0014 * |
| clean | +6.9% | 108 / 15 | 0.0001 | 0.0014 * |
| contraction_expand | +18.3% | 103 / 7 | 0.0001 | 0.0014 * |
| esl_student | +10.3% | 50 / 19 | 0.0004 | 0.0032 * |
| grammar_correct | +5.4% | 105 / 32 | 0.0001 | 0.0014 * |
| homoglyph | +2.9% | 57 / 42 | 0.1587 | 0.5315 |
| human_edit | -1.5% | 6 / 13 | 0.1689 | 0.5315 |
| launder_lite | -6.7% | 19 / 39 | 0.0116 | 0.0696 |
| light_human_edit | +18.0% | 56 / 2 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +0.6% | 73 / 68 | 0.7414 | 0.7414 |
| roundtrip_fr | +9.3% | 48 / 20 | 0.0009 | 0.0063 * |
| typo | -5.0% | 51 / 77 | 0.0303 | 0.1515 |
| whitespace_noise | +3.2% | 64 / 47 | 0.1329 | 0.5315 |
| zero_width | -8.2% | 17 / 60 | 0.0001 | 0.0014 * |

### fast_detect_gpt vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -24.8% | 10 / 140 | 0.0001 | 0.0014 * |
| clean | +5.8% | 96 / 18 | 0.0001 | 0.0014 * |
| contraction_expand | +14.9% | 86 / 8 | 0.0001 | 0.0014 * |
| esl_student | +2.0% | 37 / 31 | 0.5452 | 1.0000 |
| grammar_correct | +4.8% | 102 / 38 | 0.0001 | 0.0014 * |
| homoglyph | -10.7% | 36 / 92 | 0.0001 | 0.0014 * |
| human_edit | -1.0% | 9 / 14 | 0.4097 | 1.0000 |
| launder_lite | -6.3% | 27 / 46 | 0.0318 | 0.1590 |
| light_human_edit | +15.7% | 52 / 5 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +3.8% | 104 / 71 | 0.0157 | 0.0942 |
| roundtrip_fr | +0.7% | 35 / 33 | 0.9040 | 1.0000 |
| typo | -12.6% | 30 / 96 | 0.0001 | 0.0014 * |
| whitespace_noise | -0.4% | 60 / 62 | 0.9307 | 1.0000 |
| zero_width | -25.4% | 11 / 144 | 0.0001 | 0.0014 * |

### perplexity vs roberta_openai

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | +0.0% | 0 / 0 | 1.0000 | 1.0000 |
| clean | +1.9% | 36 / 10 | 0.0001 | 0.0014 * |
| contraction_expand | +4.4% | 30 / 7 | 0.0001 | 0.0014 * |
| esl_student | +9.0% | 43 / 16 | 0.0007 | 0.0035 * |
| grammar_correct | +5.4% | 105 / 32 | 0.0001 | 0.0014 * |
| homoglyph | +1.0% | 5 / 0 | 0.0608 | 0.1824 |
| human_edit | +3.4% | 26 / 10 | 0.0100 | 0.0400 * |
| launder_lite | +17.0% | 73 / 22 | 0.0001 | 0.0014 * |
| light_human_edit | +11.7% | 39 / 4 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +15.6% | 175 / 40 | 0.0001 | 0.0014 * |
| roundtrip_fr | +14.3% | 50 / 7 | 0.0001 | 0.0014 * |
| typo | +8.0% | 44 / 2 | 0.0001 | 0.0014 * |
| whitespace_noise | +17.7% | 114 / 21 | 0.0001 | 0.0014 * |
| zero_width | +0.2% | 1 / 0 | 1.0000 | 1.0000 |

### perplexity vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -29.0% | 3 / 155 | 0.0001 | 0.0014 * |
| clean | +7.0% | 106 / 12 | 0.0001 | 0.0014 * |
| contraction_expand | +17.7% | 99 / 6 | 0.0001 | 0.0014 * |
| esl_student | +17.7% | 66 / 13 | 0.0001 | 0.0014 * |
| grammar_correct | +4.2% | 108 / 51 | 0.0001 | 0.0014 * |
| homoglyph | -18.9% | 5 / 104 | 0.0001 | 0.0014 * |
| human_edit | -1.5% | 5 / 12 | 0.1393 | 0.1393 |
| launder_lite | +7.3% | 42 / 20 | 0.0070 | 0.0140 * |
| light_human_edit | +18.3% | 58 / 3 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +6.6% | 101 / 44 | 0.0001 | 0.0014 * |
| roundtrip_fr | +16.0% | 60 / 12 | 0.0001 | 0.0014 * |
| typo | -16.2% | 21 / 106 | 0.0001 | 0.0014 * |
| whitespace_noise | +8.0% | 73 / 31 | 0.0001 | 0.0014 * |
| zero_width | -14.7% | 0 / 77 | 0.0001 | 0.0014 * |

### perplexity vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -32.4% | 0 / 170 | 0.0001 | 0.0014 * |
| clean | +5.9% | 94 / 15 | 0.0001 | 0.0014 * |
| contraction_expand | +14.3% | 84 / 9 | 0.0001 | 0.0014 * |
| esl_student | +9.3% | 46 / 18 | 0.0009 | 0.0045 * |
| grammar_correct | +3.6% | 104 / 56 | 0.0004 | 0.0024 * |
| homoglyph | -32.4% | 4 / 174 | 0.0001 | 0.0014 * |
| human_edit | -1.0% | 9 / 14 | 0.4036 | 0.4036 |
| launder_lite | +7.7% | 51 / 28 | 0.0138 | 0.0414 * |
| light_human_edit | +16.0% | 53 / 5 | 0.0001 | 0.0014 * |
| paraphrase_t5 | +9.8% | 133 / 48 | 0.0001 | 0.0014 * |
| roundtrip_fr | +7.3% | 43 / 21 | 0.0084 | 0.0336 * |
| typo | -23.9% | 15 / 140 | 0.0001 | 0.0014 * |
| whitespace_noise | +4.4% | 70 / 47 | 0.0419 | 0.0838 |
| zero_width | -31.9% | 1 / 168 | 0.0001 | 0.0014 * |

### roberta_openai vs stylometric_gbm

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -29.0% | 3 / 155 | 0.0001 | 0.0014 * |
| clean | +5.1% | 93 / 25 | 0.0001 | 0.0014 * |
| contraction_expand | +13.4% | 86 / 16 | 0.0001 | 0.0014 * |
| esl_student | +8.7% | 49 / 23 | 0.0032 | 0.0160 * |
| grammar_correct | -1.2% | 87 / 103 | 0.2780 | 0.5559 |
| homoglyph | -19.8% | 1 / 105 | 0.0001 | 0.0014 * |
| human_edit | -4.8% | 6 / 29 | 0.0002 | 0.0014 * |
| launder_lite | -9.7% | 33 / 62 | 0.0052 | 0.0208 * |
| light_human_edit | +6.7% | 43 / 23 | 0.0209 | 0.0627 |
| paraphrase_t5 | -9.0% | 69 / 147 | 0.0001 | 0.0014 * |
| roundtrip_fr | +1.7% | 41 / 36 | 0.6555 | 0.6555 |
| typo | -24.2% | 4 / 131 | 0.0001 | 0.0014 * |
| whitespace_noise | -9.7% | 41 / 92 | 0.0001 | 0.0014 * |
| zero_width | -14.9% | 0 / 78 | 0.0001 | 0.0014 * |

### roberta_openai vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -32.4% | 0 / 170 | 0.0001 | 0.0014 * |
| clean | +3.9% | 88 / 35 | 0.0001 | 0.0014 * |
| contraction_expand | +9.9% | 78 / 26 | 0.0001 | 0.0014 * |
| esl_student | +0.3% | 38 / 37 | 1.0000 | 1.0000 |
| grammar_correct | -1.9% | 81 / 106 | 0.0769 | 0.2307 |
| homoglyph | -33.4% | 1 / 176 | 0.0001 | 0.0014 * |
| human_edit | -4.4% | 8 / 29 | 0.0008 | 0.0056 * |
| launder_lite | -9.3% | 40 / 68 | 0.0078 | 0.0390 * |
| light_human_edit | +4.3% | 39 / 26 | 0.1297 | 0.2594 |
| paraphrase_t5 | -5.8% | 93 / 143 | 0.0017 | 0.0102 * |
| roundtrip_fr | -7.0% | 33 / 54 | 0.0326 | 0.1304 |
| typo | -31.9% | 0 / 167 | 0.0001 | 0.0014 * |
| whitespace_noise | -13.4% | 44 / 114 | 0.0001 | 0.0014 * |
| zero_width | -32.1% | 0 / 168 | 0.0001 | 0.0014 * |

### stylometric_gbm vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -3.4% | 55 / 73 | 0.1336 | 0.9351 |
| clean | -1.1% | 64 / 79 | 0.2490 | 1.0000 |
| contraction_expand | -3.4% | 56 / 74 | 0.1369 | 0.9351 |
| esl_student | -8.3% | 31 / 56 | 0.0090 | 0.0900 |
| grammar_correct | -0.7% | 69 / 78 | 0.5142 | 1.0000 |
| homoglyph | -13.5% | 37 / 108 | 0.0001 | 0.0014 * |
| human_edit | +0.4% | 9 / 7 | 0.8028 | 1.0000 |
| launder_lite | +0.3% | 43 / 42 | 1.0000 | 1.0000 |
| light_human_edit | -2.3% | 35 / 42 | 0.4925 | 1.0000 |
| paraphrase_t5 | +3.2% | 100 / 72 | 0.0397 | 0.3573 |
| roundtrip_fr | -8.7% | 29 / 55 | 0.0060 | 0.0660 |
| typo | -7.6% | 49 / 89 | 0.0005 | 0.0060 * |
| whitespace_noise | -3.6% | 55 / 74 | 0.1126 | 0.9007 |
| zero_width | -17.2% | 28 / 118 | 0.0001 | 0.0014 * |

