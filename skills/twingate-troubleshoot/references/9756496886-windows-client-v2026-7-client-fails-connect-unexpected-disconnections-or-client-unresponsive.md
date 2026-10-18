---
source: https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive
type: help
fetched: 2026-10-18
source_version: e282bb13f6ee5fb6e8b3a26e0b79980162e9758d8a2bec6ec36a5c67f0987a3c
trust: official
---

# [Windows Client] v2026.7 – Connection Failures & Unresponsive Client

## Summary
A known bug in Twingate Windows Client v2026.7 causes connection failures, unexpected disconnections, or an unresponsive client following network change events (power-on, reboot, sleep/wake). The root cause is a failure to detect DNS servers when a default route is absent at startup. The fix is to upgrade to v2026.36.

---

## Applicable To
- **Component:** Twingate Windows Client
- **Affected version:** 2026.7
- **Fixed version:** 2026.36

---

## Symptoms
- Login fails with "Could not join network"
- Connection toggle spins then returns to OFF
- Client disconnects shortly after connecting or cannot connect at all
- Stopping Twingate service via `services.msc` hangs in "Stopping" state
- Reboot does not recover the client

---

## Root Cause
Occurs when all three conditions are met:
1. Device is not connected to a network immediately after sign-in (no auto-connect)
2. DHCP has not yet assigned network configuration to the interface
3. No default route is present — client cannot identify a bypass interface

Client fails DNS detection → network initialization fails → service enters zombie state with no clean recovery path.

---

## Resolution

### Step 1 – Terminate stuck Twingate processes
1. System tray → **Twingate** → **Quit**
2. Open **Task Manager** → end all Twingate-related processes:
   - `Twingate.exe`
   - `Twingate.Service.exe`

### Step 2 – Upgrade to v2026.36
Download from the [Twingate Downloads page](https://www.twingate.com/download) or directly:
- **EXE installer** – for individual installs
- **MSI installer** – for managed/enterprise deployments

---

## Log Verification

**Log locations** (via System tray → Client → More → Troubleshoot → View Logs):
- `%PROGRAMDATA%\Twingate\logs\` → `C:\ProgramData\Twingate\logs\`
- `%LOCALAPPDATA%\Twingate\logs\` → `C:\Users\<user>\AppData\Local\Twingate\logs\`

**Check `Twingate.Service.log`** for repeating loop:
```
[INFO] [client] Start packet manager initialization.
[ERROR] [libsdwan] failed to initialize libhydra: code -1
```

**Check `system-events.log`** for:
- `System.AccessViolationException` in `Twingate.Service.exe` (crash at `PktDevice_WFPBlockTrafficOutsideTun`)
- Windows Error Reporting entry: `Event Name: APPCRASH`, `P2: 2026.7.2078.0`

---

## Gotchas
- Rebooting **does not** reliably recover the client — manual process termination is required before upgrading
- The service zombie state means `services.msc` stop command may hang indefinitely
- `system-events.log` is only created after clicking "View Logs" in the client UI

---

## Related Docs
- [Twingate Downloads Page](https://www.twingate.com/download)
- Twingate Client troubleshooting logs path: `Client → More → Troubleshoot → View Logs`