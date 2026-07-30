"""Gradio demo for Enterprise Service Desk on Hugging Face Spaces."""

import gradio as gr

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever
from app.llm import create_llm
from app.agents.supervisor import route
from app.agents.hr_agent import confirm_leave

# Build the RAG pipeline once at startup.
documents = load_documents()
chunks = split_documents(documents)
embeddings = create_embeddings()
vector_store = create_vector_store(chunks, embeddings)
retriever = create_retriever(vector_store)
llm = create_llm()

# Conversation state
_pending_leave_query = None


def chatbot(message: str, history: list) -> str:
    """Handle a single user message and return the assistant response."""
    global _pending_leave_query

    # Check if we're waiting for leave confirmation
    if _pending_leave_query is not None:
        result = confirm_leave(_pending_leave_query, message)
        _pending_leave_query = None
        return result

    # Normal routing
    response = route(message, retriever, llm)

    # Check if HR returned a confirmation prompt
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

demo = gr.ChatInterface(
    chatbot,
    title="Enterprise Service Desk",
    description="Multi-Agent RAG Demo\n\nSupported departments:\n\n\u2022 HR\n\u2022 IT\n\u2022 Finance",
    examples=examples,
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
