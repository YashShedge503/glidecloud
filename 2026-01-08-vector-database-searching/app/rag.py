from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from operator import itemgetter
from app.vectordb import get_vector_db
from app.config import LLM_MODEL, OLLAMA_BASE_URL

def get_rag_chain():
    # Setup LLM
    llm = ChatOllama(
        model=LLM_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0
    )

    # Setup Retriever
    retriever = get_vector_db().as_retriever(search_kwargs={"k": 4})

    # Prompt Template
    prompt = ChatPromptTemplate.from_template("""
    Answer the user's question based ONLY on the following context. 
    If the answer is not in the context, just say you don't know.
    
    Context:
    {context}
    
    Question: {input}
    """)

    # Build the Chain (Using LCEL)
    setup_and_retrieval = RunnableParallel(
        {"context": itemgetter("input") | retriever, "input": itemgetter("input")}
    )

    # Generate the answer
    # This takes the context+input from Step A, feeds it to the prompt -> LLM -> Text
    answer_generation = prompt | llm | StrOutputParser()

    # Step C: Combine everything
    # This runs Step A, then calculates Step B (answer), and returns a dictionary with BOTH.
    # Result: {"context": [...], "input": "...", "answer": "The AI response"}
    final_chain = setup_and_retrieval.assign(answer=answer_generation)
    
    return final_chain
