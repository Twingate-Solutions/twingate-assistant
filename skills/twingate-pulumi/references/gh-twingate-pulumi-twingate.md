---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-09-13
source_version: 0ebeb23bef7cd83e199cc529ffc159cfa2e2cde2
---

# Twingate Pulumi Provider

## Summary
Pulumi provider for managing Twingate infrastructure as code. Supports Python, TypeScript/JavaScript, Go, and .NET. Wraps the Twingate API to manage resources like networks, connectors, and access policies.

## Key Information
- Package name varies by language: `@twingate/pulumi-twingate` (Node), `pulumi-twingate` (Python), `Twingate.Twingate` (.NET)
- Go module: `github.com/pulumi/pulumi-twingate/sdk/go/...`
- Full API reference at [Pulumi Registry](https://www.pulumi.com/registry/packages/twingate/api-docs/)

## Prerequisites
- Pulumi CLI installed
- Twingate Admin Console access with API token
- Your Twingate network ID
- For local development: Go 1.24+, Node.js 22+

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

| Config Key | Env Variable | Required | Description |
|---|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API token from Twingate Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (subdomain prefix, e.g. `autoco` from `autoco.twingate.com`) |
| `twingate:url` | — | No | Defaults to `twingate.com`; rarely changed |

Set via Pulumi config:
```bash
pulumi config set twingate:apiToken <token> --secret
pulumi config set twingate:network <network-id>
```

## Local Development (Step-by-Step)

1. Build provider and SDKs:
   ```bash
   make development          # all SDKs
   make provider build_nodejs  # provider + Node.js only
   ```

2. Install the local plugin manually (required for local builds):
   ```bash
   pulumi plugin install resource twingate <version> \
     --file bin/pulumi-resource-twingate
   ```

3. Verify installation:
   ```bash
   pulumi plugin ls | grep twingate
   ```

4. Test GitHub Actions workflows locally (optional):
   ```bash
   brew install act
   act pull_request -j lint
   ```

## Gotchas

- **404 on `pulumi up`/`pulumi preview`**: Local/alpha builds won't be found in GitHub Releases. Always install the plugin manually with `--file bin/pulumi-resource-twingate`. The exact version string (including `+dirty` suffix) must match what the build produced — check the error message for the exact string.
- **Network ID format**: The `twingate:network` value is just the subdomain prefix, not the full hostname.
- **`act` setup**: First run prompts for Docker image size — choose "Medium" for most workflows.

## Related Docs
- [Twingate API Overview](https://docs.twingate.com/docs/api-overview)
- [Pulumi Registry – Twingate](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- [Pulumi CLI Install](https://www.pulumi.com/docs/install/)
- [act (local GitHub Actions runner)](https://github.com/nektos/act)