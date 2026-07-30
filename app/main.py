"""Main entry point for Enterprise Service Desk."""

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever
from app.llm import create_llm
from app.agents.supervisor import route
from app.agents.hr_agent import confirm_leave


_retriever = None
_llm = None


def _get_retriever():
    """Lazily initialize and return the retriever."""
    global _retriever
    if _retriever is None:
        from pathlib import Path

        from app.rag.embeddings import create_embeddings
        from app.rag.vectordb import Chroma, _get_vector_store_path
        from app.rag.retriever import create_retriever

        db_path = Path(_get_vector_store_path())
        if db_path.exists() and (db_path / "chroma.sqlite3").exists():
            embeddings = create_embeddings()
            _retriever = Chroma(
                embedding_function=embeddings,
                persist_directory=str(db_path),
            )
            _retriever = _retriever.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 3},
            )
        else:
            from app.rag.loader import load_documents
            from app.rag.splitter import split_documents
            from app.rag.vectordb import create_vector_store

            documents = load_documents()
            chunks = split_documents(documents)
            embeddings = create_embeddings()
            vector_store = create_vector_store(chunks, embeddings)
            _retriever = create_retriever(vector_store)
    return _retriever


def _get_llm():
    """Lazily initialize and return the LLM."""
    global _llm
    if _llm is None:
        _llm = create_llm()
    return _llm


def main() -> None:
    """Run the interactive terminal chat loop."""
    print("========================================")
    print("Enterprise Service Desk")
    print("========================================")
    print()
    print("Commands:")
    print()
    print("exit")
    print()
    print("----------------------------------------")

    pending_query = None

    while True:
        user_input = input("You > ")
        if user_input == "exit":
            print("Goodbye.")
            break

        if pending_query is not None:
            result = confirm_leave(pending_query, user_input)
            print("Assistant >", result)
            print("----------------------------------------")
            pending_query = None
        else:
            retriever = _get_retriever()
            llm = _get_llm()
            response = route(user_input, retriever, llm)
            print("Assistant >", response)
            print("----------------------------------------")


if __name__ == "__main__":
    main()