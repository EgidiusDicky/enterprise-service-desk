"""Leave request service layer.

Provides leave request persistence to JSON data store.
"""

import json

_LEAVE_PATH = "enterprise_data/leave_requests.json"


def create_leave_request(request: dict) -> dict:
    """Append a leave request to the data store.

    Args:
        request: The leave request dictionary to persist.

    Returns:
        The same request dictionary that was created.
    """
    with open(_LEAVE_PATH) as f:
        requests = json.load(f)

    requests.append(request)

    with open(_LEAVE_PATH, "w") as f:
        json.dump(requests, f, indent=2)

    return request