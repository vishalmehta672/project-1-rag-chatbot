from app.services.vector_store import search_chunks
from app.services.llm_service import generate_answer

def ask_question(question):

    chunks = search_chunks(question)

    context = "\n".join(chunks)

    answer = generate_answer(context, question)

    return answer