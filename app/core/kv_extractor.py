import re

COMMON_FIELDS = [
    "Name", "First Name", "Last Name", "Age", "Gender", "Date of Birth", "DOB",
    "Blood Group", "City", "State", "Nationality", "Email", "Phone",
    "Address", "Experience", "Education", "Degree", "Graduation Year",
    "Company", "Position", "Salary", "Certification"
]

def guess_key_value(line):
    line = line.strip()

    # Case 1: "Key: Value"
    match = re.match(r"(.+?)\s*[:\-]\s*(.+)", line)
    if match:
        return match.group(1).strip(), match.group(2).strip()

    # Case 2: Try matching known fields at start
    for f in COMMON_FIELDS:
        if line.lower().startswith(f.lower()):
            return f, line[len(f):].strip(" :-")

    # Case 3: Try pattern like "Born on XX"
    dob_match = re.search(r"\b\d{1,2}-\w{3}-\d{2,4}\b", line)
    if dob_match:
        return "Date of Birth", dob_match.group()

    # Case 4: No key–value found
    return "", line
