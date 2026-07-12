from stress_test.transforms import perturbation  # noqa: F401  (registers transforms)
from stress_test.transforms.base import REGISTRY, MetamorphicRelation, TransformResult, register
from stress_test.transforms.compose import NAMED_PIPELINES, Pipeline, build_pipeline

# model-backed transforms are imported lazily by name to avoid requiring torch:
# `import stress_test.transforms.model_backed` registers them when needed.

__all__ = [
    "REGISTRY",
    "MetamorphicRelation",
    "TransformResult",
    "register",
    "NAMED_PIPELINES",
    "Pipeline",
    "build_pipeline",
]
