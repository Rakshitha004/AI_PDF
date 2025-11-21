from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os
from app.pipeline import run_pipeline

app = FastAPI(title="AI PDF → Excel Structuring API")

# Temporary directories for API
UPLOAD_DIR = "data/input/"
OUTPUT_DIR = "data/output/"

# Create folders safely
for folder in [UPLOAD_DIR, OUTPUT_DIR]:
    # If a FILE exists in place of a folder, delete it
    if os.path.isfile(folder):
        os.remove(folder)

    # If directory doesn't exist, create it
    if not os.path.isdir(folder):
        os.makedirs(folder)



@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    """
    Accepts a PDF upload,
    saves it temporarily,
    runs the pipeline,
    and returns the generated Excel file.
    """

    # Save uploaded PDF
    input_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = os.path.join(OUTPUT_DIR, "output.xlsx")

    # Run your extraction → preprocessing → key:value → Excel pipeline
    run_pipeline(input_path, output_path)

    # Return the generated Excel
    return FileResponse(
        output_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="output.xlsx"
    )
