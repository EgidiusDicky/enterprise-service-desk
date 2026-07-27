"""Manual smoke test for the HR leave confirmation workflow."""

import json
from pathlib import Path

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever
from app.llm import create_llm
from app.agents.hr_agent import answer

documents = load_documents()
chunks = split_documents(documents)
embeddings = create_embeddings()
vector_store = create_vector_store(chunks, embeddings)
retriever = create_retriever(vector_store)
llm = create_llm()

response = answer(
    "Saya ingin cuti tanggal 12 Agustus karena acara keluarga.",
    retriever,
    llm,
)

print(response)
print()

file_path = (
    Path(__file__).resolve().parent.parent
    / "enterprise_data"
    / "leave_requests.json"
)

with open(file_path, "r") as f:
    current = json.load(f)

print(current)