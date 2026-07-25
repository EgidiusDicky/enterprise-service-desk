"""Tool for creating leave requests."""

import json
import uuid
from pathlib import Path


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