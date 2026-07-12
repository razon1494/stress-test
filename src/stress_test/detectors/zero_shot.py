"""Zero-shot statistical detectors: perplexity threshold, Fast-DetectGPT
(analytic sampling discrepancy), Binoculars. Lazy torch imports; model sizes
chosen for Kaggle free tier (see docs/zero_budget_plan.md).

NOTE: Binoculars here defaults to a small same-tokenizer pair
('Binoculars-lite'); the original paper uses falcon-7b / falcon-7b-instruct.
Report the deviation explicitly in the paper.
"""

from __future__ import annotations

from functools import lru_cache

import numpy as np

from stress_test.detectors.base import Detector


@lru_cache(maxsize=3)
def _causal_lm(model_name: str):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()
    if torch.cuda.is_available():
        model = model.to("cuda")
    return tokenizer, model


def _token_logprobs(model_name: str, text: str):
    """Returns (token_logprobs, full_logits[1:], token_ids[1:]) for one text."""
    import torch
    import torch.nn.functional as F

    tokenizer, model = _causal_lm(model_name)
    ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    ids = {k: v.to(model.device) for k, v in ids.items()}
    with torch.no_grad():
        logits = model(**ids).logits[0]
    targets = ids["input_ids"][0][1:]
    logits = logits[:-1]
    logprobs = F.log_softmax(logits.float(), dim=-1)
    token_lp = logprobs.gather(-1, targets.unsqueeze(-1)).squeeze(-1)
    return token_lp.cpu(), logprobs.cpu(), targets.cpu()


class PerplexityDetector(Detector):
    """score = -mean NLL: machine text is (typically) low-perplexity under a
    reference LM, so higher score = more machine-like."""

    name = "perplexity"

    def __init__(self, model_name: str = "gpt2"):
        self.model_name = model_name

    def score(self, texts: list[str]) -> np.ndarray:
        out = []
        for text in texts:
            token_lp, _, _ = _token_logprobs(self.model_name, text)
            out.append(float(token_lp.mean()))
        return np.asarray(out)


class FastDetectGPT(Detector):
    """Analytic conditional sampling discrepancy (Bao et al., ICLR 2024):
    d = (sum log p(x_t) - sum mu_t) / sqrt(sum var_t), with mu/var taken under
    the model's own next-token distribution. Higher = more machine-like."""

    name = "fast_detect_gpt"

    def __init__(self, model_name: str = "gpt2-large"):
        self.model_name = model_name

    def score(self, texts: list[str]) -> np.ndarray:
        import torch

        out = []
        for text in texts:
            token_lp, logprobs, _ = _token_logprobs(self.model_name, text)
            probs = torch.exp(logprobs)
            mu = (probs * logprobs).sum(-1)
            var = (probs * logprobs.square()).sum(-1) - mu.square()
            denom = float(var.sum().clamp(min=1e-8).sqrt())
            out.append(float((token_lp.sum() - mu.sum()) / denom))
        return np.asarray(out)


class BinocularsLite(Detector):
    """B(x) = PPL_observer(x) / X-PPL(observer, performer): near 1 for machine
    text, higher for human (Hans et al., ICML 2024). score = -B so that higher
    = more machine-like, matching the Detector convention.

    Observer/performer must share a tokenizer."""

    name = "binoculars_lite"

    def __init__(self, observer: str = "gpt2", performer: str = "distilgpt2"):
        self.observer = observer
        self.performer = performer

    def score(self, texts: list[str]) -> np.ndarray:
        import torch
        import torch.nn.functional as F

        out = []
        for text in texts:
            obs_lp, obs_logprobs, _ = _token_logprobs(self.observer, text)
            _, perf_logprobs, _ = _token_logprobs(self.performer, text)
            log_ppl = float(-obs_lp.mean())
            perf_probs = torch.exp(perf_logprobs)
            # cross-entropy of observer's predictions under performer's distribution
            x_ent = float(-(perf_probs * obs_logprobs).sum(-1).mean())
            out.append(-log_ppl / max(x_ent, 1e-8))
        return np.asarray(out)
