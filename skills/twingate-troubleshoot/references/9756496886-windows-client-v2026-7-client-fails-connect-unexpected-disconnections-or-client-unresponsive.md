---
source: https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive
type: help
fetched: 2026-08-09
source_version: 503dbfa878d1f2a157f4d55e4f5cc0d7044e6604334866ba078126767bd1db15
---

# [Windows Client] v2026.7 Connection Failures & Unresponsiveness

## Page Title
Windows Client v2026.7 | Client Fails to Connect, Unexpected Disconnections, or Client Unresponsive

## Summary
A known bug in Twingate Windows Client v2026.7 causes connection failures, unexpected disconnections, or a completely unresponsive client after network change events. The root cause is a failure to detect DNS servers when no default route exists at startup. The fix is to upgrade to v2026.36.

## Key Information
- **Affected version:** 2026.7 only
- **Platform:** Windows
- **Fix version:** 2026.36
- **Trigger events:** Device power-on, reboot, or sleep/wake when network is not immediately available
- **Root cause:** Client cannot identify bypass interface when DHCP hasn't assigned config yet; initialization fails and can get permanently stuck

## Symptoms
- "Could not join network" login error
- Connection slider spins then returns to OFF
- Client disconnects shortly after connecting
- `services.msc` hangs on "Stopping" when stopping Twingate service
- Rebooting does not recover the client

## Resolution: Upgrade to v2026.36

### If client is in faulted/zombie state (pre-upgrade steps required):
1. **Quit client:** System tray → Twingate → Quit
2. **Kill remaining processes:** Task Manager → end `Twingate.exe` and `Twingate.Service.exe`
3. **Install upgrade:** Download and run installer

### Download Links
- [EXE Installer](https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive) (standard)
- [MSI Installer](https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive) (managed deployments)

## Log Verification

### Log Locations
| Log | Path |
|-----|------|
| Service log | `C:\ProgramData\Twingate\logs\Twingate.Service.log` |
| System events | `C:\Users\<user>\AppData\Local\Twingate\logs\system-events.log` |

**Access via:** System tray → Twingate Client → More → Troubleshoot → View Logs

### Confirming the Bug via Logs

**In `Twingate.Service.log`** — look for repeating loop:
```
[INFO] [client] Start packet manager initialization.
[ERROR] [libsdwan] failed to initialize libhydra: code -1
```

**In `system-events.log`** — look for both:
1. `System.AccessViolationException` crash in `Twingate.Service.exe` at `PktDevice_WFPBlockTrafficOutsideTun`
2. Windows Error Reporting `APPCRASH` with `P1: Twingate.Service.exe`, `P2: 2026.7.2078.0`

## Gotchas
- Rebooting **does not reliably recover** the client — manual process termination required before upgrade
- The service enters a zombie state; standard stop via `services.msc` will hang
- Issue only triggers under specific timing: sign-in before network/DHCP is ready

## Related Docs
- Twingate Downloads page (for latest releases)
- Twingate Windows Client release notes