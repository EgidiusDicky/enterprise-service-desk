"""Manual smoke test for lazy loading initialization."""

import demo

retriever1 = demo._get_retriever()
retriever2 = demo._get_retriever()

print("Lazy loading initialized successfully.")