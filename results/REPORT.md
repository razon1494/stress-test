# STRESS-Test Leaderboard

| Detector | Clean TPR | RS | WCP | FAR (worst) | HCI |
|---|---|---|---|---|---|
| deberta_hc3_ft | 96.6% | nan | 71.3% | 3.3% | -0.036 |
| perplexity | 95.0% | nan | 54.0% | 4.6% | 0.008 |
| tfidf_logreg | 64.9% | nan | 42.7% | 4.0% | -0.073 |
| stylometric_gbm | 59.2% | nan | 42.7% | 3.3% | -0.043 |
| roberta_openai | 85.1% | nan | 40.0% | 20.0% | -0.206 |
| fast_detect_gpt | 94.7% | nan | 26.7% | 3.5% | -0.018 |
| binoculars_lite | 96.2% | nan | 22.7% | 3.5% | 0.034 |

## Reliability Card — tfidf_logreg

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 64.9% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 42.7% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.9% | FPR on clean human text |
| False-Accusation Rate, worst | 4.0% | on `launder_lite` — the social-cost number |
| Hardness Collapse (HCI) | -0.073 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 44.9% | evasion by transforms that PRESERVE meaning |

## Reliability Card — stylometric_gbm

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 59.2% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 42.7% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.9% | FPR on clean human text |
| False-Accusation Rate, worst | 3.3% | on `esl_student` — the social-cost number |
| Hardness Collapse (HCI) | -0.043 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 49.7% | evasion by transforms that PRESERVE meaning |

## Reliability Card — perplexity

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 95.0% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 54.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.9% | FPR on clean human text |
| False-Accusation Rate, worst | 4.6% | on `grammar_correct` — the social-cost number |
| Hardness Collapse (HCI) | 0.008 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 20.1% | evasion by transforms that PRESERVE meaning |

## Reliability Card — fast_detect_gpt

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 94.7% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 26.7% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.9% | FPR on clean human text |
| False-Accusation Rate, worst | 3.5% | on `paraphrase_t5` — the social-cost number |
| Hardness Collapse (HCI) | -0.018 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 34.7% | evasion by transforms that PRESERVE meaning |

## Reliability Card — binoculars_lite

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 96.2% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 22.7% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.9% | FPR on clean human text |
| False-Accusation Rate, worst | 3.5% | on `paraphrase_t5` — the social-cost number |
| Hardness Collapse (HCI) | 0.034 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 33.4% | evasion by transforms that PRESERVE meaning |

## Reliability Card — roberta_openai

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 85.1% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 40.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.9% | FPR on clean human text |
| False-Accusation Rate, worst | 20.0% | on `launder_lite` — the social-cost number |
| Hardness Collapse (HCI) | -0.206 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 39.7% | evasion by transforms that PRESERVE meaning |

## Reliability Card — deberta_hc3_ft

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 96.6% | headline number everyone else reports |
| Robustness Score (RS) | nan | mean retained performance across transforms |
| Transformation Stability (TS) | nan | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 71.3% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.9% | FPR on clean human text |
| False-Accusation Rate, worst | 3.3% | on `paraphrase_t5` — the social-cost number |
| Hardness Collapse (HCI) | -0.036 | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 9.5% | evasion by transforms that PRESERVE meaning |

## Quality-Adjusted Evasion (machine class, semsim >= 0.85)

| Detector | Condition | Raw evasion | QAES | Valid fraction | n |
|---|---|---|---|---|---|
| tfidf_logreg | esl_student | 38.0% | 38.3% | 94.0% | 150 |
| tfidf_logreg | grammar_correct | 36.3% | 36.3% | 100.0% | 262 |
| tfidf_logreg | launder_lite | 57.3% | 57.7% | 82.0% | 150 |
| tfidf_logreg | light_human_edit | 36.7% | 36.7% | 100.0% | 150 |
| tfidf_logreg | paraphrase_t5 | 63.0% | 62.9% | 95.8% | 262 |
| tfidf_logreg | roundtrip_fr | 36.7% | 37.6% | 94.0% | 150 |
| stylometric_gbm | esl_student | 51.3% | 51.1% | 94.0% | 150 |
| stylometric_gbm | grammar_correct | 40.8% | 40.8% | 100.0% | 262 |
| stylometric_gbm | launder_lite | 57.3% | 57.7% | 82.0% | 150 |
| stylometric_gbm | light_human_edit | 40.0% | 40.0% | 100.0% | 150 |
| stylometric_gbm | paraphrase_t5 | 57.3% | 57.0% | 95.8% | 262 |
| stylometric_gbm | roundtrip_fr | 51.3% | 51.8% | 94.0% | 150 |
| perplexity | esl_student | 16.7% | 16.3% | 94.0% | 150 |
| perplexity | grammar_correct | 3.8% | 3.8% | 100.0% | 262 |
| perplexity | launder_lite | 46.0% | 43.1% | 82.0% | 150 |
| perplexity | light_human_edit | 2.7% | 2.7% | 100.0% | 150 |
| perplexity | paraphrase_t5 | 34.0% | 35.1% | 95.8% | 262 |
| perplexity | roundtrip_fr | 20.0% | 19.9% | 94.0% | 150 |
| fast_detect_gpt | esl_student | 34.0% | 34.8% | 94.0% | 150 |
| fast_detect_gpt | grammar_correct | 7.6% | 7.6% | 100.0% | 262 |
| fast_detect_gpt | launder_lite | 73.3% | 72.4% | 82.0% | 150 |
| fast_detect_gpt | light_human_edit | 5.3% | 5.3% | 100.0% | 150 |
| fast_detect_gpt | paraphrase_t5 | 51.1% | 51.8% | 95.8% | 262 |
| fast_detect_gpt | roundtrip_fr | 35.3% | 36.2% | 94.0% | 150 |
| binoculars_lite | esl_student | 30.7% | 29.8% | 94.0% | 150 |
| binoculars_lite | grammar_correct | 4.6% | 4.6% | 100.0% | 262 |
| binoculars_lite | launder_lite | 77.3% | 75.6% | 82.0% | 150 |
| binoculars_lite | light_human_edit | 2.7% | 2.7% | 100.0% | 150 |
| binoculars_lite | paraphrase_t5 | 55.3% | 55.8% | 95.8% | 262 |
| binoculars_lite | roundtrip_fr | 33.3% | 31.9% | 94.0% | 150 |
| roberta_openai | esl_student | 30.7% | 31.2% | 94.0% | 150 |
| roberta_openai | grammar_correct | 22.5% | 22.5% | 100.0% | 262 |
| roberta_openai | launder_lite | 60.0% | 62.6% | 82.0% | 150 |
| roberta_openai | light_human_edit | 25.3% | 25.3% | 100.0% | 150 |
| roberta_openai | paraphrase_t5 | 49.2% | 49.0% | 95.8% | 262 |
| roberta_openai | roundtrip_fr | 47.3% | 47.5% | 94.0% | 150 |
| deberta_hc3_ft | esl_student | 8.0% | 8.5% | 94.0% | 150 |
| deberta_hc3_ft | grammar_correct | 3.4% | 3.4% | 100.0% | 262 |
| deberta_hc3_ft | launder_lite | 28.7% | 25.2% | 82.0% | 150 |
| deberta_hc3_ft | light_human_edit | 3.3% | 3.3% | 100.0% | 150 |
| deberta_hc3_ft | paraphrase_t5 | 8.8% | 8.8% | 95.8% | 262 |
| deberta_hc3_ft | roundtrip_fr | 7.3% | 7.8% | 94.0% | 150 |
