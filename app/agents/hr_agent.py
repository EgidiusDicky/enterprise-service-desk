"""HR specialist agent for handling HR-related queries."""

from langchain_core.language_models import BaseLanguageModel
from langchain_core.retrievers import BaseRetriever

from app.tools.retrieve_tool import retrieve_context
from app.tools.validation_tool import validate_context
from app.tools.response_tool import generate_response
from app.tools.workflow_tool import create_leave_request
from app.tools.task_lookup_tool import get_employee_tasks


def answer(query: str, retriever: BaseRetriever, llm: BaseLanguageModel) -> str:
    """Answer an HR query using retrieval and LLM generation."""
    documents = retrieve_context(retriever, query)

    if not validate_context(documents):
        return "I don't have enough information from the HR knowledge base."

    response = generate_response(llm, query, documents)

    query_lower = query.lower()
    is_request = "cuti" in query_lower and "bagaimana" not in query_lower

    if is_request:
        tasks = get_employee_tasks("EMP001")

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

        leave_request = create_leave_request(
            employee_id="EMP001",
            start_date="2026-08-12",
            end_date="2026-08-14",
            reason=query,
        )
        response += (
            f"\n\nLeave request has been created successfully.\n"
            f"Current status: {leave_request['status']}."
        )

    return response