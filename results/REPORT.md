# STRESS-Test Leaderboard

| Detector | Clean TPR | RS | WCP | FAR (worst) | HCI |
|---|---|---|---|---|---|
| tfidf_logreg | 79.4% | 0.942 | 58.0% | 9.3% | -0.056 |
| stylometric_gbm | 65.3% | 0.875 | 49.3% | 5.3% | -0.044 |
| perplexity | 94.3% | 0.562 | 49.3% | 3.2% | 0.008 |
| fast_detect_gpt | 96.6% | 0.693 | 38.7% | 8.5% | 0.025 |
| binoculars_lite | 98.9% | 0.603 | 38.0% | 5.3% | 0.060 |
| roberta_openai | 78.6% | 0.472 | 34.7% | 16.0% | -0.105 |

## Reliability Card — tfidf_logreg

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 79.4% | headline number everyone else reports |
| Robustness Score (RS) | 0.942 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.888 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 58.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 9.3% | on `launder_lite` — the social-cost number |
| Hardness Collapse (HCI) | -0.056 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 30.6% | evasion by transforms that PRESERVE meaning |

## Reliability Card — stylometric_gbm

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 65.3% | headline number everyone else reports |
| Robustness Score (RS) | 0.875 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.856 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 49.3% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 5.3% | on `launder_lite` — the social-cost number |
| Hardness Collapse (HCI) | -0.044 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 42.9% | evasion by transforms that PRESERVE meaning |

## Reliability Card — perplexity

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 94.3% | headline number everyone else reports |
| Robustness Score (RS) | 0.562 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.293 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 49.3% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 3.2% | on `grammar_correct` — the social-cost number |
| Hardness Collapse (HCI) | 0.008 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 23.0% | evasion by transforms that PRESERVE meaning |

## Reliability Card — fast_detect_gpt

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 96.6% | headline number everyone else reports |
| Robustness Score (RS) | 0.693 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.646 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 38.7% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 8.5% | on `paraphrase_t5` — the social-cost number |
| Hardness Collapse (HCI) | 0.025 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 25.3% | evasion by transforms that PRESERVE meaning |

## Reliability Card — binoculars_lite

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 98.9% | headline number everyone else reports |
| Robustness Score (RS) | 0.603 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.461 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 38.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 5.3% | on `paraphrase_t5` — the social-cost number |
| Hardness Collapse (HCI) | 0.060 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 25.8% | evasion by transforms that PRESERVE meaning |

## Reliability Card — roberta_openai

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 78.6% | headline number everyone else reports |
| Robustness Score (RS) | 0.472 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.204 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 34.7% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 1.0% | FPR on clean human text |
| False-Accusation Rate, worst | 16.0% | on `launder_lite` — the social-cost number |
| Hardness Collapse (HCI) | -0.105 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 45.1% | evasion by transforms that PRESERVE meaning |

## Quality-Adjusted Evasion (machine class, semsim >= 0.85)

| Detector | Condition | Raw evasion | QAES | Valid fraction | n |
|---|---|---|---|---|---|
| tfidf_logreg | esl_student | 24.7% | 25.5% | 94.0% | 150 |
| tfidf_logreg | grammar_correct | 22.1% | 22.1% | 100.0% | 262 |
| tfidf_logreg | launder_lite | 42.0% | 41.5% | 82.0% | 150 |
| tfidf_logreg | light_human_edit | 22.7% | 22.7% | 100.0% | 150 |
| tfidf_logreg | paraphrase_t5 | 45.0% | 45.4% | 95.8% | 262 |
| tfidf_logreg | roundtrip_fr | 25.3% | 26.2% | 94.0% | 150 |
| stylometric_gbm | esl_student | 43.3% | 43.3% | 94.0% | 150 |
| stylometric_gbm | grammar_correct | 35.9% | 35.9% | 100.0% | 262 |
| stylometric_gbm | launder_lite | 50.7% | 51.2% | 82.0% | 150 |
| stylometric_gbm | light_human_edit | 34.7% | 34.7% | 100.0% | 150 |
| stylometric_gbm | paraphrase_t5 | 49.6% | 49.4% | 95.8% | 262 |
| stylometric_gbm | roundtrip_fr | 43.3% | 43.3% | 94.0% | 150 |
| perplexity | esl_student | 19.3% | 19.1% | 94.0% | 150 |
| perplexity | grammar_correct | 5.3% | 5.3% | 100.0% | 262 |
| perplexity | launder_lite | 50.7% | 46.3% | 82.0% | 150 |
| perplexity | light_human_edit | 4.7% | 4.7% | 100.0% | 150 |
| perplexity | paraphrase_t5 | 40.1% | 40.6% | 95.8% | 262 |
| perplexity | roundtrip_fr | 22.7% | 22.0% | 94.0% | 150 |
| fast_detect_gpt | esl_student | 24.7% | 25.5% | 94.0% | 150 |
| fast_detect_gpt | grammar_correct | 5.0% | 5.0% | 100.0% | 262 |
| fast_detect_gpt | launder_lite | 61.3% | 57.7% | 82.0% | 150 |
| fast_detect_gpt | light_human_edit | 4.0% | 4.0% | 100.0% | 150 |
| fast_detect_gpt | paraphrase_t5 | 34.0% | 35.1% | 95.8% | 262 |
| fast_detect_gpt | roundtrip_fr | 24.7% | 24.8% | 94.0% | 150 |
| binoculars_lite | esl_student | 24.0% | 24.1% | 94.0% | 150 |
| binoculars_lite | grammar_correct | 2.7% | 2.7% | 100.0% | 262 |
| binoculars_lite | launder_lite | 62.0% | 61.0% | 82.0% | 150 |
| binoculars_lite | light_human_edit | 0.7% | 0.7% | 100.0% | 150 |
| binoculars_lite | paraphrase_t5 | 42.0% | 42.2% | 95.8% | 262 |
| binoculars_lite | roundtrip_fr | 24.7% | 24.1% | 94.0% | 150 |
| roberta_openai | esl_student | 38.0% | 38.3% | 94.0% | 150 |
| roberta_openai | grammar_correct | 26.7% | 26.7% | 100.0% | 262 |
| roberta_openai | launder_lite | 65.3% | 67.5% | 82.0% | 150 |
| roberta_openai | light_human_edit | 29.3% | 29.3% | 100.0% | 150 |
| roberta_openai | paraphrase_t5 | 55.3% | 55.4% | 95.8% | 262 |
| roberta_openai | roundtrip_fr | 52.7% | 53.2% | 94.0% | 150 |
