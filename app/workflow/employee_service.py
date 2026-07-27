"""Employee data service layer.

Provides employee lookup from JSON data store.
"""

import json

_EMPLOYEES_PATH = "enterprise_data/employees.json"


def get_employee(name: str) -> dict | None:
    """Look up an employee by name.

    Args:
        name: The employee name to search for.

    Returns:
        Employee dictionary if found, None otherwise.
    """
    with open(_EMPLOYEES_PATH) as f:
        employees = json.load(f)

    for employee in employees:
        if employee["name"] == name:
            return employee

    return None