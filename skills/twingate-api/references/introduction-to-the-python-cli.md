# Twingate Python CLI Introduction

## Page Title
Introduction to the Twingate Python CLI

## Summary
An open-source CLI tool that wraps Twingate GraphQL APIs to automate administrative tasks available in the Admin Panel. Supports CRUD operations on Resources, Groups, Connectors, Devices, Users, Service Accounts, and Remote Networks. Maintained outside Twingate's core engineering team; support via GitHub Issues.

## Key Information
- **GitHub repo**: Clone to get started; pull periodically for updates
- **Object types**: `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`
- **Output formats**: JSON (default), CSV, DF (dataframe/human-readable table)
- **Session-based auth**: Login creates a named session reused across commands
- **Help flag**: `-h` works at every level of the command hierarchy for contextual help

## Prerequisites
- Python 3
- `pandas` library installed
- Twingate API Key
- Twingate tenant name

## Step-by-Step

### Initial Setup
```bash
git clone <repo>
cd <cli-folder>
python3 ./tgcli.py auth list  # Should return [''] if ready
```

### Authenticate
```bash
python3 ./tgcli.py auth login -t <tenant> -a <apikey>
# Returns auto-generated session name (e.g., OrangeElk)

# Or specify session name:
python3 ./tgcli.py auth login -t <tenant> -a <apikey> -s mysession
```

### Run Commands
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
| `-a APIKEY` | API Key (used at login) |
| `-t TENANT` | Tenant name (used at login) |
| `-v` | Show version |
| `-h` | Contextual help at any level |

## Gotchas
- Running any command without `-s` will fail with `error: no session name passed`
- If `auth list` returns an error (not empty list), a Python library is missing—install it and retry
- Session name is auto-generated (random words) unless `-s` is explicitly specified at login
- This is community/open-source—not officially supported by Twingate product engineering

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/)
- GitHub Issues page (for support)
- GitHub repository (for source and updates)