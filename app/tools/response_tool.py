"""Tool for generating LLM responses from retrieved context."""

from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel


def generate_response(
    llm: BaseLanguageModel, query: str, documents: list[Document]
) -> str:
    """Generate an answer using the LLM given context and user query."""
    context = "\n\n".join(doc.page_content for doc in documents)
    query_lower = query.lower()
    is_indonesian = any(kata in query_lower for kata in
        ["bagaimana", "apakah", "saya", "kamu", "bisa", "tolong",
         "cuti", "izin", "lembur", "bpjs",
         "pembayaran", "pembelian", "pengajuan"])

    lang_instruction = "Use Indonesian." if is_indonesian else "Use English."

    prompt = (
        "You are an internal enterprise assistant.\n"
        "Answer ONLY using the provided context.\n"
        "Do not add assumptions.\n"
        "Do not invent procedures.\n"
        "If the answer is not found in the context, reply:\n"
        "'I don't have enough information from the knowledge base.'\n"
        "Answer in at most 3 bullet points.\n"
        "Maximum 80 words.\n"
        "Do not repeat the user's question.\n"
        "Be concise.\n"
        "Answer only what was asked.\n"
        f"{lang_instruction}\n"
        f"\nContext:\n{context}"
        f"\n\nQuestion: {query}\n\nAnswer:"
    )
    result = llm.invoke(prompt)
    return result if isinstance(result, str) else result.content