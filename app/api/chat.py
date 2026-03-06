from fastapi import APIRouter
from app.services.query_service import ask_question

router = APIRouter()

@router.get("/")
def home():
    return {"message": "AI Knowledge Base API"}

@router.post("/ask")
def ask(question: str):

    answer = ask_question(question)

    return {"answer": answer}



