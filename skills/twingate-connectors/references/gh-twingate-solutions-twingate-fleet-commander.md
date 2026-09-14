---
source: https://github.com/Twingate-Solutions/twingate-fleet-commander
type: github
fetched: 2026-09-13
source_version: 10ce60afa7eb61c32a7cf53809d1724fd6a46534
---

<!-- triage: unassigned -->

# Twingate Fleet Commander

## Summary
Fleet Commander (FC) is an example/reference containerized control plane that autoscales Twingate Connector fleets on a single host. It runs a continuous async loop that discovers managed Connector containers, evaluates load/liveness signals, and provisions or removes Connectors via the Docker socket and Twingate GraphQL Admin API. Provided as-is under Apache 2.0; not a supported product.

## Key Information
- Supports three compute backends: local Docker (default), AWS ECS, Azure ACI — set via `FC_PLATFORM`
- Self-provisions Connectors; no seed Connectors or pre-minted tokens required
- Exposes status UI, `/healthz`, `/readyz`, and `/metrics` (Prometheus) on port 8080 (loopback-bound by default)
- Structured JSON logs to stdout; every cycle emits a `loop.cycle.complete` heartbeat
- Optional: manual override endpoints (disabled by default), log-shipper to S3-compatible storage
- `fc-teardown` must be run before `docker compose down` to avoid orphaned Connectors

## Prerequisites
- Docker with socket access on the control-plane host
- Twingate account with a Remote Network and an Admin API key
- Python extras for non-Docker backends: `pip install -e '.[ecs]'` or `pip install -e '.[aci]'`

## Usage / Step-by-Step

**Bootstrap (fastest path):**
```bash
git clone <repo> fleet-commander && cd fleet-commander
TWINGATE_NETWORK=acme TWINGATE_API_KEY=tgp_xxx ./deploy/bootstrap.sh
```

**Manual path:**
```bash
cp .env.example .env          # set TWINGATE_NETWORK + TWINGATE_API_KEY
cp config/config.example.yaml config/config.yaml
docker compose up -d
```

**Teardown (order matters):**
```bash
docker compose exec fc fc-teardown
docker compose --profile shipping down -v
```

## Configuration Values

| Variable / Key | Type | Description |
|---|---|---|
| `TWINGATE_NETWORK` | env | The labels before `.twingate.com` in your Admin Console URL — `acme` (legacy) or `acme.us1` (shard-based). Copy the host from the console rather than assuming a single label. The GraphQL endpoint (`https://<TWINGATE_NETWORK>.twingate.com/api/graphql/`) is derived from this value. |
| `TWINGATE_API_KEY` | env | Twingate Admin API key (Admin or DevOps role); stored as `SecretStr`, never logged |
| `FC_PLATFORM` | env | Compute backend: `docker` (default), `ecs`, `aci` |
| `FC_OVERRIDE_ENABLED` | env | Enable manual override endpoints (default: `false`) |
| `FC_OVERRIDE_SECRET` | env | Shared secret for override header (≥16 chars) |
| `TWINGATE_SHIPPER_*` | env | Log-shipper config block (S3 endpoint, keys, filter) |
| `min_connectors` / `max_connectors` | YAML | Fleet size floor/ceiling per Remote Network |
| `scale_up_trigger` | YAML | `any`, `mean`, or `quorum` (default) |
| `quorum_fraction` | YAML | Fraction of hot Connectors required to scale up (default: `0.5`) |

## Gotchas
- **Teardown order is critical:** `docker compose down` without `fc-teardown` first leaves Connector containers and logical Connectors orphaned in the tenant
- **`TWINGATE_NETWORK` format:** legacy tenants use a single label (e.g. `acme`); shard-based tenants use two labels (e.g. `acme.us1`). Copy the hostname from the Admin Console URL rather than guessing
- **Docker socket = root-equivalent:** treat the FC host as a trusted node; never expose port 8080 publicly without TLS
- **Socket proxy does not make the network safe:** allowlisting `containers/create` still permits host compromise; restrict network access to