# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI (`tg`)

## Summary
Open-source CLI tool built on Twingate's GraphQL APIs, written in JavaScript (Node/Deno compatible). Provides pre-built binaries for Windows, Mac, and Linux. Supports full CRUD operations for resources, groups, users, networks, connectors, devices, service accounts, and import/export.

## Key Information
- **Source**: Open-source, community-maintained (not Twingate product team); support via GitHub Issues
- **Auth**: Prompts for account name + API key on first run; option to save credentials to file
- **Alternatives**: Python CLI available for Python developers
- **ID format**: Entities use base64-encoded IDs (e.g., `VXNlcjoxMzY3Ng==`); names can substitute IDs in most commands

## Prerequisites
- Twingate account name and API key
- For `png`/`svg` export: [GraphViz](https://graphviz.org) installed and on PATH
- Referenced entities (users, groups, resources, networks) must exist before referencing them in commands

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | — |
| `-l, --log-level` | Log verbosity | `INFO` |
| `-V, --version` | Show version | — |

## Command Reference

### `user`
- `list` — List all users

### `group`
- `list` / `create <name> [UserIds...]` / `remove <id>` / `remove_bulk [ids...]`
- `add_user <groupNameOrId> [userIds...]` / `remove_user`
- `add_resource <groupNameOrId> [resourceNamesOrIds...]` / `remove_resource`
- `set_policy <groupNameOrId> <securityPolicyNameOrId>`
- `copy <source> <destination>` — copies all users from source to new group

### `resource`
- `list` / `create <remoteNetworkNameOrId> <name> <address> [groupNamesOrIds...]`
- `remove <id>` / `remove_bulk [ids...]`
- `add_group <resourceNameOrId> [groupNamesOrIds...]`

### `network`
- `list` / `create <name>`

### `connector`
- `list` / `create <remoteNetworkNameOrId> [name]` — returns `ACCESS_TOKEN` and `REFRESH_TOKEN`

### `device`
- `list`

### `policy`
- `list` / `add_group <securityPolicyNameOrId> [groupNamesOrIds...]`

### `service`
- `list` / `create <name> [resourceNamesOrIds...]` / `remove <id>`
- `add_resource <serviceAccountId> [resourceNamesOrIds...]`
- `key_create <serviceAccountId> <keyName> <expirationTimeInDays>` — returns JSON token object with private key

### `export`
| Flag | Values | Default |
|------|--------|---------|
| `-f, --format` | `xlsx`, `json`, `dot`, `png`, `svg` | `xlsx` |
| `-o, --output-file` | filename | auto-generated |
| `-n/-r/-g/-u/-d` | remote-networks/resources/groups/users/devices | all included |

### `import`
- `-f <file>` (required) — path to Excel file
- `-n/-r/-g/-d` — scope flags
- `-s, --sync` — match existing entities by natural identifier
- `-y, --assume-yes` — skip prompts

## Gotchas
- `group add_user` / `resource create` require user/group **IDs**, not email addresses or names
- `service remove` fails if service account has active keys
- `policy add_group` **replaces** existing policy assignment on groups
- `png`/`svg` export requires GraphViz on PATH
- This is a community tool — no official Twingate product support

## Related Docs
- [Twingate Python CLI](https://www.twin