"""Embedding model initialization for the RAG pipeline."""

from langchain_community.embeddings import HuggingFaceEmbeddings


def create_embeddings() -> HuggingFaceEmbeddings:
    """Return a configured HuggingFace embedding model instance."""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )