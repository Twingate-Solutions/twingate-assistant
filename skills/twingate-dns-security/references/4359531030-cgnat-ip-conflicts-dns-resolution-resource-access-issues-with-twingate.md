---
source: https://help.twingate.com/articles/4359531030-cgnat-ip-conflicts-dns-resolution-resource-access-issues-with-twingate
type: help
fetched: 2026-10-25
source_version: 6b94f77481178e74c0362dfa381bce9701a5726da2c2ea75622f2f5afd0ed99f
trust: official
---

# CGNAT IP Conflicts: DNS Resolution & Resource Access Issues with Twingate

## Summary
Twingate Client reserves the `100.96/12` CGNAT IP range exclusively for its encrypted tunneling infrastructure. Any DNS servers or network resources using IPs in this range will be blocked or misrouted when the Twingate Client is active.

## Key Information
- Twingate intercepts **all traffic** in the `100.96/12` CGNAT range, treating it as internal tunnel traffic
- Two failure modes: DNS resolution failures and blocked access to non-Twingate CGNAT resources
- Applies to all Twingate Client operating systems

## Identifying the Issue

**Check DNS servers for conflicting IPs:**

| OS | Command |
|----|---------|
| Windows | `ipconfig` |
| Linux | `ifconfig` |
| macOS | `scutil --dns` |

Look for any DNS server IPs falling within `100.96/12`. If found, they are the conflict source.

**Check if a resource uses CGNAT IPs:**
1. Disable Twingate Client → test resource access
2. Re-enable Twingate Client → test resource access again
3. If resource is only inaccessible **with Twingate active**, CGNAT conflict is confirmed

## Configuration Values
- **Conflicting range:** `100.96.0.0/12`

## Resolution

**DNS conflict fix** — change system DNS to servers outside the CGNAT range:
- Google DNS: `8.8.8.8` / `8.8.4.4`
- Quad9: `9.9.9.9` / `149.112.112.112`

**Non-Twingate resource conflict fix:**
- Reassign the resource an IP outside `100.96/12` if you control it
- If IP cannot be changed, contact Twingate Support

## Gotchas
- CGNAT conflicts are not surfaced as obvious Twingate errors — they manifest as general DNS or connectivity failures
- ISP-assigned CGNAT addresses (common in mobile or carrier-grade NAT environments) may also fall in this range
- No Twingate-side configuration option exists to exempt specific CGNAT IPs from interception; IP reassignment or DNS change is required

## Related Docs
- Twingate Support contact for cases where resource IP cannot be changed