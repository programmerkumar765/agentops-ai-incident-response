from app.tools.logs import get_service_logs
from app.tools.metrics import get_service_metrics
from app.tools.kubernetes import get_kubernetes_status
from app.tools.deployments import get_recent_deployments


AVAILABLE_TOOLS = {
    "get_service_logs": get_service_logs,
    "get_service_metrics": get_service_metrics,
    "get_kubernetes_status": get_kubernetes_status,
    "get_recent_deployments": get_recent_deployments
}
