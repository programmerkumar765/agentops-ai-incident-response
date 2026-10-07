# Database Timeout Runbook

## Symptoms

- Elevated API latency
- Database connection exhaustion
- Request timeout errors

## Investigation

1. Check active database connections.
2. Inspect connection-pool utilization.
3. Review recently deployed queries.
4. Check slow-query metrics.

## Remediation

Potential remediation actions include query optimization, connection-pool tuning, or rollback of a problematic deployment.
