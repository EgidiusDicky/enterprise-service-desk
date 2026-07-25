"""Supervisor agent that routes user requests to specialist agents."""

from langchain_core.language_models import BaseLanguageModel
from langchain_core.retrievers import BaseRetriever

from app.agents.hr_agent import answer as hr_answer
from app.agents.it_agent import answer as it_answer
from app.agents.finance_agent import answer as finance_answer


def route(query: str, retriever: BaseRetriever, llm: BaseLanguageModel) -> str:
    """Route a query to the appropriate department agent based on keywords."""
    query_lower = query.lower()

    hr_keywords = ["cuti", "izin", "lembur", "bpjs"]
    it_keywords = ["password", "vpn", "email", "laptop"]
    finance_keywords = ["reimbursement", "invoice", "pembayaran", "pembelian"]

    if any(kw in query_lower for kw in hr_keywords):
        return hr_answer(query, retriever, llm)

    if any(kw in query_lower for kw in it_keywords):
        return it_answer(query, retriever, llm)

    if any(kw in query_lower for kw in finance_keywords):
        return finance_answer(query, retriever, llm)

    return "I cannot determine which department should answer your request."