---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-10-25
source_version: f13f111e8fb8660694651ba929e2ff5d063cc95f
trust: official
---

# Twingate Pulumi Provider

A Pulumi resource provider for managing Twingate infrastructure. Supports Python, TypeScript/JavaScript, Go, and .NET.

## Key Information

- Wraps the Twingate API to enable infrastructure-as-code management of Twingate resources
- Available via standard package registries for all supported languages
- Full API reference hosted on the [Pulumi registry](https://www.pulumi.com/registry/packages/twingate/api-docs/)

## Prerequisites

- A Twingate account with API access (API token from the Admin Console)
- Pulumi CLI installed
- Language runtime for your chosen SDK (Node.js 22+, Python, Go 1.24+, or .NET)

## Installation

| Language | Command |
|---|---|
| Node.js | `npm install @twingate/pulumi-twingate` or `yarn add @twingate/pulumi-twingate` |
| Python | `pip install pulumi-twingate` |
| Go | `go get github.com/pulumi/pulumi-twingate/sdk/go/...` |
| .NET | `dotnet add package Twingate.Twingate` |

## Configuration Values

| Key | Env Var | Required | Description |
|---|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | Yes | API token from the Twingate Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Yes | Network ID (the subdomain portion of your Admin Console URL, e.g. `autoco` from `autoco.twingate.com`) |
| `twingate:url` | — | No | Defaults to `twingate.com`; do not change under normal circumstances |

## Building Locally

1. Build the provider and SDKs:
   ```bash
   make development        # all SDKs
   make provider build_nodejs  # provider + Node.js only
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

- Local development builds include a version suffix such as `+dirty` for uncommitted changes. Pulumi will attempt to fetch this version from GitHub releases and fail with a 404. Always install the local binary manually using `--file` after building.
- The exact version string to use in `pulumi plugin install` appears in the 404 error message Pulumi produces—copy it from there.
- `twingate:url` should not be changed in normal use; modifying it is intended only for internal or testing environments.

## Related Docs

- [Twingate API overview](https://docs.twingate.com/docs/api-overview)
- [Pulumi registry – Twingate](https://www.pulumi.com/registry/packages/twingate/api-docs/)
- [Pulumi CLI installation](https://www.pulumi.com/docs/install/)