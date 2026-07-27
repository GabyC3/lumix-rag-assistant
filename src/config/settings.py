import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DOCUMENTS_PATH = PROJECT_ROOT / "data" / "documents"

VECTOR_DB_PATH = PROJECT_ROOT / "data" / "vector_db"

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-3.5-flash-lite"

TOP_K = 4