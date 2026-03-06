import chromadb

client = chromadb.Client()

collection = client.create_collection("documents")

collection.add(
    documents=["AI is amazing"],
    ids=["doc1"]
)