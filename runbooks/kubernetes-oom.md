# Kubernetes OOM Runbook

## Symptoms

- Container restarts
- OOMKilled pod status
- High memory utilization

## Investigation

Review pod memory consumption, resource limits, deployment changes, and application memory behavior.

## Safety

Scaling or restarting workloads should require human approval in production environments.
