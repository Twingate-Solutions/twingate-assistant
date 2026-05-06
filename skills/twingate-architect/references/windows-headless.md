# Windows Headless Mode

## Summary
Twingate's Windows client can run in headless mode using a Service Key, enabling automated/unattended operation controlled via Windows Services. Installation is performed via command line with the `service_secret` switch pointing to a valid Service Key JSON file.

## Key Information
- Requires a Service Account and Service Key from Twingate Admin Console
- Client controlled via Windows Services (start/stop `Twingate Service`)
- Does **not** auto-start by default; configure Windows service settings manually
- Service Key is securely stored after installation; original file location doesn't matter post-install
- Valid Service Key required for updates and reinstalls

## Prerequisites
- Service account created in Twingate Admin Console
- Service Key downloaded as JSON file
- Administrator permissions for installation and key management
- Windows Client EXE installer (from [public changelog](https://www.twingate.com/docs/windows-headless))

## Step-by-Step

**Install:**
```cmd
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json /qn
```

**With debug logging:**
```cmd
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json log_level=debug /qn
```

**Update Service Key (method 1 - sc command):**
```cmd
sc stop twingate.service
sc start twingate.service --config --service_secret C:\path\to\service\secret.json
```

**Update Service Key (method 2 - reinstall):**
```cmd
TwingateWindowsInstaller.exe service_secret=C:\path\to\service_key.json
```

**Delete stored Service Key:**
```cmd
sc start twingate.service --config --reset
```

## Configuration Values

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `service_secret` | Yes | — | Path to Service Key JSON file |
| `log_level` | No | `info` | Log verbosity level |
| `/qn` | No | — | Silent install flag |

**Config file path:** `C:\Program Files\Twingate\headless.conf`  
**Log output path:** `C:\ProgramData\Twingate\logs`

## Gotchas
- Service must be **restarted** after any key or config changes
- If originally installed *without* `service_secret`, you cannot use `sc` to add a key — must do a fresh install
- Deleting the Service Key immediately disconnects the client from Twingate
- Client won't auto-start after install; must configure Windows service startup type manually

## Related Docs
- [Services / Service Keys documentation](https://www.twingate.com/docs/services)
- [Twingate public changelog](https://www.twingate.com/changelog) (for latest installer download)