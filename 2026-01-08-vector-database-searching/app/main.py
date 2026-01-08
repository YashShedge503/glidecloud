import argparse
import time
import os
from app.loader import load_and_split_pdfs
from app.vectordb import get_vector_db
from app.rag import get_rag_chain
from app.config import PDF_DIR

def run_ingest():
    """Loads PDFs and updates the Vector DB"""
    print("Starting Ingestion Process...")
    
    # Load and Split Documents
    docs = load_and_split_pdfs(PDF_DIR)
    
    if not docs:
        print("No documents found to ingest.")
        return

    # get Vector Database Instance
    vectordb = get_vector_db()
    
    # add documents to the database
    print(f"Generating Embeddings for {len(docs)} chunks...")
    vectordb.add_documents(docs)
    
    try:
        vectordb.persist() 
    except AttributeError:
        pass
        
    print(f" Successfully ingested {len(docs)} chunks into the database.")

def run_chat():
    """Runs the interactive chat loop"""
    print("\n" + "="*50)
    print(" RAG Chat System Initialized")
    print("Type 'exit' or 'quit' to stop.")
    print("="*50 + "\n")

    # Initialize the RAG chain
    qa_chain = get_rag_chain()

    while True:
        try:
            query = input(" Enter your query: ")
            
            # Check for exit commands
            if query.lower() in ["exit", "quit"]:
                print("Goodbye! ")
                break
            
            # Skip empty queries
            if not query.strip():
                continue

            print("Thinking... ")
            start_time = time.time()
            
            # EXECUTE CHAIN 
            response = qa_chain.invoke(query)

            
            end_time = time.time()

            # DISPLAY ANSWER
            # the key for the answer is now 'answer'
            print("\n" + "-"*20 + " 🤖 ANSWER " + "-"*20)
            print(response.content)
            print("-" * 50)
            print(f"Answered in {end_time - start_time:.2f}s")
            print("="*50 + "\n")

        except KeyboardInterrupt:
            print("\nGoodbye! ")
            break
        except Exception as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RAG System Controller")
    parser.add_argument("mode", choices=["ingest", "chat"], help="Choose 'ingest' to process PDFs or 'chat' to ask questions.")
    
    args = parser.parse_args()
    
    if args.mode == "ingest":
        run_ingest()
    elif args.mode == "chat":
        run_chat()