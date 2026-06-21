# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended deployments. It is installed via command-line switches and controlled through Windows Services.

## Key Information
- Requires a Service Account and Service Key from the Twingate Admin console
- Client controlled via Windows Services (`Twingate Service`)
- Does **not** start automatically by default (modify service settings to change)
- Service Key is securely stored after installation; original file can be removed, but is needed for updates/reinstalls
- Logs output to `C:\ProgramData\Twingate\logs`
- Additional config available at `C:\Program Files\Twingate\headless.conf`

## Prerequisites
- Service account and Service Key created in Twingate Admin console
- Windows Client EXE installer (from [public changelog](https://www.twingate.com/docs/windows-headless))
- Administrator permissions for service management

## Step-by-Step: Installation

```bash
# Silent install with service key
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json /qn

# Silent install with debug logging
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json log_level=debug /qn
```

## Configuration Values

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `service_secret` | Yes | — | Path to Service Key JSON file |
| `log_level` | No | `info` | Log verbosity; see `headless.conf` for levels |
| `/qn` | No | — | Silent install flag |

**Config file path:** `C:\Program Files\Twingate\headless.conf`

## Key Rotation / Upgrades

**Update Service Key via `sc`:**
```bash
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\service\secret.json
```

**Update Service Key via reinstall:**
```bash
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

**Delete stored Service Key:**
```bash
sc start twingate.service --config --reset
```

**Upgrade client:** Re-run installer with `service_secret` switch.

## Gotchas
- Service must be **restarted** for any config changes to take effect
- If client was previously installed **without** a Service Key, you must do a **fresh install** with `service_secret`; `sc` command alone won't work
- Deleting the Service Key disconnects the client immediately; a new key is required to reconnect
- Client does not auto-start after installation by default

## Related Docs
- [Services (Service Accounts & Keys)](https://www.twingate.com/docs/services)
- [Twingate Public Changelog](https://www.twingate.com/docs/windows-headless) (for installer download)