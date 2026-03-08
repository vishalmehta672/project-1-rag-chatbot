from app.services.vector_store import search_chunks
from app.services.llm_service import generate_answer
from app.utils.cache import set_cached_response

def ask_question(question):
    print("Returning answer...")
    chunks = search_chunks(question)
    print(f"Retrieved {len(chunks)} chunks from vector store.")
    
    context = "\n".join(chunks)
    print(f"Context:\n{context}\n")
    answer = generate_answer(context, question)
    set_cached_response(question, answer)

    return answer