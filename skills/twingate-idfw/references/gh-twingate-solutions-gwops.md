---
source: https://github.com/Twingate-Solutions/gwops
type: github
fetched: 2026-10-28
source_version: 29048d3993aae1b162affd5c6b32cfad2550924a
trust: official
---

# gwops: Twingate Gateway with Managed Control Plane

A Python asyncio control plane (PID 1) that supervises the official Twingate Gateway binary, manages TLS/SSH certificate lifecycles, synchronizes Twingate tenant resources from a declarative YAML seed file, and exposes a small admin API. Intended as a reference example, not a supported product.

The repo's documentation (~70 pages: recipes, guides, operations, reference, architecture) is also one of the most detailed public write-ups of how the Gateway 2.0 binary itself behaves — certificate modes, config schema, recording output, web-app upstream TLS, limits. Useful for custom/self-built Gateway deployments even when gwops itself is not used. See the Documentation Map below; the docs are not bundled here, read them from the repo.

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

Follow the [Quickstart](https://github.com/Twingate-Solutions/gwops/blob/main/quickstart/README.md) in the repository for an end-to-end first deployment fronting one SSH host.

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

## Gateway Binary Behaviour (applies beyond gwops)

From the repo's architecture and limitations pages; true of the Gateway 2.0 binary, not only the wrapper.

- No `config validate` subcommand — gwops pre-flights a candidate config by spawning the binary on it for 5 s
- No SIGHUP config reload — any config change means a restart, which drops open connections; certificate files are hot-reloaded without restart
- No recording sink — recordings, HTTP audit lines and operational lines are written to stderr with logger names `session_recording`, `audit`, `system`; something must read and forward them
- SSH recording covers interactive shells only (no `exec`/`subsystem`); Kubernetes recording covers interactive `exec`/`attach` with a TTY; web-app traffic produces HTTP audit lines only
- SSH port forwarding is neither gated nor audited by the gateway
- One Kubernetes cluster per gateway instance
- Private CA mode and public-certificate mode are mutually exclusive on one gateway; public mode serves DNS names only and certificates chaining to ISRG Root X1
- Web-app upstream TLS requires TLS 1.3; client-to-gateway is HTTP/1.1 only; `Host` cannot be rewritten; no wildcard web-app addresses
- The gateway closes a client connection at access-token expiry (cuts long-lived WebSockets/SSE); no clock leeway on token issue time — keep the host on NTP
- Each SSH target must trust the SSH CA public key itself

Verify exact behaviour against `reference/limitations.md` and `architecture/gateway-process.md` in the repo; these follow the pinned gateway version.

## Documentation Map

Base URL: `https://github.com/Twingate-Solutions/gwops/blob/main/`. Recipes are complete deployments (full `seed.yaml`, `.env`, `compose.yaml`, tenant prerequisites, verify, day-2); guides cover one capability each.

**Recipes (`recipes/`)**

| Scenario | File |
|---|---|
| SSH fleet, generated CAs | `ssh-fleet-generated-ca.md` |
| SSH fleet already trusting your SSH CA | `ssh-fleet-existing-ssh-ca.md` |
| Kubernetes + web apps, CA from Vault/secret store | `k8s-and-web-apps-ca-from-secret-store.md` |
| Developer kubectl access | `developer-kubectl-access.md` |
| Internal web apps for managed devices (CA installed on devices) | `internal-web-apps-managed-devices.md` |
| Browser-trusted web apps, Let's Encrypt via Cloudflare DNS-01 | `public-web-apps-acme-cloudflare.md` |
| Browser-trusted web apps, certs from your own ACME client | `public-web-apps-own-acme-client.md` |
| SSH, Kubernetes and web apps on one gateway | `all-in-one-gateway.md` |
| Private and public gateways on one host | `private-and-public-gateways-one-host.md` |
| One gateway per Remote Network or cluster | `multiple-remote-networks.md` |
| Adopt an existing Gateway object | `adopt-existing-gateway.md` |
| Seed in Git, deployed by CI (GitOps) | `gitops-seed.md` |
| Upstreams that self-register | `self-registering-upstreams.md` |
| Session recording into a SIEM/log pipeline | `recording-to-siem.md` |
| Restricted egress / outbound proxies | `restricted-egress.md` |
| Contractor/vendor access on a separate gateway | `third-party-access.md` |
| Homelab or small office | `homelab-small-office.md` |
| Cloud VM (AWS, Azure, Google Cloud) | `cloud-vm.md` |
| Inside a Kubernetes cluster (untested) | `kubernetes-hosted.md` |

**Guides (`guides/`)**: `gateway-modes.md` (pinned-gateway vs remote-network mode), `private-ca-generated.md`, `private-ca-byo.md`, `on-demand-issuance.md`, `public-certs-files.md`, `public-certs-acme.md`, `public-mode-mixed.md`, `ssh-resources.md`, `kubernetes.md`, `web-apps.md`, `web-apps-identity.md` (token/identity header injection), `web-apps-upstream-tls.md` (private upstream CAs, plaintext upstreams), `access-control.md`, `session-recording.md`, `automation-and-ci.md`.

**Operations (`operations/`)**: `monitoring.md`, `troubleshooting.md` (symptom-to-cause tables), `admin-api-behind-tls-proxy.md`, `ca-and-leaf-rotation.md`, `backup-and-restore.md`, `upgrades-and-pins.md`, `build-and-publish.md`.

**Reference (`reference/`)**: `seed.md` (every seed key), `environment.md`, `image.md` (ports, mounts, `/data` layout, egress), `admin-api.md`, `recording-wire-format.md` (receiver HTTP contract), `log-events.md`, `limitations.md`, `development.md`, `glossary.md`.

**Architecture (`architecture/`)**: `README.md` (component map, design principles), `gateway-process.md` (rendering, pre-flight, drain-restart), `certificates.md`, `acme.md`, `reconciler.md`, `configuration-model.md`, `twingate-integration.md` (what it does on the tenant), `web-apps.md` (JWKS reachability, upstream TLS probe), `recording-pipeline.md`, `security-model.md`, `admin-api.md`, `health-and-observability.md`, `startup-and-shutdown.md`.

## Gotchas

- **Unsupported example project**: provided as-is under Apache 2.0 with no warranty or support
- Admin API is plain HTTP; do not expose on a routable interface without a TLS proxy
- Session recordings are not redacted — terminal output, URLs, and request headers are forwarded as-is
- The container does not join the Twingate network itself; clients reach it through a separate Connector
- gwops only modifies resources it originally created; objects made via the Admin Console are never touched
- gwops never creates groups, security policies, Remote Networks or Connectors; losing `/data/state.json` makes it forget which resources it owns — back up `/data`
- CA and leaf keys are files on `/data`; no HSM/KMS/Vault integration (a secrets agent can write CA files into the mounts)
- Gatorcast must be 0.6.0+ before upgrading gwops to Gateway 2.0.0, or recording lines are silently dropped
