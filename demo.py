"""Gradio demo for Enterprise Service Desk on Hugging Face Spaces."""

import gradio as gr

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
        from app.llm import create_llm

        _llm = create_llm()
    return _llm


# Conversation state
_pending_leave_query = None


def chatbot(message: str, history: list) -> str:
    """Handle a single user message and return the assistant response."""
    global _pending_leave_query

    if _pending_leave_query is not None:
        result = confirm_leave(_pending_leave_query, message)
        _pending_leave_query = None
        return result

    retriever = _get_retriever()
    llm = _get_llm()
    response = route(message, retriever, llm)

    if "Confirmation:" in response or "Konfirmasi:" in response:
        _pending_leave_query = message

    return response


examples = [
    "Apa yang bisa kamu lakukan?",
    "Bagaimana cara cuti?",
    "Bagaimana cara reset password?",
    "Bagaimana cara reimbursement?",
    "Saya ingin cuti tanggal 25 Agustus.",
    "What can you do?",
    "How do I reset my password?",
    "How do I submit reimbursement?",
    "I want to apply for leave on August 25.",
]

print("Starting Enterprise Service Desk...")

demo = gr.ChatInterface(
    chatbot,
    title="Enterprise Service Desk",
    description="Multi-Agent RAG Demo\n\nSupported departments:\n\n\u2022 HR\n\u2022 IT\n\u2022 Finance",
    examples=examples,
)

if __name__ == "__main__":
    port = int(__import__("os").getenv("PORT", 7860))
    print(f"PORT={port}")
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
    )
    print("Gradio server has stopped.")
