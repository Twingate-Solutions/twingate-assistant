# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool built on Twingate GraphQL APIs, written in JavaScript with pre-built binaries for Windows/Mac/Linux. Supports full CRUD operations for users, groups, networks, connectors, resources, devices, policies, and service accounts. Node/Deno developers can extend it; Python users may prefer the Python CLI alternative.

## Key Information
- Wraps Twingate GraphQL API
- Open-source; support via GitHub Issues only (not Twingate product team)
- Prompts interactively for account name and API key; option to save credentials to file
- Accepts names OR IDs for most entity references (e.g., `groupNameOrId`)
- IDs are base64-encoded strings (e.g., `VXNlcjoxMzY3Ng==`)

## Prerequisites
- Twingate account name
- Twingate API key
- GraphViz installed (only for `png`/`svg` export formats)

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

## Configuration Values

**Global flags:**
- `-a, --account-name <string>` — Twingate account name
- `-l, --log-level [level]` — Default: `INFO`; Values: `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `SEVERE`, `FATAL`, `QUIET`, `SILENT`

**Export flags:**
- `-f, --format` — Default: `xlsx`; Values: `xlsx`, `json`, `dot`, `png`, `svg`
- `-o, --output-file` — Output filename
- `-n/-r/-g/-u/-d` — Include remote networks/resources/groups/users/devices

**Import flags:**
- `-f, --file <string>` — Path to Excel file (required)
- `-s, --sync` — Sync entities by natural identifier
- `-y, --assume-yes` — Skip prompts

## Gotchas
- **Service account removal**: Cannot remove a service account with active keys (must be 0 active keys first)
- **User references**: Must use User ID (base64), not email address, when adding users to groups
- **`policy add_group`**: Replaces existing security policy on groups — does not append
- **`group copy`**: Copies users from source group to destination; destination group is created new
- **png/svg export**: Requires GraphViz on system PATH
- **`service key_create`**: Returns private key in response — store immediately, not retrievable later

## Related Docs
- Twingate Python CLI
- Twingate GraphQL API
- GitHub Issues (support channel)
- GraphViz installation