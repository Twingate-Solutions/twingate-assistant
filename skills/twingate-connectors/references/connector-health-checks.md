# Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks only validate service state, not network connectivity to Twingate infrastructure. Useful for debugging and automated monitoring.

## Key Information
- Health check returns `OK` with exit code `0` on success
- Non-zero exit code or any other response indicates failure
- Does **not** verify network connectivity to Twingate infrastructure
- Only checks if the Connector service itself is running correctly

## Health Check Commands by Deployment Type

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

### Container (non-Docker orchestration)
```bash
connectorctl health
```
- AWS ECS natively supports Docker image health check definitions — no additional config needed
- Other orchestrators: exec `connectorctl health` inside the container

## Configuration Values
| Context | Command/Value |
|---|---|
| systemd binary | `twingate-connectorctl health` |
| Container binary | `connectorctl health` |
| Success exit code | `0` |
| Success response | `OK` |

## Automation
- Override the `Dockerfile HEALTHCHECK` directive in the Twingate container image to trigger custom actions based on health check results
- Or use your orchestration platform's native health check equivalent

## Gotchas
- A healthy result does **not** mean the Connector has established connectivity to Twingate's infrastructure — only that the service process is running
- `twingate-connectorctl` (systemd) vs `connectorctl` (container) — different binary names per deployment type
- Replace `container-name` with the actual container ID when using `docker inspect`

## Related Docs
- Connector deployment (systemd, Docker, container orchestration)
- Dockerfile HEALTHCHECK override documentation