---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-11-01
source_version: eb86de16bca0ec81de497fed9f9c3c605ee87a9d
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

## Gotchas

- Do not edit files under `docs/` directly — they are overwritten by `make docs`. Edit `templates/` instead.
- Acceptance tests (`make testacc`) run against a real Twingate network and will create/modify live resources.
- The repo description references a Kubernetes controller/CRD, but the actual content is a Terraform provider; the description appears to be inaccurate metadata.

## Related Docs

- [Terraform Registry – Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Twingate API documentation](https://docs.twingate.com/docs/api-overview)
- [Terraform Provider Development](https://developer.hashicorp.com/terraform/plugin)