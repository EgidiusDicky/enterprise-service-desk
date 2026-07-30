"""Vector store creation for the RAG pipeline."""

from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

_DEFAULT_DB_PATH = "data/chroma"


def _get_vector_store_path() -> str:
    """Return the configured Chroma persistence directory."""
    return _DEFAULT_DB_PATH


def create_vector_store(
    documents: list[Document], embeddings: Embeddings
) -> Chroma:
    """Create or load a Chroma vector store.

    If the persistent directory already exists, load it directly.
    Otherwise, create it from the provided documents and persist.
    """
    persist_dir = Path(_get_vector_store_path())
    persist_dir.mkdir(parents=True, exist_ok=True)

    if _is_existing_db(persist_dir):
        return Chroma(
            embedding_function=embeddings,
            persist_directory=str(persist_dir),
        )

    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=str(persist_dir),
    )


def _is_existing_db(path: Path) -> bool:
    """Check whether a Chroma database already exists at the given path."""
    return (
        path.exists()
        and any(path.iterdir())
        and (path / "chroma.sqlite3").exists()
    )