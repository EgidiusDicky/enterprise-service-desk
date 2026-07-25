"""IT specialist agent for handling IT-related queries."""

from langchain_core.language_models import BaseLanguageModel
from langchain_core.retrievers import BaseRetriever

from app.tools.retrieve_tool import retrieve_context
from app.tools.validation_tool import validate_context
from app.tools.response_tool import generate_response


def answer(query: str, retriever: BaseRetriever, llm: BaseLanguageModel) -> str:
    """Answer an IT query using retrieval and LLM generation."""
    documents = retrieve_context(retriever, query)

    if not validate_context(documents):
        return "I don't have enough information from the IT knowledge base."

    return generate_response(llm, query, documents)