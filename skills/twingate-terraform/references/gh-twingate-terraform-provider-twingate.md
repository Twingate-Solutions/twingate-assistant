---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-11-08
source_version: 611ea671fb5d3560c8c98b90cc70f96c377e18f9
trust: official
---

# Twingate Terraform Provider

Terraform provider for managing Twingate resources (networks, resources, groups, connectors, service accounts, etc.) via infrastructure-as-code. Supports GitOps-driven access policy and network configuration through standard Terraform workflows.

## Key Information

- Written in Go; published to the Terraform Registry
- Current release: v5.2.0
- Adds `tls_mode` to web app resource `upstream` and `downstream` fields in v5.2.0
- Documentation in `docs/` is auto-generated from `templates/`; edit only `templates/`

## Prerequisites

- Bash
- Go 1.26+ (only needed to build from source)
- Terraform 1.14.x
- A Twingate account with an API token that has Read, Write, and Provision permissions

## Usage / Step-by-Step

**Build from source:**
```shell
make build
```

**Install locally for testing:**
```shell
make install
```

**Run unit tests:**
```shell
make test
```

**Run acceptance tests** (requires live Twingate network):
```shell
export TWINGATE_URL=twingate.com
export TWINGATE_NETWORK=<your-network-slug>
export TWINGATE_API_TOKEN=<api-token>
make testacc
```

**Regenerate docs:**
```shell
make docs
```

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base Twingate URL (e.g., `twingate.com`) |
| `TWINGATE_NETWORK` | Network slug (the subdomain portion of `<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write, and Provision permissions |

## Example Deployments

The `examples/` directory contains complete, runnable Terraform configurations. Corresponding guide pages live under `docs/guides/`.

### DigitalOcean – SSH Gateway with Self-Signed CA (`do-gateway-ssh-self-signed`)
Deploys three Droplets (Connector, Gateway, SSH server) on the region's default VPC. A DigitalOcean cloud firewall restricts inbound traffic to the VPC range; SSH on port 22 from anywhere is additionally allowed for troubleshooting. The Gateway is registered using its private IP. TLS and SSH keys are injected via `user_data`/`templatefile()`.

### DigitalOcean – HTTPS Gateway with Self-Signed CA (`do-gateway-https-self-signed`)
Deploys three Droplets (Connector, Gateway, httpbin) on the region's default VPC. A cloud firewall allows inbound traffic only from the VPC IP range. The Gateway terminates TLS on port 8443 and proxies to httpbin over HTTP. `twingate_web_app_resource` uses `downstream.tls_mode = "TLS13"` and `request_header_rewrites` to inject identity headers. `terraform apply` writes `do_example_https_ca.crt` for local trust store import. CA rotation is done by replacing `tls_private_key.x509_ca`.

### GCE – HTTPS Gateway with Self-Signed CA (`gce-gateway-https-self-signed`)
Deploys three GCE VMs (Connector, Gateway, httpbin) on a dedicated VPC with Cloud NAT for internet access. The Gateway VM uses a reserved internal IP and is tagged `iap-ssh` for IAP-based SSH access. `twingate_web_app_resource` uses `downstream.tls_mode = "TLS13"` and `request_header_rewrites`. `terraform apply` writes `gce_example_https_ca.crt`. CA rotation uses `terraform apply -replace=tls_private_key.x509_ca`.

> **Warning (all self-signed CA examples):** Private keys and certificates are stored unencrypted in Terraform state. Use a remote backend with encryption.

## Gotchas

- Do not edit files under `docs/` directly — they are overwritten by `make docs`. Edit `templates/` instead.
- Acceptance tests (`make testacc`) run against a real Twingate network and will create/modify live resources.
- The repo description references a