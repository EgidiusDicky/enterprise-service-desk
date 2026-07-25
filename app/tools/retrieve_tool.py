"""Tool for retrieving relevant context from a vector store."""

from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document


def retrieve_context(retriever: BaseRetriever, query: str) -> list[Document]:
    """Retrieve relevant documents for a given query."""
    return retriever.invoke(query)