from typing import List, Optional
from pydantic import BaseModel


class Incident(BaseModel):
    incident_id: str
    service: str
    severity: str
    error_rate: float
    p95_latency_ms: float
    description: Optional[str] = None


class RootCauseAnalysis(BaseModel):
    root_cause: str
    confidence: float
    evidence: List[str]
    recommended_actions: List[str]
    human_approval_required: bool = True
