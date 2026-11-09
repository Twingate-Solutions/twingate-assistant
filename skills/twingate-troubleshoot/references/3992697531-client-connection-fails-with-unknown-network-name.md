---
source: https://help.twingate.com/articles/3992697531-client-connection-fails-with-unknown-network-name
type: help
fetched: 2026-11-08
source_version: a41acee06c145b0fead1413970cf8bc96cb93652ab29940d138ccdc4c16b74cb
trust: official
---

# Client Connection Fails with "Unknown Network Name"

## Page Title
Client connection fails with "Unknown network name"

## Summary
Windows Twingate clients may fail to connect with an "Unknown network name" error when antivirus or security software interferes with the TLS handshake. The root cause is a broken SSL/TLS channel between the client and the Twingate controller. Whitelisting Twingate in the AV solution resolves the issue.

## Key Information
- **Affected component:** Twingate Client (Windows only)
- **Known trigger:** Elastic AV (and potentially other AV/security tools)
- **Core failure:** AV intercepts/blocks TLS session to `<network>.twingate.com`
- **Error codes:** `errorCode: 602`, `open_url timeout`

## Prerequisites
- Access to Windows PowerShell
- Admin rights to modify antivirus whitelist/exclusions
- Access to Twingate log files

## Log File Signatures

**`Twingate.Service.log`:**
```
[ERROR] [SDWAN] controller_t::operator (): failed to get an access token: open_url timeout
[ERROR] ConnectionManager Auth failed. errorCode: 602, errorMessage: open_url timeout
```

**`twingate.log`:**
```
[ERROR] ControllerServerValidator.ValidateAsync Failed to validate controller url
System.Net.WebException: The request was aborted: Could not create SSL/TLS secure channel.
```

## Diagnostic Steps

1. Confirm Twingate service is running in Windows Services.
2. Test TLS connectivity via PowerShell (.NET Framework, same stack the client uses):
   ```powershell
   invoke-webrequest -UseBasicParsing -uri "https://<network>.twingate.com" | Select-Object StatusCode
   ```
3. If result is `Could not create SSL/TLS secure channel` error (not a status code), TLS is being blocked.
4. Check Windows Event Logs for related errors (typically none in this scenario).
5. Review installed security/AV/DNS/remote-access software against Twingate's Known Incompatibility list.

## Resolution

1. Add the Twingate service executable to the **AV whitelist/exclusions** (e.g., Elastic AV).
2. Disable Windows Defender if it is also active and conflicting.
3. **Reboot** the system.
4. Re-run the PowerShell test to confirm TLS succeeds before retesting the client.

## Configuration Values
| Item | Value |
|------|-------|
| Test URL pattern | `https://<network>.twingate.com` |
| Error code | `602` |

## Gotchas
- Windows Event Logs may show **no relevant errors** — absence of event log entries does not rule out AV interference.
- The PowerShell `invoke-webrequest` test is specifically useful because it uses .NET Framework, matching the client's network stack.
- Multiple security tools may interact (e.g., both Elastic AV and Windows Defender active simultaneously).

## Related Docs
- [Twingate Known Incompatibility Overview](https://help.twingate.com) — covers other AV/security software conflicts