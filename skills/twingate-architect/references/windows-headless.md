# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/non-interactive deployments. The client is installed via command line with a `service_secret` parameter and controlled through Windows Services.

## Key Information
- Requires a Service Account and Service Key from Twingate Admin Console
- Client controlled via Windows Services (`Twingate Service`)
- Does **not** auto-start by default; modify Windows service settings to change startup behavior
- Service Key is securely stored after installation; original file can be moved/deleted
- A valid Service Key is still required for updates/reinstalls

## Prerequisites
- Service Account created in Twingate Admin Console
- Valid Service Key (`.json` file) downloaded
- Administrator permissions for installation and service management
- Windows Client EXE installer (from [public changelog](https://www.twingate.com/docs/windows-headless))

## Step-by-Step Installation

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

**Upgrade client:** Re-run installer with `service_secret` switch pointing to valid key.

## Gotchas
- Service must be **restarted** for any key or config changes to take effect
- If originally installed **without** a Service Key, you cannot use `sc` to add one — must do a fresh install with `service_secret`
- Deleting the Service Key disconnects the client immediately; requires new key to reconnect
- Client will **not auto-start** after installation by default

## Related Docs
- [Services documentation](https://www.twingate.com/docs/services) — creating Service accounts and keys
- [Public changelog](https://www.twingate.com/changelog) — download latest Windows installer