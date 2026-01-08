from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from app.vectordb import get_vector_db
from app.config import LLM_MODEL, OLLAMA_BASE_URL


def get_rag_chain():
    # 1. LLM
    llm = ChatOllama(
        model=LLM_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0
    )

    # 2. Retriever
    retriever = get_vector_db().as_retriever(search_kwargs={"k": 4})

    # 3. Prompt
    prompt = ChatPromptTemplate.from_template("""
    Answer the question using ONLY the context below.
    If the answer is not present, say you don't know.

    Context:
    {context}

    Question:
    {question}
    """)

    # 4. Modern LCEL RAG chain (NO langchain.chains)
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
    )

    return rag_chain
