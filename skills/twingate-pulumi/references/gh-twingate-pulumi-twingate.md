---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-08-06
source_version: b5d3664b715a2d35d81f95621c7fd07d0c611a54
---

<!-- triage: unassigned -->

# Twingate Pulumi Provider

## Summary
Pulumi provider for managing Twingate infrastructure as code. Supports Python, TypeScript/JavaScript, Go, and .NET. Wraps the Twingate API to manage resources like networks, connectors, and access policies.

## Key Information
- Package name: `@twingate/pulumi-twingate` (Node.js), `pulumi-twingate` (Python), `Twingate.Twingate` (.NET)
- Go module: `github.com/pulumi/pulumi-twingate/sdk/go/`
- Full API docs at [Pulumi Registry](https://www.pulumi.com/registry/packages/twingate/api-docs/)

## Prerequisites
- Pulumi CLI installed
- Twingate account with API access (Admin Console required)
- **For local development only:**
  - Go 1.24+
  - Node.js 22+

## Installation

| Language | Command |
|---|---|
| Node.js | `npm install @twingate/pulumi-twingate` |
| Python | `pip install pulumi-twingate` |
| Go | `go get github.com/pulumi/pulumi-twingate/sdk/go/...` |
| .NET | `dotnet add package Twingate.Twingate` |

## Configuration Values

| Config Key | Env Var | Required | Description |
|---|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API key from Twingate Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (subdomain prefix, e.g. `autoco` from `autoco.twingate.com`) |
| `twingate:url` | — | No | Defaults to `twingate.com`; do not change normally |

Set via Pulumi config or environment variables:
```bash
pulumi config set twingate:apiToken <token> --secret
pulumi config set twingate:network <network-id>
```

## Local Development Build

```bash
# Full build (all SDKs)
make development

# Provider + Node.js SDK only
make provider build_nodejs

# Install local plugin manually after building
pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate

# Verify
pulumi plugin ls | grep twingate
```

### Testing Workflows Locally
Uses [`act`](https://github.com/nektos/act) to run GitHub Actions locally:
```bash
act --list
act pull_request -j lint
```

## Gotchas

- **404 error on `pulumi up`/`pulumi preview` with local builds**: Pulumi tries to download the plugin from GitHub Releases. Local dev builds (version strings containing `+dirty` or alpha tags) won't resolve. Fix: manually install with `--file bin/pulumi-resource-twingate`.
- **Version string**: Check the exact version from the error message — it includes build metadata (e.g., `v4.1.0-alpha.1772811417+dirty`).
- **`twingate:network`** is the subdomain only, not the full hostname.
- First run of `act` prompts for Docker image size — choose "Medium."

## Related Docs
- [Twingate API Overview](https://docs.twingate.com/docs/api-overview)
- [Pulumi Registry – Twingate](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- [Pulumi CLI Install](https://www.pulumi.com/docs/install/)
- [act (local GitHub Actions runner)](https://github.com/nektos/act)