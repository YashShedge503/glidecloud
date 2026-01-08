import chromadb
from langchain_community.vectorstores import Chroma
from app.config import CHROMA_PERSIST_DIR
from app.embeddings import get_embedding_function

def get_vector_db():
    embedding = get_embedding_function()


    return Chroma(
        persist_directory=CHROMA_PERSIST_DIR,
        embedding_function=embedding,
        collection_name="rag_collection"
    )