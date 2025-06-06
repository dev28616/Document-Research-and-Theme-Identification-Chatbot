# backend/app/models/schema.py
from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    answer: str
    themes: str
    sources: List[str]
    citations: List[str]
