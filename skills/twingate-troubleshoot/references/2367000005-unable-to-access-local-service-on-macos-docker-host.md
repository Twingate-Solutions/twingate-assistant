---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-11-01
source_version: cf84a8153bfb943b8c5d85d06d61de73ae50fc4b85560dd75c736d013093315e
trust: official
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When a Twingate Connector runs in Docker Desktop for Mac, it cannot reach host services via `localhost`, `127.0.0.1`, or `--network host`. Use Docker Desktop's special hostname `host.docker.internal` or a custom `--add-host` mapping to route container traffic back to the macOS host.

## Key Information
- Docker Desktop for Mac isolates containers from the host network — standard loopback addresses don't work from within containers
- `host.docker.internal` is automatically resolved by Docker Desktop; no extra config needed
- `host-gateway` is a Docker special value that resolves to the host IP at container start time
- Existing containers cannot have arguments added — must remove and recreate

## Prerequisites
- macOS with Docker Desktop for Mac installed
- Twingate Connector deployed via Docker on that host
- Access to Twingate Admin Console to configure Resources

## Step-by-Step

### Option 1: Use `host.docker.internal` (simplest)
1. No changes needed to the Connector container
2. In Twingate Admin Console, add `host.docker.internal` as a Resource on the Connector's Remote Network
3. Clients connect using `host.docker.internal:<port>`

### Option 2: Custom hostname via `--add-host`
1. Stop and remove the existing Connector container
2. Re-run with `--add-host <hostname.internal>:host-gateway` added to `docker run`
3. In Twingate Admin Console, add `<hostname.internal>` as a Resource on the Connector's Remote Network
4. Clients connect using `<hostname.internal>:<port>`

## Configuration Values

| Parameter | Value | Notes |
|---|---|---|
| `--add-host` | `<hostname.internal>:host-gateway` | Replace hostname with your choice |
| `TWINGATE_NETWORK` | `<network-name>` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | `<access-token>` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | `<refresh-token>` | From Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | `$(hostname)` | Auto-populated at runtime |
| `TWINGATE_LABEL_DEPLOYED_BY` | `docker` | Static label |
| `--sysctl` | `net.ipv4.ping_group_range="0 2147483647"` | Required for ICMP/ping support |
| Image | `twingate/connector:1` | Official Twingate connector image |

## Gotchas
- `--network host` does **not** work on macOS Docker — it's a Linux-only feature
- Cannot modify a running container's arguments; must `docker rm` and recreate
- `host.docker.internal` is Docker Desktop-specific; not available in standard Linux Docker without explicit `--add-host`
- The Resource address in the Admin Console must exactly match the hostname used (`host.docker.internal` or your custom one)

## Related Docs
- [Docker: Connect a container to a service on the host](https://docs.docker.com/desktop/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)