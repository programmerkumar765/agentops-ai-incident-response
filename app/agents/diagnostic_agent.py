class DiagnosticAgent:
    """Collects diagnostic evidence from infrastructure tools."""

    def investigate(self, service: str) -> dict:
        return {
            "service": service,
            "evidence": [
                "Elevated API latency detected",
                "Error rate above normal baseline",
                "Recent deployment identified",
                "Infrastructure metrics require correlation"
            ]
        }
