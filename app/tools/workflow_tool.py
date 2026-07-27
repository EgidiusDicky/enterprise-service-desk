"""Tools for creating leave requests, IT tickets, and reimbursements."""

import json
import uuid
from pathlib import Path


def create_reimbursement(employee_id: str, amount: float, description: str) -> dict:
    """Create a new reimbursement request and persist it to the JSON file."""
    file_path = (
        Path(__file__).resolve().parent.parent.parent
        / "enterprise_data"
        / "reimbursements.json"
    )

    with open(file_path, "r") as f:
        reimbursements = json.load(f)

    new_reimbursement = {
        "reimbursement_id": str(uuid.uuid4()),
        "employee_id": employee_id,
        "amount": amount,
        "description": description,
        "status": "Pending",
    }

    reimbursements.append(new_reimbursement)

    with open(file_path, "w") as f:
        json.dump(reimbursements, f, indent=2)

    return new_reimbursement


def create_it_ticket(employee_id: str, issue: str) -> dict:
    """Create a new IT ticket and persist it to the JSON file."""
    file_path = (
        Path(__file__).resolve().parent.parent.parent
        / "enterprise_data"
        / "it_tickets.json"
    )

    with open(file_path, "r") as f:
        tickets = json.load(f)

    new_ticket = {
        "ticket_id": str(uuid.uuid4()),
        "employee_id": employee_id,
        "issue": issue,
        "status": "Open",
    }

    tickets.append(new_ticket)

    with open(file_path, "w") as f:
        json.dump(tickets, f, indent=2)

    return new_ticket


def create_leave_request(
    employee_id: str,
    start_date: str,
    end_date: str,
    reason: str,
) -> dict:
    """Create a new leave request and persist it to the JSON file."""
    file_path = (
        Path(__file__).resolve().parent.parent.parent
        / "enterprise_data"
        / "leave_requests.json"
    )

    with open(file_path, "r") as f:
        requests = json.load(f)

    new_request = {
        "request_id": str(uuid.uuid4()),
        "employee_id": employee_id,
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "status": "Pending",
    }

    requests.append(new_request)

    with open(file_path, "w") as f:
        json.dump(requests, f, indent=2)

    return new_request