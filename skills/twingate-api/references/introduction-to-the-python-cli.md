# Twingate Python CLI - Introduction

## Page Title
Introduction to the Twingate Python CLI

## Summary
Open-source CLI tool that wraps Twingate GraphQL APIs to automate administrative functions available in the Admin Panel. Requires Python 3 and the `pandas` library. Maintained outside Twingate's core engineering team; support via GitHub Issues.

## Key Information
- Supports CRUD operations on: Resources, Devices, Groups, Connectors, Users, Service Accounts, Service Account Keys, Remote Networks, Policies
- Returns JSON by default; supports CSV and DF (dataframe/table) output formats
- Session-based authentication — authenticate once, reuse session name for subsequent commands
- Use `-h` at any level of the command for contextual help

## Prerequisites
- Python 3
- `pandas` library (`pip install pandas`)
- Twingate API Key
- Twingate tenant name

## Step-by-Step

1. **Clone repo**: `git clone <github-repo-url>`
2. **Verify install**: `python3 ./tgcli.py auth list` → should return `['']`
3. **Authenticate**:
   ```bash
   python3 ./tgcli.py auth login -t <tenant> -a <apikey>
   # Returns session name e.g. "OrangeElk"
   ```
4. **Use session in commands**:
   ```bash
   python3 ./tgcli.py -s OrangeElk resource list
   ```

## Configuration Values

| Flag | Description | Required |
|------|-------------|----------|
| `-a` / `--apikey` | Twingate API Key | Yes (for login) |
| `-t` / `--tenant` | Twingate tenant name | Yes (for login) |
| `-s` / `--session` | Session name | Optional (auto-generated if omitted) |
| `-f` / `--format` | Output format: `JSON`, `CSV`, `DF` | No (default: JSON) |
| `-v` / `--version` | Show version | No |

**Object types**: `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`

## Gotchas
- Running any command without `-s <sessionname>` after login will fail with `error: no session name passed`
- Missing `pandas` causes errors on first run — install it manually and retry
- Session name is auto-generated (random words) unless specified with `-s` at login time
- Pull latest version from GitHub periodically as features are actively added

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/api-overview)
- [GitHub Repository](https://github.com/Twingate-Labs/tg-cli) (issues and contributions)