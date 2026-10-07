class RunbookRetriever:
    """Retrieves operational knowledge relevant to an incident."""

    def retrieve(self, query: str) -> list[str]:
        return [
            "Database timeout troubleshooting runbook",
            "Kubernetes pod restart investigation guide"
        ]
