"""Retriever for fetching relevant context in the RAG pipeline."""


class Retriever:
    """Retrieves relevant document chunks for a given query."""

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        """Fetch the most relevant text chunks for the query."""
        pass