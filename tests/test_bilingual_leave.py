"""Manual smoke test for bilingual leave request workflow.

NOTE: This test will prompt for user input twice.
Type 'no' or 'tidak' to test cancellation for each.
"""

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

print("=== Indonesian Leave Request ===")
response_id = answer(
    "Saya ingin cuti tanggal 12 Agustus karena acara keluarga.",
    retriever,
    llm,
)
print(response_id)
print()

print("=== English Leave Request ===")
response_en = answer(
    "I want to apply for leave on August 12 because of a family event.",
    retriever,
    llm,
)
print(response_en)