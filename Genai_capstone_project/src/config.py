import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./logs.db")
    LLM_MODEL = os.getenv("LLM_MODEL", "llama3")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    
    # Simulating Cloud Credentials (fake for now)
    AWS_REGION = "us-east-1"