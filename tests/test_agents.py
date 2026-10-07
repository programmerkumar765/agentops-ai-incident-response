from app.agents.safety_agent import SafetyAgent


def test_destructive_action_is_blocked():
    agent = SafetyAgent()

    result = agent.validate_action("delete_deployment")

    assert result["allowed"] is False
