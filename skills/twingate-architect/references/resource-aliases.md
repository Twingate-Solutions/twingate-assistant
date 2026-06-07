# Resource Aliases

## Summary
Aliases add extra addresses to Twingate Resources, accessible only through Twingate without requiring DNS record setup. They work alongside (not replacing) the original address and are protocol agnostic.

## Key Information
- Aliases function as pseudo-A records, only resolvable via Twingate
- Multiple users with Resource access can all use the alias
- Original Resource address remains fully functional alongside alias
- Protocol agnostic — works with any protocol (HTTP, SSH, etc.)

## Prerequisites
Minimum version requirements:
| Component | Version |
|-----------|---------|
| Connector | 1.50.0+ |
| macOS Client | 1.0.27+ |
| Windows Client | 1.0.29+ |
| Linux Client | 1.0.79+ |
| iOS | 1.0.27+ |
| Android | 1.0.24+ |

## Configuration Values
No DNS records required. Aliases are configured directly on the Resource in the Twingate Admin Console.

## Gotchas

**HTTPS Certificate Errors**
- Aliases have no built-in HTTPS support — accessing HTTPS resources via alias will produce certificate errors
- Fix: Create and register a TLS certificate for the alias domain (use a controlled domain subdomain or distribute a private certificate)

**HTTP Host Headers**
- HTTP requests via alias set `Host:` to the alias name, not the original address
- May affect virtual host routing on web servers

**Avoid `.local` TLD**
- `.local` conflicts with mDNS (Bonjour, zeroconf) — alias may fail on many devices
- Use instead: `alias.internal`, `alias.corp`, or a subdomain of a domain you control

**No Single Label Domains**
- Aliases must contain at least one `.` (e.g., `router.internal` ✓, `router` ✗)
- Use: `router.internal`, `router.corp`, or `router.yourdomain.com`

## Related Docs
- Twingate Resources configuration
- Connector setup and versioning
- DNS and split tunneling