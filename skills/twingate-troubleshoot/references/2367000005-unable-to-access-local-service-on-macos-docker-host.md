---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-09-06
source_version: c4adcd77a5799d29064a8537f2278d5cc99000a9c08cdea26ae9fe7f9a820338
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When running a Twingate Connector as a Docker container on macOS, additional Docker arguments are required to access services running on the macOS host. Without these arguments, the Connector cannot route traffic to localhost services on the host machine.

## Key Information
- Issue is specific to Docker Desktop for Mac (not Linux Docker hosts)
- Requires adding a custom host entry that maps to the Docker host gateway IP
- The chosen hostname becomes the Twingate Resource address in the Admin Console

## Prerequisites
- macOS host with Docker Desktop for Mac installed
- Twingate Connector deployed via Docker container
- Access to Twingate Admin Console

## Step-by-Step

1. **Start the Connector container** with the `--add-host` flag:
   ```bash
   docker run --add-host <HOSTNAME>:host-gateway \
     ... \
     twingate/connector
   ```
   Replace `<HOSTNAME>` with an internal hostname of your choosing (e.g., `mac-host`).

2. **Add the hostname as a Twingate Resource** in the Admin Console:
   - Navigate to the Remote Network where the Connector resides
   - Add `<HOSTNAME>` (the same value used in `--add-host`) as a Resource

## Configuration Values

| Parameter | Value | Notes |
|-----------|-------|-------|
| `--add-host` | `<HOSTNAME>:host-gateway` | Docker flag; `host-gateway` resolves to host's internal IP |
| Resource address | `<HOSTNAME>` | Must match the hostname used in `--add-host` |

## Gotchas
- `host-gateway` is a Docker Desktop for Mac special value — do not substitute a literal IP unless necessary
- The hostname used in `--add-host` and the Twingate Resource definition must match exactly
- This workaround is needed because Docker on macOS uses a VM layer; Linux Docker hosts can typically reach host services via `172.17.0.1` directly without this flag

## Related Docs
- [Docker: Connect from container to host service](https://docs.docker.com/desktop/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)