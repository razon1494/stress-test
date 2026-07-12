"""Composition engine: transformation pipelines as chained metamorphic relations.

The compositional axis (chain depth 1-3, order effects) is a core novelty claim
— see docs/related_work.md claim 1. NAMED_PIPELINES are the realistic
'laundering' and 'innocent-user' chains reported in the paper; Worst-Case
Performance is defined over these, not over arbitrary garbage-producing chains.
"""

from __future__ import annotations

import numpy as np

from stress_test.transforms.base import REGISTRY, MetamorphicRelation, TransformResult


class Pipeline(MetamorphicRelation):
    category = "pipeline"

    def __init__(self, name: str, steps: list[MetamorphicRelation]):
        self.name = name
        self.steps = steps
        self.semantics_lossy = any(s.semantics_lossy for s in steps)

    def apply(self, text: str, rng: np.random.Generator) -> str:
        for step in self.steps:
            text = step.apply(text, rng)
        return text

    def __call__(self, text: str, seed: int = 0) -> TransformResult:
        result = super().__call__(text, seed)
        result.params["steps"] = [s.name for s in self.steps]
        return result

    def params(self) -> dict:
        return {"depth": len(self.steps)}


# name -> ordered list of registered transform names
NAMED_PIPELINES: dict[str, list[str]] = {
    # a non-native speaker drafting via translation, then cleaning up
    "esl_student": ["roundtrip_fr", "grammar_correct"],
    # deliberate laundering of machine text
    "content_launderer": ["paraphrase_t5", "roundtrip_de", "paraphrase_t5"],
    # the innocent human whose only 'crime' is using a grammar checker
    "innocent_grammar_user": ["grammar_correct"],
    # casual human cleanup: fix typos, expand contractions
    "light_human_edit": ["contraction_expand", "grammar_correct"],
    # cheap adversarial stack (defeated by normalization? -> ablation)
    "unicode_attacker": ["homoglyph", "zero_width", "whitespace_noise"],
    # depth-2 semantic laundering, light enough for a laptop GPU
    "launder_lite": ["paraphrase_t5", "roundtrip_fr"],
    # depth-3 semantic chain for the composition-depth analysis
    "deep_launder": ["paraphrase_t5", "simplify", "formalize"],
}


def build_pipeline(name: str, step_names: list[str] | None = None) -> Pipeline:
    steps = step_names if step_names is not None else NAMED_PIPELINES[name]
    return Pipeline(name, [REGISTRY[s]() for s in steps])
