# Resource Aliases

## Summary
Aliases add extra addresses to Twingate Resources, accessible to anyone with Resource access without replacing the original address. They function like pseudo-A records, are protocol-agnostic, and require no DNS configuration. Aliases only work through Twingate.

## Key Information
- Aliases coexist with original Resource addresses (both remain usable)
- No DNS record setup required
- Protocol-agnostic (works with any protocol)
- Accessible only via Twingate clients

## Prerequisites (Minimum Versions)
| Component | Minimum Version |
|-----------|----------------|
| Connector | 1.50.0 |
| macOS Client | 1.0.27 |
| Windows Client | 1.0.29 |
| Linux Client | 1.0.79 |
| iOS Client | 1.0.27 |
| Android Client | 1.0.24 |

## Configuration Values
- Aliases are set per-Resource in the Twingate admin console
- No CLI flags or API params documented on this page

## Gotchas

**HTTPS / TLS Certificate Errors**
- Aliases have no built-in HTTPS support; accessing HTTPS resources via alias will cause certificate errors
- Fix: Create and register a TLS certificate for the alias domain (use a controlled domain or distribute a private cert)

**HTTP Host Headers**
- HTTP requests via alias set `Host:` to the alias name, not the original address
- May affect virtual host routing on web servers

**`.local` TLD**
- Avoid `.local` aliases — conflicts with mDNS (Bonjour, zeroconf)
- Use alternatives: `alias.internal`, `alias.corp`, or a subdomain of a domain you control

**Single Label Domains**
- Aliases must contain at least one `.` (e.g., `router` is invalid; `router.internal` is valid)
- Use `router.internal`, `router.corp`, or `router.yourdomain.com`

## Recommended Alias Patterns
- `resource.internal`
- `resource.corp`
- `resource.yourdomain.com` (subdomain of controlled domain)

## Related Docs
- Twingate Resources configuration
- Connector setup and versioning
- TLS/certificate management (external)