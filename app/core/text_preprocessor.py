import re
import nltk

# Download punkt tokenizer only once
nltk.download('punkt')

def clean_text(text: str) -> str:
    """
    Basic normalization of extracted text.
    Removes extra spaces, fixes line breaks, etc.
    """
    # Replace multiple spaces with one
    text = re.sub(r'\s+', ' ', text)
    
    # Replace weird line breaks
    text = text.replace("\n ", " ").replace(" \n", " ").replace("\n", " ")

    return text.strip()


def split_into_sentences(text: str):
    """
    Splits cleaned text into proper sentences.
    This uses NLTK's robust sentence tokenizer, suitable for ANY PDF content.
    """
    sentences = nltk.sent_tokenize(text)
    
    # Additional cleaning: remove empty sentences
    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences


def preprocess_text(raw_text: str):
    """
    Full preprocessing pipeline:
    - Clean raw text
    - Split into sentences
    Returns a list of clean, meaningful sentences.
    """
    cleaned = clean_text(raw_text)
    sentences = split_into_sentences(cleaned)
    return sentences
