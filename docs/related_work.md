# Related-work notes and differentiation

These are working notes for the manuscript, not a systematic review or a claim
of definitive novelty. Every comparison should be checked against the cited
paper and its latest public version before submission.

## Positioning

STRESS-Test studies detector reliability under transformations using four
connected ideas:

1. apply transformations to both human and machine text;
2. freeze a decision threshold instead of relying only on ranking metrics;
3. evaluate composed, realistic transformation pipelines;
4. report quality-, hardness-, and subgroup-aware results alongside averages.

The intended contribution is the joint protocol. Several individual elements
already appear in prior work and should not be presented as independently novel.

## Comparison with closely related work

| Work | Relevant contribution | Relationship to STRESS-Test |
|---|---|---|
| RAID (Dugan et al.) | Large detector benchmark with adversarial attacks and per-domain thresholds at a fixed FPR | Motivates domain-aware operating points and strong low-FPR baselines; STRESS-Test additionally studies symmetric human-side transformations and composition |
| DetectRL (Wu et al.) | Evaluates attacks across human and machine text using AUROC/F1 | Motivates testing whether threshold-free summaries conceal false-accusation drift at a fixed operating point |
| DIPPER (Krishna et al.) | Controlled paraphrasing and evaluation at 1% FPR | Establishes paraphrase robustness as a central detector failure mode and motivates the operating point used here |
| Sadasivan et al. | Recursive paraphrasing, quality analysis, spoofing, and theoretical limits on detection | Motivates repeated transformations, explicit quality control, and caution about universal detector claims |
| Liang et al. | Documents detector bias against non-native English writing and analyzes perplexity as a mechanism | Motivates writer/register slices and the investigation of benign editing effects |
| MAGE | Multi-generator and multi-domain detection benchmark | Provides a natural future source for generator-diverse validation beyond the current HC3 core |
| M4GT-Bench | Multilingual and multi-generator evaluation | Provides a future multilingual extension; the current repository does not implement that extension |
| HC3 | Paired human/ChatGPT answers across five domains | Supplies the current machine-text core and therefore limits generator diversity |

## Claims that the current evidence can support

- Clean TPR and transformation robustness can rank detector families
  differently in the current HC3-based experiment.
- Fixed-threshold analysis exposes false-accusation movement that AUROC alone
  cannot localize.
- Detector vulnerabilities differ by mechanism: surface, likelihood, and
  supervised transformer detectors respond differently to the same changes.
- Writing-register slices are heterogeneous and cannot be reduced to a simple
  native/non-native ordering.

These are preliminary observations from the present data and calibration
regimes. They should not be generalized to commercial detectors, unseen
generators, or deployment populations without further experiments.

## Differentiation hypotheses still requiring confirmation

- No prior benchmark jointly covers symmetric transformations, realistic
  composition, fixed-threshold FAR, per-example quality filtering, and
  hardness-aware analysis.
- Quality-adjusted evasion adds useful information beyond aggregate
  quality/attack-success trade-offs.
- A detector-relative hardness definition is more informative than a universal
  text-only difficulty score.
- Register and predictability explain subgroup FAR differences better than
  native status alone.

The first hypothesis requires a broader literature search. The remaining three
require independent calibration, completed human annotation, more generators,
and confirmatory statistical analyses.

## Submission checklist for related-work claims

- Verify paper titles, authors, venues, and version dates from primary sources.
- Confirm RAID and DetectRL transformation/composition details from their code
  and appendices.
- Review recent benchmarks of human-edited machine text, including Beemo-style
  evaluations.
- Replace categorical language such as “first,” “only,” or “none” with a scoped
  statement unless the literature search justifies it.
- Cite a source next to every quantitative comparison.
