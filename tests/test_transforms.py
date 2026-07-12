import numpy as np

from stress_test.transforms import REGISTRY, Pipeline, build_pipeline
from stress_test.transforms.base import MetamorphicRelation
from stress_test.transforms.perturbation import (
    CaseNoise,
    ContractionExpansion,
    HomoglyphSubstitution,
    TypoInjection,
    ZeroWidthInsertion,
    normalize,
)

SAMPLE = (
    "It's a well-known fact that detectors don't handle edited text well. "
    "The experiment can't succeed unless we measure this carefully across many domains."
)


def test_perturbations_are_deterministic_under_seed():
    for cls in (HomoglyphSubstitution, ZeroWidthInsertion, TypoInjection, CaseNoise):
        t = cls()
        assert t(SAMPLE, seed=7).text == t(SAMPLE, seed=7).text


def test_perturbations_change_text():
    for t in (HomoglyphSubstitution(rate=0.5), ZeroWidthInsertion(rate=0.5), CaseNoise(rate=0.5)):
        assert t(SAMPLE, seed=0).text != SAMPLE


def test_all_registered_transforms_are_label_preserving():
    for name, cls in REGISTRY.items():
        assert cls.label_preserving, f"{name} must be a label-preserving metamorphic relation"


def test_contraction_expansion_known_answer():
    result = ContractionExpansion()("It's fine, don't worry.", seed=0).text
    assert result == "It is fine, do not worry."


def test_normalize_undoes_cheap_perturbations():
    perturbed = HomoglyphSubstitution(rate=1.0)(SAMPLE, seed=0).text
    perturbed = ZeroWidthInsertion(rate=1.0).apply(perturbed, np.random.default_rng(0))
    assert perturbed != SAMPLE
    assert normalize(perturbed) == SAMPLE


def test_pipeline_applies_steps_in_order():
    class AppendA(MetamorphicRelation):
        name, category = "append_a", "test"

        def apply(self, text, rng):
            return text + "A"

    class AppendB(MetamorphicRelation):
        name, category = "append_b", "test"

        def apply(self, text, rng):
            return text + "B"

    result = Pipeline("test", [AppendA(), AppendB()])("x", seed=0)
    assert result.text == "xAB"
    assert result.params["steps"] == ["append_a", "append_b"]
    assert result.params["depth"] == 2


def test_build_pipeline_from_registry_names():
    p = build_pipeline("cheap", ["contraction_expand", "case_noise"])
    assert p("Don't stop.", seed=0).text != "Don't stop."
