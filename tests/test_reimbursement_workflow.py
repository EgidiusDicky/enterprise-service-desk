"""Manual smoke test for the reimbursement workflow."""

import json
from pathlib import Path

from app.tools.workflow_tool import create_reimbursement

reimbursement = create_reimbursement(
    employee_id="EMP001",
    amount=250000,
    description="Taxi from airport",
)

print("Created Reimbursement:")
print(reimbursement)
print()

file_path = (
    Path(__file__).resolve().parent.parent
    / "enterprise_data"
    / "reimbursements.json"
)

with open(file_path, "r") as f:
    current = json.load(f)

print("Current Reimbursements:")
print(current)