---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-08-09
source_version: 9d00ea155f19c91a6cafbe3c587740ae90a9c243b4171c1740e52ea1cd2fa1da
---

# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool built on Twingate's GraphQL APIs, written in JavaScript. Provides full account management capabilities including users, groups, resources, connectors, networks, devices, policies, and service accounts. Available as pre-built binaries for Windows, Mac, and Linux.

## Key Information
- **Source**: Open-source, community-maintained (not Twingate product engineering)
- **Support**: GitHub Issues page only
- **Alternative**: Python CLI available for Python developers
- **Auth**: Prompts for account name + API key on first run; offers to save credentials to file
- **IDs**: All entities use base64-encoded IDs (e.g., `VXNlcjoxMzY3Ng==`); names can often be used interchangeably

## Prerequisites
- Download binary from GitHub releases page
- Twingate account name
- Twingate API key
- GraphViz installed (only for PNG/SVG export formats)

## Commands Reference

| Command | Subcommands |
|---------|-------------|
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
- `-l, --log-level [level]` — `TRACE`, `DEBUG`, `INFO` (default), `WARN`, `ERROR`, `SEVERE`, `FATAL`, `QUIET`, `SILENT`

**Export flags:**
- `-f, --format` — `xlsx` (default), `json`, `dot`, `png`, `svg`
- `-o, --output-file` — output filename
- `-n/-r/-g/-u/-d` — include Remote Networks / Resources / Groups / Users / Devices

**Import flags:**
- `-f, --file <string>` — path to Excel file (required)
- `-s, --sync` — sync entities by natural identifier
- `-y, --assume-yes` — skip confirmation prompts

## Step-by-Step Examples

```bash
# Create connector (returns ACCESS_TOKEN and REFRESH_TOKEN)
./tg connector create "myRemoteNetwork" "myNewConnector"

# Create service key (returns full JSON token object with private_key)
./tg service key_create "<serviceAccountId>" "keyName" "365"

# Create resource with groups
./tg resource create "myRemoteNetwork" "myResource" "1.1.1.1" "group1" "group2"

# Export all to xlsx
./tg export

# Export resources as JSON
./tg export -r -f json

# Import from xlsx with sync
./tg import -f export.xlsx -n -r -g -s -y
```

## Gotchas
- **Service account removal** requires 0 active keys first
- **`policy add_group`** replaces existing policy assignments on groups
- **User IDs required** (not email addresses) when adding users to groups via CLI
- **`group copy`** copies users only, not resources
- **PNG/SVG export** requires GraphViz on system PATH
- **`group remove_resource`** help text says "Add resources" but actually removes (doc typo)
- Credentials saved to local file after first authenticated command

## Related Docs
- Twingate Python CLI
- Twingate GraphQL API
- GitHub releases page (binary downloads)
- GitHub Issues (support)