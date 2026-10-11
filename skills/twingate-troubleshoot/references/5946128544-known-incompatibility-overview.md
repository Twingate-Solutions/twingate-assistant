---
source: https://help.twingate.com/articles/5946128544-known-incompatibility-overview
type: help
fetched: 2026-10-11
source_version: 376d620985421778f67cd866f0058da5fa3078fe0e0f463378f0ed35dfa58a1c
trust: official
---

# Known Incompatibility Overview

## Page Title
Known Incompatibility Overview

## Summary
Twingate may conflict with VPN, DNS filtering, and security software that modifies network routing, DNS settings, or encrypted tunnels. This article identifies known incompatible applications and provides troubleshooting steps. Some software interferes even when disabled, requiring full uninstallation.

## Key Information
- Twingate uses IP addresses in the **100.96/12 CGNAT range** — conflicts occur if local network or DNS settings overlap this range
- Conflicts arise when third-party software attempts to: modify routing tables, enforce custom DNS, or create overlapping encrypted tunnels
- Software may intercept traffic even when "disabled" — exclusions may be insufficient

## Known Incompatible Applications

**VPN / ZTNA:**
- Zscaler

**DNS Clients:**
- Cisco Umbrella (via Cisco Secure Client — previously worked with AnyConnect; breaking DNS changes in Secure Client broke the workaround)
- DNSFilter
- AdGuard (locally installed) / AdGuard for Mac

**Antivirus / Security:**
- Avast: Real Site Protection

## Troubleshooting Steps
1. Temporarily uninstall suspected conflicting software to isolate the issue
2. If uninstalling resolves it, try these workarounds before permanent removal:
   - Enable **bypass/compatibility mode** on VPN, ZTNA, or network-filtering software
   - Add **DNS exclusions** for Twingate Resources and `*.twingate.com`
   - For AV/EDR software, create **exceptions** for `*.twingate.com`
3. If exclusions don't work, full uninstall may be required

## Configuration Values
| Target | Value |
|--------|-------|
| DNS exclusion domain | `*.twingate.com` |
| AV/EDR exception domain | `*.twingate.com` |
| Conflicting IP range | `100.96/12` (CGNAT) |

## Gotchas
- **Cisco AnyConnect → Secure Client migration**: The Umbrella Internal Domains workaround no longer functions after migration to Cisco Secure Client due to breaking DNS handling changes
- Security software that is **not actively running** can still cause conflicts — passive interception is common
- Local DNS or network configurations using `100.96/12` addresses will conflict with Twingate's internal addressing

## Related Docs
- Twingate knowledge base article on DNS IP conflicts within the 100.96/12 CGNAT range (linked from source page)
- Per-application troubleshooting articles for Zscaler, Cisco Umbrella, DNSFilter, AdGuard, and Avast (linked from source page)