from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from app.utils.embeddings import create_embedding

client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "documents"


def store_chunks(chunks, embeddings):
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

    query_vector = create_embedding(query)

    results = client.query_points(
        collection_name="documents",
        query=query_vector.tolist(),
        limit=3
    )

    chunks = [hit.payload["text"] for hit in results.points]

    return chunks