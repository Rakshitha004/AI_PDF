# pipeline.py

from core.pdf_loader import extract_text_from_pdf
from core.kv_extractor import guess_key_value
from core.comments_extractor import generate_comment
from core.excel_writer import write_rows_to_excel
from core.text_preprocessor import preprocess_text

def run_pipeline(pdf_path, output_path):
    # 1. Extract text
    raw_text = extract_text_from_pdf(pdf_path)

    # 2. Clean + split into lines/sentences
    sentences = preprocess_text(raw_text)

    rows = []

    # 3. Process each line
    for s in sentences:
        key, value = guess_key_value(s)
        comment = generate_comment(key, value, s)  # pass original line

        rows.append({
            "Key": key,
            "Value": value,
            "Comments": comment
        })

    # 4. Save Excel
    write_rows_to_excel(rows, output_path)
# pipeline.py

from core.pdf_loader import extract_text_from_pdf
from core.kv_extractor import guess_key_value
from core.comments_extractor import generate_comment
from core.excel_writer import write_rows_to_excel
from core.text_preprocessor import preprocess_text

def run_pipeline(pdf_path, output_path):
    # 1. Extract text
    raw_text = extract_text_from_pdf(pdf_path)

    # 2. Clean + split into lines/sentences
    sentences = preprocess_text(raw_text)

    rows = []

    # 3. Process each line
    for s in sentences:
        key, value = guess_key_value(s)
        comment = generate_comment(key, value, s)  # pass original line

        rows.append({
            "Key": key,
            "Value": value,
            "Comments": comment
        })

    # 4. Save Excel
    write_rows_to_excel(rows, output_path)




