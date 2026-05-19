# Twingate Python CLI - Introduction

## Page Title
Introduction to the Twingate Python CLI

## Summary
An open-source Python CLI tool wrapping Twingate's GraphQL APIs to automate administrative functions. Supports CRUD operations on Resources, Devices, Groups, Connectors, Users, Service Accounts, and Remote Networks. Maintained outside Twingate's core engineering team via GitHub.

## Key Information
- Open source project; support via GitHub Issues only
- Wraps Twingate GraphQL API
- Session-based authentication (stores API key + tenant per named session)
- Output formats: `JSON` (default), `CSV`, `DF` (dataframe/table)
- Use `-h` at any level for contextual help

## Prerequisites
- Python 3
- `pandas` library installed
- Twingate API Key
- Twingate tenant name

## Step-by-Step

**Install & Verify:**
```bash
git clone <repo>
cd <repo>
python3 ./tgcli.py auth list  # should return ['']
```

**Authenticate (create session):**
```bash
python3 ./tgcli.py auth login -t <tenant> -a <apikey> [-s <session_name>]
# Returns auto-generated session name (e.g., OrangeElk) if -s omitted
```

**Run commands with session:**
```bash
python3 ./tgcli.py -s OrangeElk resource list
python3 ./tgcli.py -s OrangeElk -f CSV resource list
python3 ./tgcli.py -s OrangeElk -f DF resource list
```

## Configuration Values / CLI Flags

| Flag | Description |
|------|-------------|
| `-s SESSIONNAME` | Session name (required for most commands) |
| `-f OUTPUTFORMAT` | Output format: `JSON`, `CSV`, `DF` |
| `-a APIKEY` | API key (used with `auth login`) |
| `-t TENANT` | Tenant name (used with `auth login`) |
| `-v` | Show version |
| `-h` | Contextual help at any command level |

**Supported object types:** `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`

## Gotchas
- Commands fail with `error: no session name passed` if `-s` flag is omitted after login
- Missing `pandas` library causes errors on first run — install manually if needed
- Pull latest from GitHub periodically; features are actively added
- Session name is auto-generated (random words) unless `-s` is specified at login

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/graphql)
- GitHub repository (linked from docs page)
- GitHub Issues page (for CLI-specific support)