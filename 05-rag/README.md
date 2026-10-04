# 05 · RAG (retrieval-augmented generation)

Letting the model answer from documents I give it, instead of only from memory.
I built the free version on Colab — no Google Cloud needed: sentence-transformers
for embeddings, FAISS to search them, and TinyLlama to write the answer.

## Files
- `rag_faiss.ipynb` — the Colab notebook.

## What it does
The flow: documents → embed each one → store in FAISS → embed the question →
retrieve the closest document → feed it to the model → answer.
- **Embedding model:** `all-MiniLM-L6-v2` (turns text into meaning-vectors).
- **Vector store:** FAISS (searches by meaning, not keywords).
- **Answer model:** `TinyLlama-1.1B-Chat`.

## What I saw
- **Question:** "When does Dr. Example teach Databases?"
- **Retrieved context:** "Dr. Example teaches Databases on Mondays at 10 AM."
- **Answer (with context):** "Dr. Example teaches Databases on Mondays at 10 AM."
— correct, lifted straight from the retrieved line. TinyLlama then kept going
  and invented a couple of extra Q&A pairs on its own (small models tend to keep
  generating); the real answer is the first line.

- **Without context (same question, no retrieval):** the model guessed / made
  something up.

## Terms
- **Embedding** — text turned into a list of numbers that captures its meaning;
  similar meaning gives similar numbers.
- **Vector store (FAISS)** — a searchable box of those number-lists.
- **Retriever** — embeds the question and pulls the closest-matching document.

## Takeaways
- Retrieval is what turns guessing into answering — the model only got it right
  because the correct document was handed to it.
- A RAG answer is only as good as what gets retrieved. If the store holds
  something false, the model repeats it as fact — which is exactly the setup for
  the poisoning exercise in `07`.
- TinyLlama is small and sometimes rambled even with the right context; a bigger
  model answers more cleanly.