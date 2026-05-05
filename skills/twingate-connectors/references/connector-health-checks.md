# Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks confirm service status only — they do not validate network connectivity to Twingate infrastructure.

## Key Information
- Returns `OK` with exit code `0` on success
- Any other response or nonzero exit code indicates failure
- Does **not** check Twingate network connectivity — only service health
- Docker deployments have health checks built into the container image

## Health Check Commands by Deployment Type

| Deployment | Command/Method |
|---|---|
| systemd | `twingate-connectorctl health` |
| Docker | Built-in; visible via `docker ps` under Status |
| Non-Docker container | `connectorctl health` (exec inside container) |

## Step-by-Step

### systemd
```bash
twingate-connectorctl health
```

### Docker
```bash
# Quick status
docker ps

# Detailed health info
docker inspect --format "{{json .State.Health }}" <container-name>
```

### Non-Docker Container (e.g., AWS ECS)
```bash
# Execute inside the container
connectorctl health
```

## Configuration Values
- **Success response:** `OK`
- **Success exit code:** `0`
- **Failure:** Any non-`OK` response or nonzero exit code

## Automation / Custom Health Check Behavior
- Override the `Dockerfile HEALTHCHECK` directive in the Twingate container image to trigger automated actions
- Or use your orchestration platform's native health check equivalent (e.g., ECS health check definitions natively support Docker image health check specs — no extra config needed)

## Gotchas
- A healthy result **does not mean** the Connector has established connectivity to Twingate's infrastructure — only that the service process is running
- For non-Docker orchestration platforms without native Docker health check support, you must manually exec `connectorctl health` inside the container
- `docker inspect` requires the container name or ID — not a container image name

## Related Docs
- Connector deployment (systemd, Docker, ECS)
- Twingate Connector configuration
- Docker HEALTHCHECK documentation