---
source: https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive
type: help
fetched: 2026-08-16
source_version: f265e705524161302031dc3b8b5d374892785ba7dc5426ead1ee027d3dfa241c
---

# [Windows Client] v2026.7 Connection Failures & Unresponsive Client

## Summary
A known bug in Twingate Windows Client v2026.7 causes connection failures, unexpected disconnections, or an unresponsive client following network change events (power on, reboot, sleep/wake). The root cause is a failure to detect DNS servers when a network/DHCP/default route is not yet available at initialization. Fix is available in v2026.36.

## Key Information
- **Affected version**: Windows Client v2026.7 only
- **Fix version**: Windows Client v2026.36
- **Trigger**: Network change events (boot, reboot, sleep/wake) where network isn't immediately available
- **Root cause**: Client fails DNS detection when DHCP hasn't assigned config or no default route exists; can enter zombie/stuck state with no self-recovery

## Symptoms
- Login error: `Could not join network`
- Connection toggle spins then returns to OFF
- Client disconnects immediately after connecting
- `services.msc` stop hangs on "Stopping"
- Rebooting does not recover the client

## Resolution: Upgrade to v2026.36

### If client is functional:
Download and install v2026.36 directly:
- [EXE Installer](https://help.twingate.com/articles/9756496886) (consumer)
- [MSI Installer](https://help.twingate.com/articles/9756496886) (managed deployments)

### If client is in zombie/stuck state:
1. System tray → Twingate → **Quit**
2. Open Task Manager → end all Twingate processes:
   - `Twingate.exe`
   - `Twingate.Service.exe`
3. Proceed with v2026.36 installer

## Log Verification

**Log locations** (via System tray → Client → More → Troubleshoot → View Logs):
- `%PROGRAMDATA%\Twingate\logs\` (`C:\ProgramData\Twingate\logs`)
- `%LOCALAPPDATA%\Twingate\logs\`

**Check 1** — `Twingate.Service.log` for looping error:
```
[INFO] [client] Start packet manager initialization.
[ERROR] [libsdwan] failed to initialize libhydra: code -1
```

**Check 2** — `system-events.log` for crash signature:
```
Application: Twingate.Service.exe
Exception Info: System.AccessViolationException
at .PktDevice_WFPBlockTrafficOutsideTun(_PktDevice*, Boolean)
```

**Check 3** — `system-events.log` for Windows Error Reporting:
```
Event Name: APPCRASH
P1: Twingate.Service.exe
P2: 2026.7.2078.0
```

## Gotchas
- Rebooting alone does **not** reliably recover the client when in zombie state
- Must forcefully kill `Twingate.Service.exe` via Task Manager before upgrading if service is hung
- `system-events.log` is only created **after** clicking "View Logs" in the client UI

## Related Docs
- Twingate Downloads page (for latest client versions)
- Windows Client troubleshooting logs guide