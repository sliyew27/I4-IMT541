# Information Structures & Access Technologies Demo

This Python script demonstrates how to access three different types of information structures using different access technologies. It is designed to meet the requirements of an assignment asking for:

- Three different **information structures**: JSON, CSV, and PDF.
- Three different **access methods**: local file read, HTTP request, and PDF parsing.

---

## Files Used

- **JSON File (Local Load):**  
  `2017 Current Population Survey Civic Engagement and Volunteering Supplement.json`

- **CSV File (Access via HTTP):**  
  Accessed live from AmeriCorps:  
  https://data.americorps.gov/api/views/twy4-5nxu/rows.csv?accessType=DOWNLOAD

- **PDF File (Local Read):**  
  `2023 Current Population Survey Civic Engagement and Volunteering.pdf`

---

## How to Run

1. Make sure you have Python 3 installed.
2. Install required packages:

```bash
pip install pandas requests PyPDF2
```

3. Run the script:

```bash
python access_data_structures.py
```

Make sure the JSON and PDF files are in the same folder as the script.

---

## What Each Section Does

### JSON (Local Load)

- Loads a `.json` file stored locally.
- **Pros:** Fast, easy to use offline.
- **Cons:** Requires you to manually maintain the file.

### CSV (HTTP Access)

- Downloads a `.csv` from a live URL using `requests` and reads it with `pandas`.
- **Pros:** Automated, always gets current data.
- **Cons:** Depends on internet and URL staying the same.

### PDF (Local Load)

- Reads a `.pdf` using `PyPDF2` and extracts the first page of text.
- **Pros:** Good for reading official documents.
- **Cons:** Hard to analyze; not structured like CSV or JSON.

---

## File List

- `access_data_structures.py` — the main Python script
- `README.md` — this file

---

## Notes

This project is a simple demonstration and does not require editing the data — only accessing it. Each method is explained in comments within the code.
