import re

def extract_key_value(sentence: str):
    """
    Generic Key-Value extraction.
    Works for ANY PDF because:
    - It uses common language patterns
    - Falls back to storing full sentence as value if no key found
    """

    original = sentence.strip()

    # Common patterns like:
    # "He was born on...", "His age is...", "He joined as...", "He scored..."
    patterns = [
        r'(.+?) was born on (.+)', 
        r'(.+?) is (.+)',
        r'(.+?) was (.+)',
        r'(.+?) are (.+)',
        r'(.+?) were (.+)',
        r'(.+?) has (.+)',
        r'(.+?) have (.+)',
        r'(.+?) includes (.+)',
        r'(.+?) earned (.+)',
        r'(.+?) achieved (.+)',
        r'(.+?) joined (.+)'
    ]

    for pattern in patterns:
        match = re.match(pattern, sentence, re.IGNORECASE)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            return key, value, original

    # If sentence contains a colon → strong indicator of key-value
    if ":" in sentence:
        parts = sentence.split(":", 1)
        key = parts[0].strip()
        value = parts[1].strip()
        return key, value, original

    # Default fallback: treat entire sentence as value
    return "Information", original, original


def convert_sentences_to_rows(sentences):
    """
    Convert list of sentences into rows:
    Key, Value, Comments
    Always preserves original text.
    """

    rows = []

    for sent in sentences:
        key, value, comments = extract_key_value(sent)
        rows.append({
            "Key": key,
            "Value": value,
            "Comments": comments
        })

    return rows
