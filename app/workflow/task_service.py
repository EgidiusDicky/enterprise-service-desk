"""Task data service layer.

Provides task lookup from JSON data store.
"""

import json

_EMPLOYEES_PATH = "enterprise_data/employees.json"
_TASKS_PATH = "enterprise_data/tasks.json"


def get_tasks(employee_name: str) -> list:
    """Return all tasks belonging to the given employee.

    Args:
        employee_name: The employee name to look up tasks for.

    Returns:
        List of task dictionaries for the employee.
    """
    with open(_EMPLOYEES_PATH) as f:
        employees = json.load(f)

    employee_id = None
    for emp in employees:
        if emp["name"] == employee_name:
            employee_id = emp["id"]
            break

    if employee_id is None:
        return []

    with open(_TASKS_PATH) as f:
        tasks = json.load(f)

    result = []
    for task in tasks:
        if task["employee_id"] == f"EMP{employee_id:03d}":
            result.append(task)

    return result