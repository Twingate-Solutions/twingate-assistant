---
source: https://github.com/Twingate-Solutions/gwops
type: github
fetched: 2026-10-28
source_version: 29048d3993aae1b162affd5c6b32cfad2550924a
trust: official
---

<!-- triage: unassigned -->

# gwops: Twingate Gateway with Managed Control Plane

A Python asyncio control plane (PID 1) that supervises the official Twingate Gateway binary, manages TLS/SSH certificate lifecycles, synchronizes Twingate tenant resources from a declarative YAML seed file, and exposes a small admin API. Intended as a reference example, not a supported product.

## Key Information

- Runs `twingate/gateway:2.0.0` (pinned by digest) inside a single container
- Manages X.509/SSH CAs, mints/renews TLS leaves, supports ACME (Let's Encrypt, Cloudflare DNS-01)
- Syncs SSH, Kubernetes, and web-app resources to a Twingate tenant via GraphQL API; only touches objects it created
- Hot-reloads renewed certificates without restarting the gateway process
- L7 reverse proxy for internal HTTP(S) apps with optional token/identity header injection
- Optional session recording delivery to an HTTP NDJSON receiver via bounded on-disk spool
- Admin API on `127.0.0.1:8081` (bearer-authenticated); changes persist as overlays on the seed
- Built for `linux/amd64` only

## Prerequisites

- Docker Engine + Docker Compose v2
- `linux/amd64` host
- Twingate tenant with a Remote Network and healthy Connector reachable on TCP 8443
- Twingate API key with read/write access (resources, certificate authorities, gateways)

## Usage

Follow the [Quickstart](quickstart/README.md) in the repository for an end-to-end first deployment fronting one SSH host.

1. Create `/config/seed.yaml` describing your SSH hosts, Kubernetes API server, and/or web apps
2. Supply required environment variables (see below)
3. Mount a persistent `/data` volume for gwops state
4. Run via `docker compose up` using the provided `compose.yaml`

## Configuration Values

| Variable | Purpose |
|---|---|
| `TWINGATE_API_KEY` | Twingate tenant API key (read/write) |
| `GWOPS_ADMIN_TOKEN` | Bearer token for admin API authentication |
| `GWOPS_AUTOMATION_TOKEN` | Token for automation access |
| `GWOPS_RECORDING_TOKEN` | Token for recording receiver authentication |

- Secrets are accepted only via environment variables; never in seed files, overlays, rendered configs, or logs
- `admin_api.bind` seed key controls the bind address (default `127.0.0.1`; set `0.0.0.0` to allow host access)
- Seed file path: `/config/seed.yaml` (read-only mount)
- State/data path: `/data` (persistent volume)

## Gotchas

- **Unsupported example project**: provided as-is under Apache 2.0 with no warranty or support
- Admin API is plain HTTP; do not expose on a routable interface without a TLS proxy
- Session recordings are not redacted — terminal output, URLs, and request headers are forwarded as-is
- The container does not join the Twingate network itself; clients reach it through a separate Connector
- gwops only modifies resources it originally created; objects made via the Admin Console are never touched

## Related Docs

- [Quickstart](quickstart/README.md)
- [Seed reference](reference/seed.md)
- [Admin API reference](reference/admin-api.md)
- [Image reference](reference/image.md)
- [Architecture](architecture/README.md)
- [Security model](architecture/security-model.md)
- [Known limitations](reference/limitations.md)
- [Upgrades and pins](operations/upgrades-and-pins.md)