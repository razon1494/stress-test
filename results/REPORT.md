# STRESS-Test Leaderboard

| Detector | Clean TPR | RS | WCP | FAR (worst) | HCI |
|---|---|---|---|---|---|
| tfidf_logreg | 88.5% | 0.940 | 68.0% | 11.3% | nan |
| perplexity | 93.9% | 0.551 | 46.0% | 2.7% | nan |

## Reliability Card — tfidf_logreg

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 88.5% | headline number everyone else reports |
| Robustness Score (RS) | 0.940 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.900 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 68.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.8% | FPR on clean human text |
| False-Accusation Rate, worst | 11.3% | on `launder_lite` — the social-cost number |
| Hardness Collapse (HCI) | n/a | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 22.3% | evasion by transforms that PRESERVE meaning |

## Reliability Card — perplexity

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 93.9% | headline number everyone else reports |
| Robustness Score (RS) | 0.551 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.283 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 46.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.8% | FPR on clean human text |
| False-Accusation Rate, worst | 2.7% | on `esl_student` — the social-cost number |
| Hardness Collapse (HCI) | n/a | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 24.9% | evasion by transforms that PRESERVE meaning |

## Quality-Adjusted Evasion (machine class, semsim >= 0.85)

| Detector | Condition | Raw evasion | QAES | Valid fraction | n |
|---|---|---|---|---|---|
| tfidf_logreg | esl_student | 16.7% | 17.0% | 94.0% | 150 |
| tfidf_logreg | grammar_correct | 15.3% | 15.3% | 100.0% | 150 |
| tfidf_logreg | launder_lite | 32.0% | 31.7% | 82.0% | 150 |
| tfidf_logreg | light_human_edit | 14.7% | 14.7% | 100.0% | 150 |
| tfidf_logreg | paraphrase_t5 | 37.3% | 38.5% | 95.3% | 150 |
| tfidf_logreg | roundtrip_fr | 16.0% | 16.3% | 94.0% | 150 |
| perplexity | esl_student | 22.0% | 22.0% | 94.0% | 150 |
| perplexity | grammar_correct | 4.7% | 4.7% | 100.0% | 150 |
| perplexity | launder_lite | 54.0% | 50.4% | 82.0% | 150 |
| perplexity | light_human_edit | 4.7% | 4.7% | 100.0% | 150 |
| perplexity | paraphrase_t5 | 42.7% | 42.7% | 95.3% | 150 |
| perplexity | roundtrip_fr | 26.0% | 24.8% | 94.0% | 150 |
