# Twingate Terraform Provider

## Summary
Official Terraform provider for Twingate, enabling infrastructure-as-code management of Twingate network resources. Written in Go and published on the Terraform Registry. Supports GitOps-driven access policy and network configuration via CRD-like resource definitions.

## Key Information
- Current latest release: v4.1.1 (Apr 15, 2026); 82 total releases
- License: MPL-2.0
- Requires Go 1.24 to build from source
- Requires Terraform 1.x
- Docs in `docs/` are auto-generated from `templates/`; edit `templates/` only

## Prerequisites
- Go 1.24+
- Terraform 1.x
- Twingate API token with **Read, Write & Provision** permissions
- Twingate network slug

## Environment Variables (Required for Acceptance Tests)

| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base URL, e.g. `twingate.com` |
| `TWINGATE_NETWORK` | Network slug (e.g., `myorg` from `myorg.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Step-by-Step: Common Tasks

**Build:**
```bash
make build
```

**Run unit tests:**
```bash
make test
```

**Run acceptance tests (requires env vars above):**
```bash
make testacc
```

**Install locally for testing:**
```bash
make install
```

**Regenerate docs:**
```bash
# Edit files in templates/ first, then:
make docs
```

## Gotchas
- Do **not** manually edit files in `docs/` — they are auto-generated and will be overwritten
- Acceptance tests run against a **real** Twingate network; ensure test credentials are for a non-production environment
- API token must have all three permission levels (Read, Write, Provision) or acceptance tests will fail

## Related Docs
- [Terraform Registry: Twingate Provider](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- Provider docs: `/docs` directory in repo (auto-generated)
- Templates source: `/templates` directory in repo