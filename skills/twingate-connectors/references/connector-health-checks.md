# Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks only validate service state, not network connectivity to Twingate infrastructure.

## Key Information
- Returns `OK` with exit code `0` on success; any other response or nonzero exit code = failure
- Does **not** verify network connectivity to Twingate infrastructure
- Built into the Docker container image natively

## Prerequisites
- A deployed Twingate Connector (systemd, Docker, or container orchestration)

## Running a Health Check by Deployment Type

| Deployment | Command/Method |
|---|---|
| systemd | `twingate-connectorctl health` |
| Docker | `docker ps` (check Status column) |
| Docker (detailed) | `docker inspect --format "{{json .State.Health }}" <container-name>` |
| Generic container | `connectorctl health` (exec inside container) |
| AWS ECS | Natively supported via Docker image health check definition — no extra config needed |

## Configuration Values
- **Dockerfile HEALTHCHECK**: Can be overridden in the container image to trigger automated actions based on health check results
- **Orchestration equivalent**: Use your platform's native health check hook to automate responses

## Gotchas
- A healthy response does **not** mean the Connector has established connectivity to Twingate's infrastructure — only that the service process is running
- For Docker, `docker ps` shows basic status; `docker inspect` provides full health detail
- For non-Docker container runtimes, you must exec `connectorctl health` manually unless the orchestrator supports Docker-native health check definitions

## Related Docs
- Connector deployment (systemd, Docker, container orchestration)
- Dockerfile HEALTHCHECK override documentation