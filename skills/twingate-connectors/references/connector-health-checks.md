# Connector Health Checks

## Summary
Twingate Connectors expose an internal health check to verify the Connector service is running correctly. Health checks only validate service state—not network connectivity to Twingate infrastructure. Returns `OK` with exit code `0` on success; any other response or nonzero exit code indicates failure.

## Key Information
- Health checks confirm the Connector service is running, **not** that it has established network connectivity to Twingate
- Success response: `OK` + exit code `0`
- Failure: any other response or nonzero exit code

## Running a Health Check by Deployment Type

### systemd
```bash
twingate-connectorctl health
```

### Docker
Health check is built into the container image.
```bash
# View status
docker ps

# Detailed health info
docker inspect --format "{{json .State.Health }}" <container-name>
```

### Other Container Orchestration (e.g., AWS ECS)
- Services that natively support Docker image health check definitions require no additional configuration
- Otherwise, exec into the container:
```bash
connectorctl health
```

## Automating Actions Based on Health Check

Override the `Dockerfile HEALTHCHECK` directive in the Twingate container image, or use your orchestration platform's equivalent health check mechanism.

## Gotchas
- A healthy response does **not** mean the Connector is connected to Twingate's network infrastructure
- `twingate-connectorctl` (with prefix) is used for systemd; `connectorctl` (no prefix) is used inside containers
- Docker deployment shows health status automatically via `docker ps`—no manual invocation needed

## Related Docs
- Connector deployment (systemd, Docker, container orchestration)
- Dockerfile HEALTHCHECK override documentation