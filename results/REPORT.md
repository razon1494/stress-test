# STRESS-Test Leaderboard

| Detector | Clean TPR | RS | WCP | FAR (worst) | HCI |
|---|---|---|---|---|---|
| deberta_hc3_ft | 72.1% | nan | 56.7% | 5.7% | -0.017 |
| binoculars_lite | 99.6% | nan | 49.3% | 7.8% | 0.149 |
| tfidf_logreg | 57.3% | nan | 34.7% | 2.7% | -0.017 |
| perplexity | 88.2% | nan | 30.0% | 3.0% | 0.000 |
| fast_detect_gpt | 95.0% | nan | 29.3% | 5.0% | 0.008 |
| roberta_openai | 51.9% | nan | 20.0% | 8.1% | -0.039 |
| stylometric_gbm | 24.4% | nan | 16.0% | 1.1% | 0.000 |

## Reliability Card — tfidf_logreg

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 57.3% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 34.7% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 2.7% | on `launder_lite` — the social-cost number |
| Hardness Collapse (HCI) | -0.017 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 53.3% | evasion by transforms that PRESERVE meaning |

## Reliability Card — stylometric_gbm

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 24.4% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 16.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 1.1% | on `human_edit` — the social-cost number |
| Hardness Collapse (HCI) | 0.000 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 81.7% | evasion by transforms that PRESERVE meaning |

## Reliability Card — perplexity

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 88.2% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 30.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 3.0% | on `human_edit` — the social-cost number |
| Hardness Collapse (HCI) | 0.000 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 36.3% | evasion by transforms that PRESERVE meaning |

## Reliability Card — fast_detect_gpt

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 95.0% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 29.3% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 5.0% | on `paraphrase_t5` — the social-cost number |
| Hardness Collapse (HCI) | 0.008 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 32.0% | evasion by transforms that PRESERVE meaning |

## Reliability Card — binoculars_lite

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 99.6% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 49.3% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 7.8% | on `paraphrase_t5` — the social-cost number |
| Hardness Collapse (HCI) | 0.149 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 19.2% | evasion by transforms that PRESERVE meaning |

## Reliability Card — roberta_openai

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 51.9% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 20.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 8.1% | on `paraphrase_t5` — the social-cost number |
| Hardness Collapse (HCI) | -0.039 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 65.2% | evasion by transforms that PRESERVE meaning |

## Reliability Card — deberta_hc3_ft

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 72.1% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 56.7% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 5.7% | on `human_edit` — the social-cost number |
| Hardness Collapse (HCI) | -0.017 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 29.8% | evasion by transforms that PRESERVE meaning |

## Quality-Adjusted Evasion (machine class, semsim >= 0.85)

| Detector | Condition | Raw evasion | QAES | Valid fraction | n |
|---|---|---|---|---|---|
| tfidf_logreg | esl_student | 48.0% | 48.9% | 94.0% | 150 |
| tfidf_logreg | grammar_correct | 43.5% | 43.5% | 100.0% | 262 |
| tfidf_logreg | launder_lite | 65.3% | 65.0% | 82.0% | 150 |
| tfidf_logreg | light_human_edit | 44.0% | 44.0% | 100.0% | 150 |
| tfidf_logreg | paraphrase_t5 | 71.0% | 71.3% | 95.8% | 262 |
| tfidf_logreg | roundtrip_fr | 46.0% | 46.8% | 94.0% | 150 |
| stylometric_gbm | esl_student | 83.3% | 84.4% | 94.0% | 150 |
| stylometric_gbm | grammar_correct | 73.7% | 73.7% | 100.0% | 262 |
| stylometric_gbm | launder_lite | 84.0% | 82.9% | 82.0% | 150 |
| stylometric_gbm | light_human_edit | 78.7% | 78.7% | 100.0% | 150 |
| stylometric_gbm | paraphrase_t5 | 84.7% | 85.3% | 95.8% | 262 |
| stylometric_gbm | roundtrip_fr | 84.0% | 85.1% | 94.0% | 150 |
| perplexity | esl_student | 35.3% | 34.0% | 94.0% | 150 |
| perplexity | grammar_correct | 8.8% | 8.8% | 100.0% | 262 |
| perplexity | launder_lite | 70.0% | 67.5% | 82.0% | 150 |
| perplexity | light_human_edit | 7.3% | 7.3% | 100.0% | 150 |
| perplexity | paraphrase_t5 | 61.8% | 61.8% | 95.8% | 262 |
| perplexity | roundtrip_fr | 39.3% | 38.3% | 94.0% | 150 |
| fast_detect_gpt | esl_student | 31.3% | 31.9% | 94.0% | 150 |
| fast_detect_gpt | grammar_correct | 6.5% | 6.5% | 100.0% | 262 |
| fast_detect_gpt | launder_lite | 70.7% | 69.1% | 82.0% | 150 |
| fast_detect_gpt | light_human_edit | 4.7% | 4.7% | 100.0% | 150 |
| fast_detect_gpt | paraphrase_t5 | 45.0% | 46.2% | 95.8% | 262 |
| fast_detect_gpt | roundtrip_fr | 32.7% | 33.3% | 94.0% | 150 |
| binoculars_lite | esl_student | 17.3% | 17.0% | 94.0% | 150 |
| binoculars_lite | grammar_correct | 1.1% | 1.1% | 100.0% | 262 |
| binoculars_lite | launder_lite | 50.7% | 48.8% | 82.0% | 150 |
| binoculars_lite | light_human_edit | 0.7% | 0.7% | 100.0% | 150 |
| binoculars_lite | paraphrase_t5 | 30.5% | 30.3% | 95.8% | 262 |
| binoculars_lite | roundtrip_fr | 17.3% | 17.0% | 94.0% | 150 |
| roberta_openai | esl_student | 62.0% | 63.1% | 94.0% | 150 |
| roberta_openai | grammar_correct | 52.3% | 52.3% | 100.0% | 262 |
| roberta_openai | launder_lite | 80.0% | 79.7% | 82.0% | 150 |
| roberta_openai | light_human_edit | 53.3% | 53.3% | 100.0% | 150 |
| roberta_openai | paraphrase_t5 | 72.9% | 73.3% | 95.8% | 262 |
| roberta_openai | roundtrip_fr | 68.0% | 69.5% | 94.0% | 150 |
| deberta_hc3_ft | esl_student | 32.7% | 32.6% | 94.0% | 150 |
| deberta_hc3_ft | grammar_correct | 26.7% | 26.7% | 100.0% | 262 |
| deberta_hc3_ft | launder_lite | 43.3% | 39.8% | 82.0% | 150 |
| deberta_hc3_ft | light_human_edit | 26.7% | 26.7% | 100.0% | 150 |
| deberta_hc3_ft | paraphrase_t5 | 20.6% | 20.3% | 95.8% | 262 |
| deberta_hc3_ft | roundtrip_fr | 34.0% | 32.6% | 94.0% | 150 |
