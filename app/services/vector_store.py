from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from app.utils.embeddings import create_embedding

client = QdrantClient(
    host="qdrant",
    port=6333
)

COLLECTION_NAME = "documents"


def create_collection():
    """Create collection if it does not exist"""

    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:
        print("Creating Qdrant collection...")

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,           # embedding size for all-MiniLM-L6-v2
                distance=Distance.COSINE
            ),
        )


def store_chunks(chunks, embeddings):

    create_collection()   # ← ensure collection exists

    print("Storing vectors...")
    points = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        points.append(
            PointStruct(
                id=i,
                vector=embedding,
                payload={"text": chunk}
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


def search_chunks(query):

    print("Searching vectors...")

    query_vector = create_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector.tolist(),
        limit=5
    )

    chunks = [hit.payload["text"] for hit in results.points]

    return chunks