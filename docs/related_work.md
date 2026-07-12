# Related Work & Differentiation — VERIFIED against the PDFs (Week-1 done)

Status: all eight papers in `docs/Related Papers/` read and verified 2026-07-12.
The two open questions from v1 of this doc are now answered; claims restated below
in their verified (and in one case *stronger*) form.

## 1. The two make-or-break questions — ANSWERED

**Q1. Does RAID compose attacks?** **No.** RAID's design is a cross-product: one
generation per (domain × model × decoding × penalty × single attack). The 11 attacks
(alternative spelling, article deletion, paragraph insertion, upper-lower swap,
zero-width space, whitespace, homoglyph, number swap, paraphrase, synonym swap,
misspelling) are applied one at a time, never chained. DetectRL likewise applies its
attack types singly; its "data mixing" is sentence-level source mixing, not a
transformation chain. → **Compositional-pipeline claim fully intact.**

**Q2. Does DetectRL report FPR on perturbed human text?** **No — and this is our
biggest opening.** DetectRL DOES attack human text (Task 4: 89,600 attacked human
samples vs 11,200 raw) but evaluates ONLY with AUROC/F1. Their conclusion (§3, Table 6):
paraphrase on human text costs zero-shot detectors 7.95% AUROC, while *perturbation
attacks on human text INCREASE average AUROC by 10.22%* — they conclude attacks on
human text are essentially harmless or even helpful. **AUROC is threshold-free; it
cannot see false accusations at a deployed operating point.** Our own first HC3 run
already shows the artifact: homoglyph perturbation left TF-IDF TPR unchanged while
DOUBLING FPR on human text (0.76% → 1.53%) at a frozen 1%-FPR threshold.
→ **Revisionist headline experiment: "Attacks on human text look harmless under AUROC
and are not harmless at deployed thresholds — we re-evaluate DetectRL's Task-4
conclusion under threshold transfer."**

## 2. Verified paper-by-paper table

