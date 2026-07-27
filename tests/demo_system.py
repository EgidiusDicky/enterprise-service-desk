"""End-to-end demonstration of the enterprise service desk."""

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

print("========================================")
print("ENTERPRISE SERVICE DESK DEMO")
print("========================================")
print()

queries = [
    "Bagaimana cara mengajukan cuti?",
    "Bagaimana cara reset password?",
    "Bagaimana cara reimbursement?",
]

for query in queries:
    print("========================================")
    print("USER")
    print(query)
    print()
    print("ASSISTANT")
    response = route(query, retriever, llm)
    print(response)
    print()
    print("========================================")

print("========================================")
print("END OF DEMO")
print("========================================")