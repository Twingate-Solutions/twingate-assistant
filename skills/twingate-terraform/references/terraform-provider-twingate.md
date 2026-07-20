# Twingate Terraform Provider

## Summary
Official Terraform provider for Twingate, enabling infrastructure-as-code management of Twingate network resources. Written in Go, it exposes Twingate objects (resources, groups, connectors, policies) as Terraform-managed infrastructure. Supports GitOps-driven access policy and network configuration.

## Key Information
- Current release: v4.2.2 (85 total releases)
- License: MPL-2.0
- Registry: [Terraform Registry](https://registry.terraform.io/providers/Twingate/twingate)
- Language: Go (96.6%)
- Docs in `docs/` are auto-generated from `templates/` — edit templates only

## Prerequisites
- Go 1.26+ (to build)
- Terraform 1.14.x
- Twingate API token with **Read, Write & Provision** permissions
- Bash

## Environment Variables (Required for Acceptance Tests & Provider Auth)

| Variable | Description | Example |
|---|---|---|
| `TWINGATE_URL` | Base Twingate domain | `twingate.com` |
| `TWINGATE_NETWORK` | Network slug | `myorg` (from `myorg.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token | `<token>` |

## Step-by-Step

### Build
```bash
make build
```

### Install Locally (for testing)
```bash
make install
```

### Run Unit Tests
```bash
make test
```

### Run Acceptance Tests (requires live network)
```bash
export TWINGATE_URL=twingate.com
export TWINGATE_NETWORK=<slug>
export TWINGATE_API_TOKEN=<token>
make testacc
```

### Update Documentation
```bash
# Edit files in templates/ only
make docs
# Outputs to docs/ (auto-generated, do not edit directly)
```

## Gotchas
- **Do not manually edit `docs/`** — these are auto-generated from `templates/`; changes will be overwritten
- `TWINGATE_NETWORK` is the slug only (e.g., `myorg`), not the full domain
- API token must have all three permissions: Read, Write, AND Provision
- Acceptance tests run against a real Twingate network — use a non-production network

## Related Docs
- [Terraform Registry Page](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- Provider examples: `/examples` directory in repo
- Template source: `/templates` directory in repo