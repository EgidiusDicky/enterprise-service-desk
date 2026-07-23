"""Manual smoke test for the vector database."""

from pathlib import Path

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store

documents = load_documents()
chunks = split_documents(documents)
embeddings = create_embeddings()

persist_dir = (
    Path(__file__).resolve().parent.parent
    / "knowledge_base"
    / "vector_store"
)

vector_store = create_vector_store(chunks, embeddings)

print(f"Total original documents: {len(documents)}")
print(f"Total chunks: {len(chunks)}")
print(f"Embedding model initialized: {type(embeddings).__name__}")
print(f"Vector store created successfully: {type(vector_store).__name__}")
print(f"Persist directory: {persist_dir}")