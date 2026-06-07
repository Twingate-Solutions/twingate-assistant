# Twingate Python CLI - Introduction

## Page Title
Introduction to the Twingate Python CLI

## Summary
An open-source CLI tool that wraps Twingate's GraphQL APIs to automate administrative functions available in the Admin Panel. Supports CRUD operations on Resources, Groups, Connectors, Devices, Users, Service Accounts, and Remote Networks. Maintained outside of Twingate's core engineering team; use GitHub Issues for support.

## Key Information
- Open-source project on GitHub (not officially supported by Twingate product team)
- Wraps Twingate GraphQL APIs
- Output formats: JSON (default), CSV, DF (DataFrame/table)
- Session-based authentication; sessions persist across commands
- Use `-h` at any command level for contextual help

## Prerequisites
- Python 3
- `pandas` library (`pip install pandas`)
- Twingate API Key
- Twingate tenant name
- Clone the CLI repo from GitHub

## Step-by-Step

### Initial Setup
```bash
git clone <twingate-python-cli-repo>
cd <repo-folder>
python3 ./tgcli.py auth list  # Should return empty list if setup is correct
```

### Authenticate
```bash
python3 ./tgcli.py auth login -t <tenant> -a <api-key> [-s <session-name>]
# Returns a session name (random if -s not specified), e.g., "OrangeElk"
```

### Run Commands Using Session
```bash
python3 ./tgcli.py -s OrangeElk resource list
python3 ./tgcli.py -s OrangeElk -f CSV resource list
python3 ./tgcli.py -s OrangeElk -f DF resource list
```

## Configuration Values / CLI Flags

| Flag | Description |
|------|-------------|
| `-s SESSIONNAME` | Session name to use |
| `-f OUTPUTFORMAT` | Output format: `JSON`, `CSV`, `DF` |
| `-v` | Show version |
| `-h` | Contextual help (works at every level) |
| `-a APIKEY` | API key (used with `auth login`) |
| `-t TENANT` | Tenant name (used with `auth login`) |

### Supported Object Types
`auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`

### Auth Operations
`login`, `logout`, `list`

## Gotchas
- Commands fail with `no session name passed` error if `-s` is not provided after authentication
- Missing `pandas` library causes errors on first run — install before use
- Session names are randomly generated unless specified with `-s` during login; note the generated name for subsequent commands
- Pull latest version periodically from GitHub as features are actively added

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/)
- GitHub repository (linked from docs page)
- GitHub Issues (primary support channel)