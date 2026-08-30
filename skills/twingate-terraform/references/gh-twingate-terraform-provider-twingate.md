---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-08-30
source_version: 2547a7ef3becc430b4aee7a6bd75026259231552
---

# Twingate Terraform Provider

## Summary
Terraform provider for managing Twingate resources (networks, resources, groups, connectors, policies) as infrastructure-as-code. Supports GitOps-driven access policy and network configuration via Twingate's API.

## Key Information
- Written in Go; published to the Terraform Registry
- Covers resources: `twingate_resource`, `twingate_group`, `twingate_connector`, `twingate_remote_network`, `twingate_user`, `twingate_service_account`, `twingate_ssh_resource`, `twingate_kubernetes_resource`, `twingate_web_app_resource`, `twingate_gateway`, and associated data sources
- Docs in `docs/` are auto-generated from `templates/`; edit templates, not generated files
- Latest stable release: **v4.3.2**

## Prerequisites
- Bash
- Go 1.26+ (to build)
- Terraform 1.14.x+
- A Twingate account with an API token (Read, Write & Provision permissions)

## Usage / Step-by-Step

**Build**
```shell
make build
```

**Install locally for testing**
```shell
make install
```

**Configure the provider**
```hcl
provider "twingate" {
  api_token = var.twingate_api_token
  network   = "<slug>"          # your <slug>.twingate.com
  url       = "twingate.com"
}
```

**Run unit tests**
```shell
make test
```

**Run acceptance tests** (requires live network — see env vars below)
```shell
make testacc
```

**Regenerate docs**
```shell
make docs
```

## Configuration Values

| Variable | Where Used | Description |
|---|---|---|
| `TWINGATE_API_TOKEN` | env / provider arg | API token with Read, Write & Provision permissions |
| `TWINGATE_NETWORK` | env / provider arg | Network slug (`<slug>.twingate.com`) |
| `TWINGATE_URL` | env / provider arg | Base URL, typically `twingate.com` |

All three can also be set directly in the provider block as `api_token`, `network`, and `url`.

## Resource Notes

### `twingate_ssh_resource`
- `username` and `protocols` attributes have been removed from the schema (deprecated and dropped)
- Required: `name`, `gateway_id`, `remote_network_id`, `address`
- Optional: `alias`, `is_visible`, `security_policy_id`, `tags`, `access_group`, `access_policy`

### `twingate_kubernetes_resource`
- `protocols` attribute has been removed from the schema
- Optional: `ca_file`, `in_cluster`, `is_visible`, `security_policy_id`, `tags`

### `twingate_web_app_resource` (new)
- Web App Resources accessed via a Gateway
- Required: `address`, `downstream` (port), `gateway_id`, `name`, `remote_network_id`, `upstream` (port)
- Optional: `alias`, `is_visible`, `request_header_rewrites` (map of HTTP headers to rewrite), `security_policy_id`, `tags`, `access_group`, `access_policy`
- Read-only: `id`

### `twingate_gateway_config` (removed)
- The `twingate_gateway_config` Terraform resource has been removed
- Gateway configuration is now done via a YAML file (e.g., `config.yaml.tftpl`) rendered with Terraform's `templatefile()` function and passed to the instance's startup script
- Example YAML structure includes `twingate.network`, `twingate.host`, `port`, `metricsPort`, `tls`, `ssh.gateway`, `ssh.ca` (manual or vault), with camelCase field names (e.g., `certificateFile`, `privateKeyFile`, `caBundleFile`)

## Gateway Configuration (YAML approach)

The gateway reads a YAML config file. Use `templatefile()` to render it:

```terraform
locals {
  gateway_port = 8443
  gateway_config = templatefile("${path.module}/config.yaml.