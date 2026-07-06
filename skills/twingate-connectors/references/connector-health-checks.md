# Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks only validate the service state—not network connectivity to Twingate infrastructure. Useful for debugging and automated orchestration responses.

## Key Information
- Returns `OK` with exit code `0` on success; any other response or nonzero exit code indicates failure
- Does **not** check network connectivity to Twingate's infrastructure
- Only indicates whether the Connector service itself is running correctly

## Health Check by Deployment Type

### systemd Service
```bash
twingate-connectorctl health
```

### Docker
```bash
# Status visible in:
docker ps

# Detailed health info:
docker inspect --format "{{json .State.Health }}" <container-name>
```

### Non-Docker Container (e.g., AWS ECS, Kubernetes)
```bash
# Execute inside container:
connectorctl health
```

## Configuration Values

| Context | Command/Value |
|---|---|
| systemd binary | `twingate-connectorctl health` |
| Container binary | `connectorctl health` |
| Docker inspect format | `{{json .State.Health }}` |
| Success response | `OK` |
| Success exit code | `0` |

## Automated Actions
- Override the `Dockerfile HEALTHCHECK` directive in the Twingate container image to trigger custom actions based on health check results
- AWS ECS and similar orchestrators natively support Docker image `HEALTHCHECK` definitions—no extra config needed
- Use orchestration service equivalents (e.g., Kubernetes liveness probes) for non-Docker environments

## Gotchas
- **Health check ≠ connectivity check**: A healthy status does not mean the Connector has established a connection to Twingate's network
- `twingate-connectorctl` (systemd) vs `connectorctl` (container)—note the difference in binary names
- Replace `container-name` with actual container ID when using `docker inspect`

## Related Docs
- Connector deployment (systemd, Docker, ECS)
- Dockerfile HEALTHCHECK override documentation
- Container orchestration service configuration