import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from fastapi import FastAPI
from backend.app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Theme Identifier API")

app.include_router(router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
