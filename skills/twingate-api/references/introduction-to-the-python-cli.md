# Twingate Python CLI

## Summary
Open-source CLI tool wrapping Twingate GraphQL APIs to automate administrative tasks. Maintained outside core engineering—support via GitHub Issues. Requires Python 3 and pandas library.

## Key Information
- **Repo**: Clone from [GitHub](https://github.com/Twingate-Labs/tg-cli) (open source)
- **Authentication**: Session-based; create once, reuse session name across commands
- **Output formats**: JSON (default), CSV, DF (dataframe/table)
- **Supported objects**: `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`, `service`

## Prerequisites
- Python 3
- `pandas` library (`pip install pandas`)
- Twingate API Key
- Twingate tenant name

## Step-by-Step

### Setup & Auth
```bash
# Clone repo, then verify install
python3 ./tgcli.py auth list  # returns [''] if OK

# Login (creates named session)
python3 ./tgcli.py auth login -t <tenant> -a <apikey>
# Returns auto-generated session name (e.g., OrangeElk)

# Login with custom session name
python3 ./tgcli.py auth login -t <tenant> -a <apikey> -s mysession
```

### Basic Usage Pattern
```bash
python3 ./tgcli.py -s <sessionname> [-f FORMAT] <object> <operation> [params]

# Examples
python3 ./tgcli.py -s OrangeElk resource list
python3 ./tgcli.py -s OrangeElk -f CSV resource list
python3 ./tgcli.py -s OrangeElk -f DF resource list
```

### Discovery with `-h`
```bash
python3 ./tgcli.py -h                    # top-level help
python3 ./tgcli.py resource -h           # operations for object
python3 ./tgcli.py resource list -h      # params for operation
```

## Configuration Values / CLI Flags

| Flag | Description |
|------|-------------|
| `-s SESSIONNAME` | Session name (reuse across calls) |
| `-f OUTPUTFORMAT` | `JSON`, `CSV`, or `DF` |
| `-a APIKEY` | API key (login only) |
| `-t TENANT` | Tenant name (login only) |
| `-v` | Version |
| `-h` | Contextual help (works at any level) |

## Supported Operations by Object

| Object | Operations |
|--------|-----------|
| `auth` | login, logout, list |
| `resource` | list, show, create, delete |
| `device` | list, show, update trust |
| `group` | list, show, add/remove users, add/remove resources, create, delete, assign policy |
| `connector` | list, show, rename, generate tokens |
| `user` | list, show |
| `service` (account) | list, show, create, delete, add/remove resources |

## Gotchas
- Commands fail with `no session name passed` if `-s` is omitted after login
- Missing `pandas` causes errors on first run—install before use
- Session name is auto-generated (random words) unless `-s` is specified at login
- Pull updates periodically (`git pull`); CLI is actively developed

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/api)
- GitHub Issues page (for support—not Twingate official support)