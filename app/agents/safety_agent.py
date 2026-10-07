class SafetyAgent:
    """Applies approval and policy controls to remediation actions."""

    DESTRUCTIVE_ACTIONS = {
        "delete_deployment",
        "drop_database",
        "terminate_cluster"
    }

    def validate_action(self, action: str) -> dict:
        if action in self.DESTRUCTIVE_ACTIONS:
            return {
                "allowed": False,
                "reason": "Destructive operation blocked by AI safety policy."
            }

        return {
            "allowed": True,
            "human_approval_required": True
        }
