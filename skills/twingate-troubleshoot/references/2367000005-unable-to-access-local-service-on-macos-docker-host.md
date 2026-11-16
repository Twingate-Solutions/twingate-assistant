---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-11-15
source_version: aadc2388b084248b320627f9c5302a072f3411728177dc0eaf4c4abceeac2cfe
trust: official
---

# Unable to Access Local Service on macOS Docker Host

## Summary
A Twingate Connector running as a container in Docker Desktop for Mac cannot reach services on the Mac itself via `localhost`, `127.0.0.1`, or `--network host`. Docker Desktop provides a special hostname that routes from the container to the Mac host. Define a Twingate Resource using that hostname (or a custom one via `--add-host`) so the Connector can reach the host service.

## Key Information
- `localhost`, `127.0.0.1`, and `--network host` do not reach the Mac host from inside a Docker Desktop container.
- Docker Desktop automatically resolves `host.docker.internal` to the Mac host in every container.
- Option 1 needs no extra Docker arguments.
- Option 2 maps a custom hostname to the host using `--add-host <hostname.internal>:host-gateway`.
- The Resource must be created on the Remote Network where the Connector is deployed.

## Prerequisites
- macOS host with Docker Desktop for Mac
- Twingate Connector deployed on that host via Docker

## Step-by-Step

### Option 1: `host.docker.internal`
1. In the Twingate Admin Console, add `host.docker.internal` as a Resource on the Connector's Remote Network.
2. From a Twingate Client, connect using `host.docker.internal` and the service's port.

### Option 2: Custom hostname
1. Remove the existing Connector container if running (arguments can't be added to an existing container).
2. Re-run the Connector with `--add-host <hostname.internal>:host-gateway`.
3. In the Admin Console, add `<hostname.internal>` as a Resource on the same Remote Network.

## Configuration Values
Full example `docker run` (replace `<>` values):
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
- `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`: Connector credentials/tenant
- `--add-host <hostname.internal>:host-gateway`: custom hostname mapped to the host
- `--sysctl net.ipv4.ping_group_range="0 2147483647"`: allows ICMP ping

## Gotchas
- You can't add arguments to a running container; you must remove and recreate it.
- The Resource address must be the hostname (`host.docker.internal` or your custom one), not `localhost` or `127.0.0.1`.
- The Resource must be on the Remote Network containing this Connector.

## Related Docs
- Docker docs: Connect a container to a service on the host (docs.docker.com)