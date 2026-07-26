"""Evaluate accuracy of the Enterprise Service Desk system."""

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embeddings
from app.rag.vectordb import create_vector_store
from app.rag.retriever import create_retriever
from app.llm import create_llm
from app.agents.hr_agent import answer as hr_answer
from app.agents.it_agent import answer as it_answer
from app.agents.finance_agent import answer as finance_answer


def evaluate_accuracy() -> None:
    """Run test queries and print accuracy summary."""
    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = create_embeddings()
    vector_store = create_vector_store(chunks, embeddings)
    retriever = create_retriever(vector_store)
    llm = create_llm()

    test_cases = [
        {
            "query": "Bagaimana cara mengajukan cuti?",
            "agent": hr_answer,
            "expected_keywords": ["cuti"],
        },
        {
            "query": "Bagaimana cara reset password?",
            "agent": it_answer,
            "expected_keywords": ["password"],
        },
        {
            "query": "Bagaimana cara reimbursement?",
            "agent": finance_answer,
            "expected_keywords": ["reimbursement"],
        },
    ]

    correct = 0
    total = len(test_cases)

    print("=" * 50)
    print("ACCURACY EVALUATION")
    print("=" * 50)

    for case in test_cases:
        response = case["agent"](case["query"], retriever, llm)
        response_lower = response.lower()
        passed = all(
            kw.lower() in response_lower for kw in case["expected_keywords"]
        )
        if passed:
            correct += 1

        print(f"\nQuery: {case['query']}")
        print(f"Pass: {'YES' if passed else 'NO'}")
        print(f"Response: {response[:200]}...")

    print("\n" + "=" * 50)
    print(f"SUMMARY: {correct}/{total} correct ({correct / total * 100:.0f}%)")
    print("=" * 50)


if __name__ == "__main__":
    evaluate_accuracy()