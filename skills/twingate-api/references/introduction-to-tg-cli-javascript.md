# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate Javascript CLI

## Summary
Open-source CLI tool built on Twingate GraphQL APIs, written in JavaScript with pre-built binaries for Windows/Mac/Linux. Supports full CRUD operations on users, groups, networks, connectors, resources, devices, policies, and service accounts. Node/Deno developers can extend it; Python users may prefer the Python CLI alternative.

## Key Information
- **Source**: Open-source, community-maintained (not Twingate product engineering)
- **Support**: GitHub Issues only
- **Auth**: Prompts for account name + API key on first run; optionally saves credentials to file
- **References**: Accepts names OR IDs for most entity arguments (e.g., `groupNameOrId`)

## Prerequisites
- Download binary from GitHub releases page
- Twingate account name and API key
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
- `-l, --log-level [level]` — `TRACE|DEBUG|INFO|WARN|ERROR|SEVERE|FATAL|QUIET|SILENT` (default: `INFO`)

**Export flags:**
- `-f, --format` — `xlsx|json|dot|png|svg` (default: `xlsx`)
- `-o, --output-file` — output filename
- `-n` networks, `-r` resources, `-g` groups, `-u` users, `-d` devices

**Import flags:**
- `-f, --file <string>` — path to Excel file **(required)**
- `-n/-r/-g/-d` — entity type filters
- `-s, --sync` — sync by natural identifier
- `-y, --assume-yes` — skip prompts

## Step-by-Step: Create Connector with Tokens
```bash
./tg connector create "myRemoteNetwork" "myNewConnector"
# Returns ACCESS_TOKEN and REFRESH_TOKEN for connector auth
```

## Gotchas
- **User operations require ID, not email** — use `user list` to get IDs first
- **Service account removal** — fails if account has active keys (must revoke keys first)
- **`policy add_group`** — replaces existing security policy on the group (destructive)
- **`group copy`** — copies users only, not resources
- **Resource/group/network must pre-exist** before referencing in create commands
- **png/svg export** requires GraphViz on system PATH

## Related Docs
- Twingate Python CLI
- Twingate GraphQL API
- GitHub Issues (support channel)