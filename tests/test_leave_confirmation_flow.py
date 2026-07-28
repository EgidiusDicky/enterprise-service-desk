"""Manual smoke test for leave confirmation flow.

NOTE: This test will prompt for user input.
Type 'no' or 'tidak' to test cancellation.
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

response = answer(
    "Saya ingin cuti tanggal 12 Agustus karena acara keluarga.",
    retriever,
    llm,
)

print(response)