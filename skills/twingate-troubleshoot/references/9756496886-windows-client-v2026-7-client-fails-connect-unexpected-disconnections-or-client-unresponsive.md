---
source: https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive
type: help
fetched: 2026-08-06
source_version: 844a2db5263657c3c97cdbb20a132bf487ab274b154beed809f2e50b1712274d
---

# [Windows Client] v2026.7 – Connection Failures & Unresponsiveness

## Summary
A known bug in Twingate Windows Client v2026.7 causes connection failures, unexpected disconnections, or an unresponsive client following network change events (boot, reboot, sleep/wake). The root cause is a failure to detect DNS servers when no default route is present at initialization time. Fix is available in v2026.36.

## Key Information
- **Affected version:** Windows Client 2026.7 only
- **Fix version:** 2026.36
- **Trigger:** Network change events where DHCP/default route is not yet available at client initialization
- **Effect:** Client enters zombie/stuck state; rebooting does not always recover it

## Symptoms
- Login error: `Could not join network`
- Connection slider spins then returns to OFF
- Client disconnects immediately after connecting
- `services.msc` hangs on "Stopping" for Twingate service
- Reboot does not recover the client

## Resolution Steps

1. **Terminate the faulted service before upgrading:**
   - System tray → Twingate → **Quit**
   - Open Task Manager → end all Twingate processes: `Twingate.exe`, `Twingate.Service.exe`

2. **Download and install v2026.36:**
   - EXE installer (direct install)
   - MSI installer (managed/enterprise deployments)
   - Available at Twingate Downloads page

## Log Verification

**Location 1:** `C:\ProgramData\Twingate\logs\Twingate.Service.log`
- Look for looping pattern:
```
[INFO] [client] Start packet manager initialization.
[ERROR] [libsdwan] failed to initialize libhydra: code -1
```

**Location 2:** `C:\Users\<user>\AppData\Local\Twingate\logs\system-events.log`
- Search for `Twingate.Service.exe` + `.NET Runtime` error:
  - `System.AccessViolationException` at `PktDevice_WFPBlockTrafficOutsideTun`
- Search for `Twingate.Service.exe` + `Windows Error Reporting`:
  - `Event Name: APPCRASH`, `P2: 2026.7.2078.0`

**To open logs:** System tray → Twingate → Client → More → Troubleshoot → View Logs

## Gotchas
- Rebooting alone **does not** reliably recover the stuck state — manual process termination required before upgrade
- The service enters a zombie state; standard stop commands via `services.msc` will hang
- Both log files must be checked together to confirm the specific bug (not just generic crashes)
- `system-events.log` is only created after clicking "View Logs" in the client UI

## Related Docs
- Twingate Downloads page (for v2026.36 installer links)
- Windows Client troubleshooting documentation