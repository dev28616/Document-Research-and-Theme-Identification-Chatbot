import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextChunkIndexer:
    def __init__(self, model_name="all-MiniLM-L6-v2", chunk_size=500, chunk_overlap=100):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        self.model = SentenceTransformer(model_name)
        self.index = 0
        self.docs = []

    def split_and_embed(self, text, metadata=None):
        chunks = self.text_splitter.split_text(text)
        if not chunks:
            print(f"⚠️ No chunks found for: {metadata}")
            return

        embeddings = self.model.encode(chunks, convert_to_numpy=True)
        self.docs.extend([(chunk, {"metadata": metadata, "chunk": chunk}) for chunk in chunks])

        if self.index is 0:
            self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)


    def search(self, query, top_k=5):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)
        return [self.docs[i] for i in indices[0]]

    def save(self, path="faiss_index.pkl"):
        faiss.write_index(self.index, "faiss.index")
        with open("faiss_docs.pkl", "wb") as f:
            pickle.dump(self.docs, f)

    def load(self, path="faiss.index"):
        self.index = faiss.read_index("faiss.index")
        with open("faiss_docs.pkl", "rb") as f:
            self.docs = pickle.load(f)

