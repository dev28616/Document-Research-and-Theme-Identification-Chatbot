import os
import sys
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from dotenv import load_dotenv
from langchain.docstore.document import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from backend.app.services.text_splitter_embedder import TextChunkIndexer
from backend.app.services.theme_identifier import summarize_themes

load_dotenv()

# -----------------------------
# Path Configuration
# -----------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../..'))

data_file_path = os.path.join(project_root, "data", "virat.txt")
index_file_path = os.path.join(current_dir, "faiss_index.pkl")

# -----------------------------
# Load or Build Index
# -----------------------------
indexer = TextChunkIndexer()

if not os.path.exists(index_file_path):
    print("[ℹ️] FAISS index not found. Building a new one from data/virat.txt...")
    if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"[❌] Data file not found at: {data_file_path}")

    with open(data_file_path, "r", encoding="utf-8") as f:
        text_data = f.read()

    indexer.split_and_embed(text_data, metadata={"filename": "virat.txt"})
    indexer.save(index_file_path)
    print("[✅] Index built and saved.")
else:
    print("[📁] Loading existing FAISS index.")
    indexer.load(index_file_path)

# -----------------------------
# Load Gemini LLM and Chain
# -----------------------------
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

qa_chain = load_qa_chain(gemini_llm, chain_type="stuff")

# -----------------------------
# Query Index (simple answer)
# -----------------------------
def query_index(query):
    results = indexer.search(query, top_k=5)

    documents = []
    for chunk, meta in results:
        metadata = meta.get("metadata", {})
        if isinstance(metadata, dict):
            source = metadata.get("filename", "Unknown")
        else:
            source = str(metadata)
        documents.append(Document(page_content=chunk, metadata={"source": source}))

    answer = qa_chain.run(input_documents=documents, question=query)
    return answer

# -----------------------------
# Query Index with Themes
# -----------------------------


def query_index_with_themes(query):
    indexer = TextChunkIndexer()
    indexer.load("C:/Users/monda/OneDrive/Desktop/ChatBot_Theme_Identifier/backend/app/services/faiss_index.pkl")

    results = indexer.search(query, top_k=6)
    if not results:
        return {
            "answer": "No relevant information found.",
            "themes": "No themes could be synthesized.",
            "sources": []
        }

    docs = []
    sources = set()

    for chunk, meta in results:
        filename = meta["metadata"].get("filename", "unknown")
        sources.add(filename)
        docs.append(Document(page_content=chunk, metadata=meta["metadata"]))

    answer = qa_chain.run(input_documents=docs, question=query)
    theme_summary = summarize_themes(results, query)

    return {
        "answer": answer,
        "themes": theme_summary,
        "sources": list(sources)  # 👈 add source documents used
    }


