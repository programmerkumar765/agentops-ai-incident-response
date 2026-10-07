def get_recent_deployments(service: str) -> list[dict]:
    return [
        {
            "service": service,
            "version": "v2.4.1",
            "status": "deployed",
            "risk": "requires investigation"
        }
    ]
