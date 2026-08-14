---
source: https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive
type: help
fetched: 2026-08-14
source_version: 8d6d8cd227e46938df53f67bd285075f34b9c7cb5d6fd626196947c0c76658e0
---

# [Windows Client] v2026.7 Connection Failures & Unresponsiveness

## Summary
A known bug in Twingate Windows Client v2026.7 causes connection failures, unexpected disconnections, or an unresponsive client following network change events. The root cause is failure to detect DNS servers when a default route is absent at startup. The fix is included in v2026.36.

## Key Information
- **Affected version:** Windows Client v2026.7 only
- **Fix version:** v2026.36
- **Trigger:** Network change events (power on, reboot, sleep/wake) when network is not immediately available or DHCP hasn't assigned configuration yet

## Symptoms
- Login fails with "Could not join network"
- Connection toggle spins then returns to OFF
- Client disconnects shortly after connecting
- `services.msc` hangs in "Stopping" state when stopping Twingate service
- Rebooting does not recover the client

## Resolution Steps

### Upgrade to v2026.36
1. Download [EXE installer](https://www.twingate.com/downloads) or [MSI installer](https://www.twingate.com/downloads) (MSI for managed deployments)
2. If client is in faulted/zombie state, manually terminate before upgrading:
   - System tray → Twingate → **Quit**
   - Open Task Manager → end all Twingate processes:
     - `Twingate.exe`
     - `Twingate.Service.exe`
3. Proceed with installer

## Diagnostic Verification

### Log Locations
| Log File | Path |
|----------|------|
| Service log | `%PROGRAMDATA%\Twingate\logs\Twingate.Service.log` |
| System events | `%LOCALAPPDATA%\Twingate\logs\system-events.log` |

Access via: System tray → Twingate → Client → More → Troubleshoot → View Logs

### Confirm Bug in Service Log
Search `Twingate.Service.log` for this repeating loop:
```
[INFO] [client] Start packet manager initialization.
[ERROR] [libsdwan] failed to initialize libhydra: code -1
```

### Confirm Bug in System Events Log
Search `system-events.log` for **both**:

**Criteria 1:**
```
Application: Twingate.Service.exe
Exception Info: System.AccessViolationException
at .PktDevice_WFPBlockTrafficOutsideTun
```

**Criteria 2:**
```
Event Name: APPCRASH
P1: Twingate.Service.exe
P2: 2026.7.2078.0
```

## Gotchas
- Rebooting does **not** reliably recover the stuck service — manual process termination via Task Manager is required
- The service enters a zombie state; the upgrade cannot proceed without force-killing `Twingate.Service.exe`
- `system-events.log` is only created after clicking "View Logs" in the client UI

## Related Docs
- [Twingate Downloads Page](https://www.twingate.com/downloads)