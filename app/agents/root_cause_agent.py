class RootCauseAgent:
    """Produces a structured root-cause hypothesis from collected evidence."""

    def analyze(self, evidence: list[str]) -> dict:
        return {
            "root_cause": "Potential downstream dependency degradation",
            "confidence": 0.82,
            "evidence": evidence,
            "requires_validation": True
        }
