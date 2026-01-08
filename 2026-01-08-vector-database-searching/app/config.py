from dotenv import load_dotenv
import os


load_dotenv()


OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
LLM_MODEL = os.getenv("LLM_MODEL")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR")
PDF_DIR = os.getenv("PDF_DIR")