from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from app.vectordb import get_vector_db
from app.config import LLM_MODEL, OLLAMA_BASE_URL




def get_rag_chain():
    llm = ChatOllama(
    model=LLM_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=0
    )


    vectordb = get_vector_db()


    return RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(search_kwargs={"k": 4}),
    return_source_documents=True
    )