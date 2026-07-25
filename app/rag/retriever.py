"""Retriever creation for the RAG pipeline."""

from langchain_chroma import Chroma
from langchain_core.retrievers import BaseRetriever


def create_retriever(vector_store: Chroma) -> BaseRetriever:
    """Return a similarity retriever from a Chroma vector store."""
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )