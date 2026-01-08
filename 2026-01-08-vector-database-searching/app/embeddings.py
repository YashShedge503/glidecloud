from langchain_community.embeddings import OllamaEmbeddings
from app.config import EMBEDDING_MODEL, OLLAMA_BASE_URL


def get_embedding_function():
    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL
    )