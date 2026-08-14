---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-08-14
source_version: b892d5f49e74ee908d20f4e3b3e08f677131096ce464a8037be6d1e3ab09b5c9
---

# Twingate JavaScript CLI

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool built on Twingate GraphQL APIs, written in JavaScript with pre-built binaries for Windows/Mac/Linux. Supports full CRUD operations for resources, groups, users, networks, connectors, devices, service accounts, and export/import. Community-maintained project, not supported by Twingate product engineering.

## Key Information
- Binaries available on GitHub releases page; no Node/Deno install required for pre-built binaries
- Prompts interactively for account name and API key on first run; option to save credentials to file
- Commands accept names OR IDs for most entity references (e.g., `groupNameOrId`)
- `export` supports formats: `xlsx`, `json`, `dot`, `png`, `svg`
- `png`/`svg` export requires GraphViz installed and on PATH
- `import` only supports Excel (`.xlsx`) as source format

## Prerequisites
- Twingate account name
- Twingate API key
- GraphViz (only for png/svg export)

## CLI Flags (Global)
| Flag | Short | Default | Values |
|------|-------|---------|--------|
| `--account-name` | `-a` | — | string |
| `--log-level` | `-l` | `INFO` | `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `SEVERE`, `FATAL`, `QUIET`, `SILENT` |

## Command Reference

### user
- `list` — list all users

### group
- `list` / `create <name> [UserIds...]` / `remove <id>` / `remove_bulk [ids...]`
- `add_user <groupNameOrId> [userIds...]` / `remove_user`
- `add_resource <groupNameOrId> [resourceNamesOrIds...]` / `remove_resource`
- `set_policy <groupNameOrId> <securityPolicyNameOrId>`
- `copy <source> <destination>` — copies all users from source to destination

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
- `key_create <serviceAccountId> <keyName> <expirationTimeInDays>` — returns full JSON token object

### export
| Flag | Description | Default |
|------|-------------|---------|
| `-f` | Format | `xlsx` |
| `-o` | Output filename | auto-generated |
| `-n/-r/-g/-u/-d` | Include networks/resources/groups/users/devices | all included by default |

### import
| Flag | Description |
|------|-------------|
| `-f` | Path to Excel file (required) |
| `-n/-r/-g/-d` | Include networks/resources/groups/devices |
| `-s` | Sync entities by natural identifier |
| `-y` | Assume yes to all prompts |

## Gotchas
- `group add_user` / `resource create` with groups: requires IDs for users, names or IDs for groups/resources
- Service account removal fails if it has active keys
- `policy add_group` **replaces** any existing policy assignment on the group
- `group copy` copies users only, not resources

## Related Docs
- Twingate Python CLI
- Twingate GraphQL API
- GitHub Issues (support channel)