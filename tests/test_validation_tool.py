"""Manual smoke test for validation tool."""

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever
from app.tools.retrieve_tool import retrieve_context
from app.tools.validation_tool import validate_context


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

    is_valid = validate_context(results)

    print(f"Retrieved documents : {len(results)}")
    print(f"Context valid       : {is_valid}")


if __name__ == "__main__":
    main()