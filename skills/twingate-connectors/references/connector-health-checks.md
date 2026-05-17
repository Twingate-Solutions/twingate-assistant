# Connector Health Checks

## Page Title
Connector Health Checks

## Summary
The Twingate Connector provides an internal health check to verify the Connector service is running correctly. Health checks only validate the service state, not network connectivity to Twingate infrastructure. Returns `OK` with exit code `0` on success; any other result indicates failure.

## Key Information
- Health checks confirm service is running — **not** that network connectivity to Twingate is established
- Success: returns `OK`, exit code `0`
- Failure: any other response or nonzero exit code

## Health Check by Deployment Type

| Deployment | Command/Method |
|---|---|
| systemd | `twingate-connectorctl health` |
| Docker | Built-in; visible via `docker ps` under Status |
| Non-Docker container | `connectorctl health` inside container |

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

### Container (non-Docker, e.g., AWS ECS)
```bash
# Execute inside container
connectorctl health
```

## Configuration Values
- **AWS ECS**: Natively supports Docker image health check definitions — no additional config required
- Custom automation: Override `Dockerfile HEALTHCHECK` directive or use orchestration service equivalent

## Gotchas
- Health check passing does **not** mean the Connector has established connectivity to Twingate's infrastructure — only that the service process is running
- For non-Docker orchestrators without native Docker health check support, you must manually exec `connectorctl health` inside the container

## Related Docs
- Connector deployment (systemd, Docker, container)
- Dockerfile HEALTHCHECK documentation (Docker)
- AWS ECS health check configuration