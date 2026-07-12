# Zero-Budget Execution Plan

Target cash cost: **$0** (worst case < $20 if you opt into any paid API — nothing in the
default pipeline requires one). Compute: **Kaggle (30 GPU-h/week free) + Google Colab free
tier + your own CPU**. Every model below is open-weight.

## 1. Machine-generated text: reuse, don't generate

Generating text with 6 frontier LLMs is the expensive part of every detection benchmark —
so we don't do it. We build the *measurement layer* on top of existing public corpora,
which is also our scientific differentiation ("we don't compete on generation scale").

| Corpus | What it gives us | License / access |
|---|---|---|
| **HC3** (Hello-SimpleAI/HC3) | Paired human/ChatGPT answers, 5 domains | Free, HF Hub |
| **MAGE** (yaful/MAGE) | 27 generators, 10 domains, has OOD splits | Free, HF Hub |
| **RAID** (sample) | 11 generators incl. decoding variants | Free, HF Hub (large — use a stratified sample) |
| **PERSUADE / ASAP essays** | Human student essays (education domain) | Free, Kaggle |
| **ICNALE / TOEFL11** | Non-native English writing (fairness subset) | Free for research (registration) |

We generate only one small subset ourselves: **watermarked text** (KGW watermark needs
generator cooperation), using an open model (e.g. `Qwen2.5-1.5B` or `opt-1.3b`) on Kaggle.

## 2. Transformations: local open models, no APIs

| Category | Tool | Size / where it runs |
|---|---|---|
| Paraphrase | `humarin/chatgpt_paraphraser_on_T5_base` | 220M — CPU ok, GPU fast |
| Recursive paraphrase | same model, n rounds | — |
| Grammar correction | `grammarly/coedit-large` (instruction: "Fix grammatical errors...") | 770M — Colab/Kaggle |
| Simplification / formality / neutralization | `grammarly/coedit-large` (one model covers 4 transform types) | — |
| Translation round-trip | `Helsinki-NLP/opus-mt-en-{fr,de,zh}` + reverse | ~300M each — CPU ok |
| Summarization | `sshleifer/distilbart-cnn-12-6` | CPU ok |
| Char/token perturbations | pure Python (this repo) | free, instant |
| Human editing | you + 2–3 volunteer peers, small stratified sample | free |
| Expansion / style personas | optional: Gemini free tier or a local Ollama model | $0 |

**Dropped vs. the full design:** DIPPER (11B — too heavy). We approximate its effect with
recursive T5 paraphrasing at two "diversity" settings and cite DIPPER as motivation.
36 transforms → **~24 transforms** is acceptable; never cut validation or statistics.

## 3. Detectors: all open-weight

| Detector | Model | Cost |
|---|---|---|
| TF-IDF + LogReg | sklearn | CPU, free |
| Perplexity threshold | `gpt2` / `gpt2-large` | CPU slow / Kaggle fast |
| Fast-DetectGPT (analytic) | `gpt2-xl` or `EleutherAI/gpt-neo-1.3B` | Kaggle |
| Binoculars-lite | small same-tokenizer pair (note deviation from falcon-7b pair) | Kaggle |
| RoBERTa detector | `openai-community/roberta-base-openai-detector` + your DeBERTa-v3 fine-tune | Kaggle (~2 GPU-h) |
| GPTZero-style features | burstiness/ppl features + GBM (this repo) | CPU |
| Watermark (KGW) | official open implementation on our watermarked subset | Kaggle |

Commercial APIs (GPTZero, Originality): **skip**, or spend <$10 on a 200-example external
validity spot-check at the very end. Not required for the paper.

## 4. Annotation & LLM-judge

- Semantic-preservation human labels: **you + 2–3 volunteer peers**, ~600 stratified pairs,
  3-way redundancy on a 200-pair overlap subset for Krippendorff's alpha. Be transparent in
  the paper that annotators are the authors + volunteers (common for solo benchmarks).
- Large-scale semantic scoring: `sentence-transformers/all-MiniLM-L6-v2` cosine (free, CPU)
  + optional Gemini-free-tier LLM-judge, both validated against the human sample.

## 5. Compute budget sketch

- Transform application over ~30k texts x ~24 transforms: mostly T5-base-class models,
  batchable — fits comfortably in 3–4 Kaggle weeks alongside detector runs.
- Detector scoring: one pass per detector per condition; cache everything to parquet.
- DeBERTa fine-tune: ~2 h on a Kaggle T4.
- Everything cached and hashed so no step ever runs twice (`scripts/` + DVC-style manifest).
