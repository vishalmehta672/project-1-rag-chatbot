from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="RAG Document Chatbot",
    description="Chat with your documents using RAG + Qdrant + OpenAI",
    version="1.0.0"
)

# Register API routes
app.include_router(router=router, prefix="/api")
    
@app.get("/")
def root():
    return {"message": "RAG Chatbot API is running"}