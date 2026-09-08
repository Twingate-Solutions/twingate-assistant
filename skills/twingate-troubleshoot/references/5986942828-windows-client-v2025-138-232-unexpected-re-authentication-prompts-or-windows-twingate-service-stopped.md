---
source: https://help.twingate.com/articles/5986942828-windows-client-v2025-138-232-unexpected-re-authentication-prompts-or-windows-twingate-service-stopped
type: help
fetched: 2026-09-06
source_version: 8ea64dcc8081fa8ee1980ccdf58af6780c1e07f6ccf0480662873972101b23d1
---

# [Windows Client] Unexpected Re-authentication / Service Crash (v2025.138–232)

## Summary
A bug in Twingate Windows Client versions 2025.138 through 2025.232 causes `Twingate.Service.exe` to crash due to an unhandled `System.AccessViolationException`, most commonly when the device wakes from sleep. The fix is to upgrade to v2025.289 or later.

## Key Information
- **Affected versions:** 2025.138 through 2025.232
- **Affected component:** Twingate Windows Client (`Twingate.Service.exe`)
- **Root cause:** Unhandled `System.AccessViolationException` in the .NET runtime process
- **Most common trigger:** Device waking from sleep state
- **Resolution:** Upgrade to v2025.289+

## Prerequisites
- Windows OS with Twingate Client installed in affected version range

## Symptoms
- Unexpected re-authentication prompts (before security policy expiry)
- Client shows disconnected and cannot connect to Resources
- Twingate Windows Service stopped and will not restart (Windows suppresses restart after repeated crashes)

## Confirming the Issue (Log Check)

1. Click Twingate Client in the system tray
2. Navigate to **Client > More > Troubleshoot > View Logs**
3. Open the `logs` folder in the Twingate directory
4. Full path: `%USERPROFILE%\AppData\Local\Twingate\logs`
5. Open `system-events.log`
6. Search for a `[Error] .NET Runtime` entry matching:
   - `Application: Twingate.Service.exe`
   - Exception: `System.AccessViolationException: Attempted to read or write protected memory`

## Resolution
Upgrade to **v2025.289 or later**:
- **EXE installer** – for direct/manual installs
- **MSI installer** – for managed device deployments

## Gotchas
- Windows may permanently stop the service after multiple crashes and not restart it automatically — manual upgrade is required
- Re-authentication prompts in this case are **not** caused by expired security policy; they are a symptom of the service crash

## Related Docs
- Twingate Windows Client release notes
- Twingate Client troubleshooting / log collection