| Paper (verified venue) | What it does (verified numbers) | Verified gap we occupy |
|---|---|---|
| **RAID** — Dugan et al., ACL 2024, arXiv:2405.07940 | 6.2M generations; 11 generators, 8 domains (+code/Czech/German in RAID-extra), 4 decoding strategies, 11 single attacks, 12 detectors; leaderboard w/ hidden test split. Per-domain thresholds at **fixed 5% FPR** calibrated on human data. Manual review that attacks are "inconspicuous" (small mutation %), no per-example semantic conditioning. Findings we build on: naive thresholds give dangerously high FPR (LLMDet 92% @ τ=0.5); Binoculars strongest at low FPR; 40:1 machine:human ratio makes precision misleading. | No composition; attacks never applied to human text (so FPR-under-transformation is unmeasurable in their design); no hardness stratification; no calibration-drift/abstention analysis; attack success not quality-conditioned. |
| **DetectRL** — Wu et al., NeurIPS 2024 D&B, arXiv:2410.23746 | 4 LLMs (GPT-3.5, PaLM-2, Claude-instant, Llama-2-70b), 4 high-risk domains; prompt/paraphrase/perturbation/mixing attacks; 100.8k human (89.6k attacked!) + 134.4k machine; AUROC + F1 only. | See Q2. Also: only adversarial noise on human text — no *benign* transforms (grammar correction, translation), no non-native subset, no deployed-threshold protocol, no composition. |
| **DIPPER** — Krishna et al., NeurIPS 2023, arXiv:2303.13408 | 11B context-aware paraphraser w/ lexical & reorder control; DetectGPT 70.3%→4.6% **at 1% FPR** (protocol we adopt); retrieval defense catches 80–97% of paraphrased at 1% FPR over 15M-generation DB. Controls semantics (quasi-paraphrase). UMass: Krishna/Karpinska/**Iyyer**. | Single attack family; a detector stress test, not an evaluation framework. Cite as motivation + adopt their FPR discipline; do NOT position against. |
| **Sadasivan et al.** — "Can AI-Generated Text be Reliably Detected?", UMD (Feizi), arXiv:2303.13408-adjacent (verify final venue: TMLR 2025) | Recursive paraphrasing breaks watermark/neural/zero-shot/retrieval detectors; quality measured (human study + perplexity + benchmarks) as aggregate tradeoff; watermark **spoofing** (adversarial false-accusation flavor); theory: best detector AUROC bounded by TV distance. | Quality is an aggregate tradeoff analysis, not per-example conditioning of success (→ QAES); spoofing is adversarial FAR — our benign-transform FAR is complementary. |
| **Liang et al.** — Patterns 2023 (Stanford, Zou) | 7 commercial detectors on 91 human TOEFL essays: **61.22% average FPR**; 97.8% flagged by ≥1 detector; ChatGPT "enhance word choices" drops FPR to 11.77%; simplifying native 8th-grade essays raises FPR 5.19%→56.65%. Perplexity mediates the bias. | Clean text only, commercial detectors only, n=91. The bias × transformation interaction (grammar-correct/translate the non-native text, measure FAR at fixed threshold) is untouched — our fairness experiment, with their prompting result as the bridge. |
| **MAGE** — Li et al., ACL 2024 | 447k texts, 27 LLMs / 7 families, 10 domains, 8 testbeds incl. unseen-model & unseen-domain; best OOD detection 86.54%; "decreasing linguistic distinctions" analysis. Trains own detectors (unlike RAID). | Distribution shift ≠ transformation robustness; no attacks on human text, no thresholds-at-FPR, no hardness. **We reuse MAGE as a generator-diverse data source.** |
| **M4GT-Bench** — Wang et al., ACL 2024 | Multilingual multi-generator benchmark; 3 tasks: binary detection, generator attribution, human↔machine boundary detection; human-performance eval. | No transformation axis at all. Reuse (optionally) for multilingual source text. |
| **HC3** — Guo et al., 2023, arXiv:2301.07597 | ~40k questions with paired human + ChatGPT answers, 5 domains; the original ChatGPT-detection corpus. | Single generator, clean only — already wired in as our primary paired source. |

## 3. Claims, restated post-verification

1. **Compositional robustness** (depth 1→3, order effects, named realistic pipelines) —
   **confirmed novel** across all eight papers.
2. **Symmetric FAR at deployed thresholds** — **upgraded from claim to refutation
   experiment**: DetectRL measured attacked human text threshold-free and called it
   harmless; we re-measure at clean-calibrated 1% FPR and show the false-accusation
   drift AUROC hides. Plus benign transforms and the non-native subset neither RAID
   nor DetectRL touch.
3. **Threshold-transfer protocol** — *narrowed honestly*: RAID already fixes FPR (5%,
   per-domain) and DIPPER uses 1% FPR, so "we evaluate at fixed FPR" is NOT novel.
   What is: freezing the clean-calibrated threshold and re-measuring BOTH sides
   (TPR degradation AND human-side FPR drift) under transformation, plus calibration
   drift (ΔECE) and risk–coverage/abstention — none of the eight report any of these.
4. **QAES / quality-adjusted evasion** — *stated precisely*: DIPPER and Sadasivan do
   control/measure text quality (aggregate tradeoff curves, human studies); the
   benchmarks (RAID: manual "inconspicuousness" review; DetectRL: none) do not
   condition per-example attack success on validated semantic preservation, and no
   one reports quality-adjusted evasion as a benchmark metric.
5. **Hardness-aware evaluation** (5-signal score, leave-one-out committee, HCI) —
   **confirmed novel**; every paper reports averages (RAID stratifies by domain/
   decoding, DetectRL by length — none by per-example difficulty).
6. **Fairness × robustness interaction** — **confirmed open**; Liang et al. is clean-text
   only and their own vocabulary-enhancement result (61%→12% FPR) is itself evidence
   that transformations move FAR dramatically — nobody followed that thread.

## 4. Design decisions imported from the papers

- **Adopt DIPPER/RAID's fixed-FPR discipline**; use 1% (DIPPER) not 5% (RAID) as
  primary operating point; calibrate per-domain like RAID (they show pooled
  calibration hides domain FPR imbalance).
- **RAID's class-imbalance warning**: keep test conditions ~balanced; never report
  precision on generation-heavy pools.
- **Binoculars is the zero-shot detector to beat** (RAID: best at low FPR) — our
  Binoculars-lite deviation must be reported clearly.
- **Sadasivan's TV-distance bound** gives the theory paragraph for "why hardness":
  as distributions converge, per-example difficulty becomes the whole game.
- **Liang's perplexity-mediation finding** motivates perplexity-closeness as a
  hardness signal and predicts grammar-correction will RAISE non-native FAR
  (their simplification experiment shows the reverse direction moves FPR 5%→57%).

## 5. Remaining verification debt (small)

- Sadasivan et al. final venue (arXiv v2+ / TMLR?) before citing.
- Beemo (human-edited machine text) not in our PDF set — skim before claiming the
  human-edit transform is under-benchmarked.
- RAID paraphrase attack implementation (DIPPER-based or T5?) — check their Appendix
  E.4 / repo when we implement ours, to differentiate parameters.
