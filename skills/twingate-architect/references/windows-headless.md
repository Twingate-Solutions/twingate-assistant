# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended deployments. Installation is done via command line with the `service_secret` switch, and the client is controlled through Windows Services.

## Key Information
- Requires a Service Account and Service Key from Twingate Admin Console
- Download installer from [public changelog](https://www.twingate.com/docs/changelog)
- Service Key is securely stored after installation; original file can be removed
- Client does **not** start automatically by default (modify Windows service settings to change)
- Log output: `C:\ProgramData\Twingate\logs`
- Optional config file: `C:\Program Files\Twingate\headless.conf`

## Prerequisites
- Valid Service Key JSON file (from Admin Console → Services)
- Administrator permissions for install and key management operations

## Step-by-Step: Installation

```bash
# Silent install (basic)
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json /qn

# Silent install with debug logging
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json log_level=debug /qn
```

## Configuration Values

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `service_secret` | Yes | — | Path to Service Key JSON |
| `log_level` | No | `info` | Available levels in `headless.conf` |
| `/qn` | No | — | Silent install flag |

## Key Rotation

**Option 1 — sc command (requires Admin):**
```bash
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\secret.json
```

**Option 2 — Re-run installer:**
```bash
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

**Delete stored key:**
```bash
sc start twingate.service --config --reset
```

**Upgrade client:**
```bash
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

## Gotchas
- **Must restart service** for any key rotation changes to take effect
- If originally installed **without** a Service Key, must do a full fresh install with `service_secret`; `sc` command alone won't work
- Deleting the Service Key disconnects the client immediately; a new key is required to reconnect
- Auto-start is disabled by default; must manually configure Windows service startup type

## Related Docs
- [Services / Service Keys](https://www.twingate.com/docs/services)
- [Public Changelog / Downloads](https://www.twingate.com/docs/changelog)
- Linux/Mac Headless Mode documentation