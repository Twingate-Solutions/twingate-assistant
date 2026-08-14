---
source: https://www.twingate.com/docs/windows-headless
type: docs
fetched: 2026-08-14
source_version: 5d50460df5f54961f9c759577621a0ff92c1031961634682333937e2126f79be
---

# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended operation without user interaction. The client is controlled via Windows Services (start/stop) rather than a GUI.

## Key Information
- Requires a Service account and Service Key from Twingate Admin console
- Client logs stored at: `C:\ProgramData\Twingate\logs`
- Config file location: `C:\Program Files\Twingate\headless.conf`
- Service Key is securely stored by client after install; original file can be removed
- Client does **not** start automatically by default (configurable in Windows Services)

## Prerequisites
- Service account created in Twingate Admin console
- Valid Service Key (`.json` file) downloaded from Admin console
- Windows Client EXE installer (from [public changelog](https://www.twingate.com/docs/changelog))
- Administrator permissions for key rotation/deletion commands

## Step-by-Step: Installation

```cmd
# Silent install with service key
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json /qn

# Silent install with debug logging
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json log_level=debug /qn
```

## Configuration Values

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `service_secret` | Yes | — | Path to Service Key `.json` file |
| `log_level` | No | `info` | Available levels in `headless.conf` |
| `/qn` | No | — | Silent install flag |

## Key Rotation Commands

```cmd
# Method 1: sc command (stop/restart with new key)
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\service\secret.json

# Method 2: Re-run installer
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json

# Delete stored Service Key
sc start twingate.service --config --reset

# Upgrade client
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

## Gotchas
- **Service restart required** after any Service Key changes to take effect
- If previously installed **without** a Service Key, must do a fresh install with `service_secret`; cannot use `sc` command to add key for first time
- Deleting the Service Key immediately disconnects the client; requires new key to reconnect
- Original Service Key file not needed after install, but **is required** for updates/reinstalls

## Related Docs
- [Services documentation](https://www.twingate.com/docs/services) — Creating Service accounts and Keys
- [Public changelog](https://www.twingate.com/docs/changelog) — Download latest Windows Client EXE