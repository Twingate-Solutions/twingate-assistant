---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-11-13
source_version: d4427d5a241c39cee8076de09d0e758d131ab71c
trust: official
---

# Twingate Terraform Provider (Twingate/terraform-provider-twingate)

## Summary
This repo contains the Terraform provider for managing Twingate resources (networks, resources, access policies) as infrastructure as code. Note: the repo metadata describes it as a Kubernetes controller exposing CRDs, but the README and release notes describe a Terraform provider. The latest release is v5.2.0, which adds `tls_mode` to the web app resource.

## Key Information
- Written in Go; built as a Terraform provider plugin.
- Latest release: v5.2.0 (changelog compares against v5.1.1).
- v5.2.0 adds `tls_mode` to the web app resource's `upstream` and `downstream` settings (PR #999).
- Other v5.2.0 changes: Go module dependency bumps and documentation updates migrating Gateway config in the AWS, DigitalOcean, GCE Vault, and GCE Self Signed SSH examples.
- Docs in `docs/` are auto-generated from `templates/`.
- Coverage is tracked on Codecov.
- Contributions are released under the project's open source license (see `LICENSE`).

## Prerequisites
- Bash
- Go 1.26 (to build the provider)
- Terraform 1.14.x
- For acceptance tests: a real Twingate network and an API token with Read, Write & Provision permissions

## Usage / Step-by-Step
1. Build the provider: `make build`
2. Run unit tests: `make test`
3. Set the acceptance test environment variables (below).
4. Run acceptance tests: `make testacc`
5. Install locally for testing: `make install`
6. To update docs, edit files in `templates/`, then run `make docs`.

## Configuration Values
Environment variables for acceptance tests:
- `TWINGATE_URL`: Twingate domain, e.g. `twingate.com`
- `TWINGATE_NETWORK`: your network slug (`<slug>.twingate.com`)
- `TWINGATE_API_TOKEN`: API token with Read, Write & Provision permissions

Resource attributes (v5.2.0):
- `tls_mode` on web app resource `upstream` and `downstream`

## Gotchas
- Do not edit files in `docs/` manually; they are overwritten by `make docs`.
- Acceptance tests (`make testacc`) run against a real Twingate network, so use a suitable test network and token.
- The repo description does not match the README content (Kubernetes controller vs. Terraform provider); treat the README as authoritative.
- Version requirements (Go 1.26, Terraform 1.14.x) are specific; mismatched versions may fail to build or run.

## Related Docs
- Release notes: https://github.com/Twingate/terraform-provider-twingate/compare/v5.1.1...v5.2.0
- `tls_mode` PR: https://github.com/Twingate/terraform-provider-twingate/pull/999
- Go install: https://golang.org/doc/install
- Terraform downloads: https://www.terraform.io/downloads.html