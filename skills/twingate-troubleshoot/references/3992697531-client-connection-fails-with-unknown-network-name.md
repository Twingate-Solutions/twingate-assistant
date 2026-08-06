---
source: https://help.twingate.com/articles/3992697531-client-connection-fails-with-unknown-network-name
type: help
fetched: 2026-08-06
source_version: c6144bef17bd94679abf36a965b16d13080fbc95ada9251d6db410dc230c6543
---

# Client Connection Fails with "Unknown Network Name"

## Summary
Twingate Windows client fails to connect and reports "Unknown network name" due to antivirus/security software interfering with TLS connections. The issue manifests as SSL/TLS channel creation failures when the client attempts to reach the Twingate controller URL.

## Key Information
- **Component**: Twingate Client (Windows only)
- **Root cause**: AV/security software (e.g., Elastic AV) blocks or intercepts TLS sessions
- **Error code**: 602 (`open_url timeout`)
- **Log files involved**: `Twingate.Service.log` and `twingate.log`

## Symptoms
- Client UI shows "Unknown network name"
- `Twingate.Service.log` error: `failed to get an access token: open_url timeout`, errorCode 602
- `twingate.log` error: `Could not create SSL/TLS secure channel` when validating controller URL

## Diagnostic Steps

1. Verify Twingate service is running in Windows Services
2. Test TLS connectivity using PowerShell (.NET Framework, same stack as Twingate client):
   ```powershell
   invoke-webrequest -UseBasicParsing -uri "https://<tenant>.twingate.com" | Select-Object StatusCode
   ```
3. If output is `Could not create SSL/TLS secure channel` error (not a status code), TLS is being blocked
4. Check Windows Event Logs (no relevant errors expected in this scenario)
5. Review installed security/DNS/remote access software against Known Incompatibility list

## Resolution
1. Whitelist the Twingate service in your antivirus solution (e.g., Elastic AV)
2. Disable Windows Defender if applicable
3. Reboot the system

## Gotchas
- No errors appear in Windows Event Logs, making this harder to diagnose without checking Twingate-specific logs
- The PowerShell `invoke-webrequest` test is meaningful because it uses .NET Framework, the same underlying stack as the Twingate Windows client — browser tests may succeed while Twingate still fails
- Other security software (DNS filters, remote access tools) can cause the same symptoms

## Related Docs
- [Known Incompatibility Overview](https://help.twingate.com/articles/known-incompatibility-overview)