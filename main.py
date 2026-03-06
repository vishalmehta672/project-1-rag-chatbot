from fastapi import FastAPI
from app.services.query_service import ask_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Knowledge Base API"}

@app.post("/ask")
def ask(question: str):

    answer = ask_question(question)

    return {"answer": answer}