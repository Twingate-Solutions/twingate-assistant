---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-11-13
source_version: 520e8da17a29d2f2018bd3adc4a9adb430612e277613c613dcd09e872cd815b6
trust: official
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When the Twingate Connector runs as a container in Docker Desktop for Mac, it cannot reach services on the Mac itself via `localhost`, `127.0.0.1`, or `--network host`. Docker Desktop provides a special address that routes from the container back to the Mac. Point the Twingate Resource at that address instead.

## Key Information
- Applies to: Twingate Connector on Docker for macOS.
- `host.docker.internal` is resolved automatically by Docker Desktop to the Mac host in every container, so no extra `docker run` arguments are needed.
- Alternatively, use `--add-host <hostname.internal>:host-gateway` to map a custom hostname to the host.
- The Resource must be added on the Remote Network where the Connector is deployed.

## Prerequisites
- macOS host with Docker Desktop for Mac installed.
- Twingate Connector deployed on that host using Docker.

## Step-by-Step

**Option 1: `host.docker.internal`**
1. In the Twingate Admin Console, add `host.docker.internal` as a Resource on the Connector's Remote Network.
2. From a Twingate Client, connect using `host.docker.internal` and the service's port.

**Option 2: custom hostname**
1. Add `--add-host <hostname.internal>:host-gateway` to the Connector's `docker run` command.
2. If the Connector is already running, remove the container and re-run the command (arguments can't be added to an existing container).
3. In the Admin Console, add `<hostname.internal>` as a Resource on the same Remote Network.

## Configuration Values
Full example (values in `<>` are deployment-specific):

```
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

- `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`: Connector credentials and network name.
- `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_DEPLOYED_BY`: labels.
- `--add-host <hostname.internal>:host-gateway`: custom hostname mapping to the Mac host.

## Gotchas
- `localhost`, `127.0.0.1`, and `--network host` do not work for reaching the Mac from the container on Docker Desktop for Mac.
- Docker arguments cannot be added to a running container; you must remove and recreate it.
- Reusing the same tokens when recreating the Connector depends on your deployment; keep your credentials available before removing the container.

## Related Docs
- Docker docs: Connect a container to a service on the host (docs.docker.com)