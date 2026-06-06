from pypdf import PdfReader
from qdrant_client import QdrantClient, models
from ollama import Client

PDF_PATH = "prova.pdf"
COLLECTION_NAME = "rag_moto"
OLLAMA_HOST = "http://192.168.1.120:11434"
EMBED_MODEL = "nomic-embed-text"

ollama_client = Client(host=OLLAMA_HOST)
qdrant_client = QdrantClient(url="http://192.168.1.237:6333", check_compatibility=False)

def chunk_text(text, size=800, overlap=150):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += size - overlap
    return chunks

reader = PdfReader(PDF_PATH)
full_text = "\n".join(page.extract_text() or "" for page in reader.pages)
chunks = chunk_text(full_text)

sample = ollama_client.embeddings(model=EMBED_MODEL, prompt="test")
vector = sample["embedding"]
print("vector size:", len(vector))

if not qdrant_client.collection_exists(COLLECTION_NAME):
    qdrant_client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=len(vector),
            distance=models.Distance.COSINE,
        ),
    )

points = []
for i, chunk in enumerate(chunks):
    emb = ollama_client.embeddings(model=EMBED_MODEL, prompt=chunk)
    points.append(
        models.PointStruct(
            id=i,
            vector=emb["embedding"],
            payload={"text": chunk, "chunk": i},
        )
    )

print("chunks:", len(chunks))
print("points:", len(points))

if not points:
    raise ValueError("Nessun punto da inviare a Qdrant")

qdrant_client.upsert(collection_name=COLLECTION_NAME, points=points, wait=True)

print(f"Caricati {len(points)} chunk in Qdrant")