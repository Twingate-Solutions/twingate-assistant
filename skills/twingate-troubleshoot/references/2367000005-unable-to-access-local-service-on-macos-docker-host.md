---
source: https://help.twingate.com/articles/2367000005-unable-to-access-local-service-on-macos-docker-host
type: help
fetched: 2026-10-04
source_version: 5e520d7528676b8aa62c5ee454de9d7c2838e8652909fb15204ad6dae77fdce6
trust: official
---

# Unable to Access Local Service on macOS Docker Host

## Summary
When running a Twingate Connector as a Docker container on macOS, local services on the host are not reachable by default. An additional `--add-host` Docker argument is required to bridge the container to the macOS host network. After configuration, the host is then added as a Twingate Resource.

## Key Information
- Issue is specific to **Docker for macOS** — Linux Docker hosts do not require this workaround
- `host-gateway` is a special Docker DNS alias that resolves to the host machine's internal IP
- A custom hostname of your choice maps to `host-gateway`, which is then used as the Resource address in Twingate

## Prerequisites
- macOS host with **Docker Desktop for Mac** installed
- Twingate Connector deployment via Docker
- Access to the Twingate Admin Console

## Step-by-Step

1. **Start the Connector container** with the `--add-host` flag:
   ```
   --add-host <your-chosen-hostname>:host-gateway
   ```
   Full example command (replace `<...>` with your deployment values):
   ```
   docker run ... --add-host <your-chosen-hostname>:host-gateway <other-connector-args>
   ```

2. **Add the hostname as a Twingate Resource** in the Admin Console:
   - Navigate to the Remote Network where the Connector resides
   - Add `<your-chosen-hostname>` as a new Resource

## Configuration Values

| Parameter | Value | Notes |
|-----------|-------|-------|
| `--add-host` | `<hostname>:host-gateway` | `host-gateway` resolves to the macOS host IP |
| Resource address | `<hostname>` | Must match the hostname used in `--add-host` |

## Gotchas
- Without `--add-host`, the Connector container cannot reach services running directly on the macOS host (not in other containers)
- The hostname chosen is arbitrary but must be consistent between the Docker flag and the Twingate Resource definition
- This workaround is **macOS-specific**; Linux Docker hosts natively support `--network=host`

## Related Docs
- [Docker: Connect from a container to a service on the host](https://docs.docker.com/desktop/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)