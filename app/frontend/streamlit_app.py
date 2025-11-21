import streamlit as st
import pdfplumber
import pandas as pd
import nltk
import io
import re

# NLTK requirements
nltk.download("punkt")
nltk.download("punkt_tab")


# ------------------------------------------
# 1. PDF → TEXT
# ------------------------------------------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


# ------------------------------------------
# 2. CLEAN TEXT + SPLIT SENTENCES
# ------------------------------------------
def preprocess_text(text):
    text = re.sub(r"\s+", " ", text).strip()
    sentences = nltk.sent_tokenize(text)
    return sentences


# ------------------------------------------
# 3. EXTRACT KEY–VALUE FROM SENTENCE
# Very simple placeholder logic (customize later)
# ------------------------------------------
def extract_kv(sentence):
    if ":" in sentence:
        key, value = sentence.split(":", 1)
        return key.strip(), value.strip(), ""
    return sentence, "", ""


# ------------------------------------------
# 4. BUILD EXCEL FILE
# ------------------------------------------
def build_excel(rows):
    df = pd.DataFrame(rows, columns=["Field Name", "Extracted Value", "Comments"])
    df.index += 1
    df.index.name = "#"

    output = io.BytesIO()
    df.to_excel(output, engine="openpyxl")
    return output.getvalue()


# ------------------------------------------
# STREAMLIT UI
# ------------------------------------------
st.set_page_config(page_title="AI PDF → Excel", page_icon="📄")

st.title("📄 AI PDF → Structured Excel Generator")
st.write("Upload a PDF and get a clean Excel sheet instantly.")

uploaded_pdf = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_pdf:

    st.info("Processing your document...")

    # PDF → text
    raw_text = extract_text_from_pdf(uploaded_pdf)

    # text → sentences
    sentences = preprocess_text(raw_text)

    # extract KV pairs
    rows = [extract_kv(s) for s in sentences]

    # build excel
    excel_file = build_excel(rows)

    st.success("Excel generated successfully!")

    st.download_button(
        label="⬇️ Download Excel",
        data=excel_file,
        file_name="output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

