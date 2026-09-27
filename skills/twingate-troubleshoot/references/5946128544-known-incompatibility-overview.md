---
source: https://help.twingate.com/articles/5946128544-known-incompatibility-overview
type: help
fetched: 2026-09-27
source_version: 876dd282f5d851a073948b8aeb50cd68f55334b12c76a45891a95199d87d971e
---

# Known Incompatibility Overview

## Summary
Twingate may conflict with VPN, DNS filtering, and security software that modifies network settings. Conflicts arise when third-party applications attempt to modify routing tables, enforce custom DNS, or create overlapping encrypted tunnels. Some software causes issues even when disabled.

## Key Information
- Twingate uses IPs in the **100.96/12 CGNAT range** — conflicts occur if local network/DNS also uses this range
- Conflicts commonly involve: routing table modifications, custom DNS enforcement, overlapping encrypted tunnels
- Some security software intercepts network traffic even when "disabled" — full uninstall may be required

## Known Incompatible Applications

**VPN/ZTNA:**
- Zscaler

**DNS Clients:**
- Cisco Umbrella / Cisco Secure Client (AnyConnect replacement — broke DNS handling, no current workaround)
- DNSFilter
- AdGuard (local install), AdGuard for Mac
- Avast Real Site Protection

## Troubleshooting Steps
1. Temporarily uninstall conflicting software to confirm it's the cause
2. If resolved, try these workarounds before permanent uninstall:
   - Enable bypass/compatibility mode in VPN, ZTNA, or network filtering software
   - Add DNS exclusions for Twingate Resources and `*.twingate.com`
   - For AV/EDR: create exceptions for `*.twingate.com`
3. If exclusions don't resolve the issue → full uninstall required

## Gotchas
- **Cisco Secure Client** (Umbrella module): previously, adding Resource domains to Umbrella's Internal Domains list worked as a workaround — this no longer functions after AnyConnect's EOL replacement
- Software that appears disabled may still intercept traffic
- CGNAT IP range conflict (100.96/12) requires separate remediation — see linked KB article

## Configuration Values
| Item | Value |
|------|-------|
| Twingate CGNAT range | `100.96/12` |
| DNS/AV exception domain | `*.twingate.com` |

## Related Docs
- Twingate CGNAT range conflict KB article (linked in source)
- Per-application guides: Zscaler, Cisco Umbrella, DNSFilter, AdGuard, Avast