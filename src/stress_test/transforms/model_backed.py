"""Model-backed transformations (categories A-G). All open-weight, lazy-loaded
so importing the package never downloads a model. Sized for Colab/Kaggle free
tier — see docs/zero_budget_plan.md for the model choices.
"""

from __future__ import annotations

import re
from functools import lru_cache

import numpy as np

from stress_test.transforms.base import MetamorphicRelation, register

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def _split_sentences(text: str) -> list[str]:
    return [s for s in _SENT_SPLIT.split(text.strip()) if s]


@lru_cache(maxsize=4)
def _seq2seq(model_name: str):
    """One cached (tokenizer, model) pair per model; at most a few fit in RAM."""
    import torch
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.eval()
    if torch.cuda.is_available():
        model = model.to("cuda")
    return tokenizer, model


def _generate(model_name: str, prompts: list[str], max_new_tokens: int = 128) -> list[str]:
    import torch

    tokenizer, model = _seq2seq(model_name)
    outputs: list[str] = []
    for i in range(0, len(prompts), 8):
        batch = tokenizer(
            prompts[i : i + 8], return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(model.device)
        with torch.no_grad():
            generated = model.generate(
                **batch, max_new_tokens=max_new_tokens, num_beams=4
            )
        outputs.extend(tokenizer.batch_decode(generated, skip_special_tokens=True))
    return outputs


class _SentencewiseSeq2Seq(MetamorphicRelation):
    """Applies a seq2seq model sentence by sentence and rejoins — keeps long
    documents within the models' 512-token context."""

    model_name: str = ""
    prompt_template: str = "{sentence}"

    def apply(self, text: str, rng: np.random.Generator) -> str:
        sentences = _split_sentences(text)
        if not sentences:
            return text
        prompts = [self.prompt_template.format(sentence=s) for s in sentences]
        return " ".join(_generate(self.model_name, prompts))

    def params(self) -> dict:
        return {"model": self.model_name}


@register
class T5Paraphrase(_SentencewiseSeq2Seq):
    name = "paraphrase_t5"
    category = "paraphrasing"
    model_name = "humarin/chatgpt_paraphraser_on_T5_base"
    prompt_template = "paraphrase: {sentence}"


@register
class RecursiveParaphrase(MetamorphicRelation):
    """DIPPER-style recursive paraphrasing on a zero-budget: n rounds of the
    T5 paraphraser (cite Sadasivan et al. 2023 for the recursive attack)."""

    name = "paraphrase_recursive"
    category = "paraphrasing"

    def __init__(self, rounds: int = 3):
        self.rounds = rounds
        self._inner = T5Paraphrase()

    def apply(self, text: str, rng: np.random.Generator) -> str:
        for _ in range(self.rounds):
            text = self._inner.apply(text, rng)
        return text

    def params(self) -> dict:
        return {"rounds": self.rounds}


class _CoEdit(_SentencewiseSeq2Seq):
    """grammarly/coedit-large covers grammar, simplification, formality and
    neutralization with one 770M model — four transform types, one download."""

    model_name = "grammarly/coedit-large"


@register
class GrammarCorrection(_CoEdit):
    name = "grammar_correct"
    category = "grammar"
    prompt_template = "Fix grammatical errors in this sentence: {sentence}"


@register
class Simplification(_CoEdit):
    name = "simplify"
    category = "simplification"
    prompt_template = "Rewrite this sentence to make it easier to understand: {sentence}"


@register
class Formalization(_CoEdit):
    name = "formalize"
    category = "style"
    prompt_template = "Write this more formally: {sentence}"


@register
class Neutralization(_CoEdit):
    name = "neutralize"
    category = "style"
    prompt_template = "Remove all biased or subjective language from this sentence: {sentence}"


@register
class RoundTripTranslation(MetamorphicRelation):
    """EN -> pivot -> EN via MarianMT (~300M each way, CPU-feasible). Central to
    the non-native-writer / translation-laundering story."""

    name = "roundtrip_fr"
    category = "translation"
    pivot = "fr"

    def apply(self, text: str, rng: np.random.Generator) -> str:
        sentences = _split_sentences(text)
        if not sentences:
            return text
        forward = _generate(f"Helsinki-NLP/opus-mt-en-{self.pivot}", sentences)
        back = _generate(f"Helsinki-NLP/opus-mt-{self.pivot}-en", forward)
        return " ".join(back)

    def params(self) -> dict:
        return {"pivot": self.pivot}


@register
class RoundTripTranslationDE(RoundTripTranslation):
    name = "roundtrip_de"
    pivot = "de"


@register
class RoundTripTranslationZH(RoundTripTranslation):
    name = "roundtrip_zh"
    pivot = "zh"


@register
class Summarization(MetamorphicRelation):
    name = "summarize"
    category = "compression"
    semantics_lossy = True  # exists to stress the QAES machinery
    model_name = "sshleifer/distilbart-cnn-12-6"

    def apply(self, text: str, rng: np.random.Generator) -> str:
        return _generate(self.model_name, [text], max_new_tokens=142)[0]

    def params(self) -> dict:
        return {"model": self.model_name}
