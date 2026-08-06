---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-08-06
source_version: 625f4c524cbd83f53cb33890cdf1c245efc003d6ea9f5b1a5ac58f195f3b38a5
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When running a Twingate Connector as a Docker container on macOS, accessing local host services as Twingate Resources requires an extra Docker argument. Without it, the Connector cannot reach services running on the macOS host machine.

## Key Information
- Issue is specific to Docker Desktop for Mac (not Linux Docker hosts)
- Docker containers on macOS cannot reach the host via default networking without explicit configuration
- Requires adding a custom host entry that maps to the `host-gateway` internal Docker address

## Prerequisites
- macOS host with Docker Desktop for Mac installed
- Twingate Connector deployed as a Docker container
- Access to Twingate Admin Console

## Step-by-Step

1. **Start the Connector container** with the `--add-host` flag:
   ```bash
   docker run \
     --add-host <CUSTOM_HOSTNAME>:host-gateway \
     # ... other Connector-specific variables
     twingate/connector
   ```
   Replace `<CUSTOM_HOSTNAME>` with an internal hostname of your choosing (e.g., `dockerhost`).

2. **Add the hostname as a Twingate Resource** in the Admin Console, scoped to the Remote Network where this Connector resides.

## Configuration Values

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--add-host` | `<hostname>:host-gateway` | Maps custom hostname to Docker host gateway IP |

**Example hostname choices:** `dockerhost`, `host.docker.internal`, or any custom name you define as your Resource address.

## Gotchas
- `host-gateway` is a Docker special keyword that resolves to the host machine's internal IP — do not substitute a literal IP unless Docker version doesn't support `host-gateway`
- The hostname used in `--add-host` must exactly match what you configure as the Twingate Resource address
- This workaround is macOS-specific; Linux Docker hosts use different networking behavior

## Related Docs
- [Docker: Connect from container to host service](https://docs.docker.com/desktop/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)
- Twingate Connector deployment documentation