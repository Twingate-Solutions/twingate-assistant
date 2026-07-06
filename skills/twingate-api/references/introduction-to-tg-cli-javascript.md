# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI

## Summary
Open-source CLI tool wrapping Twingate GraphQL APIs, written in JavaScript with pre-built binaries for Windows/Mac/Linux. Supports full account management including users, groups, networks, connectors, resources, devices, policies, and service accounts. Node/Deno developers can extend it; community-supported via GitHub Issues.

## Key Information
- Binary downloads available on GitHub releases page
- Prompts for account name and API key on first run; offers to save credentials to file
- Accepts account name (`-a`) and log level (`-l`) as global flags
- Credentials saved locally after first use
- Community project — not supported by Twingate product engineering

## Prerequisites
- Twingate account name and API key
- For PNG/SVG export: GraphViz installed and on PATH

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
- `-l, --log-level` — `TRACE|DEBUG|INFO|WARN|ERROR|SEVERE|FATAL|QUIET|SILENT` (default: `INFO`)

**Export flags:**
- `-f, --format` — `xlsx|json|dot|png|svg` (default: `xlsx`)
- `-o, --output-file` — output filename
- `-n/-r/-g/-u/-d` — include remote-networks/resources/groups/users/devices

**Import flags:**
- `-f, --file <string>` — path to Excel file (required)
- `-s, --sync` — sync entities by natural identifier
- `-y, --assume-yes` — skip confirmation prompts

## Gotchas
- `group add_user` / `resource create` require **ID**, not name/email for users
- `policy add_group` **replaces** existing security policy on the group (not additive)
- `service remove` fails if service account has active keys
- `connector create` returns `ACCESS_TOKEN` and `REFRESH_TOKEN` — capture immediately, not retrievable later
- PNG/SVG export requires external GraphViz dependency
- `group copy` copies all users from source to a new destination group

## Related Docs
- [Python CLI](https://www.twingate.com/docs) — alternative for Python developers
- [GitHub Issues](https://github.com/Twingate) — support channel
- GraphViz (external) — required for graph export formats