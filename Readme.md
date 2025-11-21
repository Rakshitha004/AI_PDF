🌟 AI PDF → Structured Excel Generator
Transform any PDF into a clean, structured Excel file — automatically.
<p align="center"> <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/FastAPI-Backend-teal?style=for-the-badge"> <img src="https://img.shields.io/badge/Streamlit-Frontend-ff4b4b?style=for-the-badge"> <img src="https://img.shields.io/badge/Excel-Automation-success?style=for-the-badge"> </p> <p align="center"> <b>A modern, modular, and scalable system for extracting structured data from PDFs.</b><br> Upload → Extract → Transform → Download Excel — all in seconds ⚡ </p>
-----
📘 Overview
This project converts ANY text-based PDF into a structured Excel sheet containing:
Field Name
Extracted Value
Comments / AI-generated insights
It uses a well-defined NLP pipeline, FastAPI backend for processing, and Streamlit frontend for the user interface.
-----
🚀 Features
🔹 Upload ANY PDF
Works with resumes, profiles, business docs, academic content, and more.
🔹 Fully Automated NLP Pipeline
PDF → Raw Text
Text → Cleaned Sentences
Sentences → Key–Value Extraction
Key–Value → Excel Rows
🔹 Frontend + Backend Architecture
Streamlit UI for user interaction
FastAPI for processing
Modular Python pipeline under the hood

| Layer          | Technology                 |
| -------------- | -------------------------- |
| Frontend       | 🎨 Streamlit               |
| Backend        | ⚡ FastAPI                  |
| PDF Processing | 📄 pdfplumber              |
| NLP            | 🧠 NLTK                    |
| Excel Writer   | 📊 OpenPyXL / Pandas       |
| Architecture   | 🧩 Modular Python pipeline |



⚙️ Installation
1️⃣ Clone the Repository:git clone https://github.com/Rakshitha004/AI_PDF.git
cd AI_PDF
2️⃣ Install Dependencies:pip install -r requirements.txt
3️⃣ Download NLTK Data:import nltk
nltk.download("punkt")
nltk.download("punkt_tab")


🔹 Professional Excel Output

Including row numbering, aligned columns, and clean headers.

Streamlit Cloud:1)	https://ai-pdf-tool.streamlit.app/
