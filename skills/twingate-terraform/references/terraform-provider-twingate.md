# Twingate Terraform Provider

## Summary
The official Twingate Terraform provider enables infrastructure-as-code management of Twingate network objects. It exposes Twingate resources (networks, connectors, access policies) as Terraform-manageable CRDs. The provider supports GitOps-driven access policy and network configuration.

## Key Information
- Repository: `github.com/Twingate/terraform-provider-twingate`
- License: MPL-2.0
- Latest release: v4.2.2 (85 total releases)
- Written in Go (96.6%)
- Published on Terraform Registry

## Prerequisites
- Go 1.26+ (to build the provider)
- Terraform 1.14.x+
- Bash
- Twingate account with API token (Read, Write & Provision permissions)

## Environment Variables (Required for Acceptance Tests)
| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base URL, e.g., `twingate.com` |
| `TWINGATE_NETWORK` | Your network slug (e.g., `myorg` from `myorg.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Build & Install Steps

```bash
# Build the provider
make build

# Run unit tests
make test

# Run acceptance tests (requires env vars above)
make testacc

# Install for local testing
make install
```

## Documentation Workflow
- Edit templates in `templates/` directory
- Run `make docs` to regenerate
- **Do not manually edit** files in `docs/` — they are auto-generated

## Configuration Values
The provider is configured via the three environment variables listed above. These same values are used in the provider block in Terraform configurations:

```hcl
provider "twingate" {
  api_token = var.twingate_api_token
  network   = var.twingate_network
  url       = "twingate.com"
}
```

## Gotchas
- `docs/` files are auto-generated — manual edits will be overwritten by `make docs`
- Acceptance tests (`make testacc`) run against a **real Twingate network** — use a non-production network
- API token must have all three permission levels: Read, Write, AND Provision
- Go version requirement is 1.26 (newer than many standard installations)

## Related Docs
- [Terraform Registry Page](https://registry.terraform.io/providers/Twingate/twingate)
- [Provider Documentation](https://github.com/Twingate/terraform-provider-twingate/tree/main/docs)
- [Examples](https://github.com/Twingate/terraform-provider-twingate/tree/main/examples)
- [Contributing Guidelines](https://github.com/Twingate/terraform-provider-twingate/blob/main/CONTRIBUTING.md)
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)