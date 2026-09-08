---
source: https://help.twingate.com/articles/5946128544-known-incompatibility-overview
type: help
fetched: 2026-09-06
source_version: af18971a5440c2a3786d46d12ef602b9b292dc56b6efe962f0834fd23f9330de
---

# Known Incompatibility Overview

## Page Title
Known Incompatibility Overview

## Summary
Twingate may conflict with VPN, DNS filtering, and security software that modifies network settings at the OS level. Conflicts arise when multiple applications compete over routing tables, DNS configuration, or encrypted tunnels. This page identifies known incompatible software and provides mitigation strategies.

## Key Information
- Twingate operates at the network level and can conflict with other network-modifying software
- Three primary conflict vectors: routing table modifications, custom DNS enforcement, overlapping encrypted tunnels
- Twingate uses the **100.96/12 CGNAT range** for Client-Connector-Resource communication — local network IPs in this range will cause conflicts
- Software can interfere **even when disabled** (not just when actively running)

## Known Incompatible Software
| Category | Software |
|----------|----------|
| VPN/ZTNA | Zscaler |
| DNS Clients | Cisco Umbrella, DNSFilter, AdGuard (local), AdGuard for Mac |
| Antivirus | Avast Real Site Protection |

## Troubleshooting Steps
1. Temporarily **uninstall** conflicting software to confirm it is the cause
2. If uninstall resolves the issue, try these workarounds before permanently removing:
   - Enable **bypass/compatibility mode** in VPN, ZTNA, or network filtering software
   - Add **DNS exclusions** for Twingate Resources and `*.twingate.com`
   - For AV/EDR software, create **exceptions** for `*.twingate.com`
3. If exclusions don't resolve the issue → **full uninstall required**

## Configuration Values
- DNS exclusion domain: `*.twingate.com`
- Conflicting IP range: `100.96/12` (CGNAT)

## Gotchas
- Some security software continues intercepting traffic even when toggled "off" — disabling is not sufficient to test compatibility, uninstall is required
- CGNAT range conflict (`100.96/12`) can cause silent connectivity failures if local network uses overlapping IPs
- Each listed application has its own linked troubleshooting article with specific guidance (not covered on this page)

## Related Docs
- Twingate KB article on DNS IP conflict within 100.96/12 CGNAT range
- Zscaler-specific troubleshooting article
- Cisco Umbrella-specific troubleshooting article
- DNSFilter-specific troubleshooting article
- AdGuard-specific troubleshooting articles (local app + Mac)
- Avast Real Site Protection troubleshooting article