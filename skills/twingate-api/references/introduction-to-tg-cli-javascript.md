---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-08-16
source_version: b892d5f49e74ee908d20f4e3b3e08f677131096ce464a8037be6d1e3ab09b5c9
---

# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool for managing Twingate resources via GraphQL APIs, written in JavaScript. Provides pre-built binaries for Windows/Mac/Linux. Covers users, groups, networks, connectors, resources, devices, policies, service accounts, export, and import operations.

## Key Information
- Source: GitHub (open-source, community-maintained — not official product engineering)
- Written in JavaScript; extensible for Node/Deno developers
- Prompts for account name and API key on first use; offers to save credentials to file
- IDs are base64-encoded (e.g., `VXNlcjoxMzY3Ng==`)
- Names or IDs accepted interchangeably for most entity references

## Prerequisites
- Download binary from GitHub releases page
- Twingate account name
- Twingate API key
- For png/svg export: GraphViz installed and on PATH

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | — |
| `-l, --log-level` | TRACE/DEBUG/INFO/WARN/ERROR/SEVERE/FATAL/QUIET/SILENT | INFO |
| `-h, --help` | Show help | — |
| `-V, --version` | Show version | — |

## Commands & Usage

| Command | Subcommands |
|---------|-------------|
| `user` | `list` |
| `group` | `list`, `create`, `remove`, `remove_bulk`, `add_user`, `remove_user`, `add_resource`, `remove_resource`, `set_policy`, `copy` |
| `network` | `list`, `create` |
| `connector` | `list`, `create <remoteNetworkNameOrId> [name]` |
| `resource` | `list`, `create`, `remove`, `remove_bulk`, `add_group` |
| `device` | `list` |
| `policy` | `list`, `add_group` |
| `service` | `list`, `create`, `remove`, `add_resource`, `key_create` |
| `export` | `-f xlsx\|json\|dot\|png\|svg`, `-o`, `-n`, `-r`, `-g`, `-u`, `-d` |
| `import` | `-f <file>`, `-n`, `-r`, `-g`, `-d`, `-s` (sync), `-y` (assume yes) |

## Export Flags
`-n` networks, `-r` resources, `-g` groups, `-u` users, `-d` devices  
Default format: `xlsx`

## Gotchas
- `group add_user` / `resource create` with groups: requires IDs for users, names accepted for groups/resources
- Service account removal fails if it has active keys
- `policy add_group`: replaces existing policy assignment on the group
- `connector create` returns `ACCESS_TOKEN` and `REFRESH_TOKEN` — capture output immediately
- `service key_create` returns full JSON token object including private key — capture immediately
- Remote network must exist before creating connectors or resources
- png/svg export silently fails without GraphViz on PATH

## Related Docs
- [Twingate Python CLI](https://www.twingate.com/docs) (alternative for Python developers)
- [Twingate GraphQL API](https://www.twingate.com/docs)
- [GitHub Issues](https://github.com/Twingate/twingate-js-cli/issues) (support channel)