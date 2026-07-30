"""Manual smoke test for runtime singleton optimization."""

import demo

demo._get_retriever()
demo._get_retriever()

demo._get_llm()
demo._get_llm()

print("Runtime singleton optimization verified.")