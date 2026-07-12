# STRESS-Test Leaderboard

| Detector | Clean TPR | RS | WCP | FAR (worst) | HCI |
|---|---|---|---|---|---|
| tfidf_logreg | 88.5% | 0.999 | 87.4% | 1.5% | nan |

## Reliability Card — tfidf_logreg

*Operating point: threshold calibrated once at 1% FPR on clean human text (never re-tuned).*

| Axis | Value | Meaning |
|---|---|---|
| Clean TPR @ 1% FPR | 88.5% | headline number everyone else reports |
| Robustness Score (RS) | 0.999 | mean retained performance across transforms |
| Transformation Stability (TS) | 0.994 | 1 = uniform across transforms, low = fragile |
| Worst-Case Perf (WCP) | 87.4% | on `typo` — what deployers should assume |
| False-Accusation Rate, clean | 0.8% | FPR on clean human text |
| False-Accusation Rate, worst | 1.5% | on `homoglyph` — the social-cost number |
| Hardness Collapse (HCI) | n/a | 0 = uniform over difficulty, 1 = collapses on hard cases |
| ECE clean → shifted | n/a → n/a | is confidence still meaningful under shift? |
| Quality-Adjusted Evasion | n/a | evasion by transforms that PRESERVE meaning |
