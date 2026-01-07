from app.rag import get_rag_chain

def query_rag(question: str):
    qa = get_rag_chain()
    result = qa(question)
    return result

if __name__ == "__main__":
    response = query_rag("What is Retrieval Augmented Generation?")
    print(response["result"])