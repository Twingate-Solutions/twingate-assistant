---
source: https://help.twingate.com/articles/3992697531-client-connection-fails-with-unknown-network-name
type: help
fetched: 2026-10-04
source_version: 1c68b64dc0acc6cc2bb7b61deda6b2f4b7f636738e165336239b87ca66c69a6d
trust: official
---

# Client Connection Fails with "Unknown Network Name"

## Page Title
Client connection fails with "Unknown network name"

## Summary
Windows Twingate clients may fail to connect and report "Unknown network name" when antivirus or security software (e.g., Elastic AV) interferes with the TLS connection to the Twingate controller. The root cause is SSL/TLS session interruption by a third-party security tool. Whitelisting the Twingate service in the AV solution resolves the issue.

## Applicable To
- **Component:** Twingate Client
- **Platform:** Windows
- **Related software:** Antivirus solutions (documented case: Elastic AV)

## Key Information
- Error code `602` with message `open_url timeout` appears in `Twingate.Service.log`
- `twingate.log` shows `Could not create SSL/TLS secure channel` on controller URL validation
- Twingate Windows Client uses **.NET Framework** for HTTP connections
- No relevant errors typically appear in Windows Event Logs

## Symptoms
- Client fails to connect with "Unknown network name"
- `Twingate.Service.log`: `[ERROR] ConnectionManager Auth failed. errorCode: 602, errorMessage: open_url timeout`
- `twingate.log`: `HttpRequestException` → `Could not create SSL/TLS secure channel`

## Troubleshooting Steps

1. **Verify Twingate service is running** on the Windows host.

2. **Test TLS connectivity via PowerShell** (uses .NET Framework, same as Twingate client):
   ```powershell
   invoke-webrequest -UseBasicParsing -uri "https://<network>.twingate.com" | Select-Object StatusCode
   ```
   - **Expected:** HTTP status code (e.g., `200`)
   - **Failure indicator:** `Could not create SSL/TLS secure channel` — confirms TLS is being blocked

3. **Check for known incompatible software** (AV, DNS, remote access tools) — see Related Docs.

## Resolution
- **Whitelist the Twingate service** in your antivirus solution (e.g., Elastic AV)
- **Disable Windows Defender** (if applicable) and **reboot** the system
- Confirm connectivity with the PowerShell test command above after changes

## Gotchas
- Windows Event Logs will appear clean — do not rely on them for diagnosis
- The PowerShell `invoke-webrequest` test is critical because it uses the same .NET Framework stack as the Twingate client, making it an accurate proxy test
- Disabling AV temporarily to confirm the cause before whitelisting is a useful diagnostic step

## Log File Locations
| Log | Relevant Error |
|-----|---------------|
| `Twingate.Service.log` | `errorCode: 602, open_url timeout` |
| `twingate.log` | `Could not create SSL/TLS secure channel` |

## Related Docs
- [Known Incompatibility Overview](https://help.twingate.com) — check for full list of conflicting security/DNS/remote access software