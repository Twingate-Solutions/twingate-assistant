---
source: https://www.twingate.com/docs/resource-aliases
type: docs
fetched: 2026-08-14
source_version: 66269e876d5bf3af90e7e00b1c5b154ec3a76f7b9942ee9695a345f7b4824838
---

# Resource Aliases

## Summary
Aliases add extra addresses to Twingate Resources, accessible to anyone with Resource access without replacing the original address. They function as pseudo-A records handled entirely within Twingate—no DNS setup required. Aliases are protocol-agnostic but have important caveats for HTTPS and certain domain formats.

## Key Information
- Aliases coexist with the original Resource address (both remain usable)
- Only accessible via Twingate; no external DNS records needed
- Protocol-agnostic (works with any protocol)
- Think of them as internal-only pseudo-A records

## Prerequisites / Version Requirements
| Component | Minimum Version |
|-----------|----------------|
| Connector | 1.50.0 |
| macOS Client | 1.0.27 |
| Windows Client | 1.0.29 |
| Linux Client | 1.0.79 |
| iOS Client | 1.0.27 |
| Android Client | 1.0.24 |

## Configuration Values
- Set via Twingate Admin Console on the Resource configuration page
- No CLI flags or env vars; no external DNS record creation needed

## Gotchas

**HTTPS / TLS:** Aliases cause certificate errors on HTTPS sites. To fix, either:
- Use a subdomain of a domain you control and issue a valid TLS cert for it
- Create and distribute a private/internal CA cert for the alias

**Host Headers (HTTP):** The `Host` header is set to the alias name (e.g., `Host: router.internal`), which may affect virtual host routing on the server side.

**`.local` TLD:** Avoid using `.local`—it conflicts with mDNS (Bonjour/zeroconf) and will likely break on most devices. Use `.internal`, `.corp`, or a subdomain of a domain you control instead.

**Single-label domains:** Aliases must contain at least one `.` (e.g., `router` is invalid; `router.internal` is valid). Use `router.internal`, `router.corp`, or `router.yourdomain.com`.

## Recommended Alias Formats
- `alias.internal`
- `alias.corp`
- `alias.yourdomain.com` (subdomain of a controlled domain)

## Related Docs
- Twingate Resources configuration
- Connector installation/upgrade (to meet minimum version requirements)
- TLS certificate management for HTTPS Resources