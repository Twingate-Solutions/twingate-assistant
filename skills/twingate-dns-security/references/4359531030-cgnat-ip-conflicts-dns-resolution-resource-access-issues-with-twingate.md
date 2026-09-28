---
source: https://help.twingate.com/articles/4359531030-cgnat-ip-conflicts-dns-resolution-resource-access-issues-with-twingate
type: help
fetched: 2026-09-27
source_version: b9a8e2b2f527ed7c67af11af69db8b48f8bb71775d0d73b77c458743f802d378
---

# CGNAT IP Conflicts: DNS Resolution & Resource Access Issues with Twingate

## Summary
Twingate Client reserves the `100.96/12` CGNAT range exclusively for its encrypted tunnel traffic, causing conflicts when other services (DNS servers or non-Twingate resources) use IPs in this range. Affected traffic gets blocked or misrouted by the Twingate Client.

## Key Information
- Twingate uses `100.96/12` CGNAT range internally; all traffic in this range is assumed to be Twingate tunnel traffic
- Two failure modes: DNS resolution failures and connectivity drops to non-Twingate CGNAT resources
- Issue only manifests when Twingate Client is active

## Prerequisites
- Access to system terminal/command prompt
- Knowledge of your network's DNS configuration
- Ability to modify DNS settings or resource IP assignments

## Identifying the Issue

### Check DNS Configuration
| OS | Command |
|----|---------|
| Windows | `ipconfig` |
| Linux | `ifconfig` |
| macOS | `scutil --dns` |

Look for DNS server IPs falling within `100.96/12` range.

### Check CGNAT Resource Conflicts
1. Disable Twingate Client → test resource access
2. Re-enable Twingate Client → test resource access again
3. If resource is only inaccessible **with Twingate active** → CGNAT conflict confirmed

## Configuration Values
- **Conflicting IP range:** `100.96.0.0/12` (Twingate reserved CGNAT space)

## Solutions

### DNS Resolution Failures
Change DNS servers to addresses outside `100.96/12`:
| Provider | Primary | Secondary |
|----------|---------|-----------|
| Google DNS | `8.8.8.8` | `8.8.4.4` |
| Quad9 | `9.9.9.9` | `149.112.112.112` |

### Non-Twingate CGNAT Resource Conflicts
- **If you manage the resource:** Reassign it an IP outside `100.96/12`
- **If you cannot change the IP:** Contact Twingate Support

## Gotchas
- Applies to **all Twingate Client operating systems**
- No Twingate-side configuration can exempt specific CGNAT IPs from interception — IP reassignment or DNS change is required
- CGNAT conflicts are silent by default; no obvious error message indicates the root cause

## Related Docs
- Twingate Client documentation (general)
- Twingate Support (for unresolvable CGNAT IP conflicts)