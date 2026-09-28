---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-09-27
source_version: e6ea2decc713695f82b931ec9ff41c90f12f01de
---

# Twingate Pulumi Resource Provider

Pulumi provider for managing Twingate infrastructure as code. Supports Python, TypeScript/JavaScript, Go, and .NET. Wraps the Twingate API to manage resources such as networks, connectors, and access policies.

## Key Information

- Package name varies by language: `@twingate/pulumi-twingate` (Node.js), `pulumi-twingate` (Python), `github.com/pulumi/pulumi-twingate/sdk/go` (Go), `Twingate.Twingate` (.NET)
- Full API reference available on the [Pulumi Registry](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- Local development builds produce versioned binaries that must be manually installed as Pulumi plugins

## Prerequisites

- Twingate account with API access and Admin Console access
- Pulumi CLI
- For local development: Go 1.24+, Node.js 22+

## Configuration Values

| Config Key | Env Var | Required | Description |
|---|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API token from Twingate Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (subdomain portion of Admin Console URL, e.g., `autoco` from `autoco.twingate.com`) |
| `twingate:url` | — | No | Defaults to `twingate.com`; do not change under normal use |

## Usage

### Install the SDK

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

### Local Development Build

```bash
# Build all SDKs
make development

# Build provider and Node.js SDK only
make provider build_nodejs

# Install the local plugin
pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate

# Verify
pulumi plugin ls | grep twingate
```

### Testing Workflows Locally

```bash
# Install act (macOS)
brew install act

# List available jobs
act --list

# Run a specific job
act pull_request -j lint
```

## Gotchas

- **404 error on `pulumi up`/`pulumi preview`**: Local development builds include `+dirty` in the version string and are not published to GitHub Releases. You must manually install the plugin with `pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate`. Check the error message for the exact version string.
- `twingate:network` is the subdomain only, not the full hostname.
- First run of `act` prompts for a Docker image size; select "Medium" for most workflows.

## Related Docs

- [Twingate API Overview](https://docs.twingate.com/docs/api-overview)
- [Pulumi Registry – Twingate](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- [Pulumi CLI Installation](https://www.pulumi.com/docs/install/)
- [act GitHub Actions local runner](https://github.com/nektos/act)