# Twingate Terraform Provider

## Summary
The official Twingate Terraform provider enables infrastructure-as-code management of Twingate network objects. It exposes Twingate resources as Terraform-managed CRDs, supporting GitOps-driven access policy and network configuration.

## Key Information
- Repository: `github.com/Twingate/terraform-provider-twingate`
- License: MPL-2.0
- Current release: v4.2.0 (83 total releases)
- Written in Go (96.6%)
- Published on Terraform Registry

## Prerequisites
- Go 1.26+ (to build)
- Terraform 1.14.x+
- Bash
- Twingate API token with **Read, Write & Provision** permissions

## Build & Install Steps

```bash
# Build
make build

# Install locally for testing
make install

# Run unit tests
make test

# Run acceptance tests (requires env vars)
make testacc
```

## Configuration Values

### Required Environment Variables (acceptance tests / provider config)
| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base URL, e.g. `twingate.com` |
| `TWINGATE_NETWORK` | Network slug (e.g., `<slug>` from `<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Documentation
- Source files: `templates/` (edit these)
- Generated files: `docs/` (auto-generated — **do not edit manually**)
- Regenerate docs: `make docs`

## Gotchas
- Do not manually edit files in `docs/` — they are auto-generated from `templates/`
- API token must have all three permission levels: Read, Write, **and** Provision
- `TWINGATE_NETWORK` is the slug only, not the full domain

## Related Docs
- [Terraform Registry Provider Page](https://registry.terraform.io/providers/Twingate/twingate/latest)
- Twingate API documentation (for token generation)
- `examples/` directory in repo for usage examples
- `CONTRIBUTING` file in repo for contribution guidelines