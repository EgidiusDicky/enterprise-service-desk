"""Manual smoke test for the IT ticket workflow."""

import json
from pathlib import Path

from app.tools.workflow_tool import create_it_ticket

ticket = create_it_ticket(
    employee_id="EMP001",
    issue="Cannot connect VPN",
)

print("Created IT Ticket:")
print(ticket)
print()

file_path = (
    Path(__file__).resolve().parent.parent
    / "enterprise_data"
    / "it_tickets.json"
)

with open(file_path, "r") as f:
    current = json.load(f)

print("Current IT Tickets:")
print(current)