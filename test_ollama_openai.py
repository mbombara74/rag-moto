import requests

OLLAMA_URL = "http://192.168.1.120:11434/api/tags"

r = requests.get(OLLAMA_URL, timeout=10)
r.raise_for_status()

data = r.json()
models = data.get("models", [])

print("Connessione OK")
for m in models:
    print(m.get("name"))