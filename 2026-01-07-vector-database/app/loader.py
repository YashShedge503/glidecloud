from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os




def load_and_split_pdfs(pdf_dir):
    documents = []


    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_dir, file))
            documents.extend(loader.load())


        splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
        )


    return splitter.split_documents(documents)