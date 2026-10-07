from app.agents.triage_agent import TriageAgent
from app.agents.diagnostic_agent import DiagnosticAgent
from app.agents.root_cause_agent import RootCauseAgent
from app.agents.remediation_agent import RemediationAgent


class IncidentWorkflow:
    """Agent workflow for incident investigation."""

    def __init__(self):
        self.triage = TriageAgent()
        self.diagnostics = DiagnosticAgent()
        self.root_cause = RootCauseAgent()
        self.remediation = RemediationAgent()

    def process(self, incident):
        triage_result = self.triage.analyze(incident)

        diagnostics = self.diagnostics.investigate(
            triage_result["affected_service"]
        )

        root_cause = self.root_cause.analyze(
            diagnostics["evidence"]
        )

        remediation = self.remediation.recommend(
            root_cause["root_cause"]
        )

        return {
            "triage": triage_result,
            "diagnostics": diagnostics,
            "root_cause": root_cause,
            "remediation": remediation
        }
