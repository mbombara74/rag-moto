# RAG Moto

Progetto di studio per costruire un sistema RAG locale con Python, Ollama e Qdrant.

## Obiettivo

Creare un flusso semplice che:
- legge un PDF,
- lo spezza in chunk,
- trasforma i chunk in embeddings,
- salva i dati in Qdrant,
- recupera i chunk più rilevanti,
- genera una risposta con Ollama.

## Cosa abbiamo fatto

### 1. Ambiente di sviluppo
- Configurato un container Python in VS Code.
- Sistemato `requirements.txt`.
- Verificata la connessione a Ollama sulla rete locale.

### 2. Ollama
- Usato il client Python ufficiale `ollama`.
- Verificata la connessione al server Ollama remoto.
- Usato un modello di chat locale per la risposta finale.

### 3. Lettura PDF
- Usato `pypdf` per leggere il testo del documento.
- Verificato che il PDF contenga testo estraibile.
- Ingest funzionante su un documento con 599 chunk.

### 4. Qdrant
- Avviato Qdrant in Docker.
- Verificata la connessione dal dev container.
- Caricati i chunk con vector embedding e payload.
- Testata la query semantica con recupero dei risultati.

### 5. RAG end-to-end
- Recupero dei chunk rilevanti da Qdrant.
- Costruzione del contesto.
- Generazione della risposta finale con Ollama in italiano.

## File principali

- `ingest_pdf.py`: legge il PDF e carica i chunk in Qdrant.
- `query_rag.py`: cerca i chunk più rilevanti in Qdrant.
- `rag_chat.py`: recupera i chunk e chiede a Ollama di generare la risposta.

## Concetti imparati

- **Embedding**: trasformazione di un testo in una lista di numeri che rappresenta il significato.
- **Chunk**: pezzo piccolo di documento.
- **Payload**: metadati allegati a un punto in Qdrant.
- **RAG**: sistema che recupera testo rilevante e poi genera una risposta usando quel testo.

## Stato attuale

Il progetto funziona con un singolo documento e un flusso RAG base.

## Prossimi miglioramenti
- Caricare più documenti.
- Aggiungere metadati come nome documento e pagina.
- Filtrare i risultati in Qdrant.
- Migliorare il chunking.
- Aggiungere citazioni e fonti.

- Il database vettoriale gira nella VM di sviluppo come container Docker.
- Al momento uso **Qdrant** come vector DB. Ciccia. Tanta Ciccia.