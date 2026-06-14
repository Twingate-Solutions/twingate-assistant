# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate Javascript CLI

## Summary
Open-source CLI tool wrapping Twingate GraphQL APIs, written in JavaScript (Node/Deno compatible). Provides pre-built binaries for Windows/Mac/Linux. Supports full CRUD operations for resources, groups, networks, connectors, devices, service accounts, policies, and export/import workflows.

## Key Information
- Binaries available on GitHub releases page; unzip and run directly
- Prompts for account name and API key on first run; optionally saves credentials to file
- Accepts names OR IDs for most entity references (e.g., `groupNameOrId`)
- All IDs are base64-encoded GraphQL node IDs
- Community-supported; issues via GitHub Issues page

## Prerequisites
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
| `export` | (flags-based) |
| `import` | (flags-based) |

## Configuration Values / CLI Flags

**Global flags:**
- `-a, --account-name <string>` — Twingate account name
- `-l, --log-level [level]` — `TRACE|DEBUG|INFO|WARN|ERROR|SEVERE|FATAL|QUIET|SILENT` (default: `INFO`)

**Export flags:**
- `-f, --format` — `xlsx` (default), `json`, `dot`, `png`, `svg`
- `-o, --output-file` — output filename
- `-n` remote networks, `-r` resources, `-g` groups, `-u` users, `-d` devices

**Import flags:**
- `-f, --file <string>` — path to Excel file (required)
- `-s, --sync` — sync entities by natural identifier
- `-y, --assume-yes` — skip confirmation prompts

## Step-by-Step: Create Connector (returns tokens)
```bash
./tg connector create "myRemoteNetwork" "myNewConnector"
# Returns ACCESS_TOKEN and REFRESH_TOKEN for connector configuration
```

## Gotchas
- `group add_user` / `resource create` with users: **must use IDs**, not email addresses
- Service account cannot be removed if it has active keys
- `policy add_group`: **replaces** existing security policy on affected groups
- `png`/`svg` export requires GraphViz on system PATH
- `group copy` copies all users from source to destination group
- Remote network must exist before creating connectors or resources

## Related Docs
- Twingate Python CLI (alternative for Python developers)
- Twingate GraphQL API documentation
- GitHub releases page (binaries)
- GitHub Issues page (support)