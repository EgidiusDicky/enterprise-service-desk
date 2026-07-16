"""Manual smoke test for the document loader."""

from app.rag.loader import load_documents

documents = load_documents()

print(f"Total documents loaded: {len(documents)}\n")

for doc in documents:
    print(f"File: {doc.metadata['source']}")
    print(f"Department: {doc.metadata['department']}")
    print(f"Content preview: {doc.page_content[:80]}")
    print()