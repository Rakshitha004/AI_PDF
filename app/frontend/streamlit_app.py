import streamlit as st
import requests
import base64

API_URL = "http://127.0.0.1:8000/process-pdf"

# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="AI PDF → Excel Structurer",
    page_icon="📄",
    layout="wide"
)

# ----- CUSTOM CSS -----
st.markdown("""
    <style>
        .main-container {
            background-color: #f8f9fa;
            padding: 40px 80px;
            border-radius: 12px;
            box-shadow: 0px 0px 12px rgba(0,0,0,0.08);
        }
        .title {
            font-size: 38px !important;
            font-weight: 700 !important;
            text-align: center;
            color: #222;
        }
        .sub-text {
            text-align: center;
            font-size: 17px;
            color: #555;
        }
        .status-box {
            padding: 15px 20px;
            background: #eef2ff;
            border-left: 5px solid #4f46e5;
            font-size: 16px;
            border-radius: 6px;
            margin-top: 20px;
        }
        .success-box {
            padding: 15px 20px;
            background: #e8fce8;
            border-left: 5px solid #16a34a;
            font-size: 16px;
            border-radius: 6px;
            margin-top: 20px;
        }
        .error-box {
            padding: 15px 20px;
            background: #fde8e8;
            border-left: 5px solid #dc2626;
            font-size: 16px;
            border-radius: 6px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ----- UI -----
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("<div class='title'>📄 AI PDF → Structured Excel Generator</div>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Upload any PDF and get a clean, structured Excel output instantly.</p>", unsafe_allow_html=True)

uploaded_pdf = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_pdf:
    st.markdown("<div class='status-box'>🔍 Processing your document...</div>", unsafe_allow_html=True)

    files = {"file": (uploaded_pdf.name, uploaded_pdf, "application/pdf")}

    try:
        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            # Success
            excel_bytes = response.content

            st.markdown("<div class='success-box'>✅ Excel generated successfully!</div>", unsafe_allow_html=True)

            # Download button
            st.download_button(
                label="⬇️ Download Excel File",
                data=excel_bytes,
                file_name="output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.markdown(
                f"<div class='error-box'>❌ Error: {response.text}</div>",
                unsafe_allow_html=True
            )

    except Exception as e:
        st.markdown(
            f"<div class='error-box'>⚠️ Connection Error: {str(e)}</div>",
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)
