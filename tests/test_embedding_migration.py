"""Manual smoke test for embedding migration."""

from app.rag.embeddings import create_embeddings

embeddings = create_embeddings()

print("Embedding model initialized successfully.")