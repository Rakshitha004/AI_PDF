import pandas as pd

def write_rows_to_excel(rows, output_path):
    """
    Converts extracted rows (list of dicts) into a clean Excel file.
    Excel columns:
        - #
        - Field Name
        - Extracted Value
        - Comments
    """

    # Convert to DataFrame
    df = pd.DataFrame(rows)

    # Rename columns to Option A headings
    df = df.rename(columns={
        "Key": "Field Name",
        "Value": "Extracted Value",
        "Comments": "Comments"
    })

    # Start numbering from 1 (expected output format)
    df.index += 1
    df.index.name = "#"

    # Save to Excel
    df.to_excel(output_path, engine="openpyxl")

