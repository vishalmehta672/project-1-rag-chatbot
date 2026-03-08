
from app.services.document_service import load_pdf
from app.utils.embeddings import create_embedding
from app.utils.text_splitter import split_text
from app.services.vector_store import store_chunks


def ingest_document(file_path: str) -> None:
    """Ingest a document by loading, chunking, embedding, and storing it."""
    text = load_pdf(file_path)
    chunks = split_text(text)
    _embedding = [create_embedding(chunk) for chunk in chunks]
    store_chunks(chunks, _embedding)
    print("Document stored successfully")
