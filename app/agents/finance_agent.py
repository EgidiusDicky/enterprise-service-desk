"""Finance specialist agent for handling finance-related queries."""

from langchain_core.language_models import BaseLanguageModel
from langchain_core.retrievers import BaseRetriever

from app.tools.retrieve_tool import retrieve_context
from app.tools.validation_tool import validate_context
from app.tools.response_tool import generate_response


def answer(query: str, retriever: BaseRetriever, llm: BaseLanguageModel) -> str:
    """Answer a finance query using retrieval and LLM generation."""
    documents = retrieve_context(retriever, query)

    if not validate_context(documents):
        return "I don't have enough information from the Finance knowledge base."

    return generate_response(llm, query, documents)