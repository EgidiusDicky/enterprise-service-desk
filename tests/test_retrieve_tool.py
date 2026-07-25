"""Manual smoke test for retrieve tool."""

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever
from app.tools.retrieve_tool import retrieve_context


def main() -> None:
    documents = load_documents()
    chunks = split_documents(documents)

    embeddings = create_embeddings()
    vector_store = create_vector_store(chunks, embeddings)

    retriever = create_retriever(vector_store)

    results = retrieve_context(
        retriever,
        "Bagaimana cara mengajukan cuti?"
    )

    print(f"Retrieved documents: {len(results)}")

    for i, doc in enumerate(results, start=1):
        print(f"\nDocument {i}")
        print(f"Department: {doc.metadata.get('department')}")
        print(f"Source: {doc.metadata.get('source')}")
        print(doc.page_content[:150])


if __name__ == "__main__":
    main()