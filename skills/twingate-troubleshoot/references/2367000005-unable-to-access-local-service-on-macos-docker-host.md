---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-11-08
source_version: 9387a0aa1802254894035dfab398c3e7f1ea44ebaa819a21430b20e0db787da9
trust: official
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When a Twingate Connector runs in Docker Desktop for Mac, it cannot reach host services via `localhost`, `127.0.0.1`, or `--network host`. Docker Desktop provides `host.docker.internal` as the escape hatch to route container traffic back to the Mac host.

## Key Information
- **Root cause**: Docker Desktop for Mac uses a VM layer; containers cannot bind to the host network directly
- **`--network host`** does not work on macOS Docker Desktop (Linux-only feature)
- Two resolution options: use the built-in `host.docker.internal` DNS name, or map a custom hostname via `--add-host`

## Prerequisites
- macOS with Docker Desktop for Mac installed
- Twingate Connector deployed via Docker on that host

## Step-by-Step

### Option 1: `host.docker.internal` (simplest)
1. No container changes needed — Docker Desktop resolves this automatically
2. In Twingate Admin Console → add `host.docker.internal` as a Resource on the Connector's Remote Network
3. Clients connect to `host.docker.internal:<port>`

### Option 2: Custom hostname via `--add-host`
1. Stop and remove the existing Connector container (arguments cannot be added to running containers)
2. Re-run with `--add-host <hostname.internal>:host-gateway` added to `docker run`
3. In Twingate Admin Console → add `<hostname.internal>` as a Resource on the Connector's Remote Network

## Configuration Values

| Parameter | Value | Notes |
|---|---|---|
| `--add-host` | `<hostname.internal>:host-gateway` | Replace `<hostname.internal>` with chosen name |
| Built-in hostname | `host.docker.internal` | No extra args; always available in Docker Desktop |

**Example `docker run` with custom host:**
```bash
docker run -d \
  --sysctl net.ipv4.ping_group_range="0 2147483647" \
  --env TWINGATE_NETWORK="<network-name>" \
  --env TWINGATE_ACCESS_TOKEN="<access-token>" \
  --env TWINGATE_REFRESH_TOKEN="<refresh-token>" \
  --env TWINGATE_LABEL_HOSTNAME="$(hostname)" \
  --env TWINGATE_LABEL_DEPLOYED_BY="docker" \
  --add-host <hostname.internal>:host-gateway \
  --name "twingate-connector" \
  --restart=unless-stopped \
  --pull=always \
  twingate/connector:1
```

## Gotchas
- **Cannot modify running containers**: Must `docker rm` and re-run to add `--add-host`
- `--network host` is silently ineffective on macOS; it only works on Linux
- `host-gateway` is a Docker-internal alias for the host IP; it is not a real hostname

## Related Docs
- [Docker: Connect a container to a service on the host](https://docs.docker.com/network/network-tutorial-host/)