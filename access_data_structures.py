"""
Run this script using Python 3. Make sure the following packages are installed:
pip install pandas requests PyPDF2

Save the three files in the same directory:
- JSON: 2017 Current Population Survey Civic Engagement and Volunteering Supplement.json
- PDF: 2023 Current Population Survey Civic Engagement and Volunteering.pdf

CSV is accessed via HTTP URL.
"""

# JSON Access - Manual File Load
import json

def load_json_file():
    """
    PROS:
    - Simple and fast to read.
    - Works offline once downloaded.

    CONS:
    - Must manually download and maintain the file.
    """
    with open('2017 Current Population Survey Civic Engagement and Volunteering Supplement.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    print("Sample from JSON:")
    print(list(data.items())[:2])  # print first 2 key-value pairs

# CSV Access - HTTP Download Simulation
import pandas as pd
import io
import requests

def load_csv_http():
    """
    PROS:
    - Can automate data fetching from online sources.
    - Reproducible if URLs are stable.

    CONS:
    - Needs internet connection.
    - May break if URL or format changes.
    """
    url = "https://data.americorps.gov/api/views/twy4-5nxu/rows.csv?accessType=DOWNLOAD"
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text))
    print("Sample from CSV:")
    print(df.head(2))  # show top 2 rows

# PDF Access - Local File Load
import PyPDF2

def load_pdf_file():
    """
    PROS:
    - Great for structured reports and official documents.
    - Easy to archive or share.

    CONS:
    - Hard to extract structured data.
    - Not suitable for automated processing or analysis.
    """
    with open("2023 Current Population Survey Civic Engagement and Volunteering.pdf", "rb") as file:
        reader = PyPDF2.PdfReader(file)
        print("Sample from PDF:")
        print(reader.pages[0].extract_text()[:500])  # first 500 characters from page 1

# Run all functions
if __name__ == "__main__":
    load_json_file()
    load_csv_http()
    load_pdf_file()
