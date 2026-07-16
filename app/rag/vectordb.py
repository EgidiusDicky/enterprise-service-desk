"""Vector database wrapper for the RAG pipeline."""


class VectorDatabase:
    """Stores and retrieves vector embeddings for a department."""

    def store(self, embeddings: list[list[float]], texts: list[str]) -> None:
        """Store text chunks and their embeddings."""
        pass

    def search(self, query_embedding: list[float], top_k: int = 3) -> list[str]:
        """Retrieve the most similar text chunks."""
        pass