"""Manual smoke test for greetings and small talk."""

from app.agents.supervisor import route

response_en = route("Hello!", None, None)
print(response_en)
print()

response_id = route("Halo", None, None)
print(response_id)