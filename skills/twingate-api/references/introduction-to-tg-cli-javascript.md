# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool built on Twingate GraphQL APIs, written in JavaScript (Node/Deno compatible). Provides pre-built binaries for Windows/Mac/Linux. Supports full CRUD operations for resources, groups, users, networks, connectors, devices, services, and policies, plus import/export.

## Key Information
- **Source**: GitHub open-source project (not officially supported by Twingate engineering)
- **Support**: GitHub Issues page only
- **Auth**: Prompts for account name + API key on first run; offers to save credentials to file
- **Alternatives**: Python CLI available for Python developers
- **IDs**: Most commands accept names OR base64-encoded IDs interchangeably

## Prerequisites
- Twingate account name and API key
- Pre-built binary from GitHub releases page (or Node/Deno runtime for source)
- GraphViz installed and on PATH (only for PNG/SVG export formats)

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | — |
| `-l, --log-level` | TRACE/DEBUG/INFO/WARN/ERROR/SEVERE/FATAL/QUIET/SILENT | INFO |
| `-h, --help` | Show help | — |
| `-V, --version` | Show version | — |

## Commands Reference

### user
- `list` — List all users

### group
- `list` / `create <name> [UserIds...]` / `remove <id>` / `remove_bulk [ids...]`
- `add_user <groupNameOrId> [userIds...]` / `remove_user <groupNameOrId> [userIds...]`
- `add_resource <groupNameOrId> [resourceNamesOrIds...]` / `remove_resource <groupNameOrId> [resourceNamesOrIds...]`
- `set_policy <groupNameOrId> <securityPolicyNameOrId>`
- `copy <source> <destination>` — Copies all users from source to destination group

### network
- `list` / `create <name>`

### connector
- `list` / `create <remoteNetworkNameOrId> [name]` — Returns `ACCESS_TOKEN` and `REFRESH_TOKEN` on creation

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
| `-n/-r/-g/-u/-d` | Include: Remote Networks/Resources/Groups/Users/Devices |

### import
| Flag | Description |
|------|-------------|
| `-f` | Path to Excel file (required) |
| `-n/-r/-g/-d` | Include: Remote Networks/Resources/Groups/Devices |
| `-s` | Sync entities with same natural identifier |
| `-y` | Assume yes to all prompts |

## Gotchas
- **User IDs required** (not emails) when adding users to groups
- **Service account removal** fails if account has active keys
- **`add_group` on policy** replaces existing security policy assigned to groups
- **PNG/SVG export** requires GraphViz binary on system PATH
- **Import** only supports Excel (`.xlsx`) format as source

## Related Docs
- Twingate Python CLI
- Twingate GraphQL API documentation
- GitHub releases page