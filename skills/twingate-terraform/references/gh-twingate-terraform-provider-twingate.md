---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-08-23
source_version: 6875b07f8528f796df1498039e2414a58c087042
---

# Twingate Terraform Provider

## Summary
Terraform provider for managing Twingate resources (networks, resources, groups, connectors, policies) as infrastructure-as-code. Supports GitOps-driven access policy and network configuration via Twingate's API.

## Key Information
- Written in Go; published to the Terraform Registry
- Covers resources: `twingate_resource`, `twingate_group`, `twingate_connector`, `twingate_remote_network`, `twingate_user`, `twingate_service_account`, and associated data sources
- Docs in `docs/` are auto-generated from `templates/`; edit templates, not generated files
- Latest stable release: **v4.3.1**

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

## Gotchas
- `docs/` is auto-generated — manual edits will be overwritten by `make docs`
- Acceptance tests (`make testacc`) hit a real Twingate network; all three env vars must be set or tests fail
- The repo description references "Kubernetes controller / CRDs," which is inaccurate metadata — this is a Terraform provider, not a Kubernetes controller
- Recent fix (v4.3.1): `access_group` `security_policy_id` could show inconsistent state after `apply`; update if using that attribute

## Related Docs
- [Terraform Registry – Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest/docs)
- [Twingate API Docs](https://docs.twingate.com/docs/api-overview)
- [Terraform Plugin Framework](https://developer.hashicorp.com/terraform/plugin/framework)
- [Go Installation](https://golang.org/doc/install)