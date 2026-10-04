---
source: https://help.twingate.com/articles/5946128544-known-incompatibility-overview
type: help
fetched: 2026-10-04
source_version: d4a56be50dfb1b11ba20fbe2410bdc219c97f61901075079b88830bc7eb9ac36
trust: official
---

# Known Incompatibility Overview

## Page Title
Known Incompatibility Overview

## Summary
Twingate may conflict with VPN, DNS filtering, and security software that modifies network settings at the OS level. Conflicts arise when multiple applications compete over routing tables, DNS resolution, or encrypted tunnels. This page catalogs known incompatible software and recommended workarounds.

## Key Information
- Twingate operates at the network level using IPs in the **100.96/12 CGNAT range**; local networks or DNS configs using this range will conflict
- Conflicts occur even when conflicting software is **installed but not actively running**
- Some AV/EDR/VPN tools intercept traffic despite appearing "disabled" — full uninstall may be required to isolate issues

## Known Incompatible Software

| Category | Software |
|----------|----------|
| VPN/ZTNA | Zscaler |
| DNS Clients | Cisco Umbrella, DNSFilter, AdGuard (local), Avast Real Site Protection |

**Cisco-specific note:** Cisco AnyConnect's Umbrella module previously worked with Twingate via Internal Domains list. Cisco Secure Client (AnyConnect's replacement) has breaking DNS changes — this workaround **no longer functions**.

## Troubleshooting Steps
1. Temporarily **uninstall** the conflicting software to confirm it is the cause
2. If uninstalling resolves the issue, try these workarounds before permanently removing:
   - Enable **bypass/compatibility mode** in VPN, ZTNA, or network filtering tools
   - Add **DNS exclusions** for Twingate Resources and `*.twingate.com`
   - Add **AV/EDR exceptions** for `*.twingate.com`
3. If exclusions do not resolve the issue → perform a **full uninstall**

## Configuration Values
- Twingate CGNAT IP range: `100.96/12`
- DNS/AV exclusion domain pattern: `*.twingate.com`

## Gotchas
- Software that appears disabled may still intercept network traffic
- Cisco Secure Client (successor to AnyConnect) has no known working workaround with Twingate's DNS handling
- AdGuard conflicts apply to the **locally installed application**, not necessarily browser extensions

## Related Docs
- CGNAT IP conflict details: referenced as a separate knowledge base article (linked inline on the help page)
- Per-product workaround articles linked from the help page for: Zscaler, Cisco Umbrella, DNSFilter, AdGuard for Mac, Avast Real Site Protection