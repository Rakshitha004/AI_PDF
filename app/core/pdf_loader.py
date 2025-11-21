import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from ANY PDF file in the cleanest possible way.
    Handles:
    - multi-page PDFs
    - broken lines
    - hyphenated text
    - weird spacing
    - unicode issues
    """

    final_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            raw = page.extract_text() or ""
            final_text += "\n" + raw

    # Cleaning unwanted characters
    final_text = final_text.replace("­", "")   # soft hyphen
    final_text = final_text.replace("-\n", "") # broken words
    final_text = final_text.replace("\xa0", " ") # weird spaces

    # Strip extra blank lines
    cleaned_lines = []
    for line in final_text.split("\n"):
        stripped = line.strip()
        if stripped:
            cleaned_lines.append(stripped)

    return "\n".join(cleaned_lines)

