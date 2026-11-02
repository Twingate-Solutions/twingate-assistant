---
source: https://help.twingate.com/articles/3992697531-client-connection-fails-with-unknown-network-name
type: help
fetched: 2026-11-01
source_version: c5a19d8f1e865a0e5ac897cccdf915d1533259904cbfea73e2df6a6a42c3f276
trust: official
---

# Client Connection Fails with "Unknown Network Name"

## Page Title
Client Connection Fails with "Unknown Network Name"

## Summary
The Twingate Windows client fails to connect and reports "Unknown network name" when antivirus or security software blocks or interferes with the TLS connection. The fix involves whitelisting the Twingate service in the AV solution and rebooting.

## Key Information
- **Component:** Twingate Client
- **Platform:** Windows only
- **Root Cause:** AV/security software (e.g., Elastic AV) intercepts and breaks TLS handshake to Twingate controller
- **Error codes:** `errorCode: 602`, `open_url timeout`

## Symptoms
- Client UI shows "Unknown network name"
- `Twingate.Service.log`: `failed to get an access token: open_url timeout` / `Auth failed errorCode: 602`
- `twingate.log`: `Could not create SSL/TLS secure channel` when validating `https://<tenant>.twingate.com/`

## Step-by-Step Diagnosis

1. **Verify Twingate service is running** via Windows Services or Task Manager
2. **Check Windows Event Logs** for relevant errors (often none present)
3. **Test TLS connectivity** using PowerShell (.NET Framework, same stack as Twingate client):
   ```powershell
   invoke-webrequest -UseBasicParsing -uri "https://<tenant>.twingate.com" | Select-Object StatusCode
   ```
   - **Success:** Returns `200`
   - **Failure indicator:** `Could not create SSL/TLS secure channel` → TLS is being blocked by local software

4. **Check for conflicting software** (DNS, VPN, remote access, AV) against Twingate's Known Incompatibility list

## Resolution
- **Whitelist** the Twingate service executable in the antivirus solution (e.g., Elastic AV)
- **Disable** Windows Defender if it is conflicting
- **Reboot** the system after making changes

## Gotchas
- No errors may appear in Windows Event Logs despite the connection failing — don't rely on Event Viewer to confirm or deny the issue
- The PowerShell `invoke-webrequest` test is specifically useful because it uses .NET Framework, the same stack Twingate's Windows client uses
- Issue is Windows-specific; this TLS interference pattern does not apply to other platforms

## Log File Locations
| Log | Path (typical) |
|-----|---------------|
| `Twingate.Service.log` | Windows service log |
| `twingate.log` | Client application log |

## Related Docs
- [Known Incompatibility Overview](https://help.twingate.com) — full list of software known to conflict with Twingate