# Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks confirm service status only—they do not validate network connectivity to Twingate infrastructure.

## Key Information
- Returns `OK` with exit code `0` on success
- Any other response or non-zero exit code = failure
- Does **not** check connectivity to Twingate's infrastructure
- Only reports unhealthy if the Connector service itself is not running correctly

## Health Check by Deployment Type

### systemd
```bash
twingate-connectorctl health
```

### Docker
- Health check is built into the container image
- Visible in `Status` column via `docker ps`
- Detailed output:
```bash
docker inspect --format "{{json .State.Health }}" <container-name>
```

### Other Container Orchestration (ECS, etc.)
- AWS ECS and similar services with native Docker HEALTHCHECK support: no additional config required
- Manual check inside container:
```bash
connectorctl health
```

## Automation / Custom Configuration
- Override the `Dockerfile HEALTHCHECK` directive in the Twingate container image to trigger automated actions on health check results
- Use your orchestration platform's equivalent health check mechanism

## Gotchas
- Health check **passing** does not mean the Connector has established connectivity to Twingate—only that the service process is running
- `twingate-connectorctl` (systemd) vs `connectorctl` (container) — command differs by deployment type

## Related Docs
- Connector deployment (systemd, Docker, ECS)
- Dockerfile HEALTHCHECK reference