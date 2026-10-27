---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-10-25
source_version: 52d7458d17cffc1dd7af5455a94ef32ee07538db9ae2eafbc8f48ad62b60ec52
trust: official
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When a Twingate Connector runs in Docker Desktop for Mac, it cannot reach services on the Mac host via `localhost`, `127.0.0.1`, or `--network host`. Docker Desktop provides a special DNS name (`host.docker.internal`) that routes container traffic back to the Mac host. Configure your Twingate Resource to use this address instead.

## Key Information
- **Root cause**: Docker Desktop for Mac uses a VM layer; `localhost` inside a container refers to the container, not the Mac
- **`--network host`** does not work on macOS Docker Desktop (Linux-only feature)
- Two resolution options: use built-in `host.docker.internal` or define a custom hostname via `--add-host`

## Prerequisites
- macOS with Docker Desktop for Mac installed
- Twingate Connector deployed via Docker on that host
- Access to Twingate Admin Console

## Step-by-Step

### Option 1: `host.docker.internal` (Recommended — no config change needed)
1. In Twingate Admin Console, add `host.docker.internal` as a Resource on the Remote Network where the Connector is deployed.
2. Connect from a Twingate Client using `host.docker.internal:<port>`.

### Option 2: Custom hostname via `--add-host`
1. Stop and remove the existing Connector container (arguments cannot be added to a running container).
2. Re-run with `--add-host <hostname.internal>:host-gateway` appended:

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

3. In Twingate Admin Console, add `<hostname.internal>` as a Resource on the Connector's Remote Network.

## Configuration Values

| Parameter | Value | Notes |
|---|---|---|
| `--add-host` | `<hostname>:host-gateway` | `host-gateway` resolves to Mac host IP |
| Built-in hostname | `host.docker.internal` | Auto-resolved by Docker Desktop, no flags needed |

## Gotchas
- **Cannot modify running containers**: Must remove and recreate the container to add `--add-host`
- **`host-gateway`** is a Docker special value mapping to the host; do not substitute a literal IP
- Option 1 (`host.docker.internal`) is simpler and requires no Docker run changes
- This issue is **macOS-specific**; Linux Docker hosts support `--network host` natively

## Related Docs
- [Docker: Connect a container to a service on the host](https://docs.docker.com/desktop/features/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)