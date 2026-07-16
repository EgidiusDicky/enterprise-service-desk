"""Document loader module for loading knowledge base documents."""

from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document


def load_documents() -> list[Document]:
    """Load all .md documents from the knowledge base with department metadata."""
    base_path = Path(__file__).resolve().parent.parent.parent / "knowledge_base"

    loader = DirectoryLoader(
        str(base_path),
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=True,
    )
    documents = loader.load()

    for doc in documents:
        rel_path = Path(doc.metadata["source"]).relative_to(base_path)
        department = rel_path.parts[0]
        doc.metadata["department"] = department

    return documents