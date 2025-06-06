import sys
import os
import pytesseract

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.services.extract_text import extract_text


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Test with sample files in data/
files = [
    "../data/Virat_Kohli_Bio.pdf",
    "../data/tree.jpg",
    "../data/virat.txt"
]

for file in files:
    print(f"\n--- {file} ---")
    try:
        content = extract_text(file)
        print(content[:300])  # Preview
    except Exception as e:
        print(f"Error: {e}")
