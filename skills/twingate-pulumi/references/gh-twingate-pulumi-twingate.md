---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-09-06
source_version: fc1b072a600dc5eae31e3976317e7e002884c2c7
---

# Twingate Pulumi Provider

## Summary
A Pulumi provider for managing Twingate infrastructure as code. Supports Python, TypeScript/JavaScript, Go, and .NET. Wraps the Twingate API to allow declarative management of Twingate resources.

## Key Information
- Provider package name: `twingate`
- Pulumi Registry docs: https://www.pulumi.com/registry/packages/twingate/api-docs/
- Source repo: `Twingate/pulumi-twingate`
- Requires a Twingate account with API access

## Prerequisites
- Pulumi CLI installed
- Twingate API token (from Admin Console)
- Twingate network ID
- Language-specific runtime (Node.js, Python, Go, or .NET)

## Installation

| Language | Command |
|---|---|
| Node.js | `npm install @twingate/pulumi-twingate` |
| Python | `pip install pulumi-twingate` |
| Go | `go get github.com/Twingate/pulumi-twingate/sdk/v5/go/...` |
| .NET | `dotnet add package Twingate.Twingate` |

## Configuration Values

| Config Key | Env Var | Required | Description |
|---|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API token from Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (subdomain portion of Admin URL, e.g. `autoco` from `autoco.twingate.com`) |
| `twingate:url` | — | No | Defaults to `twingate.com`; do not change normally |

Set via Pulumi config:
```bash
pulumi config set twingate:apiToken <token> --secret
pulumi config set twingate:network <network-id>
```

## Local Development

### Prerequisites
- Go 1.24+
- Node.js 22+
- Pulumi CLI

### Build Steps
```bash
# Full build (all SDKs)
make development

# Provider + Node.js SDK only
make provider build_nodejs

# Install local plugin
pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate
```

### Verify Plugin
```bash
pulumi plugin ls | grep twingate
```

## Gotchas

- **404 on `pulumi up` with local builds**: Pulumi tries to download the plugin from GitHub Releases. Local dev builds (version strings containing `+dirty` or alpha tags) won't exist there. Fix: manually install the plugin with `--file bin/pulumi-resource-twingate`.
- **Version string mismatch**: The exact version string required for `pulumi plugin install` appears in the error message — copy it from there.
- **Network ID format**: The network ID is the subdomain only, not the full URL (e.g., `autoco`, not `autoco.twingate.com`).

## Breaking Changes (v5.0.0)

Upgrades the bridged upstream provider from terraform-provider-twingate v4.3.2 to v5.0.0. The Go SDK module path moves from `github.com/Twingate/pulumi-twingate/sdk/v4` to `github.com/Twingate/pulumi-twingate/sdk/v5`.

**Removed**
- `TwingateGatewayConfig` — the upstream `twingate_gateway_config` resource no longer exists.
- `username` and `protocols` fields on `TwingateSSHResource`.
- `protocols` field on `TwingateKubernetesResource`. (`protocols` is unaffected on `TwingateResource`.)

**Added**
- `TwingateWebAppResource` — new upstream `twingate_web_app_resource`. Requires `address`, `gatewayId`, `remoteNetworkId`, and `upstream`/`downstream` port blocks.

## Testing Workflows Locally
Uses [`act`](https://github.com/nektos/act) to run GitHub Actions locally:
```bash
act --list
act pull_request -j