"""Main entry point for Enterprise Service Desk."""

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever
from app.llm import create_llm
from app.agents.supervisor import route


def main() -> None:
    """Run the interactive terminal chat loop."""
    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = create_embeddings()
    vector_store = create_vector_store(chunks, embeddings)
    retriever = create_retriever(vector_store)
    llm = create_llm()

    print("========================================")
    print("Enterprise Service Desk")
    print("Type 'exit' to quit.")
    print("========================================")

    while True:
        user_input = input("You > ")
        if user_input == "exit":
            print("Goodbye.")
            break
        response = route(user_input, retriever, llm)
        print("Assistant >", response)
        print("----------------------------------------")


if __name__ == "__main__":
    main()