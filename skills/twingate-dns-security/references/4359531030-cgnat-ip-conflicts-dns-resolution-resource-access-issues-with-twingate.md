---
source: https://help.twingate.com/articles/4359531030-cgnat-ip-conflicts-dns-resolution-resource-access-issues-with-twingate
type: help
fetched: 2026-10-04
source_version: aa5ec802bf5a6df232efd54876f51e2e9bd955503c34ccfbdf68c51917ddb736
trust: official
---

# CGNAT IP Conflicts: DNS Resolution & Resource Access Issues with Twingate

## Summary
The Twingate Client claims all traffic in the `100.96/12` CGNAT range for its encrypted tunneling. Any DNS servers or non-Twingate resources using IPs in this range will be blocked or misrouted by the Twingate Client.

## Key Information
- Twingate uses `100.96/12` CGNAT range exclusively for Client ↔ Connector ↔ Resource communication
- Two failure modes: DNS resolution failures and connectivity drops to non-Twingate CGNAT resources
- Issue affects all Twingate Client operating systems

## Prerequisites
- Twingate Client installed
- Access to system terminal/command prompt

## Diagnosis Steps

**Check for conflicting DNS servers:**

| OS | Command |
|----|---------|
| Windows | `ipconfig` |
| Linux | `ifconfig` |
| macOS | `scutil --dns` |

Look for DNS server IPs in the `100.96.0.0/12` range (covers `100.96.0.0` – `100.111.255.255`).

**Check for non-Twingate CGNAT resource conflicts:**
1. Disable Twingate Client → test resource access
2. Re-enable Twingate Client → test resource access again
3. If resource is only inaccessible with Twingate active → CGNAT conflict confirmed

## Configuration Values
- **Conflicting range:** `100.96.0.0/12`

## Resolutions

**DNS conflict fix** — change DNS to addresses outside `100.96/12`:
- Google DNS: `8.8.8.8`, `8.8.4.4`
- Quad9 DNS: `9.9.9.9`, `149.112.112.112`

**Non-Twingate CGNAT resource conflict:**
- If you control the resource: reassign it an IP outside `100.96/12`
- If you cannot change the resource IP: contact Twingate Support

## Gotchas
- The CGNAT conflict is silent — Twingate drops traffic without explicit error, making it hard to distinguish from other connectivity issues
- DNS failures caused by this conflict can appear as general internet outages, not obviously Twingate-related
- The disable/re-enable toggle test is the quickest way to confirm Twingate is the culprit

## Related Docs
- Twingate Support (for unresolvable CGNAT IP conflicts): contact via Twingate Help Center