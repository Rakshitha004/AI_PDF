import nltk
import re

def preprocess_text(raw):
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)

    # Remove junk chars
    cleaned = re.sub(r"\s+", " ", raw)

    # Smart sentence splitter
    sentences = nltk.sent_tokenize(cleaned)

    # Each sentence = one line for extraction
    return [s.strip() for s in sentences if len(s.strip()) > 2]

