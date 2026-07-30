"""Embedding model initialization for the RAG pipeline."""

from langchain_huggingface import HuggingFaceEmbeddings


_embeddings = None


def create_embeddings() -> HuggingFaceEmbeddings:
    """Return a singleton HuggingFace embedding model instance."""
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    return _embeddings
