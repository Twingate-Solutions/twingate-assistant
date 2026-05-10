# Twingate Terraform Provider

## Summary
Official Terraform provider for Twingate, enabling infrastructure-as-code management of Twingate network objects. Written in Go and published on the Terraform Registry. Supports GitOps-driven access policy and network configuration via CRD-like resource management.

## Key Information
- Repository: `Twingate/terraform-provider-twingate`
- License: MPL-2.0
- Latest release: v4.2.0 (May 2026); 83 total releases
- Language: Go 96.6%
- Docs in `docs/` are auto-generated from `templates/`; edit `templates/` only

## Prerequisites
- Go 1.24+ (to build)
- Terraform 1.x
- Twingate API token with **Read, Write & Provision** permissions
- Bash

## Environment Variables (Required for Acceptance Tests)
| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base URL, e.g. `twingate.com` |
| `TWINGATE_NETWORK` | Network slug (the `<slug>` from `<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Step-by-Step: Common Tasks

**Build:**
```bash
make build
```

**Unit Tests:**
```bash
make test
```

**Acceptance Tests (requires live network):**
```bash
export TWINGATE_URL=twingate.com
export TWINGATE_NETWORK=<your-slug>
export TWINGATE_API_TOKEN=<your-token>
make testacc
```

**Local Install (for testing):**
```bash
make install
```

**Regenerate Docs:**
```bash
# Edit files in templates/ first, then:
make docs
```

## Gotchas
- Do **not** manually edit files in `docs/`—they are auto-generated and changes will be overwritten
- Acceptance tests run against a **real** Twingate network; use a non-production network
- API token must have **all three** permission levels: Read, Write, and Provision
- `TWINGATE_NETWORK` requires just the slug portion, not the full domain

## Related Docs
- [Terraform Registry - Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- `examples/` directory in repo for usage examples
- `templates/` directory for documentation source files