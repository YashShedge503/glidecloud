from app.loader import load_and_split_pdfs
from app.vectordb import get_vector_db
from app.config import PDF_DIR




def ingest():
    docs = load_and_split_pdfs(PDF_DIR)
    vectordb = get_vector_db()
    vectordb.add_documents(docs)
    vectordb.persist()


if __name__ == "__main__":
    ingest()