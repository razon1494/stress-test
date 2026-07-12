"""Character/token-level perturbations (category H). Pure Python, zero cost.

These are the 'cheap adversarial' attacks; several are trivially defeated by
Unicode normalization, so every experiment must run with and without the
normalization-preprocessing ablation (see docs/related_work.md, claim 5).
"""

from __future__ import annotations

import re

import numpy as np

from stress_test.transforms.base import MetamorphicRelation, register

# Latin -> visually-identical Cyrillic codepoints
HOMOGLYPHS = {
    "a": "а", "c": "с", "e": "е", "i": "і", "o": "о",
    "p": "р", "x": "х", "y": "у",
    "A": "А", "B": "В", "C": "С", "E": "Е", "H": "Н",
    "K": "К", "M": "М", "O": "О", "P": "Р", "T": "Т",
    "X": "Х",
}

CONTRACTIONS = {
    "aren't": "are not", "can't": "cannot", "couldn't": "could not",
    "didn't": "did not", "doesn't": "does not", "don't": "do not",
    "hasn't": "has not", "haven't": "have not", "he's": "he is",
    "i'm": "i am", "isn't": "is not", "it's": "it is", "let's": "let us",
    "she's": "she is", "shouldn't": "should not", "that's": "that is",
    "there's": "there is", "they're": "they are", "wasn't": "was not",
    "we're": "we are", "weren't": "were not", "what's": "what is",
    "won't": "will not", "wouldn't": "would not", "you're": "you are",
}


@register
class HomoglyphSubstitution(MetamorphicRelation):
    name = "homoglyph"
    category = "perturbation"

    def __init__(self, rate: float = 0.03):
        self.rate = rate

    def apply(self, text: str, rng: np.random.Generator) -> str:
        chars = list(text)
        for i, ch in enumerate(chars):
            if ch in HOMOGLYPHS and rng.random() < self.rate:
                chars[i] = HOMOGLYPHS[ch]
        return "".join(chars)

    def params(self) -> dict:
        return {"rate": self.rate}


@register
class ZeroWidthInsertion(MetamorphicRelation):
    name = "zero_width"
    category = "perturbation"

    def __init__(self, rate: float = 0.02):
        self.rate = rate

    def apply(self, text: str, rng: np.random.Generator) -> str:
        out = []
        for ch in text:
            out.append(ch)
            if ch.isalpha() and rng.random() < self.rate:
                out.append("​")
        return "".join(out)

    def params(self) -> dict:
        return {"rate": self.rate}


@register
class TypoInjection(MetamorphicRelation):
    name = "typo"
    category = "perturbation"

    def __init__(self, word_rate: float = 0.05):
        self.word_rate = word_rate

    def apply(self, text: str, rng: np.random.Generator) -> str:
        words = text.split(" ")
        for i, word in enumerate(words):
            if len(word) < 4 or rng.random() >= self.word_rate:
                continue
            j = int(rng.integers(1, len(word) - 1))
            op = rng.choice(["swap", "drop", "double"])
            if op == "swap":
                words[i] = word[:j] + word[j + 1] + word[j] + word[j + 2:]
            elif op == "drop":
                words[i] = word[:j] + word[j + 1:]
            else:
                words[i] = word[:j] + word[j] + word[j:]
        return " ".join(words)

    def params(self) -> dict:
        return {"word_rate": self.word_rate}


@register
class CaseNoise(MetamorphicRelation):
    name = "case_noise"
    category = "perturbation"

    def __init__(self, rate: float = 0.02):
        self.rate = rate

    def apply(self, text: str, rng: np.random.Generator) -> str:
        return "".join(
            ch.swapcase() if ch.isalpha() and rng.random() < self.rate else ch
            for ch in text
        )

    def params(self) -> dict:
        return {"rate": self.rate}


@register
class ContractionExpansion(MetamorphicRelation):
    name = "contraction_expand"
    category = "perturbation"

    def apply(self, text: str, rng: np.random.Generator) -> str:
        def repl(match: re.Match) -> str:
            found = match.group(0)
            expanded = CONTRACTIONS[found.lower()]
            if found[0].isupper():
                expanded = expanded[0].upper() + expanded[1:]
            return expanded

        pattern = re.compile(
            r"\b(" + "|".join(re.escape(c) for c in CONTRACTIONS) + r")\b",
            re.IGNORECASE,
        )
        return pattern.sub(repl, text)


@register
class WhitespaceNoise(MetamorphicRelation):
    name = "whitespace_noise"
    category = "perturbation"

    def __init__(self, rate: float = 0.03):
        self.rate = rate

    def apply(self, text: str, rng: np.random.Generator) -> str:
        return re.sub(
            r" ", lambda m: "  " if rng.random() < self.rate else " ", text
        )

    def params(self) -> dict:
        return {"rate": self.rate}


def normalize(text: str) -> str:
    """Defense-side preprocessing: undoes the cheap perturbations. Used in the
    normalization ablation to separate trivial from real robustness failures."""
    import unicodedata

    text = unicodedata.normalize("NFKC", text)
    reverse = {v: k for k, v in HOMOGLYPHS.items()}
    text = "".join(reverse.get(ch, ch) for ch in text)
    text = text.replace("​", "")
    return re.sub(r" {2,}", " ", text)
