"""Manual smoke test for bilingual routing."""

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever
from app.llm import create_llm
from app.agents.supervisor import route

documents = load_documents()
chunks = split_documents(documents)
embeddings = create_embeddings()
vector_store = create_vector_store(chunks, embeddings)
retriever = create_retriever(vector_store)
llm = create_llm()

queries = [
    "Halo",
    "Hello",
    "Apa yang bisa kamu lakukan?",
    "What can you do?",
    "How do I reset my password?",
    "How do I submit reimbursement?",
]

for q in queries:
    print(f"=== {q} ===")
    print(route(q, retriever, llm))
    print()