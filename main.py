from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title="RAG Document Chatbot",
    description="Chat with your documents using RAG + Qdrant + OpenAI",
    version="1.0.0"
)

# Register API routes
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "RAG Chatbot API is running"}