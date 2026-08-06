---
source: https://help.twingate.com/articles/5986942828-windows-client-v2025-138-232-unexpected-re-authentication-prompts-or-windows-twingate-service-stopped
type: help
fetched: 2026-08-06
source_version: 59d4bd3e4c635429497879b704d49d9fb990a47ba56b7a3b6cad9c7569e55fa3
---

# [Windows Client] Unexpected Re-authentication / Service Crash (v2025.138–232)

## Summary
Twingate Windows Client versions 2025.138 through 2025.232 contain a bug where `Twingate.Service.exe` crashes due to an unhandled `System.AccessViolationException`, most commonly triggered when a device wakes from sleep. This causes unexpected re-authentication prompts or complete loss of connectivity.

## Key Information
- **Affected versions:** 2025.138 through 2025.232
- **Platform:** Windows only
- **Root cause:** Unhandled `System.AccessViolationException` in `Twingate.Service.exe` (.NET Runtime crash)
- **Trigger:** Most frequently occurs when device resumes from sleep
- **Fix version:** 2025.289 or later

## Symptoms
- Unexpected re-authentication prompts (security policy re-auth interval not expired)
- Client shows disconnected; cannot connect to Resources
- Twingate Windows Service stopped and will not restart (Windows suppresses restart after repeated crashes)

## Diagnosis Steps
1. Click Twingate icon in system tray
2. Navigate to **Client > More > Troubleshoot > View Logs**
3. Open File Explorer path: `%USERPROFILE%\AppData\Local\Twingate\logs`
4. Open `system-events.log`
5. Search for `[Error] .NET Runtime` entry where:
   - `Application: Twingate.Service.exe`
   - Exception contains `System.AccessViolationException: Attempted to read or write protected memory`

## Resolution
Upgrade to **v2025.289** or later.

| Deployment Method | Download |
|---|---|
| EXE (direct install) | Download Installer (EXE) |
| MSI (managed/enterprise) | Download Installer (MSI) |

## Gotchas
- Windows may permanently stop the service after multiple crashes and **not restart it automatically** — manual intervention or upgrade required
- Re-authentication prompt does not mean session/policy expired; it's a symptom of the service crash
- No workaround short of upgrading; restarting the service provides only temporary relief if the device continues sleeping

## Related Docs
- Twingate Windows Client release notes
- Twingate Client troubleshooting / log access