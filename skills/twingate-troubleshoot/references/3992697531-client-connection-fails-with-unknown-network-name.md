---
source: https://help.twingate.com/articles/3992697531-client-connection-fails-with-unknown-network-name
type: help
fetched: 2026-09-06
source_version: ded57806490b812805d986f2e6b47b27b4a38a0b1cd0715ab9205ded9bb5e258
---

# Client Connection Fails with "Unknown Network Name"

## Summary
Windows Twingate client fails to connect with "Unknown network name" error when antivirus/security software interferes with TLS connections. The root cause is SSL/TLS session termination by third-party security software (e.g., Elastic AV). Whitelisting the Twingate service in the AV solution resolves the issue.

## Key Information
- **Component**: Twingate Client (Windows only)
- **Error**: "Unknown network name" in client UI
- **Root cause**: Antivirus/security software blocking TLS handshake to Twingate controller

## Symptoms
- Client UI reports "Unknown network name"
- `Twingate.Service.log` shows: `[ERROR] failed to get an access token: open_url timeout` / `Auth failed. errorCode: 602`
- `twingate.log` shows: `HttpRequestException: Could not create SSL/TLS secure channel`
- No relevant errors in Windows Event Logs

## Diagnostic Steps

1. **Verify Twingate service is running** via Services console or Task Manager

2. **Test TLS connectivity via PowerShell** (uses .NET Framework, same as Twingate client):
   ```powershell
   invoke-webrequest -UseBasicParsing -uri "https://<network>.twingate.com" | Select-Object StatusCode
   ```
   - Expected: HTTP status code (e.g., `200`)
   - Failure indicator: `Could not create SSL/TLS secure channel` → confirms TLS is being blocked

3. **Check for conflicting software**: Review antivirus, DNS filtering, or remote access tools against the Known Incompatibility Overview

## Resolution
1. Whitelist the Twingate service in your antivirus solution (e.g., Elastic AV)
2. Disable Windows Defender if applicable
3. Reboot the system

## Log File Locations
| Log | Key Errors |
|-----|-----------|
| `Twingate.Service.log` | `open_url timeout`, errorCode 602 |
| `twingate.log` | SSL/TLS channel failure |

## Gotchas
- Windows Event Logs will **not** show relevant errors — check Twingate-specific logs instead
- The PowerShell test is specifically meaningful because it uses .NET Framework, matching the Twingate client's network stack
- Issue is AV-specific; not a Twingate configuration problem

## Related Docs
- Known Incompatibility Overview (Twingate help center)