# backend/app/services/build_index.py

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from backend.app.services.text_splitter_embedder import TextChunkIndexer


# Load data from the data folder
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "virat.txt")
index_save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faiss_index.pkl")

with open(data_path, "r", encoding="utf-8") as f:
    text = f.read()

indexer = TextChunkIndexer()
indexer.split_and_embed(text, metadata="chatbot_corpus.txt")
indexer.save(index_save_path)

print(f"[✅] Index created and saved at {index_save_path}")
