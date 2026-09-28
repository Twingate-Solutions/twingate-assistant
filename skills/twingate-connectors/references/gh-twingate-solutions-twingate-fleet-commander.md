---
source: https://github.com/Twingate-Solutions/twingate-fleet-commander
type: github
fetched: 2026-09-27
source_version: effa0af4844c5f9300dabf26fd45cf53b0680b27
---

# Twingate Fleet Commander

A reference example (unsupported, Apache 2.0) of a containerized control plane that autoscales Twingate Connector fleets on a single Docker host. It runs a continuous async loop to discover, monitor, provision, drain, restart, and replace Connectors by driving the local Docker socket, with the Twingate GraphQL Admin API as the bookkeeping layer. Observability is provided via structured JSON stdout logs and a Prometheus `/metrics` endpoint.

## Key Information

- Self-provisions Connectors — no seed tokens required; FC mints tokens via the Twingate API
- Supports three compute backends: `docker` (default), `ecs` (AWS), `aci` (Azure)
- Scale-up trigger modes: `any`, `mean`, `quorum` (default, configurable fraction)
- Scale-down only when every Connector signal is below the low watermark
- Optional manual overrides (scale ±1, cordon, replace) behind a shared-secret header
- Optional log-shipper (Compose `shipping` profile) for S3-compatible analytics export
- Status UI, `/healthz`, `/readyz`, `/metrics` all on port 8080 (loopback-bound by default)
- FC restarts are safe — managed Connectors keep serving across manager restarts

## Prerequisites

- Docker with Compose plugin on the host
- Twingate network name and Admin API key (`TWINGATE_API_KEY`)
- Python extras for non-Docker backends: `pip install -e '.[ecs]'` or `'.[aci]'`

## Usage

**Bootstrap (idempotent):**
```bash
git clone <repo> fleet-commander && cd fleet-commander
TWINGATE_NETWORK=acme TWINGATE_API_KEY=tgp_xxx ./deploy/bootstrap.sh
```

**Manual start:**
```bash
cp .env.example .env && cp config/config.example.yaml config/config.yaml
docker compose up -d
docker compose --profile shipping up -d  # include log-shipper
```

**Teardown (removes all managed Connectors before stopping stack):**
```bash
docker compose exec fc fc-teardown
docker compose --profile shipping down -v
```

Cloud-init snippets for EC2, Azure VM, GCP, and Proxmox are in `deploy/cloud-init/`.

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Subdomain prefix from Admin Console URL |
| `TWINGATE_API_KEY` | Twingate Admin API key |
| `FC_PLATFORM` | `docker` (default), `ecs`, or `aci` |
| `FC_OVERRIDE_ENABLED` | Enable manual override endpoints (default `false`) |
| `FC_OVERRIDE_SECRET` | Shared secret for overrides (≥16 chars) |
| `TWINGATE_SHIPPER_*` | S3-compatible bucket config for log-shipper |

Policy (watermarks, cooldowns, floor/ceiling, `scale_up_trigger`, `quorum_fraction`) is set in `config/config.yaml`. See `documentation/CONFIGURATION.md` for the full reference.

## Gotchas

- **Docker socket is root-equivalent.** Use the socket-proxy Compose variant (`deploy/compose/socket-proxy-hardened.yml`) for hardened deployments; the proxy network itself remains a trust boundary.
- Plain `docker compose down` leaves Connector containers running. Always run `fc-teardown` first.
- Port 8080 binds to loopback by default. Reach it via SSH tunnel; never expose directly without TLS.
- The override secret is a static header credential sent in clear text — only enable behind TLS.
- Sticky connections mean one hot Connector may not justify scale-up; `quorum` mode avoids over-provisioning. A persistently high `hot_connector_max` with one Connector over watermark is a load-balancing issue, not a capacity one.
- `TWINGATE_SHIPPER_DOCKER_CONTAINER_NAME_FILTER` must be updated if using the custom connector image (default filter `twingate/connector` won't match).

## Related Docs

- [Architecture](documentation/ARCHITECTURE.md)
- [Configuration](documentation/