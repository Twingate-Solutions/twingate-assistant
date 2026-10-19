---
source: https://help.twingate.com/articles/4359531030-cgnat-ip-conflicts-dns-resolution-resource-access-issues-with-twingate
type: help
fetched: 2026-10-18
source_version: 3e9a1df6f71d912b0349c1fae96c0680dae66ccd49124c1b414240133bb29f6d
trust: official
---

# CGNAT IP Conflicts: DNS Resolution & Resource Access Issues with Twingate

## Summary
Twingate Client claims the `100.96/12` CGNAT IP range for its own encrypted tunneling, blocking or misrouting any other traffic using addresses in that range. This causes two primary failure modes: DNS resolution failures (if DNS servers use CGNAT IPs) and connectivity failures to non-Twingate CGNAT-based resources.

## Key Information
- Twingate reserves the entire `100.96/12` CGNAT range; all traffic in this range is assumed to be Twingate-bound
- Affects all Twingate Client operating systems (Windows, macOS, Linux)
- Two failure modes:
  - **DNS failures**: System DNS servers assigned a `100.96/12` IP get misrouted
  - **Resource access failures**: Non-Twingate services using CGNAT IPs are dropped by the client

## Diagnosis Steps

**Check DNS configuration:**
- **Windows** (Command Prompt): `ipconfig`
- **Linux** (Terminal): `ifconfig`
- **macOS** (Terminal): `scutil --dns`

Look for DNS server IPs falling within `100.96/12`. If present, those are the conflict source.

**Check non-Twingate CGNAT resource conflicts:**
1. Disable Twingate Client → test resource access
2. Re-enable Twingate Client → test resource access again
3. If resource is only inaccessible with Twingate active → CGNAT IP conflict confirmed

## Solutions

**DNS Resolution Failure:**
Change system DNS servers to addresses outside the `100.96/12` range:

| Provider | Primary | Secondary |
|----------|---------|-----------|
| Google DNS | `8.8.8.8` | `8.8.4.4` |
| Quad9 DNS | `9.9.9.9` | `149.112.112.112` |

**Non-Twingate CGNAT Resources:**
- If you control the resource: reassign it an IP outside the `100.96/12` range
- If you cannot change the resource IP: contact Twingate Support

## Configuration Values
- **Conflicting IP range**: `100.96.0.0/12` (CGNAT range claimed by Twingate)

## Gotchas
- Twingate does **not** distinguish between its own CGNAT traffic and third-party CGNAT traffic — all `100.96/12` traffic is intercepted
- Disabling/re-enabling the client is the reliable diagnostic method; ping tests alone may be insufficient
- If your ISP or VPN assigns CGNAT addresses in this block, conflicts will occur regardless of Twingate configuration
- No client-side override or exclusion is available for this range without contacting Support

## Related Docs
- Twingate Client documentation (all OS platforms)
- Twingate Support for cases where resource IP cannot be changed