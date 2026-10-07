# AgentOps Guardian

## Agentic AI Incident Response Platform

AgentOps Guardian is a production-oriented Agentic AI engineering project designed to demonstrate autonomous incident investigation, tool-enabled reasoning, retrieval-augmented generation, safety controls, evaluation, and human-in-the-loop remediation.

## Core AI Engineering Capabilities

- Agentic AI orchestration
- Multi-agent workflow design
- MCP-style tool integration
- Retrieval-Augmented Generation (RAG)
- Operational runbook retrieval
- Root-cause analysis
- AI-assisted incident triage
- Human-in-the-loop remediation
- AI safety and tool authorization
- LLM evaluation
- Observability-ready architecture

## AI Agents

### Triage Agent

Determines incident severity, affected services, and investigation strategy.

### Diagnostic Agent

Collects application logs, service metrics, Kubernetes status, and deployment history.

### Root Cause Agent

Correlates operational evidence and generates structured root-cause hypotheses.

### Remediation Agent

Generates remediation recommendations while requiring human approval.

### Safety Agent

Blocks destructive actions and applies authorization policies before tool execution.

## Architecture

```text
Production Alert
      |
      v
Triage Agent
      |
      v
Diagnostic Agent
      |
      +------ Logs
      +------ Metrics
      +------ Kubernetes
      +------ Deployments
      |
      v
RAG / Operational Knowledge
      |
      v
Root Cause Agent
      |
      v
Remediation Agent
      |
      v
Safety Agent
      |
      v
Human Approval

ls
