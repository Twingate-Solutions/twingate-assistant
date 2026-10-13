---
source: https://help.twingate.com/articles/4359531030-cgnat-ip-conflicts-dns-resolution-resource-access-issues-with-twingate
type: help
fetched: 2026-10-11
source_version: e08f357e3adf502b3d2a6027fde16249e9b6704b5b6e860d2191db796a64f588
trust: official
---

# CGNAT IP Conflicts: DNS Resolution & Resource Access Issues with Twingate

## Summary
The Twingate Client reserves the `100.96/12` CGNAT range exclusively for its encrypted tunnels, causing traffic to unrelated services using those IPs to be blocked or misrouted. This affects two scenarios: DNS servers assigned IPs in that range, and non-Twingate services that also use CGNAT addressing.

## Key Information
- Twingate claims all traffic in the `100.96/12` CGNAT range for its own connections
- Affected scenarios: (1) DNS resolution failures, (2) connectivity to non-Twingate CGNAT resources
- Conflict is confirmed if a resource is accessible with Twingate disabled but not with it enabled

## Prerequisites
- Twingate Client installed on any OS
- Access to system network/DNS settings

## Identifying the Issue

### Check DNS Configuration
| OS | Command |
|----|---------|
| Windows | `ipconfig` (Command Prompt) |
| Linux | `ifconfig` (Terminal) |
| macOS | `scutil --dns` (Terminal) |

Check output for DNS server IPs falling within `100.96.0.0/12`.

### Check Non-Twingate CGNAT Resource Access
1. Disable Twingate Client
2. Attempt to access the resource → succeeds
3. Re-enable Twingate Client
4. Attempt access again → fails = CGNAT conflict confirmed

## Resolution

### DNS Conflict Fix
Change system DNS servers to addresses **outside** the `100.96/12` range:

| Provider | Primary | Secondary |
|----------|---------|-----------|
| Google DNS | `8.8.8.8` | `8.8.4.4` |
| Quad9 | `9.9.9.9` | `149.112.112.112` |

### Non-Twingate CGNAT Resource Conflict
- **If you control the resource:** Re-IP it to an address outside `100.96/12`
- **If you cannot re-IP:** Contact Twingate Support for additional troubleshooting options

## Configuration Values
- **Conflicting IP range:** `100.96.0.0/12` (entire range claimed by Twingate Client)

## Gotchas
- The `100.96/12` block is a subset of the broader RFC 6598 CGNAT range (`100.64.0.0/10`); only the `/12` sub-range is used by Twingate
- No in-app setting exists to exclude specific CGNAT IPs from Twingate's capture; re-IPing is the primary self-service fix
- ISPs using CGNAT for customer routing can trigger this issue without any local misconfiguration

## Related Docs
- Twingate Client documentation (all operating systems)
- Twingate Support contact for unresolvable CGNAT conflicts