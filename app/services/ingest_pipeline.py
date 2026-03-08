
from app.services.document_service import load_pdf
from app.utils.embeddings import create_embedding
from app.utils.text_splitter import split_text
from app.services.vector_store import store_chunks


text = load_pdf("data/oops.pdf")

chunks = split_text(text)

_embedding = [create_embedding(chunk) for chunk in chunks]
store_chunks(chunks,_embedding)

print("Document stored successfully")