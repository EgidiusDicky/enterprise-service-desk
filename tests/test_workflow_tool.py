"""Manual smoke test for the workflow tool."""

import json
from pathlib import Path

from app.tools.workflow_tool import create_leave_request

new_request = create_leave_request(
    employee_id="EMP001",
    start_date="2026-08-12",
    end_date="2026-08-14",
    reason="Family Event",
)

print("Created Leave Request")
print(new_request)
print()

file_path = (
    Path(__file__).resolve().parent.parent
    / "enterprise_data"
    / "leave_requests.json"
)

with open(file_path, "r") as f:
    current = json.load(f)

print("Current leave_requests.json content")
print(current)