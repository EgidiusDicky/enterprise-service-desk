"""Manual smoke test for response tool."""

from app.llm import create_llm

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever

from app.tools.retrieve_tool import retrieve_context
from app.tools.response_tool import generate_response


def main() -> None:
    documents = load_documents()
    chunks = split_documents(documents)

    embeddings = create_embeddings()
    vector_store = create_vector_store(chunks, embeddings)
    retriever = create_retriever(vector_store)

    context = retrieve_context(
        retriever,
        "Bagaimana cara mengajukan cuti?"
    )

    llm = create_llm()

    answer = generate_response(
        llm,
        "Bagaimana cara mengajukan cuti?",
        context,
    )

    print(answer)


if __name__ == "__main__":
    main()