---
source: https://www.twingate.com/docs/windows-headless
type: docs
fetched: 2026-10-25
source_version: c72285d33c9f8a04fb46a84350b7d65ae9cdb72015af5e2a2009c0e90e7325bf
trust: official
---

# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended deployment. The client is managed via Windows Services (start/stop) rather than a GUI. A valid Service Key from the Twingate Admin console is required for installation, updates, and reinstallation.

## Key Information
- Headless mode uses a **Service Account + Service Key** (not user credentials)
- Client is managed via Windows Services → **Twingate Service**
- Service does **not** start automatically by default (must configure in Windows Services)
- Service Key is securely stored after install; original file can be moved/deleted
- Logs output to `C:\ProgramData\Twingate\logs`
- Config file: `C:\Program Files\Twingate\headless.conf`

## Prerequisites
- Service account and Service Key created in Twingate Admin console (see Services docs)
- Windows Client EXE installer (download from [public changelog](https://www.twingate.com/changelog))
- Administrator permissions for `sc` commands

## Installation (Step-by-Step)

1. Download `TwingateWindowsInstaller.exe` from the Twingate public changelog page.
2. Run installer from an elevated command prompt:

```cmd
# Basic headless install
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json /quiet

# With debug logging
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json log_level=debug /quiet
```

3. Configure auto-start behavior via Windows Services if needed.
4. Start/stop via Windows Services UI or `sc start/stop twingate.service`.

## Configuration Values

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `service_secret` | Yes | — | Path to Service Key JSON file |
| `log_level` | No | `info` | Set at install or in `headless.conf` |
| `/quiet` | No | — | Silent/unattended install |

Config file path: `C:\Program Files\Twingate\headless.conf`

## Key Rotation & Upgrades

**Update Service Key (option 1 — sc command):**
```cmd
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\service\secret.json
```

**Update Service Key (option 2 — reinstall):**
```cmd
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

**Delete stored Service Key:**
```cmd
sc start twingate.service --config --reset
```

**Upgrade client:** Re-run installer with `service_secret` switch.

## Gotchas
- **Must restart the service** after any key rotation for changes to take effect.
- If originally installed **without** a Service Key, you cannot use `sc` to add one — must do a fresh installation with `service_secret`.
- Deleting the Service Key disconnects the client immediately; a new key is required to reconnect.
- A valid Service Key is required when upgrading or reinstalling — keep a copy accessible.

## Related Docs
- [Services / Service Keys documentation](https://www.twingate.com/docs/services)
- [Twingate public changelog](https://www.twingate.com/changelog) (installer downloads)