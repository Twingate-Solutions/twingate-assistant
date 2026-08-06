---
source: https://help.twingate.com/articles/4359531030-cgnat-ip-conflicts-dns-resolution-resource-access-issues-with-twingate
type: help
fetched: 2026-08-06
source_version: bb199aba8fdebf347ea1510772668648758086fc9d1e84ef8ab89a2397a37981
---

# CGNAT IP Conflicts: DNS Resolution & Resource Access Issues with Twingate

## Summary
Twingate Client reserves the `100.96/12` CGNAT range for its own encrypted tunneling. Any DNS servers or network resources using IPs in this range will conflict with Twingate, causing DNS failures or dropped traffic to non-Twingate services.

## Key Information
- Twingate claims all traffic in `100.96/12` CGNAT range as its own
- Two failure modes: DNS resolution failures and connectivity drops to non-Twingate CGNAT resources
- Applies to all Twingate Client operating systems

## Identifying the Issue

### Check DNS Configuration
| OS | Command |
|---|---|
| Windows | `ipconfig` |
| Linux | `ifconfig` |
| macOS | `scutil --dns` |

Look for DNS server IPs falling within `100.96/12`. If present, those DNS servers are conflicting.

### Check Non-Twingate CGNAT Resource Conflicts
1. Disable Twingate Client → test resource access
2. Re-enable Twingate Client → test resource access again
3. If resource is **only inaccessible with Twingate active**, CGNAT conflict confirmed

## Configuration Values
- **Conflicting IP range:** `100.96/12` (all IPs in this range are claimed by Twingate)
- **Safe replacement DNS servers:**
  - Google DNS: `8.8.8.8`, `8.8.4.4`
  - Quad9: `9.9.9.9`, `149.112.112.112`

## Resolution Steps

**DNS conflict:** Change system DNS servers to addresses outside `100.96/12` (see safe options above)

**CGNAT resource conflict:**
- Reassign the resource an IP outside `100.96/12` if you control it
- If IP cannot be changed, contact Twingate Support

## Gotchas
- Twingate does not selectively route CGNAT traffic — it intercepts **all** `100.96/12` traffic, not just its own
- ISP-assigned CGNAT addresses (common in mobile/residential networks) can trigger this silently
- No built-in Twingate configuration option to exclude specific CGNAT IPs — IP reassignment or support escalation is required

## Related Docs
- Twingate Client configuration (all OS)
- Twingate Support escalation for unresolvable CGNAT conflicts