# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool wrapping Twingate GraphQL APIs, written in JavaScript. Provides CRUD operations for users, groups, networks, connectors, resources, devices, policies, and service accounts. Pre-built binaries available for Windows/Mac/Linux; Node/Deno developers can extend it.

## Key Information
- Download binaries from GitHub releases page; unzip and run `./tg`
- Prompts for account name and API key on first use; offers to save credentials to file
- Uses base64-encoded IDs (e.g., `VXNlcjoxMzY3Ng==`) for referencing entities
- Names can often substitute for IDs in commands (e.g., `groupNameOrId`)
- Community-supported; file issues on GitHub, not Twingate product support

## Prerequisites
- Twingate account name and API key
- GraphViz installed (only for `png`/`svg` export formats)

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | — |
| `-l, --log-level` | TRACE/DEBUG/INFO/WARN/ERROR/SEVERE/FATAL/QUIET/SILENT | `INFO` |

## Commands Reference

### `user`
- `list` — list all users

### `group`
- `list` / `create <name> [UserIds...]` / `remove <id>` / `remove_bulk [groupIds...]`
- `add_user <groupNameOrId> [userIds...]` / `remove_user <groupNameOrId> [userIds...]`
- `add_resource <groupNameOrId> [resourceNamesOrIds...]` / `remove_resource <groupNameOrId> [resourceNamesOrIds...]`
- `set_policy <groupNameOrId> <securityPolicyNameOrId>`
- `copy <source> <destination>` — copies all users from source to destination group

### `network`
- `list` / `create <name>`

### `connector`
- `list` / `create <remoteNetworkNameOrId> [name]` — returns `ACCESS_TOKEN` and `REFRESH_TOKEN` on creation

### `resource`
- `list` / `create <remoteNetworkNameOrId> <name> <address> [groupNamesOrIds...]`
- `remove <id>` / `remove_bulk [resourceIds...]`
- `add_group <resourceNameOrId> [groupNamesOrIds...]`

### `device`
- `list`

### `policy`
- `list` / `add_group <securityPolicyNameOrId> [groupNamesOrIds...]`

### `service`
- `list` / `create <name> [resourceNamesOrIds...]` / `remove <id>`
- `add_resource <serviceAccountId> [resourceNamesOrIds...]`
- `key_create <serviceAccountId> <keyName> <expirationTimeInDays>` — returns full JSON token object with private key

### `export`
- Flags: `-f [xlsx|json|dot|png|svg]`, `-o <filename>`, `-n` (networks), `-r` (resources), `-g` (groups), `-u` (users), `-d` (devices)
- Default: exports all to `.xlsx`

### `import`
- Flags: `-f <excelFile>` (required), `-n/-r/-g/-d` selectors, `-s` (sync by natural ID), `-y` (assume yes)

## Gotchas
- `group add_user` / `resource create` require **IDs**, not email addresses for users
- `service remove` fails if service account has active keys
- `policy add_group` **replaces** existing policy assignment on groups
- `png`/`svg` export requires GraphViz on PATH
- `connector create` tokens shown only at creation time — save immediately

## Related Docs
- Twingate Python CLI (alternative for Python developers)
- Twingate GraphQL API documentation
- GitHub issues page for support