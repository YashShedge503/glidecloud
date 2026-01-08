from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
# These imports require the 'langchain' package we just reinstalled
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from app.vectordb import get_vector_db
from app.config import LLM_MODEL, OLLAMA_BASE_URL

def get_rag_chain():
    # 1. Setup LLM
    llm = ChatOllama(
        model=LLM_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0
    )

    # 2. Setup Retriever
    retriever = get_vector_db().as_retriever(search_kwargs={"k": 4})

    # 3. Create the Prompt Template
    prompt = ChatPromptTemplate.from_template("""
    Answer the user's question based ONLY on the following context. 
    If the answer is not in the context, just say you don't know.
    
    Context:
    {context}
    
    Question: {input}
    """)

    # 4. Create the Chain
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain