# STRESS-Test Leaderboard

| Detector | Clean TPR | RS | WCP | FAR (worst) | HCI |
|---|---|---|---|---|---|
| tfidf_logreg | 88.5% | 0.935 | 68.0% | 11.3% | nan |
| perplexity | 93.9% | 0.416 | 46.0% | 1.3% | nan |

## Reliability Card — tfidf_logreg

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 88.5% | headline number everyone else reports |
| Robustness Score (RS) | 0.935 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.885 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 68.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.8% | FPR on clean human text |
| False-Accusation Rate, worst | 11.3% | on `launder_lite` — the social-cost number |
| Hardness Collapse (HCI) | n/a | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 28.8% | evasion by transforms that PRESERVE meaning |

## Reliability Card — perplexity

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 93.9% | headline number everyone else reports |
| Robustness Score (RS) | 0.416 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.124 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 46.0% | on `launder_lite` — what deployers should assume |
| False-Accusation Rate, clean | 0.8% | FPR on clean human text |
| False-Accusation Rate, worst | 1.3% | on `roundtrip_fr` — the social-cost number |
| Hardness Collapse (HCI) | n/a | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | 39.3% | evasion by transforms that PRESERVE meaning |

## Quality-Adjusted Evasion (machine class, semsim >= 0.85)

| Detector | Condition | Raw evasion | QAES | Valid fraction | n |
|---|---|---|---|---|---|
| tfidf_logreg | launder_lite | 32.0% | 31.7% | 82.0% | 150 |
| tfidf_logreg | paraphrase_t5 | 37.3% | 38.5% | 95.3% | 150 |
| tfidf_logreg | roundtrip_fr | 16.0% | 16.3% | 94.0% | 150 |
| perplexity | launder_lite | 54.0% | 50.4% | 82.0% | 150 |
| perplexity | paraphrase_t5 | 42.7% | 42.7% | 95.3% | 150 |
| perplexity | roundtrip_fr | 26.0% | 24.8% | 94.0% | 150 |
