---
source: https://help.twingate.com/articles/4359531030-cgnat-ip-conflicts-dns-resolution-resource-access-issues-with-twingate
type: help
fetched: 2026-09-06
source_version: ee5d99281feceecc2db5e33e4e12d2a7d3ec10c8d5a46e558f320cb5c3e344ef
---

# CGNAT IP Conflicts: DNS Resolution & Resource Access Issues with Twingate

## Summary
Twingate Client reserves the 100.96/12 CGNAT IP range exclusively for its encrypted connections, causing conflicts when other services use IPs in this range. This affects both DNS resolution and connectivity to non-Twingate resources using CGNAT addresses.

## Key Information
- Twingate uses the **100.96/12 CGNAT range** for Client-Connector-Resource communication
- All traffic in this range is assumed to be Twingate traffic — unrelated services get blocked or misrouted
- Two failure modes: DNS resolution failures and dropped traffic to non-Twingate CGNAT resources

## Prerequisites
- Twingate Client installed (any OS)
- Access to system DNS settings or network configuration

## Diagnosis Steps

**Check DNS configuration for conflicting IPs:**
- Windows: `ipconfig`
- Linux: `ifconfig`
- macOS: `scutil --dns`

Look for DNS server IPs falling within `100.96.0.0/12`.

**Check non-Twingate resource conflicts:**
1. Disable Twingate Client → test resource access
2. Re-enable Twingate Client → test resource access again
3. If resource is only inaccessible with Twingate active → CGNAT conflict confirmed

## Configuration Values

| Issue | Fix |
|-------|-----|
| DNS in 100.96/12 range | Change DNS to public servers outside CGNAT range |
| Resource IP in 100.96/12 range | Reassign resource to IP outside 100.96/12 |

**Recommended replacement DNS servers:**
- Google DNS: `8.8.8.8`, `8.8.4.4`
- Quad9: `9.9.9.9`, `149.112.112.112`

## Gotchas
- The conflict range is `100.96/12` (not just `100.64/10` which is the broader CGNAT RFC range) — verify IPs against this specific subnet
- If you cannot change the resource IP and must use CGNAT space, contact Twingate Support — no self-service workaround is available
- ISP-assigned DNS servers sometimes fall in CGNAT ranges (common with mobile carriers and some broadband providers)

## Related Docs
- Twingate Client documentation (all operating systems)
- Twingate Support for unresolvable CGNAT resource conflicts