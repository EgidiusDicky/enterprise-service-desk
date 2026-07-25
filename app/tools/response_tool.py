"""Tool for generating LLM responses from retrieved context."""

from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel


def generate_response(
    llm: BaseLanguageModel, query: str, documents: list[Document]
) -> str:
    """Generate an answer using the LLM given context and user query."""
    context = "\n\n".join(doc.page_content for doc in documents)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"
    return llm.invoke(prompt)