---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-10-28
source_version: e073772365f795a6d96437a217c6b11cbd8f52a2
trust: official
---

# Twingate Terraform Provider

Terraform provider for managing Twingate network resources including Remote Networks, Resources, Connectors, and Groups. Supports GitOps-driven access policy and network configuration via standard Terraform workflows.

## Key Information

- Written in Go; provider source lives in this repo and is published to the Terraform Registry
- Acceptance tests require a live Twingate network and API token
- Documentation in `docs/` is auto-generated from `templates/` — do not edit `docs/` directly
- Latest release (v5.2.0) adds `tls_mode` to web app resource `upstream` and `downstream` fields

## Prerequisites

- Bash
- Go 1.26+
- Terraform 1.14.x+
- Twingate account with an API token scoped to Read, Write & Provision permissions (for acceptance tests)

## Usage / Step-by-Step

**Build**
```shell
make build
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

**Install locally for testing**
```shell
make install
```

**Regenerate docs**
```shell
# Edit files in templates/ first, then:
make docs
```

## Configuration Values

| Name | Type | Description |
|---|---|---|
| `TWINGATE_URL` | env var | Base Twingate URL (e.g. `twingate.com`) |
| `TWINGATE_NETWORK` | env var | Network slug (`<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | env var | API token with Read, Write & Provision permissions |

## Gotchas

- `docs/` is auto-generated; manual edits will be overwritten on the next `make docs` run
- Acceptance tests hit a real Twingate network and will create/modify live resources
- The repo description references a Kubernetes controller, but the actual content is a Terraform provider — ignore the description

## Related Docs

- [Terraform Registry – Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest/docs)
- [Twingate API documentation](https://docs.twingate.com/docs/api-overview)
- [Go installation](https://golang.org/doc/install)
- [Terraform downloads](https://www.terraform.io/downloads.html)