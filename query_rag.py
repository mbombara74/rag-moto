from qdrant_client import QdrantClient
from ollama import Client

QDRANT_URL = "http://192.168.1.237:6333"
OLLAMA_HOST = "http://192.168.1.120:11434"
COLLECTION_NAME = "rag_moto"
EMBED_MODEL = "nomic-embed-text"

qdrant_client = QdrantClient(url=QDRANT_URL, prefer_grpc=False, check_compatibility=False)
ollama_client = Client(host=OLLAMA_HOST)

question = input("Domanda: ")
query_vec = ollama_client.embeddings(model=EMBED_MODEL, prompt=question)["embedding"]

hits = qdrant_client.query_points(
    collection_name=COLLECTION_NAME,
    query=query_vec,
    limit=5,
    with_payload=True,
)

print(type(hits))
print(hits)