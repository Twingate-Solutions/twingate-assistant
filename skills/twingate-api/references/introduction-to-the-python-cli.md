# Twingate Python CLI

## Summary
Open-source CLI tool wrapping Twingate GraphQL APIs for automating administrative tasks. Maintained outside core product engineering; community-supported via GitHub issues. Requires Python 3 and the `pandas` library.

## Key Information
- Supports CRUD operations on: Resources, Devices, Groups, Connectors, Users, Service Accounts, Service Account Keys, Remote Networks, Policies
- Session-based authentication — authenticate once, reuse session name across commands
- Three output formats: JSON (default), CSV, DF (dataframe/table)
- Use `-h` at any command level for contextual help

## Prerequisites
- Python 3
- `pandas` Python library
- Twingate API key
- Twingate tenant name
- Clone repo: `git clone <twingate-python-cli-repo>`

## Step-by-Step

**1. Verify installation**
```bash
python3 ./tgcli.py auth list
# Should return [''] — empty list means working
```

**2. Authenticate and create a session**
```bash
python3 ./tgcli.py auth login -t <tenant> -a <api_key>
# Returns auto-generated session name (e.g., OrangeElk)
# Use -s <name> to specify custom session name
```

**3. Run commands using session**
```bash
python3 ./tgcli.py -s OrangeElk resource list
```

## Configuration Values

| Flag | Description | Required |
|------|-------------|----------|
| `-a APIKEY` | Twingate API key | Yes (login) |
| `-t TENANT` | Twingate tenant name | Yes (login) |
| `-s SESSIONNAME` | Session name | Optional (login), Required (other commands) |
| `-f OUTPUTFORMAT` | Output format: `JSON`, `CSV`, `DF` | No (default: JSON) |
| `-v` | Show version | No |
| `-h` | Contextual help | No |

## Gotchas
- Every non-auth command requires `-s SESSIONNAME` — omitting it returns `error: no session name passed`
- Missing `pandas` library causes errors on first run — install before using
- Pull latest version periodically; repo is actively updated
- Tool is community-maintained — no official Twingate support; use GitHub Issues

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/api-overview)
- [Python CLI GitHub Repository](https://github.com/Twingate-Labs/tg-cli)