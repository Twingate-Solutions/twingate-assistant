---
source: https://help.twingate.com/articles/1639815268-windows-client-aws-workspaces-pools-terminates-20-minutes-after-starting-twingate
type: help
fetched: 2026-11-01
source_version: 0b97c83fe74adfbdcb20983ae301c6d4aa59bdffd6496e00e0cf37ff0ea2fa20
trust: official
---

# [Windows Client] AWS WorkSpaces Pools Terminates 20 Minutes After Starting Twingate

## Summary
AWS WorkSpaces Pool instances terminate ~20 minutes after launch because Twingate intercepts DNS queries for `squid-proxy.appstream.local`, preventing the WorkSpaces heartbeat/health check from resolving this hostname. The fix is to add static hosts file entries for the hostname so local resolution bypasses Twingate's DNS.

## Key Information
- **Affected component:** Twingate Windows Client on AWS WorkSpaces Pools
- **Root cause:** Twingate's DNS handling breaks split-horizon DNS on multi-NIC setups; queries for `squid-proxy.appstream.local` go to frontend DNS servers and are not forwarded to backend DNS servers (198.19.0.2)
- **Effect:** WorkSpaces heartbeat fails → AWS terminates the instance
- **Related KB:** `[Windows Client] Limitations with Multiple NICs and Split-Horizon DNS`

## Prerequisites
- Administrator access to the WorkSpaces instance
- Twingate **disconnected** when retrieving IPs via `nslookup`

## Troubleshooting / Diagnosis

**While NOT connected to Twingate:**
```powershell
nslookup squid-proxy.appstream.local
# Expected: returns one or more A record IPs — note all of them
```

**While connected to Twingate:**
```powershell
nslookup squid-proxy.appstream.local
# Expected: no A records returned — confirms the issue
```

## Workarounds

### Method 1 — Manual hosts file edit
1. Back up `C:\Windows\System32\drivers\etc\hosts`
2. While **disconnected** from Twingate, run `nslookup squid-proxy.appstream.local` and note all returned IPs
3. Open Notepad as Administrator → open `C:\Windows\System32\drivers\etc\hosts`
4. Add one line per IP at the bottom:
   ```
   <IP1> squid-proxy.appstream.local
   <IP2> squid-proxy.appstream.local
   ```
5. Save and close

### Method 2 — Scripted (PowerShell, run once)
Run while **NOT connected** to Twingate, as Administrator. Do **not** run if Method 1 was already applied.

```powershell
Copy-Item -Path "C:\Windows\System32\drivers\etc\hosts" -Destination "C:\Windows\System32\drivers\etc\hosts.bak" -Force
Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "`r`n" -Encoding ASCII
Resolve-DnsName squid-proxy.appstream.local |
  Where-Object QueryType -eq "A" |
  ForEach-Object { "{0} {1}" -f $_.IPAddress, "squid-proxy.appstream.local" } |
  Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Encoding ASCII
```

## Gotchas
- **Run Method 2 only once.** Running it multiple times creates duplicate entries; remove all `squid-proxy.appstream.local` lines manually before re-running
- IPs for `squid-proxy.appstream.local` **vary per environment** and **can change over time** — a dynamic update script (run when Twingate is not active) is the ideal long-term solution
- WorkSpaces Pool instances are **ephemeral** — apply this fix at image creation or via automation/startup script
- Do not mix Method 1 and Method 2 without cleaning up existing entries first

## Related Docs
- `[Windows Client] Limitations with Multiple NICs and Split-Horizon DNS`