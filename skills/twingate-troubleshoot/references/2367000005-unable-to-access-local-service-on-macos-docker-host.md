---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-10-28
source_version: 130084386eab3ae25368bf7bbe6f556717ccb157f1007690b07480451b5892a5
trust: official
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When a Twingate Connector runs in Docker Desktop for Mac, it cannot reach services on the host via `localhost`, `127.0.0.1`, or `--network host`. Use Docker Desktop's `host.docker.internal` hostname or a custom `--add-host` mapping to route container traffic back to the Mac host.

## Key Information
- Docker Desktop for Mac does not support `--network host`; containers are isolated from the host network
- `host.docker.internal` is automatically available in all Docker Desktop for Mac containers
- `host-gateway` is a Docker special value that resolves to the host IP at runtime

## Prerequisites
- macOS with Docker Desktop for Mac installed
- Twingate Connector deployed via Docker on that host
- Access to Twingate Admin Console

## Step-by-Step

### Option 1: Use `host.docker.internal` (recommended, no config changes)
1. In the Twingate Admin Console, add `host.docker.internal` as a Resource on the Remote Network where the Connector is deployed
2. Connect from a Twingate Client using `host.docker.internal:<port>`

### Option 2: Custom hostname via `--add-host`
1. Stop and remove the existing Connector container (arguments cannot be added to a running container)
2. Re-run the Connector with `--add-host <hostname.internal>:host-gateway` added to the `docker run` command:
   ```sh
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
3. In the Twingate Admin Console, add `<hostname.internal>` as a Resource on the Remote Network

## Configuration Values
| Parameter | Value | Notes |
|-----------|-------|-------|
| `--add-host` | `<hostname>:host-gateway` | `host-gateway` resolves to host IP automatically |
| Built-in hostname | `host.docker.internal` | No extra flags needed |

## Gotchas
- **Cannot modify running containers** — must remove and recreate the container to add `--add-host`
- `--network host` does **not** work on Docker Desktop for Mac; it is a Linux-only feature
- `localhost`/`127.0.0.1` inside the container refers to the container itself, not the Mac host

## Related Docs
- [Docker: Connect a container to a service on the host](https://docs.docker.com/desktop/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)