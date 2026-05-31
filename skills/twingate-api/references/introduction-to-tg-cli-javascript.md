# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate Javascript CLI

## Summary
Open-source CLI tool wrapping the Twingate GraphQL API, written in JavaScript. Provides commands for managing users, groups, resources, networks, connectors, devices, service accounts, and policies. Pre-built binaries available for Windows/Mac/Linux; extensible for Node/Deno developers.

## Key Information
- GitHub releases page provides pre-built binaries (no Node.js required for binary usage)
- Wraps Twingate GraphQL API; source available for customization
- Credentials (account name + API key) prompted on first use; can be saved to config file
- Supports export to: `xlsx`, `json`, `dot`, `png`, `svg`
- Import only supports Excel (`.xlsx`) format
- Community-supported via GitHub Issues, not Twingate product engineering

## Prerequisites
- Twingate account name and API key
- GraphViz installed on PATH (only for `png`/`svg` export formats)

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | prompted |
| `-l, --log-level` | `TRACE|DEBUG|INFO|WARN|ERROR|SEVERE|FATAL|QUIET|SILENT` | `INFO` |
| `-h, --help` | Show help | — |
| `-V, --version` | Show version | — |

## Commands Reference

### user
- `list` — list all users (shows id, email, isAdmin, state, groups)

### group
- `list` | `create <name> [UserIds...]` | `remove <id>` | `remove_bulk [ids...]`
- `add_user <groupNameOrId> [userIds...]` | `remove_user <groupNameOrId> [userIds...]`
- `add_resource <groupNameOrId> [resourceNamesOrIds...]` | `remove_resource <groupNameOrId> [resourceNamesOrIds...]`
- `set_policy <groupNameOrId> <securityPolicyNameOrId>`
- `copy <source> <destination>` — copies all users from source to destination

### network
- `list` | `create <name>`

### connector
- `list` | `create <remoteNetworkNameOrId> [name]` — returns `ACCESS_TOKEN` and `REFRESH_TOKEN`

### resource
- `list` | `create <remoteNetworkNameOrId> <name> <address> [groupNamesOrIds...]`
- `remove <id>` | `remove_bulk [ids...]`
- `add_group <resourceNameOrId> [groupNamesOrIds...]`

### device
- `list` — read-only

### policy
- `list` | `add_group <securityPolicyNameOrId> [groupNamesOrIds...]`

### service
- `list` | `create <name> [resourceNamesOrIds...]` | `remove <id>`
- `add_resource <serviceAccountId> [resourceNamesOrIds...]`
- `key_create <serviceAccountId> <keyName> <expirationTimeInDays>` — returns full key JSON with private key

### export
| Flag | Description |
|------|-------------|
| `-f` | Format: `xlsx`(default), `json`, `dot`, `png`, `svg` |
| `-o` | Output filename |
| `-n/-r/-g/-u/-d` | Include: networks/resources/groups/users/devices |

### import
| Flag | Description |
|------|-------------|
| `-f` | Path to Excel file (required) |
| `-n/-r/-g/-d` | Include: networks/resources/groups/devices |
| `-s` | Sync entities with same natural identifier |
| `-y` | Assume yes to all prompts |

## Gotchas
- `group add_user` / `resource create` require **user/group IDs**, not names/emails
- `service remove` fails if service account has active keys
- `policy add_group` **replaces** any existing policy assigned to those groups
- `png`/`svg` export requires GraphViz on system PATH
- Import only supports `.xlsx` format (not JSON