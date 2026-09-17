import re


def clean_text(text: str) -> str:
    """Basic normalization while preserving useful message words."""
    text = str(text).lower()
    text = re.sub(r"http\S+|www\.\S+", " URL ", text)
    text = re.sub(r"\d+", " NUMBER ", text)
    text = re.sub(r"[^a-zA-Z_ ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
