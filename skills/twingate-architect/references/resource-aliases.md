# Resource Aliases

## Summary
Aliases add extra addresses to Twingate Resources, accessible to anyone with Resource access. They function as protocol-agnostic pseudo-A records that only work through Twingate—no DNS configuration required. Aliases supplement (not replace) original Resource addresses.

## Key Information
- Any Resource can have an alias (e.g., map `10.0.0.1` → `router.internal`)
- Aliases work with any protocol
- No external DNS records needed; resolution handled entirely by Twingate
- Aliases do not replace the original Resource address

## Prerequisites / Version Requirements
| Component | Minimum Version |
|-----------|----------------|
| Connector | 1.50.0 |
| macOS Client | 1.0.27 |
| Windows Client | 1.0.29 |
| Linux Client | 1.0.79 |
| iOS Client | 1.0.27 |
| Android Client | 1.0.24 |

## Gotchas

**HTTPS / TLS Certificates**
- Aliases have no built-in HTTPS support → certificate errors will occur
- Fix: Create and register a TLS cert for the alias domain (use a controlled domain subdomain or distribute a private CA cert)

**HTTP Host Headers**
- HTTP requests via alias set `Host:` to the alias name, not the original address
- May break virtual host routing on web servers

**`.local` TLD**
- Reserved for mDNS (Bonjour, zeroconf); using `.local` aliases will likely fail on many devices
- Use instead: `alias.internal`, `alias.corp`, or a subdomain of a domain you control

**Single Label Domains**
- Aliases must contain at least one `.` (e.g., `router` is invalid; `router.internal` is valid)
- Use: `router.internal`, `router.corp`, or `router.yourdomain.com`

## Recommended Alias Patterns
- `resource.internal`
- `resource.corp`
- `resource.yourdomain.com` (subdomain of controlled domain)

## Related Docs
- Twingate Resources configuration
- Connector deployment and versioning
- Client version management