# Annotation Guidelines — Semantic Preservation

Thank you for helping! You will see pairs of texts: an **original** and a
**transformed** version. You do NOT know (and should not try to guess) how the
transformation was made. Rate each pair on two questions.

## 1. `same_meaning_0or1` — does the transformed text say the same thing?

- **1 (yes)**: a reader would take away the same information, claims, and
  stance. Different wording, sentence order, or style is fine. Small losses of
  emphasis are fine.
- **0 (no)**: facts, claims, or stance changed; important content was added,
  dropped, or contradicted; or the text is too garbled to carry the meaning.

Rules of thumb:
- Judge *content*, not quality. An ugly but faithful rewrite is a **1**.
- A fluent, beautiful text that drops a key point is a **0**.
- If genuinely torn, ask: "would summarizing both texts produce the same
  summary?" If yes → 1.

## 2. `fluency_1to5` — how natural is the transformed text on its own?

Read only the transformed text for this one.

- **5**: fluent, natural; could pass as careful writing.
- **4**: minor awkwardness or one or two small errors.
- **3**: noticeably awkward or error-prone but fully understandable.
- **2**: hard going; frequent errors or strange phrasing.
- **1**: broken; barely readable.

## Practical notes

- Work top to bottom; do not skip rows. ~600 pairs ≈ 4–5 hours; split across
  several sittings. Please do not use AI tools to rate — the whole point is a
  human judgment.
- `comments` is optional; use it when a pair is a genuinely hard call.
- Some pairs are intentionally identical or near-identical; rate them normally.
- Your sheet shares a block of pairs with the other annotators (for measuring
  agreement); you won't know which ones. Please don't discuss ratings with
  each other until everyone is done.

When finished, return your `annotator_N.csv`. Agreement and per-condition
results are computed with:
`python scripts/11_make_annotation_batch.py --score annotation/annotator_*.csv`
