"""Manual smoke test for the task lookup tool."""

from app.tools.task_lookup_tool import get_employee_tasks

tasks = get_employee_tasks("EMP001")

print("Active Tasks:")
print(tasks)