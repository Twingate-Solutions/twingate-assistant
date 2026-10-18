---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-10-18
source_version: 55ba7a756e0faacd6b31456c453b39c527e2202b916e79a1cddb2c48748c9e1f
trust: official
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When a Twingate Connector runs in Docker Desktop for Mac, it cannot reach services on the Mac host via `localhost`, `127.0.0.1`, or `--network host`. Docker Desktop provides `host.docker.internal` as a special DNS name that resolves to the Mac host from within containers.

## Key Information
- **Root cause**: Docker Desktop for Mac uses a VM layer; containers cannot reach the Mac host via standard loopback addresses
- **Two solutions**: Use Docker's built-in `host.docker.internal` hostname, or define a custom hostname via `--add-host`
- `host.docker.internal` requires no extra Docker arguments — it's resolved automatically in all Docker Desktop for Mac containers
- The Resource must be added to the same Remote Network where the Connector is deployed

## Prerequisites
- macOS with Docker Desktop for Mac installed
- Twingate Connector deployed via Docker on that host

## Step-by-Step

### Option 1: `host.docker.internal` (recommended, no config change)
1. In Twingate Admin Console, add `host.docker.internal` as a Resource on the Connector's Remote Network
2. Specify the service port in the Resource definition
3. Connect from a Twingate Client using `host.docker.internal:<port>`

### Option 2: Custom hostname via `--add-host`
1. Stop and remove the existing Connector container (arguments cannot be added to a running container)
2. Re-run the Connector with `--add-host <hostname.internal>:host-gateway` added to the `docker run` command
3. In Twingate Admin Console, add `<hostname.internal>` as a Resource on the Connector's Remote Network

## Configuration Values

| Parameter | Value | Notes |
|---|---|---|
| `--add-host` | `<hostname.internal>:host-gateway` | Replace `<hostname.internal>` with chosen name |
| `TWINGATE_NETWORK` | `<network-name>` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | `<access-token>` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | `<refresh-token>` | Connector refresh token |
| `TWINGATE_LABEL_HOSTNAME` | `$(hostname)` | Auto-populated from host |
| `TWINGATE_LABEL_DEPLOYED_BY` | `docker` | Static label |
| `--sysctl` | `net.ipv4.ping_group_range="0 2147483647"` | Required for ICMP support |

## Gotchas
- **Cannot modify a running container**: Must remove and recreate the container to add `--add-host`
- `--network host` does **not** work on Docker Desktop for Mac (only works natively on Linux)
- `host.docker.internal` is Docker Desktop-specific; it is not available in standard Linux Docker without explicit `--add-host` configuration

## Related Docs
- [Docker: Connect a container to a service on the host](https://docs.docker.com/desktop/networking/#use-cases-and-workarounds-for-all-platforms)