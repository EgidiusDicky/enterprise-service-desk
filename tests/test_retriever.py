"""Manual smoke test for retriever."""

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever


def main() -> None:
    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = create_embeddings()
    vector_store = create_vector_store(chunks, embeddings)
    retriever = create_retriever(vector_store)

    print(f"Original documents : {len(documents)}")
    print(f"Chunks             : {len(chunks)}")
    print(f"Retriever type     : {type(retriever).__name__}")

    print("\nRetriever created successfully.")


if __name__ == "__main__":
    main()