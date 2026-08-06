---
source: https://github.com/Twingate-Solutions/twingate-custom-connector-container
type: github
fetched: 2026-08-06
source_version: d28eadc2fd8a8e4d6e4a831f87ab1aa1ce851fdc
---

<!-- triage: unassigned -->

# Twingate Custom Connector Container

## Summary
A Docker image that runs the Twingate Linux/systemd Connector inside a container. Intended for cases where custom scripts, healthchecks, or shell access are needed beyond what the official Twingate container image provides. Serves as an example/starting point for customization.

## Key Information
- Image hosted at `ghcr.io/twingate-solutions/twingate-custom-connector-container:latest`
- Runs the Twingate connector via `entrypoint.sh`; customizable via Dockerfile modifications
- Includes a healthcheck system: place executable scripts in `/healthchecks.d/` (runs every 90s); scripts must return `0` for success
- Default health check: `00-twingate-status-healthcheck.sh` verifies connector is running and connected
- Emits structured JSON resource metrics (CPU, memory, network I/O) to **stderr** every 60 seconds; filter by `"event":"metrics"` field
- Connector output (including analytics) goes to **stdout**; metrics to **stderr** to prevent stream interleaving
- Container requires `privileged: true`

## Prerequisites
- Docker with Compose
- A Twingate account with Admin Console access
- A provisioned Connector with generated Access Token and Refresh Token
- GHCR authentication (GitHub PAT with `read:packages` scope) to pull the image

## Usage / Step-by-Step

1. **Provision connector**: Admin Console → Network → Remote Networks → Remote Network → Add Connector → Manual deployment → Generate Tokens
2. **Configure `docker-compose.yml`** with required environment variables (see below)
3. **Start**:
   ```bash
   docker compose up -d
   docker compose logs -f tg-headless-connector
   ```
4. **Shell access**:
   ```bash
   docker compose exec -it tg-headless-connector bash
   twingate-connectorctl health  # returns OK if connected
   ```

## Configuration Values

| Variable | Required | Description |
|---|---|---|
| `TWINGATE_NETWORK` | Yes | Network subdomain prefix (e.g., `mycompany` from `mycompany.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Yes | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Yes | Refresh token from Admin Console |
| `TWINGATE_LOG_ANALYTICS` | No | Set to `v2` for detailed traffic logging |
| `TWINGATE_LOG_LEVEL` | No | Log verbosity; default `3`, set `7` for debug |

## Gotchas
- Container must run with `privileged: true`
- Tokens are generated once in the Admin Console; losing them requires re-generating
- Metrics stream (stderr) and connector output (stdout) are intentionally separated — do not filter metrics by stream, use the `"event":"metrics"` JSON field
- GHCR requires authentication even for public image pulls if you are unfamiliar with the registry
- When forking, publish to your own registry; GHCR push requires `write:packages` PAT scope (add `repo` scope for private repos)
- On CI, prefer `GITHUB_TOKEN` over a personal PAT

## Related Docs
- [Twingate Linux Connector documentation](https://www.twingate.com/docs/connectors-on-linux)
- [Metrics field schema and platform guidance](docs/metrics.md)
- [GitHub GHCR authentication](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry/authenticating-to-github-container-registry)
- [GitHub PAT creation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)