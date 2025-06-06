# 🧠 Gen-AI Document Theme Identifier Chatbot

## 🚀 Overview

This is a full-stack Gen-AI powered chatbot that:

- Ingests and processes 75+ documents (PDFs, images, text)
- Extracts answers from documents with paragraph-level citations
- Synthesizes themes across all retrieved content
- Presents results in a simple web UI (Streamlit)

Developed as part of the Wasserstoff Gen-AI Internship Task.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI
- **OCR:** Tesseract OCR (for scanned PDFs and images)
- **LLM:** Gemini 1.5 Flash via LangChain
- **Vector DB:** FAISS (with SentenceTransformers embeddings)
- **Text Parsing:** PyMuPDF, PIL

---

## 📁 Project Structure

```
CHATBOT_THEME_IDENTIFIER/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI routes
│   │   ├── core/         # Config files
│   │   ├── services/     # Embedding, OCR, QA, theme logic
│   │   └── main.py       # FastAPI app entry
│   ├── requirements.txt
├── data/                 # Uploaded documents
├── frontend/
│   └── streamlit_app.py  # UI app
├── scripts/              # Document indexing script
├── tests/                # Test files
├── demo/                 # Video or screenshots
├── .env
└── README.md             # You're here
```

---

## 💻 Setup Instructions

### 1. Install Requirements

```bash
pip install -r backend/requirements.txt
```

Also install Tesseract:

- **Windows:** [https://github.com/tesseract-ocr/tesseract/wiki](https://github.com/tesseract-ocr/tesseract/wiki)

### 2. Start Backend API

```bash
cd backend
uvicorn app.main:app --reload
```

### 3. Start Frontend App

```bash
cd frontend
streamlit run streamlit_app.py
```

---

## 📂 How to Use

### 📁 Upload Documents

- Upload PDFs, scanned images, or `.txt` files
- OCR + embedding is triggered automatically
- Documents are stored in `/data`

### ❓ Ask a Question

- Type your query in the input box
- Receive:
  - LLM Answer
  - Synthesized Theme(s)
  - Source Citations (filename + paragraph)

---

## ✨ Extra Features

- ✅ Paragraph-level citation (not just document/page)
- ✅ Document filtering in UI
- ✅ Realtime index update without restart
- ✅ Source document tracking

---

## 🎬 Demo Video

A sample walkthrough is available in the `/demo/` folder.


## 📩 Contact

**Submitted to:** Wasserstoff — Gen-AI Internship Task  
**By:** Debojyoti Mondal  
**Email:** [your-email@example.com]
