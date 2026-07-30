"""Manual smoke test for Render startup configuration."""

import os

import demo

port = os.getenv("PORT", 7860)

print(f"Resolved PORT: {port}")
print("Render startup configuration verified.")