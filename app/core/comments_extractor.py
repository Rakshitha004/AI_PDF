# comments_extractor.py

def generate_comment(key, value, original_line):
    """
    Generates an intelligent comment for each extracted field.
    Handles unknown or poorly extracted lines gracefully.
    """

    # 1. If key & value detected properly
    if key and value:
        return f"Extracted '{key}' with the value '{value}' from the document."

    # 2. If only key detected
    if key and not value:
        return f"Detected the field '{key}', but the detailed value was unclear in the source line."

    # 3. If only value detected
    if value and not key:
        return f"A value '{value}' was found, but no clear field name was detected."

    # 4. If nothing detected → return raw text comment
    return f"Could not map this line effectively: '{original_line}'. Included for review."

