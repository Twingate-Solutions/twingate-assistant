# Twingate JavaScript CLI

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool built on Twingate's GraphQL APIs, distributed as pre-built binaries for Windows/Mac/Linux. Supports full CRUD operations on resources, groups, users, networks, connectors, devices, service accounts, and policies. Node/Deno developers can extend it; community-supported via GitHub Issues.

## Key Information
- Binary download: GitHub releases page
- Prompts for account name and API key on first run; offers to save credentials locally
- All IDs are base64-encoded (e.g., `VXNlcjoxMzY3Ng==`)
- Names or IDs accepted interchangeably for most entity references

## Prerequisites
- Twingate account name and API key
- For PNG/SVG export: GraphViz installed and on PATH

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | — |
| `-l, --log-level` | TRACE/DEBUG/INFO/WARN/ERROR/SEVERE/FATAL/QUIET/SILENT | `INFO` |
| `-h, --help` | Help | — |
| `-V, --version` | Version | — |

## Commands Reference

### user
- `list` — list all users

### group
- `list` / `create <name> [UserIds...]` / `remove <id>` / `remove_bulk [ids...]`
- `add_user <groupNameOrId> [userIds...]` / `remove_user`
- `add_resource <groupNameOrId> [resourceNamesOrIds...]` / `remove_resource`
- `set_policy <groupNameOrId> <securityPolicyNameOrId>`
- `copy <source> <destination>` — copies all users from source to new group

### network
- `list` / `create <name>`

### connector
- `list` / `create <remoteNetworkNameOrId> [name]` — returns `ACCESS_TOKEN` and `REFRESH_TOKEN`

### resource
- `list` / `create <remoteNetworkNameOrId> <name> <address> [groupNamesOrIds...]`
- `remove <id>` / `remove_bulk [ids...]`
- `add_group <resourceNameOrId> [groupNamesOrIds...]`

### device
- `list`

### policy
- `list` / `add_group <securityPolicyNameOrId> [groupNamesOrIds...]`

### service
- `list` / `create <name> [resourceNamesOrIds...]` / `remove <id>`
- `add_resource <serviceAccountId> [resourceNamesOrIds...]`
- `key_create <serviceAccountId> <keyName> <expirationTimeInDays>` — returns full key JSON with private key

### export
| Flag | Description | Default |
|------|-------------|---------|
| `-f` | Format: xlsx/json/dot/png/svg | `xlsx` |
| `-o` | Output filename | auto-generated |
| `-n/-r/-g/-u/-d` | Include networks/resources/groups/users/devices | — |

### import
| Flag | Description |
|------|-------------|
| `-f` | Path to Excel file (required) |
| `-n/-r/-g/-d` | Include networks/resources/groups/devices |
| `-s` | Sync by natural identifier |
| `-y` | Assume yes to all prompts |

## Gotchas
- `group add_user` / `resource create` with groups: requires user/group IDs, not names
- `service remove`: fails if service account has active keys
- `policy add_group`: **replaces** any previously assigned policy on those groups
- PNG/SVG export requires GraphViz on PATH
- Not officially supported by Twingate product engineering — use GitHub Issues

## Related Docs
- Twingate Python CLI
- Twingate GraphQL API documentation
- GraphViz installation