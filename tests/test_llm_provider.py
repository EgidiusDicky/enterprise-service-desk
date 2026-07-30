"""Manual smoke test for LLM provider configuration."""

from app.config import create_llm, get_llm_provider

provider = get_llm_provider()
llm = create_llm()

print(f"Current provider:\n{provider}\n")
print(f"Current model:\n{llm.model_name}\n")
print("Configuration initialized successfully.")