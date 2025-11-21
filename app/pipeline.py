import os
from app.core.pdf_loader import extract_text_from_pdf
from app.core.text_preprocessor import preprocess_text
from app.core.kv_extractor import convert_sentences_to_rows
from app.core.excel_writer import write_rows_to_excel

def run_pipeline(pdf_path: str, output_path: str):
    """
    Full end-to-end pipeline:
    1. Load PDF
    2. Extract raw text
    3. Preprocess → sentences
    4. Convert each sentence to Key / Value / Comments
    5. Write Excel to output
    """

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at: {pdf_path}")

    print("🔍 Extracting text from PDF...")
    raw_text = extract_text_from_pdf(pdf_path)

    print("🧹 Preprocessing text...")
    sentences = preprocess_text(raw_text)

    print("🔑 Converting sentences to key-value-comments...")
    rows = convert_sentences_to_rows(sentences)

    print("📄 Writing output Excel...")
    write_rows_to_excel(rows, output_path)

    print(f"✅ Pipeline complete! Excel saved at: {output_path}")
