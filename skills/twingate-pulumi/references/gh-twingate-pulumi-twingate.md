---
source: https://github.com/Twingate/pulumi-twingate
type: github
fetched: 2026-11-19
source_version: 7c8efb6e82e920102b92fea88a63a3dd48a5fd35
trust: official
---

# Twingate/pulumi-twingate

## Summary
Pulumi provider for managing Twingate resources as code from Python, TypeScript/JavaScript, Go, or .NET. It exposes a `twingate` provider configured with an API token and network ID. Full API reference is hosted in the Pulumi registry.

## Key Information
- Languages and packages:
  - Node.js: `@twingate/pulumi-twingate` (via `npm install` or `yarn add`)
  - Python: `pip install pulumi-twingate`
  - Go: `go get github.com/pulumi/pulumi-twingate/sdk/go/...`
  - .NET: `dotnet add package Twingate.Twingate`
- Default branch: `main`.
- The repo also contains build tooling (Makefile) for building the provider and SDKs from source.

## Prerequisites
- Twingate account with an API token from the Admin Console.
- Pulumi CLI.
- For building from source: Go 1.24+, Node.js 22+, Pulumi CLI.

## Usage / Step-by-Step
**Using the provider**
1. Install the SDK for your language (see above).
2. Set `twingate:apiToken` and `twingate:network` in Pulumi config, or set the equivalent environment variables.
3. Define resources and run `pulumi up`.

**Building locally**
1. Build everything: `make development`. Or only the provider and Node.js SDK: `make provider build_nodejs`.
2. Install the local plugin, using the version string your build produced:
   `pulumi plugin install resource twingate <version> --file bin/pulumi-resource-twingate`
3. Verify with `pulumi plugin ls | grep twingate`.

**Testing workflows locally**
- Uses [`act`](https://github.com/nektos/act) (install via Homebrew on macOS, or see its installation guide for Linux and other platforms).
- `act --list` shows jobs; `act pull_request -j lint` runs the lint job.
- On first run, `act` asks for a Docker image size; "Medium" is recommended for most workflows.

## Configuration Values
| Setting | Env var | Notes |
|---|---|---|
| `twingate:apiToken` | `TWINGATE_API_TOKEN` | API access key from the Admin Console |
| `twingate:network` | `TWINGATE_NETWORK` | Network ID, e.g. `autoco` from `autoco.twingate.com` |
| `twingate:url` | – | Defaults to `twingate.com`; optional, shouldn't normally be changed |

## Gotchas
- Local development builds fail with "404 HTTP error fetching plugin" on `pulumi up`/`preview` because Pulumi tries to download the plugin from GitHub releases. Fix by installing the plugin manually with `--file bin/pulumi-resource-twingate`.
- The version string must match your build exactly (it includes `+dirty` if you have uncommitted changes). The error message shows the expected version.
- The Go install path in the README uses the `pulumi` org (`github.com/pulumi/pulumi-twingate`), although the repo is under `Twingate`.
- The README installs `act` on Linux with a piped remote script; see the act installation guide for install options instead.

## Related Docs
- Pulumi registry API docs: https://www.pulumi.com/registry/packages/twingate/api-docs/
- Twingate API overview: https://docs.twingate.com/docs/api-overview
- Pulumi install: https://www.pulumi.com/docs/install/
- act: https://github.com/nektos/act