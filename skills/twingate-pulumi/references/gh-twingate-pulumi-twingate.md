---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-11-08
source_version: 275271aff59870dc2d1cabdb8474f8d841db82bd
trust: official
---

# Twingate Pulumi Provider

Pulumi provider for managing Twingate infrastructure as code. Supports Python, TypeScript/JavaScript, Go, and .NET. Wraps the Twingate API to manage resources such as networks, connectors, and access policies.

## Key Information

- Package name varies by language: `@twingate/pulumi-twingate` (Node.js), `pulumi-twingate` (Python), `Twingate.Twingate` (.NET)
- Go module path: `github.com/pulumi/pulumi-twingate/sdk/go/...`
- Full API reference available at the [Pulumi Registry](https://www.pulumi.com/registry/packages/twingate/api-docs/)

## Prerequisites

- Pulumi CLI
- Twingate API token (from the Twingate Admin Console)
- Twingate network ID (visible in the Admin Console URL, e.g., `autoco` from `autoco.twingate.com`)
- For local development: Go 1.24+, Node.js 22+

## Configuration Values

| Config Key | Env Var | Required | Description |
|---|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API token from Twingate Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (subdomain portion of Admin Console URL) |
| `twingate:url` | — | No | Defaults to `twingate.com`; do not change unless instructed |

## Usage / Step-by-Step (Local Development Build)

1. Build the provider and SDKs:
   ```bash
   make development
   ```
2. Install the locally built plugin:
   ```bash
   pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate
   ```
   Replace `<version>` with the version string from your build output.
3. Verify installation:
   ```bash
   pulumi plugin ls | grep twingate
   ```

## Gotchas

- Local development builds include a `+dirty` suffix in the version string if there are uncommitted changes. Pulumi cannot auto-download this version and will return a 404; you must install the plugin manually with `--file`.
- The exact version string required for `pulumi plugin install` appears in the 404 error message—copy it from there.
- `twingate:url` should not be changed under normal circumstances.
- The `act` install script for Linux pipes from a GitHub raw URL into bash; visit the [act installation guide](https://github.com/nektos/act#installation) to review before running.

## Recent Changes (Unreleased / HEAD)

- **Added**: `tlsMode` field on `upstream` and `downstream` blocks of `TwingateWebAppResource`. This was present in the upstream provider since v5.2.0 but was missing from the SDKs due to a schema regeneration oversight.
- **Fixed**: HCL examples in Registry docs previously opened with a `pulumi {}` block (rejected by the Pulumi HCL language plugin); they now use `terraform {}`.
- **Fixed**: Identifiers such as `VERIFY_FULL`, `VERIFY_CA`, `GOOGLE_CLOUD`, `ON_PREMISE`, and `twingate_service_account_key` were rendered with `*` in place of `_` in generated descriptions; underscores are now preserved correctly.

## Related Docs

- [Twingate API Overview](https://docs.twingate.com/docs/api-overview)
- [Pulumi Registry – Twingate](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- [Pulumi CLI Installation](https://www.pulumi.com/docs/install/)
- [act (local GitHub Actions runner)](https://github.com/nektos/act)