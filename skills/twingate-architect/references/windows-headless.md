# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended deployments. The client is installed via command line with a `service_secret` parameter and managed through Windows Services.

## Key Information
- Requires a Service account and Service Key from Twingate Admin console
- Service Key is securely stored by the client after installation; original file can be moved/deleted
- Client does **not** start automatically by default (modify Windows service settings to change)
- Logs output to: `C:\ProgramData\Twingate\logs`
- Additional config available at: `C:\Program Files\Twingate\headless.conf`

## Prerequisites
- Valid Service Key JSON file (create via Services in Admin console)
- Windows Client EXE installer (from [public changelog](https://www.twingate.com/docs/windows-headless))
- Administrator permissions for key rotation/deletion operations

## Step-by-Step: Installation

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

## Key Rotation

**Option 1 — sc command:**
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

## Gotchas
- **Must restart service** after any key update for changes to take effect
- If originally installed **without** a Service Key, `sc` command cannot add one — must do a fresh install with `service_secret`
- Deleting the Service Key disconnects the client immediately; a new key is required to reconnect
- Original Service Key file is not needed post-install **except** when upgrading or reinstalling

## Related Docs
- [Services documentation](https://www.twingate.com/docs/services) — creating Service accounts and keys
- Headless.conf — additional config options including log levels