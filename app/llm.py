"""LLM initialization for connecting to LM Studio."""

from langchain_openai import ChatOpenAI


def create_llm() -> ChatOpenAI:
    """Return a ChatOpenAI instance connected to LM Studio."""
    return ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",
        model="local-model",
        temperature=0,
    )