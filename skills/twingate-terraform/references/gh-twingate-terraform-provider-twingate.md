---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-11-19
source_version: 535765efb428435a5a65e9e5ea561ac1fffd90eb
trust: official
---

# Twingate Terraform Provider (Twingate/terraform-provider-twingate)

## Summary
This repo contains the Terraform provider for managing Twingate resources (networks, resources, access policies, and related objects) as infrastructure as code. Note that the repo metadata description mentions a Kubernetes controller exposing CRDs, but the README and release notes describe a Terraform provider; this summary follows the README. The latest release is v5.2.0.

## Key Information
- Written in Go; built as a Terraform provider plugin.
- Latest release v5.2.0 adds `tls_mode` to the web app resource, for both `upstream` and `downstream`.
- The release also includes dependency bumps (Dependabot) and documentation updates migrating Gateway config in the AWS, DigitalOcean, GCE Vault, and GCE Self Signed SSH examples.
- Default branch: `main`.
- Documentation in `docs/` is auto-generated from `templates/`.
- Contributions are released under the project's open source license (see `LICENSE`).

## Prerequisites
- Bash
- Go 1.26 (to build the provider)
- Terraform 1.14.x
- For acceptance tests: a real Twingate network and an API token with Read, Write & Provision permissions

## Usage / Step-by-Step
1. Build the provider: `make build`
2. Run unit tests: `make test`
3. Run acceptance tests (after setting the environment variables below): `make testacc`
4. Install the provider locally for testing: `make install`
5. Update docs: edit files in `templates/`, then run `make docs`

## Configuration Values
Environment variables for acceptance tests:
- `TWINGATE_URL`: Twingate domain, e.g. `twingate.com`
- `TWINGATE_NETWORK`: your network slug (from `<slug>.twingate.com`)
- `TWINGATE_API_TOKEN`: API token with Read, Write & Provision permissions

## Gotchas
- Do not edit files in `docs/` by hand; they are overwritten by `make docs`.
- Acceptance tests run against a real Twingate network, so use a non-production network and a dedicated token.
- The repo description (Kubernetes controller/CRDs) does not match the README content; verify you are using the intended project.
- Go and Terraform version requirements are specific (Go 1.26, Terraform 1.14.x); mismatched versions may cause build or test problems.

## Related Docs
- Full changelog for v5.2.0: https://github.com/Twingate/terraform-provider-twingate/compare/v5.1.1...v5.2.0
- Web app `tls_mode` PR: https://github.com/Twingate/terraform-provider-twingate/pull/999
- Go install: https://golang.org/doc/install
- Terraform downloads: https://www.terraform.io/downloads.html