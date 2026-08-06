---
source: https://help.twingate.com/articles/5946128544-known-incompatibility-overview
type: help
fetched: 2026-08-06
source_version: 9e524825754f280e39c0c52a2d78e98bb8e26b48d0fb8658d31fe1067fd101d3
---

# Known Incompatibility Overview

## Page Title
Known Incompatibility Overview

## Summary
Twingate may conflict with VPN, DNS filtering, and security software that modifies network settings at the OS level. Conflicts arise when multiple applications compete over routing tables, DNS settings, or encrypted tunnels. This page outlines categories of incompatibility and links to specific workarounds.

## Key Information
- Twingate operates at the network level and can conflict with other network-modifying software
- Three primary conflict types: routing table modifications, custom DNS enforcement, overlapping encrypted tunnels
- Twingate uses IPs in the **100.96/12 CGNAT range** — local network or DNS IPs in this range cause connectivity failures
- Software can interfere even when **disabled but not uninstalled**

## Known Incompatible Software

| Category | Applications |
|----------|-------------|
| VPN/ZTNA | Zscaler |
| DNS Clients | Cisco Umbrella, DNSFilter, AdGuard (local), AdGuard for Mac |
| Antivirus | Avast Real Site Protection |

## Troubleshooting Steps
1. Temporarily **uninstall** (not just disable) the conflicting software to confirm it is the cause
2. If uninstalling resolves the issue, try these workarounds before permanently removing:
   - Enable **bypass/compatibility mode** in the conflicting VPN, ZTNA, or network filtering software
   - Add **DNS exclusions** for Twingate Resources and `*.twingate.com`
   - For AV/EDR software, create **process/domain exceptions** for `*.twingate.com`
3. If exclusions fail, full uninstall may be required

## Configuration Values
- **CGNAT range used by Twingate:** `100.96/12`
- **Wildcard domain for exclusions:** `*.twingate.com`

## Gotchas
- Some security software intercepts network traffic even when toggled "off" — disabling is insufficient for testing; full uninstall required to isolate the issue
- IP conflicts within `100.96/12` are non-obvious and may appear as general connectivity failures
- Each listed incompatible application has its own dedicated troubleshooting article (linked from the source page)

## Related Docs
- CGNAT range conflict details: referenced via internal knowledge base article (linked in source)
- Zscaler compatibility article
- Cisco Umbrella compatibility article
- DNSFilter compatibility article
- AdGuard / AdGuard for Mac compatibility articles
- Avast Real Site Protection compatibility article