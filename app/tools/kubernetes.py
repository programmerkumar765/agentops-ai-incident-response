def get_kubernetes_status(service: str) -> dict:
    return {
        "service": service,
        "replicas": 4,
        "available_replicas": 3,
        "restart_count": 6,
        "status": "degraded"
    }
