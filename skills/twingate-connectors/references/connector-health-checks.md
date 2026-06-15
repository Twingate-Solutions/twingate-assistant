# Connector Health Checks

## Page Title
Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks confirm service status only—they do not validate network connectivity to Twingate infrastructure. Returns `OK` with exit code `0` on success; any other response or nonzero exit code indicates failure.

## Key Information
- Health checks verify **service health only**, not network/connectivity status to Twingate
- Success response: `OK` + exit code `0`
- Failure: any other response or nonzero exit code

## Prerequisites
- A running Twingate Connector deployed via systemd, Docker, or container orchestration

## Step-by-Step by Deployment Type

### systemd
```bash
twingate-connectorctl health
```

### Docker
```bash
# Quick status
docker ps  # check "Status" column

# Detailed health info
docker inspect --format "{{json .State.Health }}" <container-name>
```

### Other Container Orchestration (ECS, etc.)
```bash
# Execute inside container
connectorctl health
```
- AWS ECS and similar services natively support Docker image health check definitions—no extra config needed

## Configuration Values

| Context | Command/Config |
|---|---|
| systemd | `twingate-connectorctl health` |
| Docker (in-container) | `connectorctl health` |
| Docker (host) | `docker inspect --format "{{json .State.Health }}" <container-name>` |
| Custom automation | Override `Dockerfile HEALTHCHECK` directive |

## Gotchas
- Health check returning **healthy ≠ network connectivity established** — a passing check only means the service process is running
- For non-Docker orchestration without native Docker health check support, you must explicitly call `connectorctl health` inside the container
- Automated actions require overriding the `Dockerfile HEALTHCHECK` or using your orchestration platform's equivalent mechanism

## Related Docs
- Connector deployment (systemd, Docker)
- Docker `HEALTHCHECK` directive documentation
- AWS ECS health check configuration