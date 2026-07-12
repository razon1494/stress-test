# STRESS-Test Statistics

*95% document-clustered bootstrap CIs; thresholds frozen at 1% FPR on clean human text.*

## Rates with confidence intervals

| Detector | Condition | TPR [95% CI] | FPR [95% CI] |
|---|---|---|---|
| perplexity | case_noise | 0.0% [0.0%, 0.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | clean | 93.9% [90.8%, 96.6%] | 0.8% [0.0%, 1.9%] |
| perplexity | contraction_expand | 93.9% [90.8%, 96.6%] | 0.8% [0.0%, 1.9%] |
| perplexity | homoglyph | 1.1% [0.0%, 2.7%] | 0.0% [0.0%, 0.0%] |
| perplexity | launder_lite | 46.0% [38.0%, 54.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | paraphrase_t5 | 57.3% [49.3%, 64.7%] | 0.0% [0.0%, 0.0%] |
| perplexity | roundtrip_fr | 74.0% [66.7%, 80.7%] | 1.3% [0.0%, 3.3%] |
| perplexity | typo | 12.2% [8.4%, 16.0%] | 0.0% [0.0%, 0.0%] |
| perplexity | whitespace_noise | 66.8% [61.1%, 72.5%] | 0.0% [0.0%, 0.0%] |
| perplexity | zero_width | 0.4% [0.0%, 1.1%] | 0.0% [0.0%, 0.0%] |
| tfidf_logreg | case_noise | 88.5% [84.7%, 92.0%] | 0.8% [0.0%, 1.9%] |
| tfidf_logreg | clean | 88.5% [84.7%, 92.0%] | 0.8% [0.0%, 1.9%] |
| tfidf_logreg | contraction_expand | 88.5% [84.7%, 92.0%] | 0.8% [0.0%, 1.9%] |
| tfidf_logreg | homoglyph | 88.2% [84.4%, 92.0%] | 1.5% [0.4%, 3.1%] |
| tfidf_logreg | launder_lite | 68.0% [60.7%, 75.3%] | 11.3% [6.0%, 16.7%] |
| tfidf_logreg | paraphrase_t5 | 62.7% [54.7%, 70.0%] | 10.7% [6.0%, 16.0%] |
| tfidf_logreg | roundtrip_fr | 84.0% [78.0%, 89.3%] | 2.7% [0.7%, 5.3%] |
| tfidf_logreg | typo | 87.4% [83.2%, 91.2%] | 1.1% [0.0%, 2.7%] |
| tfidf_logreg | whitespace_noise | 88.5% [84.7%, 92.0%] | 0.8% [0.0%, 1.9%] |
| tfidf_logreg | zero_width | 89.3% [85.5%, 92.7%] | 1.5% [0.4%, 3.1%] |

## Paired detector comparisons (per-example accuracy)

### perplexity vs tfidf_logreg

| Condition | Δ accuracy | only-A / only-B correct | p (perm) | p (Holm) |
|---|---|---|---|---|
| case_noise | -43.9% | 2 / 232 | 0.0001 | 0.0010 * |
| clean | +2.7% | 26 / 12 | 0.0351 | 0.1755 |
| contraction_expand | +2.7% | 26 / 12 | 0.0351 | 0.1755 |
| homoglyph | -42.7% | 6 / 230 | 0.0001 | 0.0010 * |
| launder_lite | -5.3% | 41 / 57 | 0.1243 | 0.2925 |
| paraphrase_t5 | +2.7% | 47 / 39 | 0.4535 | 0.4535 |
| roundtrip_fr | -4.3% | 21 / 34 | 0.0975 | 0.2925 |
| typo | -37.0% | 7 / 201 | 0.0001 | 0.0010 * |
| whitespace_noise | -10.5% | 22 / 77 | 0.0001 | 0.0010 * |
| zero_width | -43.7% | 5 / 234 | 0.0001 | 0.0010 * |

