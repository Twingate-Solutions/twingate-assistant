---
source: https://help.twingate.com/articles/9756496886-windows-client-v2026-7-client-fails-connect-unexpected-disconnections-or-client-unresponsive
type: help
fetched: 2026-11-15
source_version: 3c72d9a9684000a2042576964990c975e1d2cefa969df8a65b14f427c4ddc6d1
trust: official
---

# Page Title
[Windows Client] v2026.7 | Client Fails Connect, Unexpected Disconnections, or Client Unresponsive

## Summary
Twingate Windows Client version 2026.7 has a known issue where the client can become unresponsive, fail to connect, or disconnect unexpectedly after a network change event. The fix is included in Windows Client 2026.36. Upgrading may require manually terminating the stuck Twingate service.

## Key Information
- Applies to: Twingate Client 2026.7, Windows.
- Triggers: device power on, reboot, or sleep/wake (network change events).
- Symptoms:
  - Login fails with `Could not join network`.
  - Connection toggle spins, then returns to OFF.
  - Client disconnects shortly after connecting, or cannot connect.
  - Stopping the service in `services.msc` hangs at "Stopping".
  - Reboot doesn't always recover the client or service.
- Cause (edge case): no network right after sign-in (e.g., not set to auto-connect), DHCP hasn't yet assigned configuration, and no default route is present, so the client can't identify a bypass interface. DNS server detection fails and network initialization fails. The client can remain stuck even after connectivity returns.
- Resolution: upgrade to Windows Client **2026.36**. EXE installer is available, and MSI is available for managed device deployments. Both are on the Twingate Downloads page.

## Prerequisites
- Permission to install software and end processes on the affected Windows device.
- Installer (EXE or MSI) for 2026.36.

## Step-by-Step (Upgrade)
1. If the client has faulted, quit it: system tray > Twingate > Quit.
2. Open Task Manager and end remaining Twingate processes (`Twingate.exe`, `Twingate.Service.exe`).
3. Run the 2026.36 installer (EXE, or MSI for managed deployments).

## Confirming the Issue (Logs)
Open logs via Client > More > Troubleshoot > View Logs. This opens two folders:
- `%PROGRAMDATA%\Twingate\logs\` (`C:\ProgramData\Twingate\logs`)
- `%LOCALAPPDATA%\Twingate\logs\`

Checks:
- In `Twingate.Service.log`, search for `failed to initialize libhydra: code -1` after packet manager initialization. In a bad state it loops continuously.
- In `system-events.log` (created after clicking View Logs), search for:
  - `.NET Runtime` error for `Twingate.Service.exe` with `System.AccessViolationException` and a stack containing `PktDevice_WFPBlockTrafficOutsideTun`.
  - `Windows Error Reporting` APPCRASH entry with `P1: Twingate.Service.exe`, `P2: 2026.7.2078.0`.

## Configuration Values
- Process names: `Twingate.exe`, `Twingate.Service.exe`
- Log paths: `%PROGRAMDATA%\Twingate\logs\Twingate.Service.log`, `%LOCALAPPDATA%\Twingate\logs\system-events.log`
- Fixed version: 2026.36; affected: 2026.7

## Gotchas
- The service may be in a zombie state, so the upgrade can fail until Twingate processes are manually terminated.
- Rebooting is not a reliable fix.
- Stopping the service via `services.msc` may hang.
- Log evidence is most meaningful on version 2026.7 alongside the symptoms.

## Related Docs
- Twingate Downloads page (latest Windows Client releases)
- Twingate Client log/troubleshooting documentation (View Logs)