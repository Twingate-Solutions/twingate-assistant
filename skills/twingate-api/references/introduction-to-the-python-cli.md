# Twingate Python CLI

## Summary
Open-source CLI tool wrapping Twingate GraphQL APIs for automating administrative tasks. Maintained outside core product engineering; support via GitHub Issues. Requires Python 3 and the `pandas` library.

## Key Information
- Supports CRUD operations on: Resources, Devices, Groups, Connectors, Users, Service Accounts, Service Account Keys, Remote Networks, Policies
- Authentication is session-based; sessions persist across commands without re-authenticating
- Default output is JSON; supports CSV and DF (dataframe/table) formats
- Use `-h` at any level of the command hierarchy for contextual help

## Prerequisites
- Python 3
- `pandas` Python library
- Twingate API Key and tenant name
- Clone repo: [GitHub - Twingate Python CLI](https://github.com/Twingate-Labs/tg-cli)

## Step-by-Step

**1. Verify installation**
```bash
python3 ./tgcli.py auth list
# Returns [''] if successful; missing library error otherwise
```

**2. Authenticate (create session)**
```bash
python3 ./tgcli.py auth login -t <tenant> -a <api_key> [-s <session_name>]
# Generates random session name if -s omitted
```

**3. Run commands using session**
```bash
python3 ./tgcli.py -s <session_name> resource list
```

## Configuration Values / CLI Flags

| Flag | Description |
|------|-------------|
| `-s SESSIONNAME` | Session name (required for most commands) |
| `-a APIKEY` | API key (used during `auth login`) |
| `-t TENANT` | Twingate tenant name (used during `auth login`) |
| `-f OUTPUTFORMAT` | Output format: `JSON` (default), `CSV`, `DF` |
| `-v` | Show version |
| `-h` | Contextual help at any command level |

**Object types:** `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`

**Auth operations:** `login`, `logout`, `list`

## Gotchas
- Commands fail with `no session name passed` error if `-s` is not provided after login
- Session name is auto-generated (e.g., `OrangeElk`) unless specified with `-s` at login time
- Pull latest repo version periodically — features are actively added
- This is community-maintained; not officially supported by Twingate product engineering

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/api)
- GitHub Issues page for bug reports/feature requests