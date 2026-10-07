from app.mcp.tools import AVAILABLE_TOOLS


class MCPToolServer:
    """Lightweight abstraction representing tools exposed to AI agents."""

    def list_tools(self):
        return list(AVAILABLE_TOOLS.keys())

    def execute(self, tool_name: str, **kwargs):
        if tool_name not in AVAILABLE_TOOLS:
            raise ValueError(f"Unknown MCP tool: {tool_name}")

        return AVAILABLE_TOOLS[tool_name](**kwargs)
