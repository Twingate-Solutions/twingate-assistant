---
source: https://help.twingate.com/articles/1639815268-windows-client-aws-workspaces-pools-terminates-20-minutes-after-starting-twingate
type: help
fetched: 2026-10-04
source_version: 3a0de3cbba78149c712b43ee6afe4e04222ced5757851585af9c4edbf69c60d9
trust: official
---

# [Windows Client] AWS WorkSpaces Pools Terminates 20 Minutes After Starting Twingate

## Summary
AWS WorkSpaces Pool instances terminate ~20 minutes after launch because Twingate's DNS handling prevents resolution of `squid-proxy.appstream.local`, causing WorkSpaces heartbeat checks to fail. This is a known limitation with Twingate and multiple NICs/split-horizon DNS environments.

## Key Information
- **Affected component:** Twingate Windows Client on AWS WorkSpaces Pools
- **Root cause:** Twingate forwards DNS queries to frontend NIC DNS servers only; backend NIC DNS servers (which resolve `squid-proxy.appstream.local`) are bypassed
- **Effect:** WorkSpaces heartbeat fails → AWS terminates the instance
- **Workaround:** Add static hosts file entries for `squid-proxy.appstream.local`
- **IPs vary per environment** and may change over time — dynamic update approach recommended

## Prerequisites
- Administrator access on the WorkSpaces instance
- Access to run `nslookup` and PowerShell/Notepad as Administrator
- Must retrieve IPs **before** connecting to Twingate

## Troubleshooting / Diagnosis
1. **While NOT connected to Twingate:** `nslookup squid-proxy.appstream.local` → should return A records
2. **While connected to Twingate:** Same command → should return no A records (confirms the issue)

## Step-by-Step Workarounds

### Method 1 — Manual hosts file edit
1. Backup `C:\Windows\System32\drivers\etc\hosts`
2. Run `nslookup squid-proxy.appstream.local` while **disconnected** from Twingate; note all returned IPs
3. Open Notepad as Administrator → open `C:\Windows\System32\drivers\etc\hosts`
4. Add one line per IP at bottom: `<IP> squid-proxy.appstream.local`
5. Save and close

### Method 2 — PowerShell script (run once, while NOT connected to Twingate)
Run the following in PowerShell as Administrator:
```powershell
Copy-Item -Path "C:\Windows\System32\drivers\etc\hosts" -Destination "C:\Windows\System32\drivers\etc\hosts.bak" -Force
Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "`r`n" -Encoding ASCII
Resolve-DnsName squid-proxy.appstream.local |
  Where-Object QueryType -eq "A" |
  ForEach-Object { "{0} {1}" -f $_.IPAddress, "squid-proxy.appstream.local" } |
  Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Encoding ASCII
```

## Gotchas
- **Run Method 2 only once.** Running it multiple times creates duplicate entries; clean them manually before re-running
- Do not run Method 2 after already performing Method 1
- IPs for `squid-proxy.appstream.local` **differ per environment** and **can change** — hardcoded hosts entries may break after an AWS-side update
- WorkSpaces Pool instances are ephemeral — apply this fix at **image creation time** or via automation/startup script
- A dynamic script that updates the hosts file when Twingate is not running is the recommended long-term approach

## Related Docs
- [Windows Client] Limitations with Multiple NICs and Split-Horizon DNS (referenced in article, internal KB)