# 🛡️ LogOps AI: Automated DevOps Error Resolver

LogOps AI is an intelligent Site Reliability Engineering (SRE) tool designed to automate the detection, analysis, and resolution of cloud infrastructure errors.

Unlike standard log viewers, LogOps AI uses a Retrieval-Augmented Generation (RAG) pipeline to consult an internal Knowledge Base (SOPs) before prescribing a fix. It acts as a Level-1 AI Engineer that not only explains why a server failed but also generates the exact CLI command or SQL query to fix it, strictly adhering to company policies.

---

## 🏗️ System Architecture

The system follows a Modular Monolith architecture designed for scalability and maintainability.

### 🔁 Workflow (Data Pipeline)

1. Ingestion Layer (src/ingestion.py)
- Simulates a real-time stream of CloudWatch / Stackdriver logs
- Normalizes raw JSON logs into structured records
- Tech: Python, Faker

2. Persistence Layer (src/database.py)
- Stores incoming logs and their resolution status
- Ensures data integrity using a relational database
- Tech: SQLite, SQLAlchemy (ORM)

3. The Brain: RAG Engine (src/rag.py)
- Converts the internal troubleshooting manual into vector embeddings
- Stores embeddings for semantic search
- Tech: ChromaDB, HuggingFace Embeddings

4. Resolution Agent (src/llm.py)
- Retrieves relevant SOPs from the RAG engine
- Prompts the LLM with Error Log + Company Policy
- Outputs structured JSON (Root Cause, Fix Steps, Code Snippet)
- Tech: LangChain, Ollama (Llama 3)

5. Frontend Interface (main.py)
- Interactive dashboard for DevOps engineers
- Tech: Streamlit

---

## 🧠 The RAG Pipeline (True RAG)

This project implements True RAG to ensure the AI follows internal company rules instead of hallucinating generic fixes.

- Knowledge Base
  - knowledge_base/troubleshooting_manual.txt
  - Contains confidential SOPs
  - Example: Do not restart the payment service during business hours

- Vectorization
  - SOPs are chunked and embedded using all-MiniLM-L6-v2

- Context Retrieval
  - ChromaDB fetches only the most relevant policy

- Augmented Prompting
  - LLM receives:
    - Error log
    - Exact internal rule
  - Ensures compliance-safe fixes

---

## 🚀 Features

- Automated Log Ingestion
- Intelligent Resolution with real CLI commands (kubectl, systemctl, npm, SQL)
- Policy Compliance enforced via RAG
- Audit Trail for all resolved incidents
- Clean and interactive dashboard

---

## 🛠️ Tech Stack

- Language: Python 3.10+
- Frontend: Streamlit
- LLM: Ollama (Llama 3)
- Framework: LangChain
- Vector DB: ChromaDB
- Database: SQLite (SQLAlchemy)
- Embeddings: HuggingFace (sentence-transformers)

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- Ollama installed and running (https://ollama.com)

Pull the model:
ollama run llama3

---

### Step 1: Clone the Repository
git clone https://github.com/YashShedge503/glidecloud.git
cd glidecloud/Genai_capstone_project

---

### Step 2: Create Virtual Environment
python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### Step 3: Install Dependencies
pip install -r requirements.txt

---

### Step 4: Run the Application
Ensure Ollama is running, then start the dashboard:
streamlit run main.py

---

## 📸 Usage

1. Fetch Logs
- Click the Fetch Logs button to simulate cloud errors

2. Select an Error
- Choose a Pending error from the dashboard

3. Generate Fix
- Click Generate Fix
- The AI retrieves SOPs, explains the root cause, and generates a copy-pasteable fix command

---

## ✅ Outcome

LogOps AI behaves like a junior SRE on-call engineer by providing:
- Fast root cause analysis
- Policy-compliant fixes
- Clear audit history

Ideal for GenAI, RAG, SRE, and DevOps portfolios.
