from fastapi import FastAPI

app = FastAPI(
    title="AgentOps Guardian",
    description="Agentic AI platform for autonomous incident investigation and root cause analysis.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "AgentOps Guardian",
        "status": "active",
        "capabilities": [
            "Agentic incident triage",
            "Root cause analysis",
            "RAG-based runbook retrieval",
            "MCP tool integration",
            "Human-in-the-loop remediation",
            "LLM evaluation and observability"
        ]
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
