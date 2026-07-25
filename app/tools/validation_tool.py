"""Tool for validating retrieved context."""

from langchain_core.documents import Document


def validate_context(documents: list[Document]) -> bool:
    """Return True if documents are present, False if empty."""
    return len(documents) > 0