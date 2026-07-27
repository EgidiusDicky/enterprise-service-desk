"""Tool for generating LLM responses from retrieved context."""

from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel


def generate_response(
    llm: BaseLanguageModel, query: str, documents: list[Document]
) -> str:
    """Generate an answer using the LLM given context and user query."""
    context = "\n\n".join(doc.page_content for doc in documents)
    prompt = (
        "You are an internal enterprise assistant.\n"
        "Answer ONLY using the provided context.\n"
        "Do not add assumptions.\n"
        "Do not invent procedures.\n"
        "If the answer is not found in the context, reply:\n"
        "'I don't have enough information from the knowledge base.'\n"
        f"\nContext:\n{context}"
        f"\n\nQuestion: {query}\n\nAnswer:"
    )
    return llm.invoke(prompt)