import sys
import os


# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.services.text_splitter_embedder import TextChunkIndexer

text = """
The Securities and Exchange Board of India (SEBI) imposed a fine on the company under Section 15 of the SEBI Act.
Another document mentioned the company violated Clause 49 of the listing agreement.
"""

indexer = TextChunkIndexer()
indexer.split_and_embed(text, metadata={"source": "test-doc"})

results = indexer.search("SEBI fine", top_k=3)
print("\n🔍 Top Results for 'SEBI fine':\n")
for chunk, meta in results:
    print(f"→ {chunk}\n--- from {meta['source']}\n")
