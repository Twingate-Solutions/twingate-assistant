---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-08-09
source_version: 0c7c83cfaf0a89ee24e70eda71869c5548f3506c
---

# Twingate Pulumi Provider

## Summary
Pulumi provider for managing Twingate infrastructure (networks, resources, connectors, policies) using Python, TypeScript, Go, or .NET. Wraps the Twingate API and integrates with standard Pulumi workflows.

## Key Information
- Supports Node.js, Python, Go, and .NET SDKs
- Built on top of the Twingate REST API
- Full reference docs available on the [Pulumi Registry](https://www.pulumi.com/registry/packages/twingate/api-docs/)

## Prerequisites
- Pulumi CLI installed
- Twingate Admin Console access (to generate API token and find network ID)
- **For local dev/build only:**
  - Go 1.24+
  - Node.js 22+

## Installation

| Platform | Command |
|----------|---------|
| Node.js | `npm install @twingate/pulumi-twingate` or `yarn add @twingate/pulumi-twingate` |
| Python | `pip install pulumi-twingate` |
| Go | `go get github.com/pulumi/pulumi-twingate/sdk/go/...` |
| .NET | `dotnet add package Twingate.Twingate` |

## Configuration Values

| Config Key | Env Var | Required | Description |
|------------|---------|----------|-------------|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API token from Twingate Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (subdomain portion of `<network>.twingate.com`) |
| `twingate:url` | — | No | Defaults to `twingate.com`; do not change under normal use |

Set via Pulumi config:
```bash
pulumi config set twingate:apiToken <token>
pulumi config set twingate:network <network-id>
```

Or via environment variables.

## Local Build (Development)

```bash
# Build all SDKs
make development

# Build provider + Node.js SDK only
make provider build_nodejs

# Install local plugin after build
pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate

# Verify
pulumi plugin ls | grep twingate
```

## Gotchas
- **404 on `pulumi up`/`pulumi preview`**: Local dev builds with versions like `v4.x.x-alpha...+dirty` are not published to GitHub Releases. Must manually install the plugin with `--file bin/pulumi-resource-twingate`. Check the error message for the exact version string.
- The `twingate:url` config should not be changed unless working against a non-production Twingate environment.
- Network ID is the subdomain only (e.g., `autoco` from `autoco.twingate.com`), not the full URL.
- Local builds append `+dirty` to the version if there are uncommitted changes.

## Testing Workflows Locally
Uses [`act`](https://github.com/nektos/act) to run GitHub Actions locally:
```bash
act --list
act pull_request -j lint
```
Select "Medium" Docker image size on first run.

## Related Docs
- [Twingate API Overview](https://docs.twingate.com/docs/api-overview)
- [Pulumi Registry – Twingate](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- [Pulumi CLI Install](https://www.pulumi.com/docs/install/)
- [act (local GitHub Actions runner)](https://github.com/nektos/act)