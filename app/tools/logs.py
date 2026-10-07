def get_service_logs(service: str) -> list[str]:
    return [
        f"{service}: request timeout detected",
        f"{service}: downstream dependency latency increased",
        f"{service}: connection timeout threshold exceeded"
    ]
