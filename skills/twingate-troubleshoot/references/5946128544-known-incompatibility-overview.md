---
source: https://help.twingate.com/articles/5946128544-known-incompatibility-overview
type: help
fetched: 2026-10-18
source_version: 39e7aa38bd266b2c55318ad1cbd2f4abb7ac1109426bcf0b13e988ede2a1bae5
trust: official
---

# Known Incompatibility Overview

## Page Title
Known Incompatibility Overview

## Summary
Twingate may conflict with VPN, DNS filtering, and security software that modifies network settings at the same level Twingate operates. Conflicts arise from competing routing table modifications, custom DNS enforcement, or overlapping encrypted tunnels. The page outlines known incompatible software and recommended workarounds.

## Key Information
- Twingate uses IPs in the **100.96/12 CGNAT range**; local network or DNS settings using this range will cause conflicts
- Software can interfere even when **disabled** (not just when actively running)
- Conflicts manifest as connectivity failures to Twingate Resources

## Known Incompatible Software

| Category | Applications |
|----------|-------------|
| VPN/ZTNA | Zscaler |
| DNS Clients | Cisco Umbrella, DNSFilter |
| DNS/Ad Blocking | AdGuard (local app), AdGuard for Mac |
| Antivirus | Avast Real Site Protection |

**Note:** Cisco AnyConnect's Umbrella module previously worked with Twingate via Internal Domains list workaround. The replacement **Cisco Secure Client** introduced breaking DNS changes — this workaround **no longer works**.

## Troubleshooting Steps

1. Temporarily **uninstall** the conflicting software to confirm it's the cause
2. If uninstalling resolves the issue, apply workarounds instead of permanent removal:
   - Enable **bypass/compatibility mode** in VPN, ZTNA, or network-filtering software
   - Add **DNS exclusions** for Twingate Resources and `*.twingate.com`
   - For AV/EDR software, create **exceptions** for `*.twingate.com`
3. If exclusions don't work → full uninstall may be required

## Configuration Values
- DNS exclusion pattern: `*.twingate.com`
- AV/EDR exception pattern: `*.twingate.com`
- Conflicting IP range: `100.96/12` (CGNAT)

## Gotchas
- Some security software **intercepts traffic even when "disabled"** — disabling is insufficient for testing
- Cisco Secure Client (AnyConnect replacement) has **no known working workaround** with Twingate's DNS handling
- CGNAT range conflicts (`100.96/12`) require network-level remediation, not just software exclusions

## Related Docs
- Twingate KB article on DNS IP conflicts within the 100.96/12 CGNAT range (linked from source page)
- Per-application troubleshooting guides for: Zscaler, Cisco Umbrella, DNSFilter, AdGuard, Avast Real Site Protection