---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-08-06
source_version: 57f5b1571bc333d6bd6fa398fc68c0184d939a42
---

# Twingate Terraform Provider

## Summary
Terraform provider for managing Twingate network resources (resources, groups, connectors, users, policies) as infrastructure-as-code. Supports GitOps-driven access policy and network configuration via CRDs. Current stable release is v4.3.1.

## Key Information
- Written in Go; built on the Terraform Plugin SDK
- Covers Twingate resources: networks, connectors, groups, users, resource access policies, security policies
- Docs in `docs/` are auto-generated from `templates/`; edit only `templates/`
- Acceptance tests require a live Twingate network

## Prerequisites
- Bash
- Go 1.26+
- Terraform 1.14.x+
- Twingate account with an API token (Read, Write & Provision permissions)

## Usage / Step-by-Step

**Build**
```shell
make build
```

**Install locally (for testing)**
```shell
make install
```

**Run unit tests**
```shell
make test
```

**Run acceptance tests (live network required)**
```shell
export TWINGATE_URL=twingate.com
export TWINGATE_NETWORK=<slug>
export TWINGATE_API_TOKEN=<token>
make testacc
```

**Regenerate docs**
```shell
# Edit templates/ first, then:
make docs
```

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base Twingate URL (e.g. `twingate.com`) |
| `TWINGATE_NETWORK` | Network slug (`<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Gotchas
- `docs/` is auto-generated — manual edits will be overwritten by `make docs`
- Acceptance tests (`make testacc`) hit a real Twingate network and will create/modify resources
- `access_group` `security_policy_id` had an inconsistency-after-apply bug; fixed in v4.3.1
- The repo description references "Kubernetes controller / CRDs," which appears to describe a related but distinct project — this repo is specifically the Terraform provider

## Related Docs
- [Terraform Registry: Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest/docs)
- [Twingate API Documentation](https://docs.twingate.com/docs/api)
- [Go Installation](https://golang.org/doc/install)
- [Terraform Downloads](https://www.terraform.io/downloads.html)