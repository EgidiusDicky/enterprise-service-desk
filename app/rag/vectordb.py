"""Vector store creation for the RAG pipeline."""

from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


def create_vector_store(
    documents: list[Document], embeddings: Embeddings
) -> Chroma:
    """Create and persist a Chroma vector store from documents."""
    persist_dir = (
        Path(__file__).resolve().parent.parent.parent
        / "knowledge_base"
        / "vector_store"
    )
    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=str(persist_dir),
    )