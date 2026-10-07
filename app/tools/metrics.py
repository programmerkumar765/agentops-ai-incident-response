def get_service_metrics(service: str) -> dict:
    return {
        "service": service,
        "error_rate_percent": 18.2,
        "p95_latency_ms": 4800,
        "cpu_percent": 54,
        "memory_percent": 61
    }
