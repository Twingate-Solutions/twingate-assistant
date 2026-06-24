# Connector Health Checks

## Page Title
Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks confirm service status only — they do not validate network connectivity to Twingate infrastructure.

## Key Information
- Returns `OK` with exit code `0` on success
- Any other response or non-zero exit code = failed health check
- Does **not** check network connectivity to Twingate's infrastructure
- Only indicates whether the Connector service itself is running

## Prerequisites
- A deployed Twingate Connector (systemd, Docker, or container)

## Step-by-Step by Deployment Type

### systemd
```bash
twingate-connectorctl health
```

### Docker
```bash
# View status summary
docker ps

# View detailed health state
docker inspect --format "{{json .State.Health }}" <container-name>
```

### Other Container Orchestration (e.g., AWS ECS)
- ECS and similar services natively support Docker image `HEALTHCHECK` definitions — no extra config needed
- Otherwise, exec into container and run:
```bash
connectorctl health
```

## Configuration Values

| Context | Command/Flag |
|---|---|
| systemd | `twingate-connectorctl health` |
| Docker inspect format flag | `"{{json .State.Health }}"` |
| Non-Docker container | `connectorctl health` |

## Automation / Custom Health Check Behavior
Override the `Dockerfile HEALTHCHECK` directive in the Twingate container image, or use your orchestration platform's equivalent mechanism to trigger automated actions based on health check results.

## Gotchas
- Health check **passing** does not mean the Connector has established connectivity to Twingate — only that the service process is running
- `twingate-connectorctl` (with prefix) is used for systemd; `connectorctl` (no prefix) is used inside containers
- Docker health check status is built-in; no manual invocation required when using Docker

## Related Docs
- Connector deployment (systemd, Docker, container orchestration)
- Dockerfile HEALTHCHECK override documentation