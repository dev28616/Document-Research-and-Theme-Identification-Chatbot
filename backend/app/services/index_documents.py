import os
from pathlib import Path
import sys
import pytesseract

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from backend.app.services.extract_text import extract_text
from backend.app.services.text_splitter_embedder import TextChunkIndexer


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Setup
indexer = TextChunkIndexer()

# All files inside /data
data_dir = Path("../../../data")
all_files = list(data_dir.glob("*"))

for file_path in all_files:
    try:
        print(f"\n Processing: {file_path.name}")
        text = extract_text(str(file_path))

        if not text.strip():
            print(f" Skipped {file_path.name}: No text extracted.")
            continue

        indexer.split_and_embed(text, metadata={"filename": file_path.name})
        print(f" Indexed: {file_path.name}")

    except Exception as e:
        print(f" Error with {file_path.name}: {e}")

# Save final index
indexer.save("C:/Users/monda/OneDrive/Desktop/ChatBot_Theme_Identifier/backend/app/services/faiss_index.pkl")
print("\n All valid documents indexed and saved.")

