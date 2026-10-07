from app.models.incident import Incident


class TriageAgent:
    """Classifies incidents and determines investigation priorities."""

    def analyze(self, incident: Incident) -> dict:
        priority = "HIGH"

        if incident.severity.lower() in {"critical", "sev1"}:
            priority = "CRITICAL"
        elif incident.error_rate < 5 and incident.p95_latency_ms < 1000:
            priority = "MEDIUM"

        return {
            "incident_id": incident.incident_id,
            "priority": priority,
            "affected_service": incident.service,
            "investigation_required": True,
            "recommended_tools": [
                "service_logs",
                "service_metrics",
                "deployment_history",
                "kubernetes_status"
            ]
        }
