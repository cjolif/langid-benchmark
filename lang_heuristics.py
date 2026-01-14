import re
from collections import defaultdict

LANGS = ["en", "fr", "it", "de", "es"]

STRONG_ACCENT_MARKERS = {
    "es": ["ñ", "¿", "¡", "ó", "¿", "á"],
    "de": ["ß", "ä", "ö", "ü"],
    "fr": ["ç", "œ", "è", "ê", "à", "û" ],
    "it": [],
    "en": [],
}

SUBSTRINGS = {
    "en": ["the", "ing", "tion", "th", "and", "ow"],
    "fr": ["que", "tion", "ment", "est", "pour"],
    "it": ["zione", "gli", "che", "lla", "mente"],
    "de": ["sch", "ung", "ein", "nicht", "lich"],
    "es": ["que", "ción", "mente", "para", "esta", "este"],
}

STOP_WORDS = {
    "en": ["the", "and", "is", "of", "to"],
    "fr": ["le", "la", "les", "des", "est", "pour", "au", "avec", "et", "ou"],
    "it": ["il", "lo", "la", "che", "per", "del"],
    "de": ["der", "die", "das", "und", "nicht"],
    "es": ["el", "la", "los", "que", "para", "del", "y"],
}

def normalize(text: str) -> str:
    return re.sub(r"[^\wàâäçéèêëîïñôöùûüßœ]", " ", text.lower())

def detect_language(text: str) -> str:
    text = normalize(text)
    scores = defaultdict(int)

    # 1. Strong accent markers (very high confidence)
    for lang, markers in STRONG_ACCENT_MARKERS.items():
        for m in markers:
            if m in text:
                scores[lang] += 5

    # 2. Substring patterns
    for lang, patterns in SUBSTRINGS.items():
        for p in patterns:
            if p in text:
                scores[lang] += 2

    # 3. Stop_words
    tokens = text.split()
    for lang, words in STOP_WORDS.items():
        for w in words:
            scores[lang] += tokens.count(w)

    # 4. We don't know
    if not scores:
        return "unknown"

    return max(scores, key=scores.get)
