# Fixed debug_rag.py (Run this to confirm LLM works)
import sys
from app.config import OLLAMA_BASE_URL, LLM_MODEL
from langchain_ollama import ChatOllama

print(f"Testing LLM connection to: {OLLAMA_BASE_URL}")

try:
    llm = ChatOllama(model=LLM_MODEL, base_url=OLLAMA_BASE_URL)
    print("   - Sending Hello...")
    response = llm.invoke("Say 'Hello'!")
    print(f"✅ LLM Response: {response.content}")
except Exception as e:
    print(f"❌ LLM ERROR: {e}")