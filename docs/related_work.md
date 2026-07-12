# Related Work & Differentiation (Week-1 doc)

Purpose: exact statement of what exists, what each work lacks, and what STRESS-Test claims.
Verify every venue/year against the actual PDFs before citing (marked entries are from
memory and must be checked).

## 1. Benchmarks

| Work | What it does | What it lacks (our opening) |
|---|---|---|
| **RAID** (Dugan et al., ACL 2024) | 6M+ generations, 11 detectors, 11 adversarial attacks, 8 domains, leaderboard | Atomic attacks only (no composition); no semantic-preservation control on attack success; averages only (no hardness stratification); attacks applied to machine text only (no FPR-drift on transformed human text) |
| **DetectRL** (Wu et al., NeurIPS 2024 D&B) | Real-world attack scenarios: paraphrase, perturbation, prompt attacks | Same gaps: no composition depth analysis, no quality-adjusted evasion, no calibration/abstention analysis |
| **MAGE** (Li et al., ACL 2024) | 27 generators, 10 domains, OOD test settings | Distribution-shift focus, not transformation robustness; no operating-point / threshold-transfer protocol |
| **M4 / M4GT-Bench** (Wang et al., 2024) | Multilingual, multi-generator | No adversarial/transformation axis |
| **HC3** (Guo et al., 2023) | Paired human/ChatGPT QA corpus | Single generator, clean text only — we reuse it as a *source*, not a competitor |
| **Beemo** (2024, verify) | Human-edited machine text | Editing only; no systematic transformation taxonomy, no hardness or calibration analysis |

## 2. Attacks / robustness studies

| Work | What it does | What it lacks |
|---|---|---|
| **DIPPER** (Krishna et al., NeurIPS 2023) | 11B paraphraser evades detectors; retrieval defense | Single attack type; success not conditioned on validated meaning preservation |
| **Sadasivan et al. 2023** (UMD) | Recursive paraphrase attack + impossibility argument | Theory + one attack family; no deployment-calibrated measurement |
| **OUTFOX** (Koike et al., AAAI 2024) | Adversarial in-context detector attacks | Attack-centric, education domain only |
| **Liang et al. 2023** (Patterns) | Detectors biased against non-native English writers | Bias measured on *clean* text only — the bias x transformation interaction is untouched. **This is our fairness opening.** |

## 3. Detectors (we evaluate, not compete with)

DetectGPT (Mitchell et al., ICML 2023); **Fast-DetectGPT** (Bao et al., ICLR 2024);
**Binoculars** (Hans et al., ICML 2024); RADAR (Hu et al., NeurIPS 2023); Ghostbuster
(Verma et al., NAACL 2024); OpenAI RoBERTa detector; **KGW watermark** (Kirchenbauer et
al., ICML 2023) — paraphrase/translation removal is its known weakness, which our
transform suite tests directly.

## 4. Our claims (each must survive "RAID already did this")

1. **Compositional robustness**: degradation as a function of transformation chain depth
   (1→3) and order, with realistic named pipelines. *No prior benchmark measures composition.*
2. **Quality-adjusted evasion (QAES)**: evasion success conditioned on validated semantic
   preservation. *Prior "attack success rates" conflate evading the detector with destroying
   the text.*
3. **Hardness-aware evaluation**: per-example difficulty score (leave-one-out committee,
   validated), hardness-stratified metrics, Hardness Collapse Index. *All prior work reports
   averages.*
4. **Symmetric evaluation / False-Accusation Risk**: every transform applied to human text
   too; FPR drift at deployed thresholds, incl. non-native-writer subset. *Extends Liang et
   al. from clean-text bias to bias-under-transformation.*
5. **Threshold-transfer protocol**: calibrate once at 1% FPR on clean data, never re-tune.
   *Benchmarks that re-tune per condition (or report only AUROC) overstate robustness.*
6. **Calibration & abstention under shift**: ΔECE, risk–coverage/AURC. *Unstudied for this task.*

## 5. Threats to our differentiation (be honest)

- RAID's "recursive attacks"? — check: RAID applies attacks singly, not composed. Verify on
  their code before claiming.
- DetectRL includes some human-text perturbation? — verify their FPR reporting; if present,
  our claim narrows to "at deployed thresholds + non-native subset + composition".
- Someone publishes composition first (active area): mitigation — post arXiv early, keep the
  hardness + FAR + calibration trio as the core (harder to scoop simultaneously).

## 6. Reading order (Week 1)

RAID → DetectRL → DIPPER → Sadasivan → Binoculars → Fast-DetectGPT → Liang → KGW →
MAGE (data card only) → Beemo (data card only).
