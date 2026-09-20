---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-09-20
source_version: f64ea800147e3f3cceecd8f6c5120d1ab707a5150f8a8170d67ca31649ee5505
---

# Twingate JavaScript CLI

## Page Title
Introduction to the Twingate Javascript CLI

## Summary
Open-source CLI tool written in JavaScript that wraps Twingate GraphQL APIs. Provides pre-built binaries for Windows/Mac/Linux and supports full CRUD operations on users, groups, resources, networks, connectors, devices, service accounts, and policies. Node/Deno developers can extend it for custom use cases.

## Key Information
- **Source**: GitHub (open-source, community-maintained — not official product engineering)
- **Auth**: Prompts interactively for account name and API key; offers to save credentials to file
- **Formats**: Can refer to resources/groups by name OR by ID in most commands
- **IDs**: Base64-encoded (e.g., `VXNlcjoxMzY3Ng==`)

## Prerequisites
- Download binary from GitHub releases page
- Twingate account name and API key
- GraphViz installed (only for `png`/`svg` export formats)

## Commands Reference

| Command | Subcommands |
|---------|-------------|
| `user` | `list` |
| `group` | `list`, `create`, `remove`, `remove_bulk`, `add_user`, `remove_user`, `add_resource`, `remove_resource`, `set_policy`, `copy` |
| `network` | `list`, `create` |
| `connector` | `list`, `create` |
| `resource` | `list`, `create`, `remove`, `remove_bulk`, `add_group` |
| `device` | `list` |
| `policy` | `list`, `add_group` |
| `service` | `list`, `create`, `remove`, `add_resource`, `key_create` |
| `export` | (flags only) |
| `import` | (flags only) |

## Configuration Values

**Global flags:**
- `-a, --account-name <string>` — Twingate account name
- `-l, --log-level [level]` — `TRACE|DEBUG|INFO|WARN|ERROR|SEVERE|FATAL|QUIET|SILENT` (default: `INFO`)

**Export flags:**
- `-f, --format` — `xlsx|json|dot|png|svg` (default: `xlsx`)
- `-o, --output-file` — output filename
- `-n` networks, `-r` resources, `-g` groups, `-u` users, `-d` devices

**Import flags:**
- `-f, --file <string>` — path to Excel file (required)
- `-s, --sync` — sync by natural identifier
- `-y, --assume-yes` — skip prompts

## Gotchas
- **Service removal**: Cannot remove a service account with active keys (must revoke all keys first)
- **Policy assignment replaces**: `policy add_group` replaces existing policy assignment on the group
- **User operations require ID**: `group add_user`, `group create` with users require user IDs, not email addresses
- **Dependencies must pre-exist**: Resources, groups, networks must exist before referencing them in create/add commands
- **`group add_resource` vs `resource add_group`**: Both exist; use either depending on which entity you're referencing first
- **PNG/SVG export**: Requires GraphViz on system PATH
- **Community support only**: File issues on GitHub, not Twingate support

## Related Docs
- Twingate Python CLI (alternative for Python developers)
- Twingate GraphQL API documentation
- GitHub releases page (for binaries)
- GitHub issues page (for support)