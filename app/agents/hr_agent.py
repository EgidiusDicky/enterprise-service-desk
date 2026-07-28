"""HR specialist agent for handling HR-related queries."""

from langchain_core.language_models import BaseLanguageModel
from langchain_core.retrievers import BaseRetriever

from app.tools.retrieve_tool import retrieve_context
from app.tools.validation_tool import validate_context
from app.tools.response_tool import generate_response
from app.tools.workflow_tool import create_leave_request
from app.tools.task_lookup_tool import get_employee_tasks


_LEAVE_KEYWORDS = ["cuti", "izin", "leave", "vacation", "holiday", "day off"]


def answer(query: str, retriever: BaseRetriever, llm: BaseLanguageModel) -> str:
    """Answer an HR query using retrieval and LLM generation."""
    documents = retrieve_context(retriever, query)

    if not validate_context(documents):
        return "I don't have enough information from the HR knowledge base."

    response = generate_response(llm, query, documents)

    query_lower = query.lower()
    is_leave_knowledge = any(kw in query_lower for kw in ["bagaimana", "how"])
    has_leave_kw = any(kw in query_lower for kw in _LEAVE_KEYWORDS)
    is_request = has_leave_kw and not is_leave_knowledge

    if is_request:
        tasks = get_employee_tasks("EMP001")
        is_id = any(kw in query_lower for kw in ["cuti", "izin"])

        if is_id:
            if tasks:
                response += (
                    f"\n\nRekomendasi:\n"
                    f"Anda memiliki {len(tasks)} tugas aktif.\n"
                    f"Silakan koordinasikan penyerahan tugas dengan atasan sebelum cuti."
                )
                response += "\n\nTugas Aktif Saat Ini:"
                for task in tasks:
                    response += f"\n- {task['title']} (Tenggat: {task['deadline']})"
            else:
                response += (
                    "\n\nRekomendasi:\n"
                    "Tidak ada tugas aktif yang ditemukan.\n"
                    "Pengajuan cuti Anda dapat diproses."
                )
            response += "\n\nKonfirmasi:\nApakah Anda ingin mengajukan cuti ini?\nBalas dengan:\n- Ya\n- Tidak"

            print(response)
            print()

            confirm = input("You > ").strip().lower()
            if confirm in ("ya", "iya", "y", "yes"):
                leave_request = create_leave_request(
                    employee_id="EMP001",
                    start_date="2026-08-12",
                    end_date="2026-08-14",
                    reason=query,
                )
                return (
                    f"Pengajuan cuti berhasil dibuat.\n"
                    f"Status saat ini: {leave_request['status']}."
                )
            else:
                return "Pengajuan cuti dibatalkan."
        else:
            if tasks:
                response += (
                    f"\n\nRecommendation:\n"
                    f"You currently have {len(tasks)} active task(s).\n"
                    f"Please coordinate task handover with your supervisor before your leave begins."
                )
                response += "\n\nCurrent Active Tasks:"
                for task in tasks:
                    response += f"\n- {task['title']} (Deadline: {task['deadline']})"
            else:
                response += (
                    "\n\nRecommendation:\n"
                    "No active tasks were found.\n"
                    "Your leave request can proceed normally."
                )
            response += "\n\nConfirmation:\nDo you want to submit this leave request?\nReply with:\n- Yes\n- No"

            print(response)
            print()

            confirm = input("You > ").strip().lower()
            if confirm in ("yes", "y", "ya", "iya"):
                leave_request = create_leave_request(
                    employee_id="EMP001",
                    start_date="2026-08-12",
                    end_date="2026-08-14",
                    reason=query,
                )
                return (
                    f"Leave request has been created successfully.\n"
                    f"Current status: {leave_request['status']}."
                )
            else:
                return "Leave request cancelled."

    return response