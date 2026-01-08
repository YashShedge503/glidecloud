import pytest
import os
from app.config import PDF_DIR, LLM_MODEL, OLLAMA_BASE_URL
from app.vectordb import get_vector_db
from app.rag import get_rag_chain

# Test Configuration
def test_config_loading():
    """Ensure that the .env variables are loaded correctly."""
    assert PDF_DIR is not None, "PDF_DIR should be set"
    assert LLM_MODEL is not None, "LLM_MODEL should be set"
    assert os.path.exists(PDF_DIR), f"The data directory '{PDF_DIR}' does not exist on disk"

# Test Vector Database
def test_vector_db_connection():
    """Check if the Vector DB loads and contains data."""
    db = get_vector_db()
    assert db is not None, "Database object should not be None"
    
    # Perform a quick sanity search to ensure DB is readable
    # We search for a generic term likely to be in your docs
    results = db.similarity_search("RAG", k=1)
    assert len(results) > 0, "Database should return at least 1 result for the query 'RAG'"

# Test RAG Chain Construction
def test_rag_chain_creation():
    """Ensure the RAG chain (LLM + Retriever) builds without crashing."""
    try:
        chain = get_rag_chain()
        assert chain is not None
    except Exception as e:
        pytest.fail(f"Failed to create RAG chain: {e}")

# Integration Test
# This actually calls the LLM. It might be slow, but proves the whole system works.
@pytest.mark.skipif(not OLLAMA_BASE_URL, reason="Ollama URL not configured")
def test_full_rag_flow():
    """Test a full question-answering cycle."""
    chain = get_rag_chain()
    
    # Use a dictionary input matching your new LCEL structure
    response = chain.invoke({"input": "What is RAG?"})
    
    # Check if we got a dictionary back with an answer
    assert isinstance(response, dict)
    assert "answer" in response
    assert len(response["answer"]) > 0
    print(f"\nTest Answer: {response['answer']}")