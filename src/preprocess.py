import re
import emoji

SHENG_MAP = {
    "fiti": "nzuri",
    "poa": "nzuri",
    "imetesa": "nzuri sana",
    "imeharibika": "imevunjika",
    "pesa": "fedha",
    "fast": "haraka",
    "chelewa": "kuchelewa",
    "conman": "tapeli",
    "scam": "tapeli"
}

def clean_review(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = emoji.demojize(text, delimiters=(" ", " "))
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    words = text.split()
    normalized_words = [SHENG_MAP.get(word, word) for word in words]
    return " ".join(normalized_words)
