---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-08-06
source_version: 24515cbd382a44d5c1129a09321e9871525ea7ac15ddaa458e35f9079e261c1e
---

# Twingate JavaScript CLI

## Page Title
Introduction to the Twingate Javascript CLI

## Summary
Open-source JavaScript CLI tool for managing Twingate resources via GraphQL APIs. Provides pre-built binaries for Windows/Mac/Linux. Supports CRUD operations for users, groups, networks, connectors, resources, devices, policies, service accounts, and import/export.

## Key Information
- Written in JavaScript; extensible by Node/Deno developers
- Community-maintained (not official product engineering); support via GitHub Issues
- Prompts for account name and API key on first run; option to save credentials to file
- Accepts names or IDs interchangeably for most entity references (`nameOrId` params)

## Prerequisites
- Twingate account name and API key
- Pre-built binary from GitHub releases page (or Node/Deno runtime for source)
- GraphViz installed and on PATH for `png`/`svg` export formats

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | (prompted) |
| `-l, --log-level` | TRACE/DEBUG/INFO/WARN/ERROR/SEVERE/FATAL/QUIET/SILENT | `INFO` |
| `-V, --version` | Show version | — |

## Commands Reference

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
- `key_create <serviceAccountId> <keyName> <expirationTimeInDays>`

### export
| Flag | Description |
|------|-------------|
| `-f` | Format: `xlsx` (default), `json`, `dot`, `png`, `svg` |
| `-o` | Output filename |
| `-n/-r/-g/-u/-d` | Include networks/resources/groups/users/devices |

### import
| Flag | Description |
|------|-------------|
| `-f` | Path to Excel file (required) |
| `-n/-r/-g/-d` | Include networks/resources/groups/devices |
| `-s` | Sync entities by natural identifier |
| `-y` | Assume yes to all prompts |

## Gotchas
- `group add_user` / `resource create` with users/groups requires IDs, not names for users
- Service account removal fails if it has active keys
- `policy add_group` **replaces** existing policy assignment on groups
- `png`/`svg` export requires GraphViz on PATH
- Connector creation returns tokens only at creation time — save `ACCESS_TOKEN`/`REFRESH_TOKEN` immediately

## Related Docs
- Twingate Python CLI (alternative for Python developers)
- Twingate GraphQL API documentation
- GitHub releases page (binaries)
- GitHub Issues (community support)