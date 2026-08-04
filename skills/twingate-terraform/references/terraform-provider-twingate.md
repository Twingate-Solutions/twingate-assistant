# Twingate Terraform Provider

## Summary
Official Terraform provider for Twingate that exposes Twingate objects (networks, resources, groups, connectors) as Terraform-manageable infrastructure. Enables GitOps-driven access policy and network configuration. Licensed under MPL-2.0.

## Key Information
- Repository: `github.com/Twingate/terraform-provider-twingate`
- Language: Go
- Provider registry: Terraform Registry (HashiCorp)
- Docs in `docs/` are auto-generated from `templates/` — edit templates only

## Prerequisites
- Go 1.26+
- Terraform 1.14.x+
- Bash
- Twingate API token with **Read, Write & Provision** permissions

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
export TWINGATE_NETWORK=<slug>   # e.g., mycompany from mycompany.twingate.com
export TWINGATE_API_TOKEN=<token>
make testacc
```

### Update Documentation
```bash
# Edit files in templates/ only
make docs
# Output written to docs/ (do not edit docs/ manually)
```

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_URL` | Base Twingate URL (e.g., `twingate.com`) |
| `TWINGATE_NETWORK` | Network slug (the subdomain portion of `<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Gotchas
- `docs/` directory is **auto-generated** — manual edits will be overwritten by `make docs`
- API token must have all three permission levels: Read, Write, AND Provision
- Acceptance tests (`make testacc`) run against a real Twingate network — use a test/dev network
- Go version requirement is 1.26 (check `.go-version` or `.tool-versions` for pinned version)

## Related Docs
- [Terraform Registry - Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- Provider docs: `./docs/` directory in repo
- Examples: `./examples/` directory in repo
- Contributing guidelines: repo `CONTRIBUTING` (linked in GitHub)