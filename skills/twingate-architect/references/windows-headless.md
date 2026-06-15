# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/non-interactive deployments. It is installed via CLI with the `service_secret` switch and managed through Windows Services.

## Key Information
- Requires a Service Account and Service Key from the Twingate Admin console
- Client controlled via Windows Services (`Twingate Service`)
- Does **not** start automatically by default (must configure Windows service startup behavior)
- Service Key is securely stored by the client after installation; original file can be removed
- Logs output to `C:\ProgramData\Twingate\logs`
- Optional config file at `C:\Program Files\Twingate\headless.conf`

## Prerequisites
- Valid Service Key JSON file (from Admin console → Services)
- Windows Client EXE installer (from [public changelog](https://www.twingate.com/docs/windows-headless))
- Administrator permissions for service management

## Step-by-Step Installation

```bash
# Silent install with service key
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

## Key Rotation & Upgrades

**Update Service Key (option 1 — sc command):**
```bash
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\service\secret.json
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
- Service must be **restarted** for any config changes to take effect
- If originally installed **without** a Service Key, must do a fresh installation — cannot use `sc` command alone to add one
- Deleting the Service Key disconnects the client; requires new key to reconnect
- Auto-start must be manually configured in Windows Services settings

## Related Docs
- [Services / Service Keys documentation](https://www.twingate.com/docs/services)
- [Public changelog / installer download](https://www.twingate.com/changelog)