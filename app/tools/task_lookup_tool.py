"""Tool for looking up an employee's active tasks."""

import json
from pathlib import Path


def get_employee_tasks(employee_id: str) -> list[dict]:
    """Return active (In Progress) tasks for a given employee."""
    file_path = (
        Path(__file__).resolve().parent.parent.parent
        / "enterprise_data"
        / "tasks.json"
    )

    with open(file_path, "r") as f:
        tasks = json.load(f)

    return [t for t in tasks if t["employee_id"] == employee_id and t["status"] == "In Progress"]
