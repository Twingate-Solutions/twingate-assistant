---
source: https://help.twingate.com/articles/1639815268-windows-client-aws-workspaces-pools-terminates-20-minutes-after-starting-twingate
type: help
fetched: 2026-11-08
source_version: b9cd1eb9a4d0e5a92f8ddd9722a34212ec98ccca2ef4d858bb2ae624da3f3a99
trust: official
---

# [Windows Client] AWS WorkSpaces Pools Terminates 20 Minutes After Starting Twingate

## Summary
AWS WorkSpaces Pool instances terminate ~20 minutes after launch when Twingate is running because Twingate intercepts DNS queries for `squid-proxy.appstream.local`, preventing the WorkSpaces heartbeat health check from resolving successfully. The fix is to add static hosts file entries for the hostname so local resolution bypasses Twingate's DNS.

## Key Information
- **Affected component**: Twingate Windows Client on AWS WorkSpaces Pools
- **Root cause**: Twingate's DNS handling breaks multi-NIC split-horizon DNS resolution (see related docs below)
- **Failing hostname**: `squid-proxy.appstream.local` — required for WorkSpaces heartbeat
- **Without Twingate**: backend NIC DNS (`198.19.0.2`) resolves the hostname successfully
- **With Twingate**: query goes to frontend DNS servers (`10.30.51.4`, `10.30.50.4`), gets no A record, backend DNS never queried → heartbeat fails → AWS terminates instance
- IPs for `squid-proxy.appstream.local` vary per environment and may change over time

## Prerequisites
- Administrator access on the WorkSpaces instance
- Ability to run commands/PowerShell before Twingate is connected

## Troubleshooting / Verification

**Confirm the issue:**
```powershell
# Run WITHOUT Twingate connected — should return A records
nslookup squid-proxy.appstream.local

# Run WITH Twingate connected — should return no A records
nslookup squid-proxy.appstream.local
```

## Workarounds

### Method 1 — Manual hosts file edit
1. Back up `C:\Windows\System32\drivers\etc\hosts`
2. Run `nslookup squid-proxy.appstream.local` **without** Twingate connected; note all returned IPs
3. Open Notepad as Administrator → open the hosts file
4. Add one line per IP at the bottom:
   ```
   <IP1> squid-proxy.appstream.local
   <IP2> squid-proxy.appstream.local
   ```
5. Save and close

### Method 2 — Scripted hosts file update (run once only, without Twingate connected)
Open PowerShell as Administrator and run the following script (backs up hosts file, then appends resolved IPs):

```powershell
Copy-Item -Path "C:\Windows\System32\drivers\etc\hosts" -Destination "C:\Windows\System32\drivers\etc\hosts.bak" -Force
Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "`r`n" -Encoding ASCII

Resolve-DnsName squid-proxy.appstream.local |
    Where-Object QueryType -eq "A" |
    ForEach-Object { "{0} {1}" -f $_.IPAddress, "squid-proxy.appstream.local" } |
    Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Encoding ASCII
```

## Gotchas
- **Run Method 2 only once** — running it multiple times creates duplicate entries; clean up manually if needed
- WorkSpaces Pool instances are **ephemeral** — apply the fix at image creation or via automation script
- The IPs for `squid-proxy.appstream.local` **are environment-specific and may change** — a dynamic script that updates hosts when Twingate is not running is the recommended long-term approach
- Do not mix Method 1 and Method 2 without manually removing existing `squid-proxy.appstream.local` entries first

## Related Docs
- [Windows Client] Limitations with Multiple NICs and Split-Horizon DNS