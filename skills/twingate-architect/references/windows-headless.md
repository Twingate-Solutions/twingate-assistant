# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended deployments. The client is installed via command line with a `service_secret` parameter and controlled through Windows Services.

## Key Information
- Requires a Service Account and Service Key from Twingate Admin Console
- Client controlled via Windows Services (`Twingate Service`)
- Client does **not** start automatically by default (must configure service startup behavior manually)
- Original Service Key file not needed after install, but required for updates/reinstalls
- Logs: `C:\ProgramData\Twingate\logs`
- Optional config file: `C:\Program Files\Twingate\headless.conf`

## Prerequisites
- Service account and Service Key created in Twingate Admin Console
- Windows Client EXE installer (download from [public changelog](https://www.twingate.com/docs/windows-headless))
- Administrator permissions for key rotation/deletion operations

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
| `service_secret` | Yes | — | Path to Service Key JSON file |
| `log_level` | No | `info` | Available levels in `headless.conf` |
| `/qn` | No | — | Silent install flag |

## Key Rotation

**Option 1 — `sc` command:**
```bash
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\service\secret.json
```

**Option 2 — Re-run installer:**
```bash
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

**Delete stored key:**
```bash
sc start twingate.service --config --reset
```

**Upgrade client:** Re-run installer with `service_secret` pointing to valid key.

## Gotchas
- **Must restart service** after any key rotation for changes to take effect
- If originally installed **without** a Service Key, you cannot use `sc` to add one — must perform a fresh installation
- Deleting the Service Key immediately disconnects the client; a new key must be provisioned to reconnect
- Auto-start is disabled by default — configure Windows service startup type manually if persistence is needed

## Related Docs
- [Services (Service Accounts & Keys)](https://www.twingate.com/docs/services)
- [Public Changelog / Download](https://www.twingate.com/changelog)