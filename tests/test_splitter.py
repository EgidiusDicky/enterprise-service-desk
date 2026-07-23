"""Manual smoke test for the text splitter."""

from pathlib import Path

from app.rag.loader import load_documents
from app.rag.splitter import split_documents

documents = load_documents()
chunks = split_documents(documents)

print(f"Total original documents: {len(documents)}")
print(f"Total chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    source = Path(chunk.metadata["source"]).name
    print(f"Chunk {i}")
    print(f"Department: {chunk.metadata['department']}")
    print(f"Source: {source}")
    print(f"Length: {len(chunk.page_content)}")
    print(f"Preview: {chunk.page_content[:80]}")
    print()