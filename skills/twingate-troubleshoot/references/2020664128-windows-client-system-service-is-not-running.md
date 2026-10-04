---
source: https://help.twingate.com/articles/2020664128-windows-client-system-service-is-not-running
type: help
fetched: 2026-10-04
source_version: 5130b3dcb6658857ccc139a1dfb3c7fb35320f388388f5bdec92e6711eb9ddd7
trust: official
---

# [Windows Client] System Service Is Not Running

## Summary
The Twingate Windows Client requires the **Twingate Windows Service** to be running to establish connectivity. If the service is stopped or missing, the client will display a "system service is not running" error and fail to connect.

## Key Information
- Affects: Twingate Client on Windows platform
- The Windows service component is a hard dependency for client connectivity
- Service must be both **running** and set to **Automatic** startup

## Symptoms
- Client fails to connect
- Popup error: *"The Twingate system service is not running. To connect, restart the Twingate system service or contact your admin."*

## Troubleshooting Steps

1. Open Run dialog: **Windows Key + R**
2. Type `services.msc` → press **Enter**
3. Scroll to **Twingate Service** in the list
4. Check service status:

| Status | Action |
|--------|--------|
| Not running / null | Follow Resolution steps below |
| Running + Automatic | Restart service → restart client → retry connection |
| Fails to start | Check TAP adapter (see Gotchas) → collect logs → contact support |

## Resolution: Start & Configure Service

1. Open **Run** (`Windows Key + R`) → type `services.msc` → **Enter**
2. Scroll to **Twingate Service rc**
3. Right-click → **Start**
4. Right-click → **Properties** → set **Startup Type** to `Automatic`
5. Restart the Twingate Client application and attempt reconnection

## Gotchas
- If the service fails to start, verify the **Twingate TAP network adapter** is present and not disabled in Device Manager
- A running service that is *not* set to Automatic will cause recurrence after reboot
- If TAP adapter check passes but service still won't start, collect [detailed logs](https://help.twingate.com) and open a support ticket — do not attempt further manual fixes

## Prerequisites
- Windows OS with Twingate Client installed
- Admin rights to access `services.msc` and modify service properties

## Related Docs
- Twingate detailed log collection guide
- Twingate TAP adapter troubleshooting