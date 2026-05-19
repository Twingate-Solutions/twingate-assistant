# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended deployments. The client is installed via command line with a `service_secret` parameter and managed through Windows Services.

## Key Information
- Requires a Service Account and Service Key (created in Twingate Admin Console)
- Download installer from [public changelog](https://www.twingate.com/docs/changelog)
- Client does **not** auto-start by default; configure startup behavior in Windows Services
- Service Key is securely stored by the client after installation; original file can be removed
- A valid Service Key is still required for updates/reinstalls

## Prerequisites
- Service account and Service Key configured in Twingate Admin Console
- Administrator permissions for installation and key management
- Windows Client EXE installer

## Step-by-Step Installation

```bash
# Silent headless install
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json /qn

# With debug logging
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json log_level=debug /qn
```

## Configuration Values

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `service_secret` | Yes | — | Path to Service Key JSON file |
| `log_level` | No | `info` | Set at install or in `headless.conf` |
| `/qn` | No | — | Silent install flag |

**Config file path:** `C:\Program Files\Twingate\headless.conf`  
**Log path:** `C:\ProgramData\Twingate\logs`

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

**Upgrade client:** Re-run installer with `service_secret` pointing to valid key.

## Gotchas
- Must **restart the service** after any key change for it to take effect
- If originally installed **without** a Service Key, you cannot use `sc` to add one — must do a fresh installation
- Deleting the Service Key disconnects the client immediately; a new key is required to reconnect
- Client won't auto-start after install; must configure Windows Service startup type manually

## Related Docs
- [Services / Service Keys](https://www.twingate.com/docs/services)
- [Headless Mode Overview](https://www.twingate.com/docs/headless-mode)
- [Public Changelog / Downloads](https://www.twingate.com/docs/changelog)