"""Supervisor agent that routes user requests to specialist agents."""

from langchain_core.language_models import BaseLanguageModel
from langchain_core.retrievers import BaseRetriever

from app.agents.hr_agent import answer as hr_answer
from app.agents.it_agent import answer as it_answer
from app.agents.finance_agent import answer as finance_answer


_GREETING_EN = (
    "Hello!\n"
    "I'm the Enterprise Service Desk Assistant.\n\n"
    "I can help you with:\n\n"
    "\u2022 HR\n"
    "\u2022 IT\n"
    "\u2022 Finance\n\n"
    "How can I help you today?"
)

_GREETING_ID = (
    "Halo!\n"
    "Saya adalah Enterprise Service Desk Assistant.\n\n"
    "Saya dapat membantu mengenai:\n\n"
    "\u2022 HR\n"
    "\u2022 IT\n"
    "\u2022 Finance\n\n"
    "Ada yang bisa saya bantu?"
)

_CAPABILITIES_EN = (
    "I can help you with:\n\n"
    "\u2022 HR \u2014 leave, permit, overtime, BPJS\n"
    "\u2022 IT \u2014 password, VPN, email, laptop\n"
    "\u2022 Finance \u2014 reimbursement, invoice, payment, purchase"
)

_CAPABILITIES_ID = (
    "Saya dapat membantu mengenai:\n\n"
    "\u2022 HR \u2014 cuti, izin, lembur, BPJS\n"
    "\u2022 IT \u2014 password, VPN, email, laptop\n"
    "\u2022 Finance \u2014 reimbursement, invoice, pembayaran, pembelian"
)

_CAP_QUERIES_EN = [
    "what can you do",
    "what are your capabilities",
]

_CAP_QUERIES_ID = [
    "apa yang bisa kamu lakukan",
    "apa yang dapat kamu lakukan",
]

_GREETINGS_EN = {
    "hello", "helo", "helloo", "hi", "hii", "hey", "yo",
    "good morning", "good afternoon", "good evening",
}
_GREETINGS_ID = {
    "halo", "haloo", "hallo", "hai", "hy", "oi",
    "selamat pagi", "selamat siang", "selamat sore", "selamat malam",
}

HR_KEYWORDS = ["cuti", "izin", "lembur", "bpjs", "leave", "vacation", "holiday"]
IT_KEYWORDS = ["password", "vpn", "wifi", "email", "login", "account", "laptop"]
FINANCE_KEYWORDS = ["reimbursement", "invoice", "pembayaran", "pembelian", "expense", "claim"]



def route(
    query: str,
    retriever: BaseRetriever,
    llm: BaseLanguageModel,
    confirm: str | None = None,
) -> str:
    """Route a query to the appropriate department agent based on keywords.

    Args:
        query: The user's query.
        retriever: The document retriever.
        llm: The language model.
        confirm: Confirmation response for leave requests.
                 When None (CLI mode), the agent uses input().
                 When a string (Gradio mode), it uses that value.
    """
    query_lower = query.lower().strip()

    if query_lower.rstrip("?.") in _GREETINGS_EN:
        return _GREETING_EN

    if query_lower.rstrip("?.") in _GREETINGS_ID:
        return _GREETING_ID

    if query_lower.rstrip("?.") in _CAP_QUERIES_EN:
        return _CAPABILITIES_EN

    if query_lower.rstrip("?.") in _CAP_QUERIES_ID:
        return _CAPABILITIES_ID

    if any(kw in query_lower for kw in HR_KEYWORDS):
        return hr_answer(query, retriever, llm, confirm=confirm)

    if any(kw in query_lower for kw in IT_KEYWORDS):
        return it_answer(query, retriever, llm)

    if any(kw in query_lower for kw in FINANCE_KEYWORDS):
        return finance_answer(query, retriever, llm)

    return "I cannot determine which department should answer your request."