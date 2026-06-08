# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key instead of interactive user authentication. It is installed via command line and controlled through Windows Services. A Service Key from the Twingate Admin console is required.

## Key Information
- Headless mode uses Service accounts/Service Keys (not user accounts)
- Client controlled via Windows Services (`Twingate Service`)
- Service does **not** start automatically by default — must configure manually
- Service Key is securely stored after install; original file can be removed
- Valid Service Key still required for updates/reinstalls

## Prerequisites
- Service account and Service Key created in Twingate Admin console
- Windows Client EXE installer (from [public changelog](https://www.twingate.com/docs/changelog))
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
| `log_level` | No | `info` | Log verbosity level |
| `/qn` | No | — | Silent install flag |

**Config file path:** `C:\Program Files\Twingate\headless.conf`  
**Log output path:** `C:\ProgramData\Twingate\logs`

## Key Rotation & Upgrades

**Update Service Key (option 1 — sc command):**
```bash
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\secret.json
```

**Update Service Key (option 2 — reinstall):**
```bash
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

**Delete stored Service Key:**
```bash
sc start twingate.service --config --reset
```

**Upgrade client:** Re-run installer with `service_secret` switch.

## Gotchas
- Must **restart the service** after any key rotation for changes to take effect
- If originally installed **without** a Service Key, `sc` command cannot add one — must do a fresh install with `service_secret`
- Deleting the Service Key disconnects the client immediately; new key required to reconnect
- Auto-start is disabled by default; configure Windows service startup type manually if needed

## Related Docs
- [Services (Service Accounts & Keys)](https://www.twingate.com/docs/services)
- [Public Changelog / Installer Downloads](https://www.twingate.com/docs/changelog)
- Linux/Mac Headless Mode documentation