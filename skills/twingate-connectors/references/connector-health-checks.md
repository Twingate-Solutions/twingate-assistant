---
source: https://www.twingate.com/docs/connector-health-checks
type: docs
fetched: 2026-11-13
source_version: c2cc9e3c469fd601705c4217b5d009167bc0043ec1a727b41c4377544382585f
trust: official
---

# Connector Health Checks

## Summary
The Twingate Connector includes a built-in internal health check for debugging whether the Connector service is running correctly. It does not verify network connectivity to Twingate's infrastructure. The way you run it depends on how the Connector is deployed.

## Key Information
- Success: outputs `OK` and exits with status code `0`.
- Failure: any other output, or any nonzero exit code.
- Reports unhealthy only if the Connector service itself is not running correctly.
- Does **not** check connectivity to Twingate's infrastructure.
- Docker images ship with the health check built in.
- Automated actions can be driven by the result (see Deployment below).

## Prerequisites
- A deployed Twingate Connector (systemd, Docker, or other container runtime).
- Shell access to the host or container to run the command.

## Step-by-Step: Running a Health Check

**systemd service**
```
twingate-connectorctl health
```

**Docker**
- Run `docker ps` and read the health state under Status.
- For detail:
```
docker inspect --format "{{json .State.Health }}" container-name
```
Replace `container-name` with the container name or ID.

**Container not via Docker (e.g., AWS ECS)**
- Orchestrators that natively support Docker image health check definitions (such as AWS ECS) need no extra configuration.
- Otherwise, run this inside the container:
```
connectorctl health
```

## Configuration Values
- Command (systemd): `twingate-connectorctl health`
- Command (inside container): `connectorctl health`
- Expected output: `OK`, exit code `0`
- Docker inspect format string: `{{json .State.Health }}`
- Override point: the `HEALTHCHECK` instruction in the Connector container image's Dockerfile, or the orchestrator's equivalent setting.

## Deployment (Automated Actions)
To act on health results automatically, override the Dockerfile `HEALTHCHECK` in the Twingate Connector container image, or use your orchestration service's equivalent health check mechanism.

## Gotchas
- A passing health check does not mean the Connector can reach Twingate. Check connectivity separately.
- The command name differs: `twingate-connectorctl` on systemd hosts vs `connectorctl` inside containers.
- Any output other than `OK`, or any nonzero exit, counts as failure, including errors.

## Related Docs
- Twingate Connector deployment guides (Linux/systemd, Docker, AWS ECS, other orchestrators)
- Connector troubleshooting and logs documentation