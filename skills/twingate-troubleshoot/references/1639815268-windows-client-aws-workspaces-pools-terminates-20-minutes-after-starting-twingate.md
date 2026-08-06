---
source: https://help.twingate.com/articles/1639815268-windows-client-aws-workspaces-pools-terminates-20-minutes-after-starting-twingate
type: help
fetched: 2026-08-06
source_version: f46faf5c7ac30a03e123da16ea49ec7bc7e7c92bb43812e0dcf65af39a7d7e4f
---

# [Windows Client] AWS WorkSpaces Pools Terminates 20 Minutes After Starting Twingate

## Summary
AWS WorkSpaces Pool instances terminate ~20 minutes after launch because Twingate intercepts DNS queries for `squid-proxy.appstream.local`, preventing the WorkSpaces health check from resolving this hostname. The fix is to add static hosts file entries so the hostname resolves locally regardless of Twingate's DNS handling.

## Key Information
- **Affected component:** Twingate Windows Client on AWS WorkSpaces Pools
- **Root cause:** Multi-NIC split-horizon DNS limitation — Twingate forwards DNS to frontend NICs only, skipping backend NIC DNS servers that resolve `squid-proxy.appstream.local`
- **Effect:** WorkSpaces heartbeat fails → AWS terminates the instance
- **IPs for `squid-proxy.appstream.local` vary per environment and may change over time**
- WorkSpaces Pool instances are ephemeral; fix must be applied at image creation or via automation

## Prerequisites
- Administrator access on the WorkSpaces instance
- Must perform `nslookup` **before** connecting Twingate to capture correct IPs
- Related: [Windows Client] Limitations with Multiple NICs and Split-Horizon DNS

## Troubleshooting / Diagnosis
```powershell
# Without Twingate connected — should return IPs:
nslookup squid-proxy.appstream.local

# With Twingate connected — should return nothing (confirms issue):
nslookup squid-proxy.appstream.local
```

## Workaround: Method 1 — Manual Hosts File Update
1. Back up `C:\Windows\System32\drivers\etc\hosts`
2. Run `nslookup squid-proxy.appstream.local` **without** Twingate connected; record all returned IPs
3. Open Notepad as Administrator → open `C:\Windows\System32\drivers\etc\hosts`
4. Add one line per IP at the bottom:
   ```
   <IP1> squid-proxy.appstream.local
   <IP2> squid-proxy.appstream.local
   ```
5. Save and close

## Workaround: Method 2 — Scripted Update (Run Once, Without Twingate Connected)
Open PowerShell as Administrator and run:
```powershell
Copy-Item -Path "C:\Windows\System32\drivers\etc\hosts" -Destination "C:\Windows\System32\drivers\etc\hosts.bak" -Force
Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "`r`n" -Encoding ASCII
Resolve-DnsName squid-proxy.appstream.local |
  Where-Object QueryType -eq "A" |
  ForEach-Object { "{0} {1}" -f $_.IPAddress, "squid-proxy.appstream.local" } |
  Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Encoding ASCII
```

## Gotchas
- **Method 2 must only run once** — running multiple times creates duplicate entries; remove all `squid-proxy.appstream.local` lines manually if this occurs
- IPs are **environment-specific** and **subject to change** — a dynamic script triggered when Twingate is not running is the recommended long-term approach
- Must capture IPs **before** connecting Twingate; resolution fails after connection
- Apply fix at **image creation time** due to ephemeral nature of WorkSpaces Pools

## Related Docs
- [Windows Client] Limitations with Multiple NICs and Split-Horizon DNS