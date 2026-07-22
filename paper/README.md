# Building the manuscript

The manuscript uses BibTeX citations and a committed vector figure. Build it
with `latexmk` so references and cross-references receive all required passes:

```bash
cd paper
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

Do not enable a LaTeX or Overleaf **draft/fast** compilation mode: that mode can
replace included graphics with filename boxes. A successful build must contain
a populated References section, resolved numbered citations, and the rendered
`figures/perplexity_by_corpus.pdf` chart.

GitHub Actions performs the same build and rejects the output when the
bibliography is empty, citations or references are unresolved, or Figure 1 was
not read by the compiler. The workflow artifact contains `main.pdf`, `main.bbl`,
and `main.log` for inspection.
