from stress_test.detectors.base import Detector, calibrate_threshold, evaluate_at_threshold
from stress_test.detectors.stylometric import StylometricDetector
from stress_test.detectors.tfidf_lr import TfidfLogReg

# torch-backed detectors (PerplexityDetector, FastDetectGPT, BinocularsLite,
# TransformerDetector) are imported from their modules directly to keep the
# base install torch-free.

__all__ = [
    "Detector",
    "calibrate_threshold",
    "evaluate_at_threshold",
    "StylometricDetector",
    "TfidfLogReg",
]
