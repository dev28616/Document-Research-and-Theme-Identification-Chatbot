# 📁 File: app.py
# Description: Streamlit-based web interface for uploading documents, asking questions, and viewing answers

import streamlit as st
from extract_text import extract_text
from text_splitter_embedder import split_text, embed_chunks, save_index
from search_query import query_index
import os
import tempfile

st.set_page_config(page_title="📚 AI Document Q&A", layout="wide")
st.title("📚 AI-Powered Document Chatbot")
st.markdown("Upload PDFs/images, ask questions, and explore summarized answers with citations.")

# --- File Upload ---
uploaded_files = st.file_uploader("📤 Upload your documents (PDF, image, text)", type=["pdf", "png", "jpg", "jpeg", "txt"], accept_multiple_files=True)

# --- Upload Button ---
if st.button("🧠 Process Documents") and uploaded_files:
    all_text = ""

    with st.spinner("🔍 Extracting & indexing text from uploaded documents..."):
        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(file.read())
                tmp_path = tmp_file.name
                text = extract_text(tmp_path)
                all_text += f"\n{text}"
                os.unlink(tmp_path)  # Cleanup temp file

        # Chunk + Embed + Store
        chunks = split_text(all_text)
        index = embed_chunks(chunks)
        save_index(index)

    st.success("✅ Documents processed and indexed successfully!")

# --- Q&A Section ---
st.markdown("---")
st.subheader("❓ Ask a Question")
query = st.text_input("Enter your question below")

if st.button("🔎 Search") and query:
    try:
        results = query_index(query)

        st.markdown("### 📄 Top Relevant Passages")
        for i, doc in enumerate(results, 1):
            with st.expander(f"Result {i}"):
                st.write(doc.page_content)

    except Exception as e:
        st.error(f"Error: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ for Wasserstoff AI Internship Task")
