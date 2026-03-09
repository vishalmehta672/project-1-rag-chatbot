import os
import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from app.utils.embeddings import create_embedding

# Lazy initialization - client created on first use
_client = None

def get_client():
    """Get or create Qdrant client lazily"""
    global _client
    if _client is None:
        # Read environment variables when actually creating the client
        host = os.getenv("QDRANT_HOST", "localhost")
        port = int(os.getenv("QDRANT_PORT", 6333))
        print(f"Connecting to Qdrant at {host}:{port}")
        _client = QdrantClient(
            host=host,
            port=port
        )
    return _client

COLLECTION_NAME = "documents"


def create_collection():
    """Create collection if it does not exist"""

    try:
        collections = get_client().get_collections().collections
        names = [c.name for c in collections]

        if COLLECTION_NAME not in names:
            print("Creating Qdrant collection...")

            get_client().create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                ),
            )
    except Exception as e:
        print("Error checking/creating collection:", e)
        raise


def store_chunks(chunks, embeddings):
    """Store document chunks into Qdrant"""

    create_collection()

    print(f"Storing {len(chunks)} vectors...")

    points = []

    for chunk, embedding in zip(chunks, embeddings):

        point = PointStruct(
            id=str(uuid.uuid4()),   # unique id
            vector=embedding,
            payload={
                "text": chunk
            }
        )

        points.append(point)

    get_client().upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print("Vectors stored successfully.")


def search_chunks(query, limit=5):
    """Search similar chunks"""

    print("Searching vectors...")

    query_vector = create_embedding(query)

    results = get_client().query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector.tolist(),
        limit=limit
    )

    chunks = [hit.payload["text"] for hit in results.points]

    return chunks