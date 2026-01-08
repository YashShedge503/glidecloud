from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def load_and_split_pdfs(pdf_dir):
    documents = []
    
    # Check if directory exists
    if not os.path.exists(pdf_dir):
        print(f"Error: Directory '{pdf_dir}' not found.")
        return []

    print(f"Loading PDFs from {pdf_dir}...")
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            file_path = os.path.join(pdf_dir, file)
            print(f" - Processing: {file}")
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

    # Create splitter once
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    print(f"Splitting {len(documents)} pages into chunks...")
    return splitter.split_documents(documents)