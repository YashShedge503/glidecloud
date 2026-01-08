from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.rag import get_rag_chain
import os

# Initialize FastAPI
app = FastAPI()

# Allow CORS (our local HTML file can cnnect to this server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# define the Request Structure
class QueryRequest(BaseModel):
    query: str

# initialize Chain (Global variable to load once)
rag_chain = get_rag_chain()

@app.post("/search")
async def search(request: QueryRequest):
    try:
        # run the RAG pipeline
        response = rag_chain.invoke({"input": request.query})
        
        # format the context for the frontend
        sources = []
        if "context" in response:
            for doc in response["context"]:
                sources.append({
                    "source": os.path.basename(doc.metadata.get("source", "Unknown")),
                    "page": doc.metadata.get("page", "N/A"),
                    "content": doc.page_content
                })

        return {
            "answer": response["answer"],
            "sources": sources
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)