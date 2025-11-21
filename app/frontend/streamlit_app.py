import streamlit as st
import os
import tempfile
import sys

root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(root)

from pipeline import run_pipeline

st.set_page_config(page_title="AI PDF Extractor", layout="wide")

st.title("📄 AI PDF → Excel Extractor")

uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_pdf:
    st.info("Processing your PDF... ⏳")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_pdf.read())
        pdf_path = tmp.name

    output_path = os.path.join(tempfile.gettempdir(), "Extracted_Output.xlsx")

    run_pipeline(pdf_path, output_path)

    st.success("Done! Download below 👇")

    with open(output_path, "rb") as f:
        st.download_button("📥 Download Excel", f, "Extracted_Output.xlsx")


