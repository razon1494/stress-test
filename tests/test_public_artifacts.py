"""Guardrails for professor-facing repository artifacts.

These tests keep the public README tied to the structured result file and catch
the placeholder/stale-claim problems that previously drifted into the draft.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _readme_result_rows() -> dict[str, list[str]]:
    rows: dict[str, list[str]] = {}
    for line in _read("README.md").splitlines():
        if not line.startswith("|") or "Detector" in line or set(line) <= {"|", "-", ":"}:
            continue
        cells = [cell.strip().replace("**", "") for cell in line.strip("|").split("|")]
        if len(cells) == 5 and cells[1].endswith("%"):
            rows[cells[0]] = cells[1:]
    return rows


@pytest.mark.parametrize(
    ("result_key", "readme_label"),
    [
        ("fast_detect_gpt", "Fast-DetectGPT"),
        ("binoculars_lite", "Binoculars-lite"),
        ("deberta_hc3_ft", "DeBERTa-v3, HC3 fine-tune"),
        ("perplexity", "GPT-2 perplexity"),
        ("roberta_openai", "OpenAI RoBERTa detector"),
        ("tfidf_logreg", "TF-IDF + logistic regression"),
        ("stylometric_gbm", "Stylometric GBM"),
    ],
)
def test_readme_headline_matches_structured_results(result_key: str, readme_label: str) -> None:
    results = json.loads(_read("results/per_domain.json"))
    row = _readme_result_rows()[readme_label]
    payload = results[result_key]

    clean_tpr = float(row[0].removesuffix("%")) / 100
    robustness = float(row[1])
    worst_case = float(row[2].removesuffix("%")) / 100
    human_edit_far = float(row[3].removesuffix("%")) / 100

    assert clean_tpr == pytest.approx(payload["conditions"]["clean"]["tpr"], abs=0.0005)
    assert robustness == pytest.approx(payload["rs"], abs=0.0005)
    assert worst_case == pytest.approx(payload["wcp"]["wcp"], abs=0.0005)
    assert human_edit_far == pytest.approx(
        payload["conditions"]["human_edit"]["fpr"], abs=0.0005
    )


def test_public_artifacts_have_no_repository_placeholders_or_stale_rate() -> None:
    public_text = "\n".join(
        _read(path)
        for path in ("README.md", "CITATION.cff", "paper/main.tex", "results/REPORT.md")
    )
    assert "<your-username>" not in public_text
    assert "15.3\\%" not in public_text
    assert "validated against human judgments" not in public_text
    assert "what deployers should assume" not in public_text
    assert "headline number everyone else reports" not in public_text
    assert "social-cost number" not in public_text


def test_paper_citations_and_graphics_resolve() -> None:
    paper = _read("paper/main.tex")
    bibliography = _read("paper/references.bib")
    bib_keys = set(re.findall(r"@[A-Za-z]+\{([^,]+),", bibliography))

    cited_keys: set[str] = set()
    for group in re.findall(r"\\cite(?:p|t|alp)?\{([^}]+)\}", paper):
        cited_keys.update(key.strip() for key in group.split(","))
    assert cited_keys <= bib_keys, f"missing bibliography keys: {sorted(cited_keys - bib_keys)}"

    for graphic in re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", paper):
        assert (ROOT / "paper" / graphic).exists(), f"missing paper graphic: {graphic}"


def test_paper_environments_are_balanced() -> None:
    paper = _read("paper/main.tex")
    stack: list[str] = []
    for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", paper):
        kind, environment = match.groups()
        if kind == "begin":
            stack.append(environment)
        else:
            assert stack, f"unmatched end for {environment}"
            assert stack.pop() == environment, f"misnested environment: {environment}"
    assert not stack, f"unclosed environments: {stack}"


@pytest.mark.parametrize(
    "document",
    [
        "README.md",
        "docs/related_work.md",
        "docs/reproducibility.md",
        "docs/result_provenance.md",
        "docs/zero_budget_plan.md",
    ],
)
def test_local_markdown_links_resolve(document: str) -> None:
    source = ROOT / document
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("mailto:") or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        assert (source.parent / path).resolve().exists(), f"broken link in {document}: {target}"
