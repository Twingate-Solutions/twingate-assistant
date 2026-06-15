# Twingate Terraform Provider

## Summary
The Twingate Terraform Provider enables infrastructure-as-code management of Twingate network objects. It exposes Twingate resources (networks, connectors, resources, groups, policies) as Terraform-managed infrastructure. The provider supports GitOps-driven access policy and network configuration.

## Key Information
- Latest release: v4.2.1 (June 8, 2026)
- Language: Go (96.6%)
- License: MPL-2.0
- 84 releases published; 617 commits on `main`
- Docs in `docs/` are auto-generated from `templates/` — edit templates only

## Prerequisites
- Go 1.26+ (to build the provider)
- Terraform 1.14.x
- Twingate API token with **Read, Write & Provision** permissions
- Bash

## Step-by-Step

### Build
```bash
make build
```

### Install (local testing)
```bash
make install
```

### Run Unit Tests
```bash
make test
```

### Run Acceptance Tests
```bash
export TWINGATE_URL=twingate.com
export TWINGATE_NETWORK=<your-slug>   # e.g., slug from <slug>.twingate.com
export TWINGATE_API_TOKEN=<api-token>
make testacc
```

### Update Documentation
```bash
# Edit files in templates/ only, then regenerate:
make docs
```

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base Twingate URL (e.g., `twingate.com`) |
| `TWINGATE_NETWORK` | Network slug (subdomain portion of `<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Gotchas
- **Do not manually edit `docs/` files** — they are auto-generated from `templates/`. Changes will be overwritten on next `make docs`.
- Acceptance tests (`make testacc`) run against a **real Twingate network** — all three env vars must be set first.
- API token requires all three permission levels (Read, Write, Provision); missing Provision will cause failures.

## Related Docs
- [Terraform Registry - Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- [Provider docs/](https://github.com/Twingate/terraform-provider-twingate/tree/main/docs) — auto-generated resource and data source references
- [examples/](https://github.com/Twingate/terraform-provider-twingate/tree/main/examples) — usage examples per resource type