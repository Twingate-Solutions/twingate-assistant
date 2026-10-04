---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-10-04
source_version: bfa036b5a7ca336a38c8b069fbc31ba6bf19b23f
trust: official
---

# Twingate Pulumi Resource Provider

Pulumi provider for managing Twingate infrastructure. Supports Python, TypeScript/JavaScript, Go, and .NET. Wraps the Twingate API to allow declarative management of Twingate resources via Pulumi stacks.

## Key Information

- Package names: `@twingate/pulumi-twingate` (Node.js), `pulumi-twingate` (Python), `github.com/pulumi/pulumi-twingate/sdk/go/...` (Go), `Twingate.Twingate` (.NET)
- Requires a Twingate API token and network ID, available from the Twingate Admin Console
- Full API reference at the [Pulumi registry](https://www.pulumi.com/registry/packages/twingate/api-docs/)

## Prerequisites

- Twingate account with API access
- Pulumi CLI
- For local development: Go 1.24+, Node.js 22+

## Configuration Values

| Config Key | Env Variable | Required | Description |
|---|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API token from Twingate Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (subdomain portion of Admin Console URL) |
| `twingate:url` | — | No | Defaults to `twingate.com`; do not change unless instructed |

## Usage

Install the package for your language, then configure the provider:

```bash
pulumi config set twingate:apiToken <token> --secret
pulumi config set twingate:network <network-id>
```

Alternatively, set `TWINGATE_API_TOKEN` and `TWINGATE_NETWORK` environment variables before running `pulumi up`.

## Local Development

1. Build the provider and SDKs:
   ```bash
   make development
   ```
2. Install the locally built plugin:
   ```bash
   pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate
   ```
3. Verify:
   ```bash
   pulumi plugin ls | grep twingate
   ```

## Gotchas

- Local development builds produce version strings with `+dirty` suffixes (e.g., `v4.1.0-alpha.1772811417+dirty`). Pulumi cannot fetch these from GitHub releases automatically; you must install the plugin manually with `--file` as shown above.
- The `twingate:url` config value should not be changed under normal circumstances.
- The `act` tool for local GitHub Actions testing requires Docker. On first run it will prompt for an image size; choose **Medium** for most workflows.

## Related Docs

- [Twingate API Overview](https://docs.twingate.com/docs/api-overview)
- [Pulumi Registry – Twingate](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- [Pulumi CLI install](https://www.pulumi.com/docs/install/)
- [act (local GitHub Actions runner)](https://github.com/nektos/act)