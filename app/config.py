"""Configuration settings for Enterprise Service Desk."""

import os

from langchain_openai import ChatOpenAI


def _get_env(key: str, default: str) -> str:
    """Read an environment variable with a default fallback."""
    return os.getenv(key, default)


def get_llm_provider() -> str:
    """Get the configured LLM provider. Defaults to 'lmstudio'."""
    return _get_env("LLM_PROVIDER", "lmstudio").lower()


def create_llm() -> ChatOpenAI:
    """Create a ChatOpenAI instance based on the configured provider."""
    provider = get_llm_provider()

    if provider == "lmstudio":
        return ChatOpenAI(
            base_url=_get_env("LMSTUDIO_BASE_URL", "http://localhost:1234/v1"),
            api_key="lm-studio",
            model=_get_env("LMSTUDIO_MODEL", "local-model"),
            temperature=0,
        )

    if provider == "openai":
        api_key = _get_env("OPENAI_API_KEY", "")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is required when LLM_PROVIDER is 'openai'")
        return ChatOpenAI(
            api_key=api_key,
            model=_get_env("OPENAI_MODEL", "gpt-4.1-mini"),
            temperature=0,
        )

    if provider == "openrouter":
        api_key = _get_env("OPENROUTER_API_KEY", "")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY is required when LLM_PROVIDER is 'openrouter'")
        return ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            model=_get_env("OPENROUTER_MODEL", "openai/gpt-4.1-mini"),
            temperature=0,
        )

    raise ValueError(f"Unknown LLM_PROVIDER: {provider}")