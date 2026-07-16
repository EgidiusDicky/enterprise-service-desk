"""Supervisor agent that routes user requests to specialist agents."""


class SupervisorAgent:
    """Routes user queries to the appropriate department agent."""

    def route(self, query: str) -> str:
        """Determine which department should handle the query."""
        pass