import pdfplumber

def extract_text_from_pdf(pdf_file):
    """
    Extracts raw text from any PDF file.
    Works for multi-page PDFs.
    Returns a single string containing all text.
    """
    full_text = ""

    # Open PDF using pdfplumber
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            # Some PDFs may have empty pages or strange formatting
            if text:
                full_text += text + "\n"

    return full_text.strip()  # Final clean text
