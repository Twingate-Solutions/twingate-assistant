# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool for managing Twingate resources via GraphQL API, written in JavaScript. Provides commands for users, groups, networks, connectors, resources, devices, policies, service accounts, and import/export. Pre-built binaries available for Windows, Mac, and Linux.

## Key Information
- GitHub: download binaries from releases page; issues tracked there (community-supported, not official product team)
- Prompts for account name and API key on first run; offers to save credentials to file
- Python CLI alternative available for Python developers
- All entity references accept either name or ID (e.g., `groupNameOrId`)

## Prerequisites
- Twingate account name and API key
- GraphViz installed (only for PNG/SVG export formats)
- Resources/groups/users/networks must pre-exist before referencing in create commands

## Commands Reference

| Command | Subcommands |
|---|---|
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

## Configuration Values / CLI Flags

**Global flags:**
- `-a, --account-name <string>` — Twingate account name
- `-l, --log-level` — `TRACE|DEBUG|INFO|WARN|ERROR|SEVERE|FATAL|QUIET|SILENT` (default: `INFO`)

**Export flags:**
- `-f, --format` — `xlsx|json|dot|png|svg` (default: `xlsx`)
- `-o, --output-file` — output filename
- `-n` networks, `-r` resources, `-g` groups, `-u` users, `-d` devices

**Import flags:**
- `-f, --file <string>` — path to Excel file (required)
- `-n` networks, `-r` resources, `-g` groups, `-d` devices
- `-s, --sync` — sync entities by natural identifier
- `-y, --assume-yes` — skip confirmation prompts

## Gotchas
- `group create` and `group add_user` require **User IDs**, not email addresses
- `service remove` fails if the service account has active keys
- `policy add_group` **replaces** any existing policy assignment on the group
- `connector create` returns `ACCESS_TOKEN` and `REFRESH_TOKEN` — capture immediately as they won't be shown again
- PNG/SVG export requires GraphViz on system PATH
- `remove_resource` command help text incorrectly says "Add resources" (it removes)

## Related Docs
- Twingate Python CLI
- Twingate GraphQL API
- GitHub Issues page (support channel)
- GraphViz installation (for visualization exports)