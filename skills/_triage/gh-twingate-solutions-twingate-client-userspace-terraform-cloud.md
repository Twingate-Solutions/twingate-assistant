---
source: https://github.com/Twingate-Solutions/twingate-client-userspace-terraform-cloud
type: github
fetched: 2026-10-11
source_version: 4f66a1b1d35f712b1a90ed409a513488f0251817
trust: official
---

<!-- triage: unassigned -->

# Twingate Tunnel Provider for HCP Terraform

## Summary
A custom Terraform provider that starts the Twingate Client in userspace mode during HCP Terraform plan/apply runs, enabling HashiCorp-hosted workers to reach private resources without root access, custom images, or self-hosted agents. It exposes ephemeral resources that return local tunnel addresses for use by other providers. Provided as an unsupported reference example under Apache 2.0.

## Key Information
- Implements two ephemeral resource types: `twingatetunnel_tcp` (raw TCP tunnel) and `twingatetunnel_http_proxy` (HTTP CONNECT proxy)
- Requires no root privileges or custom worker image
- Downloads the `twingated` binary from the Twingate apt repo at runtime unless `client_path` is set
- No published registry builds; must be compiled and hosted yourself
- Developed with LLM assistance; review code before any production use

## Prerequisites
- Terraform `>= 1.10`
- A Twingate Service Account key with access to the target Resource
- Linux x86_64 or arm64 worker (HCP-hosted workers qualify)
- Outbound access to: `packages.twingate.com`, `s3.amazonaws.com`, `archive.ubuntu.com` (port 443); Twingate Controller/Relays (443, 30000–31000)

## Usage / Step-by-Step

**1. Bootstrap Twingate resources** using `examples/01-bootstrap-twingate`:
```bash
export TWINGATE_API_TOKEN=...
export TWINGATE_NETWORK=acme
cd examples/01-bootstrap-twingate
terraform init && terraform apply -var db_address=db.internal
terraform output -raw service_key
```

**2. Build the provider binary:**
```bash
VERSION=0.1.0
GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -trimpath \
  -ldflags "-X main.version=$VERSION" \
  -o terraform-provider-twingatetunnel_v$VERSION .
```

**3. Host the provider** via HCP private registry or by committing it to `terraform.d/plugins/<source>/<version>/linux_amd64/` in your config repo.

**4. Set workspace environment variable** `TWINGATE_SERVICE_KEY` (sensitive) to the service key JSON.

**5. Configure providers** using ephemeral resources:
```hcl
ephemeral "twingatetunnel_tcp" "db" {
  destination = "db.internal:5432"
}
provider "postgresql" {
  host = ephemeral.twingatetunnel_tcp.db.local_host
  port = ephemeral.twingatetunnel_tcp.db.local_port
}
```

## Configuration Values

**Provider (`twingatetunnel`):**
| Attribute | Default | Notes |
|---|---|---|
| `service_key` | `TWINGATE_SERVICE_KEY` env | Service Account key JSON |
| `client_version` | latest | Pin apt package version |
| `client_path` | — | Path to preinstalled `twingated` |
| `client_url` / `client_sha256` | — | Custom `.deb` mirror |
| `fetch_missing_libraries` | `true` | Fetch missing shared libs |
| `log_dir` | `/tmp/twingatetunnel/logs` | |
| `cache_dir` | `/tmp/twingatetunnel/cache` | |

**`twingatetunnel_tcp`:** `destination` (required), `local_host`, `local_port`, `ready_timeout` (default `90s`)

**`twingatetunnel_http_proxy`:** `probe_destination`, `ready_timeout` (default `90s`); outputs `proxy_url`, `proxy_host`, `proxy_port`

## Gotchas
- `local_port` defaults to a random free port; don't hardcode it
- Service key must match the exact Resource address/port configured in Twingate
- If `fetch_missing_libraries = false` and the worker lacks required shared libraries, the client will fail to start
- The `client_