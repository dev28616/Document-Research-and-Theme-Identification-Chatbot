import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.services.search_query import query_index_with_themes
from fastapi import File, UploadFile
from backend.app.services.extract_text import extract_text
from backend.app.services.text_splitter_embedder import TextChunkIndexer
from pathlib import Path
from backend.app.models.schema import QueryRequest, QueryResponse


router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    result = query_index_with_themes(request.query)
    return QueryResponse(
        query=request.query,
        answer=result["answer"],
        themes=result["themes"],
        sources=result.get("sources", []),
        citations=result.get("citations", [])
    )





UPLOAD_DIR = Path("../../../data")
UPLOAD_DIR.mkdir(exist_ok=True)

upload_indexer = TextChunkIndexer()
upload_indexer.load("C:/Users/monda/OneDrive/Desktop/ChatBot_Theme_Identifier/backend/app/services/faiss_index.pkl")  # Load existing index

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    content = await file.read()
    file_path.write_bytes(content)

    try:
        extracted_text = extract_text(str(file_path))
        if not extracted_text.strip():
            return {"status": "failed", "reason": "No text found in file."}

        upload_indexer.split_and_embed(extracted_text, metadata={"filename": file.filename})
        upload_indexer.save("C:/Users/monda/OneDrive/Desktop/ChatBot_Theme_Identifier/backend/app/services/faiss_index.pkl")

        return {"status": "success", "filename": file.filename}
    except Exception as e:
        return {"status": "failed", "reason": str(e)}
