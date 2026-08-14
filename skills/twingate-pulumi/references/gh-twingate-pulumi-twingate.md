---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-08-14
source_version: 9f4488dd291c6faad9a88dd605d8793a02e9867d
---

# Twingate Pulumi Provider

## Summary
A Pulumi resource provider for managing Twingate infrastructure as code. Supports Python, TypeScript/JavaScript, Go, and .NET. Wraps the Twingate API to allow declarative management of Twingate network resources.

## Key Information
- Package names: `@twingate/pulumi-twingate` (Node.js), `pulumi-twingate` (Python), `Twingate.Twingate` (.NET)
- Go module: `github.com/pulumi/pulumi-twingate/sdk/go/...`
- Full API reference available on the [Pulumi Registry](https://www.pulumi.com/registry/packages/twingate/api-docs/)

## Prerequisites
- Pulumi CLI installed
- Twingate account with Admin Console access
- Twingate API token (from Admin Console)
- Twingate network ID
- **For local development:** Go 1.24+, Node.js 22+

## Installation

```bash
# Node.js
npm install @twingate/pulumi-twingate

# Python
pip install pulumi-twingate

# Go
go get github.com/pulumi/pulumi-twingate/sdk/go/...

# .NET
dotnet add package Twingate.Twingate
```

## Configuration Values

| Config Key | Environment Variable | Required | Description |
|---|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API token from Twingate Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (subdomain portion of Admin Console URL, e.g., `autoco` from `autoco.twingate.com`) |
| `twingate:url` | — | No | Base URL; defaults to `twingate.com` |

Set via Pulumi config or environment variables:
```bash
pulumi config set twingate:apiToken <token>
pulumi config set twingate:network <network-id>
```

## Local Development

```bash
# Build all SDKs
make development

# Build provider + Node.js SDK only
make provider build_nodejs

# Install local plugin manually
pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate

# Verify
pulumi plugin ls | grep twingate
```

## Gotchas
- **404 on `pulumi up`/`pulumi preview` with local builds:** Local dev builds (with version strings like `v4.x.x-alpha+dirty`) won't be found on GitHub Releases. Must manually install with `pulumi plugin install ... --file bin/pulumi-resource-twingate`. Check the error message for the exact version string to use.
- The `twingate:url` config value should not be changed under normal circumstances.
- Build version strings include `+dirty` if there are uncommitted changes; the exact string appears in error messages and must match what's passed to `pulumi plugin install`.

## Testing CI Workflows Locally
Uses [`act`](https://github.com/nektos/act) to run GitHub Actions locally. Choose "Medium" Docker image on first run.
```bash
act --list
act pull_request -j lint
```

## Related Docs
- [Twingate API Overview](https://docs.twingate.com/docs/api-overview)
- [Pulumi Registry – Twingate](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- [Pulumi CLI Installation](https://www.pulumi.com/docs/install/)