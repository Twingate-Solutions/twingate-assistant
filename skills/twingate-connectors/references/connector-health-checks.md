---
source: https://www.twingate.com/docs/connector-health-checks
type: docs
fetched: 2026-08-14
source_version: c1143a494d222456ade9b5cc6e1e21d9173f2e21ed8055dd165b8b5f91316e5c
---

# Connector Health Checks

## Summary
Twingate Connectors include a built-in health check mechanism to verify the Connector service is running correctly. Health checks only validate service status—not network connectivity to Twingate infrastructure. Returns `OK` with exit code `0` on success; any other response or nonzero exit code indicates failure.

## Key Information
- Health checks confirm the Connector **service is running**, not that it has established network connectivity to Twingate
- Success response: `OK` + exit code `0`
- Failure: any other response or nonzero exit code

## Prerequisites
- A deployed Twingate Connector (systemd, Docker, or other container)

## Running a Health Check by Deployment Type

| Deployment | Command/Method |
|---|---|
| systemd | `twingate-connectorctl health` |
| Docker | Built-in; visible via `docker ps` under **Status** |
| Non-Docker container | `connectorctl health` inside the container |

### Docker Detailed Inspection
```bash
docker inspect --format "{{json .State.Health }}" <container-name>
```
Replace `<container-name>` with the container ID or name.

## Automation / Custom Actions
- Override the `Dockerfile HEALTHCHECK` directive in the Twingate container image to trigger custom actions based on health check results
- Use your orchestration service's native health check equivalent (e.g., AWS ECS natively supports Docker image health check definitions—no additional config needed)

## Gotchas
- A **healthy** status does **not** mean the Connector has connectivity to Twingate's infrastructure
- For non-Docker orchestrators without native Docker health check support, you must exec `connectorctl health` inside the container manually or via orchestration hooks

## Related Docs
- Connector deployment guides (systemd, Docker, container orchestration)
- Twingate Connector configuration reference