---
source: https://help.twingate.com/articles/5946128544-known-incompatibility-overview
type: help
fetched: 2026-10-25
source_version: 5cfd093bdce71ec38e57c866b31bb8f6f26cb7c99c0530d7f8a711ae3e4fbd91
trust: official
---

# Known Incompatibility Overview

## Page Title
Known Incompatibility Overview

## Summary
Twingate may conflict with VPN, DNS filtering, and security software that modifies network settings at the OS level. Conflicts arise when multiple applications compete over routing tables, DNS settings, or encrypted tunnels. This article lists known incompatible software and recommended workarounds.

## Key Information
- Twingate operates at the network level and can conflict with software that modifies routing tables, enforces custom DNS, or establishes encrypted tunnels
- Twingate uses IPs in the **100.96/12 CGNAT range** — conflicts occur if your local network or DNS settings overlap this range
- Some security software intercepts traffic even when "disabled" — full uninstall may be required to isolate issues

## Known Incompatible Software

**VPN / ZTNA:**
- Zscaler

**DNS Clients:**
- Cisco Umbrella / Cisco Secure Client (formerly AnyConnect — the Internal Domains workaround no longer works with Secure Client due to breaking DNS handling changes)
- DNSFilter
- AdGuard (locally installed)
- AdGuard for Mac

**Antivirus / Security:**
- Avast Real Site Protection

## Troubleshooting Steps
1. Temporarily uninstall conflicting software to confirm it is the cause
2. If uninstalling resolves the issue, try these workarounds before permanent removal:
   - Enable **bypass/compatibility mode** in VPN, ZTNA, or network filtering software
   - Add **DNS exclusions** for Twingate Resources and `*.twingate.com`
   - For AV/EDR software, create **exceptions** for `*.twingate.com`
3. If exclusions don't work, full uninstall may be necessary

## Configuration Values
| Context | Value |
|---|---|
| Twingate CGNAT range | `100.96/12` |
| DNS/AV exclusion domain | `*.twingate.com` |

## Gotchas
- **Cisco Secure Client** replaced AnyConnect and broke the previously working Internal Domains workaround — no known workaround for Cisco Umbrella + Secure Client combination
- Security software can intercept traffic **even when toggled off** — "disabled" does not mean inactive at the network level
- CGNAT IP range conflicts are a common, non-obvious source of connectivity failures

## Related Docs
- Twingate CGNAT range conflict KB article (linked inline, URL not provided)
- Per-product workaround articles linked from the main page for: Zscaler, Cisco Umbrella, DNSFilter, AdGuard, Avast