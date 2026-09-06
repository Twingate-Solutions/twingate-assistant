---
source: https://help.twingate.com/articles/1639815268-windows-client-aws-workspaces-pools-terminates-20-minutes-after-starting-twingate
type: help
fetched: 2026-09-06
source_version: 362205458f860164bd9e362e6a0a5d29eb966b2c7d9a9952fa82cdd0881583aa
---

# [Windows Client] AWS WorkSpaces Pools Terminates 20 Minutes After Starting Twingate

## Summary
AWS WorkSpaces Pool instances terminate ~20 minutes after launch because Twingate intercepts DNS queries for `squid-proxy.appstream.local`, preventing the WorkSpaces heartbeat health check from resolving the hostname. The fix is to hardcode the correct IPs in the Windows hosts file.

## Key Information
- **Root cause**: Twingate's DNS handling breaks multi-NIC split-horizon DNS resolution; queries never reach the backend NIC's DNS servers (198.19.0.2)
- **Affected hostname**: `squid-proxy.appstream.local`
- **Symptom**: Instance terminates ~20 minutes after Twingate connects
- **IPs for this hostname vary per AWS environment and may change over time**
- WorkSpaces Pool instances are ephemeral — fix must be applied at image creation or via automation

## Prerequisites
- Administrator access to the WorkSpaces Pool instance
- Ability to modify `C:\Windows\System32\drivers\etc\hosts`
- Must retrieve IPs **while Twingate is disconnected**

## Troubleshooting / Diagnosis
```powershell
# While NOT connected to Twingate (should return IPs):
nslookup squid-proxy.appstream.local

# While connected to Twingate (should return nothing — confirms issue):
nslookup squid-proxy.appstream.local
```

## Workarounds

### Method 1 — Manual hosts file edit
1. Back up `C:\Windows\System32\drivers\etc\hosts`
2. Run `nslookup squid-proxy.appstream.local` while **disconnected** from Twingate; record all returned IPs
3. Open Notepad as Administrator → open the hosts file
4. Add one line per IP at the bottom:
   ```
   <IP1> squid-proxy.appstream.local
   <IP2> squid-proxy.appstream.local
   ```
5. Save and close

### Method 2 — PowerShell script (run once, while disconnected from Twingate)
```powershell
Copy-Item -Path "C:\Windows\System32\drivers\etc\hosts" -Destination "C:\Windows\System32\drivers\etc\hosts.bak" -Force
Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "`r`n" -Encoding ASCII
Resolve-DnsName squid-proxy.appstream.local |
  Where-Object QueryType -eq "A" |
  ForEach-Object { "{0} {1}" -f $_.IPAddress, "squid-proxy.appstream.local" } |
  Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Encoding ASCII
```

## Gotchas
- **Run Method 2 only once** — re-running creates duplicate entries; manually remove all `squid-proxy.appstream.local` lines before re-running
- **Do not run while connected to Twingate** — DNS lookup will fail, adding no entries
- IPs for `squid-proxy.appstream.local` differ per AWS environment and can change; a dynamic script triggered when Twingate is not running is the ideal long-term solution
- Apply fix during image creation for ephemeral WorkSpaces Pool instances

## Related Docs
- [[Windows Client] Limitations with Multiple NICs and Split-Horizon DNS](https://help.twingate.com)