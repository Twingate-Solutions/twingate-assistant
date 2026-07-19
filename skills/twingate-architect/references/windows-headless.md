# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended deployments. The client is installed via command line with the `service_secret` switch and controlled through Windows Services.

## Key Information
- Requires a Service Account and Service Key from Twingate Admin console
- Client controlled via Windows Services (`Twingate Service`)
- Service does **not** start automatically by default (configurable in Windows service settings)
- Service Key is securely stored after installation; original file doesn't need to be retained
- Logs output to `C:\ProgramData\Twingate\logs`
- Additional config available at `C:\Program Files\Twingate\headless.conf`

## Prerequisites
- Service account and Service Key created in Twingate Admin console
- Windows Client EXE installer (download from [public changelog](https://www.twingate.com/docs/windows-headless))
- Administrator permissions for key rotation/deletion operations

## Step-by-Step

### Installation
```bat
# Silent headless install
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json /qn

# With debug logging
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json log_level=debug /qn
```

### Start/Stop
- Manage via Windows Services UI, or `sc start`/`sc stop twingate.service`

### Update Service Key (two options)
```bat
# Option 1: sc command
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\service\secret.json

# Option 2: Re-run installer
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

### Delete Service Key
```bat
sc start twingate.service --config --reset
```

## Configuration Values

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `service_secret` | Yes | — | Path to Service Key JSON file |
| `log_level` | No | `info` | Log verbosity; see `headless.conf` for levels |
| `/qn` | No | — | Silent install flag |

## Gotchas
- **Must restart service** after any Service Key changes to take effect
- If previously installed **without** a Service Key, you cannot use `sc` command to add one — must do a fresh installation with `service_secret`
- Deleting the Service Key (`--reset`) immediately disconnects the client; requires new key to reconnect
- Valid Service Key required for upgrades and reinstalls, even though original file isn't needed during normal operation
- Auto-start is disabled by default; must configure Windows service startup type manually

## Related Docs
- [Services documentation](https://www.twingate.com/docs/services) — Creating Service accounts and Service Keys
- [Public changelog](https://www.twingate.com/changelog) — Download latest Windows Client installer
- `headless.conf` — Full list of available log levels and optional config options