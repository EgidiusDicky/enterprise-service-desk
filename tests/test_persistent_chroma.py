"""Manual smoke test for persistent Chroma vector store."""

from pathlib import Path

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever

documents = load_documents()
chunks = split_documents(documents)
embeddings = create_embeddings()

db_path = Path("data/chroma")
if db_path.exists() and (db_path / "chroma.sqlite3").exists():
    print("Loading existing Chroma database...")
else:
    print("Creating new Chroma database...")

vector_store = create_vector_store(chunks, embeddings)
retriever = create_retriever(vector_store)

print("Persistent Chroma initialized successfully.")