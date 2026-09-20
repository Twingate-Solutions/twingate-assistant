---
source: https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive
type: help
fetched: 2026-09-20
source_version: 5c94cf13cfd9040481685ff67ed42ba9b3ff1fa393be2bac43678b8a5fb93ad3
---

# [Windows Client] v2026.7 Connection Failures & Unresponsive Client

## Summary
A known bug in Twingate Windows Client v2026.7 causes connection failures, unexpected disconnections, or a completely unresponsive client following network change events. The root cause is a failure to detect DNS servers when no default route exists at initialization time. The fix is available in v2026.36.

## Key Information
- **Affected version:** Windows Client v2026.7 only
- **Fix version:** v2026.36
- **Trigger:** Network change events (power on, reboot, sleep/wake) when network is not immediately available or DHCP hasn't assigned config yet
- **Core failure:** Client fails to identify bypass interface → DNS detection fails → initialization hangs or crashes → service enters zombie state

## Symptoms
- Login error: `Could not join network`
- Connection toggle spins then returns to OFF
- Client disconnects shortly after connecting or cannot connect at all
- Stopping Twingate service via `services.msc` hangs at "Stopping"
- Rebooting does not reliably recover the client

## Resolution Steps

1. **Quit the Twingate Client:** System tray → Twingate → Quit
2. **Kill remaining processes:** Task Manager → end `Twingate.exe` and `Twingate.Service.exe`
3. **Download and install v2026.36:**
   - [EXE Installer](https://help.twingate.com/articles/9756496886) (standard)
   - [MSI Installer](https://help.twingate.com/articles/9756496886) (managed deployments)

> **Note:** Manually terminating the service is required if the client has faulted — the service will be in a zombie state and block the installer.

## Log Confirmation

**Service log** (`%PROGRAMDATA%\Twingate\logs\Twingate.Service.log`):
```
[INFO] [client] Start packet manager initialization.
[ERROR] [libsdwan] failed to initialize libhydra: code -1
```
Look for this looping continuously.

**System events log** (`%LOCALAPPDATA%\Twingate\logs\system-events.log`):
- `.NET Runtime` error with `System.AccessViolationException` in `PktDevice_WFPBlockTrafficOutsideTun`
- `Windows Error Reporting` APPCRASH event with `P1: Twingate.Service.exe`, `P2: 2026.7.2078.0`

## Log File Locations
| Log | Path |
|-----|------|
| Service log | `C:\ProgramData\Twingate\logs\Twingate.Service.log` |
| System events | `C:\Users\<user>\AppData\Local\Twingate\logs\system-events.log` |

Access via: System tray → Twingate → Client → More → Troubleshoot → View Logs

## Gotchas
- Rebooting alone does **not** reliably fix the zombie service state
- The system events log is only created after clicking "View Logs" in the client UI
- MSI installer is required for managed/enterprise deployments

## Related Docs
- [Twingate Downloads Page](https://www.twingate.com/downloads)