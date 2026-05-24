# Twingate Python CLI - Introduction

## Page Title
Introduction to the Twingate Python CLI

## Summary
An open-source Python CLI tool that wraps Twingate's GraphQL APIs to automate administrative functions available in the Admin Panel. It supports CRUD operations on Resources, Groups, Connectors, Devices, Users, Service Accounts, and Remote Networks. Maintained outside Twingate's product engineering team; support via GitHub Issues.

## Key Information
- Open-source project on GitHub (not officially product-supported)
- Wraps Twingate GraphQL APIs
- Session-based authentication; sessions persist across commands
- Supports output formats: JSON (default), CSV, DF (dataframes/table)
- Use `-h` at any level for contextual help

## Prerequisites
- Python 3
- `pandas` library
- Twingate API Key
- Twingate tenant name
- Clone the CLI repository from GitHub

## Step-by-Step

**Install & Verify:**
```bash
git clone <repo>
cd <repo>
python3 ./tgcli.py auth list  # Should return ['']
```

**Authenticate (create session):**
```bash
python3 ./tgcli.py auth login -t <tenant> -a <apikey> [-s <session_name>]
# Returns auto-generated session name (e.g., OrangeElk) if -s omitted
```

**Run Commands:**
```bash
python3 ./tgcli.py -s <session_name> [-f CSV|DF] <object> <operation>
# Example:
python3 ./tgcli.py -s OrangeElk -f CSV resource list
```

## Configuration Values

| Flag | Description |
|------|-------------|
| `-s SESSIONNAME` | Session name (global or per-auth) |
| `-f OUTPUTFORMAT` | Output format: `JSON`, `CSV`, `DF` |
| `-a APIKEY` | API key for login |
| `-t TENANT` | Twingate tenant name for login |
| `-v` | Show version |
| `-h` | Contextual help at any command level |

**Supported object types:** `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`

## Gotchas
- Commands fail with `no session name passed` if `-s` is omitted after login — must pass session name on every non-auth command
- Missing `pandas` library causes errors on first run; install manually if needed
- Session name is auto-generated (random words) unless specified with `-s` during `auth login`
- Pull latest from GitHub periodically; features are actively added

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/graphql-api)
- GitHub repository (linked from docs page)
- GitHub Issues (for support)