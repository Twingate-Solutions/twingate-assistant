---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-10-04
source_version: a88e981b52ebf9f987b79cbdb541c042316d7d4f
trust: official
---

# Twingate Terraform Provider

## Summary
Terraform provider for managing Twingate resources (networks, connectors, remote networks, resources, groups, users, service accounts). Enables infrastructure-as-code workflows for Twingate access policy and network configuration via the Twingate API.

## Key Information
- Written in Go; built on the Terraform Plugin Framework
- Supports resources and data sources for groups, remote networks, connectors, resources, users, and service accounts
- Documentation in `docs/` is auto-generated from `templates/`; edit only the templates
- Acceptance tests require a live Twingate network and API token

## Prerequisites
- Bash
- Go 1.26+
- Terraform 1.14.x
- Twingate account with an API token (Read, Write & Provision permissions) for acceptance tests

## Usage / Step-by-Step

**Build**
```shell
make build
```

**Install locally**
```shell
make install
```

**Run unit tests**
```shell
make test
```

**Run acceptance tests**
```shell
export TWINGATE_URL=twingate.com
export TWINGATE_NETWORK=<slug>
export TWINGATE_API_TOKEN=<token>
make testacc
```

**Regenerate docs**
```shell
make docs
```

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base Twingate URL (e.g., `twingate.com`) |
| `TWINGATE_NETWORK` | Network slug (`<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Gotchas
- Files under `docs/` are auto-generated; manual edits will be overwritten by `make docs`
- Acceptance tests (`make testacc`) run against a real Twingate network and will create/modify live resources
- The repo description references a Kubernetes controller/CRD pattern, but the actual repo is a standard Terraform provider
- `twingate_kubernetes_resource`, `twingate_ssh_resource`, and `twingate_web_app_resource` each expose a read-only `tags_all` attribute (Map of String) that includes both resource-level tags and default tags from the provider configuration

## Related Docs
- [Terraform Registry – Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest/docs)
- [Twingate API documentation](https://docs.twingate.com/docs/api-overview)
- [Terraform Plugin Framework](https://developer.hashicorp.com/terraform/plugin/framework)