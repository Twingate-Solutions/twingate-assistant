---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-09-20
source_version: 75c5a2a3a557217b61e69fe5e2fa8806332cc4b6
---

# Twingate Terraform Provider

## Summary
Terraform provider for managing Twingate resources (networks, resources, groups, connectors, policies) as infrastructure-as-code. Supports GitOps-driven access policy and network configuration via Twingate's API.

## Key Information
- Written in Go; published to the Terraform Registry
- Covers resources: `twingate_resource`, `twingate_group`, `twingate_connector`, `twingate_remote_network`, `twingate_user`, `twingate_service_account`, `twingate_ssh_resource`, `twingate_kubernetes_resource`, `twingate_web_app_resource`, and associated data sources
- Docs in `docs/` are auto-generated from `templates/`; edit templates, not generated files
- Coverage reporting: Codecov (switched from Coveralls)
- Latest stable release: **v5.0.2**

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

## Breaking Changes in v5.0.0

### Removed: `twingate_gateway_config` resource
The resource has been removed entirely. It only ever rendered a static YAML document; no remote object was created. Replace it with Terraform's built-in `templatefile()` function:

```terraform
locals {
  gateway_config = templatefile("${path.module}/config.yaml.tftpl", {
    twingate_network = var.tg_network
    twingate_host    = var.tg_url
    port             = local.gateway_port
  })
}
```

Remove the old resource from state:
```bash
terraform state rm twingate_gateway_config.<name>
```

Any reference to `twingate_gateway_config.config.content` becomes `local.gateway_config`. If a `lifecycle` block used `replace_triggered_by` pointing at the old resource, wrap the rendered config in a `terraform_data` resource instead.

### Removed: `username` from `twingate_ssh_resource`
The `username` attribute has been removed. It only fed the now-removed `twingate_gateway_config`; the Gateway now takes the username from the runtime connection. No state change is required since the attribute never reached the Twingate API. A config that still sets `username` fails with `Unsupported argument`.

Note: `ssh.gateway.username` in the Gateway's YAML config (the OS user the Gateway process runs as) is unrelated and still required.

### Removed: `protocols` from `twingate_ssh_resource` and `twingate_kubernetes_resource`
Port restrictions do not apply to SSH and Kubernetes resources, so `protocols` never had any effect. Remove it from configs. A config that still sets `protocols` on either resource fails with `Unsupported argument`.

## New in v5.0.0

### New resource: `twingate_web_app_resource`
Web App Resources are Twingate resources accessed via a Gateway.