# Connector Health Checks

## Page Title
Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks confirm service status only — they do not verify network connectivity to Twingate infrastructure.

## Key Information
- Returns `OK` with exit code `0` on success
- Any other response or non-zero exit code indicates failure
- Does **not** check network connectivity to Twingate's infrastructure — only confirms the service process is healthy

## Prerequisites
- A deployed Twingate Connector (systemd, Docker, or container orchestration)

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
- ECS and similar services that support Docker image health check definitions work natively — no extra config needed
- Otherwise, exec into the container and run:
```bash
connectorctl health
```

## Configuration Values
| Context | Command/Config |
|---|---|
| systemd | `twingate-connectorctl health` |
| Docker inspect | `docker inspect --format "{{json .State.Health }}" <container-name>` |
| Generic container | `connectorctl health` |
| Custom automation | Override `Dockerfile HEALTHCHECK` directive |

## Gotchas
- Health check **passing does not mean the Connector has network access** to Twingate — it only confirms the service process is running
- For non-Docker orchestration platforms without native Docker healthcheck support, you must exec the command manually or script it
- Override the `HEALTHCHECK` in the Dockerfile if you need custom automated actions on health state changes

## Related Docs
- Connector deployment guides (systemd, Docker, container orchestration)
- Twingate Connector Docker image reference