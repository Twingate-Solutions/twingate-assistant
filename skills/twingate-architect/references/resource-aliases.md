# Resource Aliases

## Summary
Aliases add extra addresses to Twingate Resources, accessible to anyone with Resource access. They function as pseudo-A records resolvable only through Twingate, requiring no DNS configuration. Aliases coexist with original addresses rather than replacing them.

## Key Information
- Aliases work alongside original Resource addresses (both remain accessible)
- Protocol agnostic — works with any protocol
- No DNS record setup required; resolution handled by Twingate
- Accessible only via Twingate clients

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
No env vars or CLI flags. Aliases are configured per-Resource in the Twingate Admin Console.

## Gotchas

**HTTPS / TLS Certificate Errors**
- Aliases have no built-in HTTPS support → certificate errors when accessing HTTPS resources via alias
- Fix: Create/register a TLS certificate for the alias domain (use a controlled domain subdomain or distribute a private CA cert)

**HTTP Host Headers**
- HTTP requests via alias set `Host:` to the alias value (e.g., `Host: router.internal`)
- May affect virtual host routing on web servers

**`.local` TLD**
- Conflicts with mDNS/Bonjour (Apple, Linux zeroconf)
- Avoid `.local` aliases — use `.internal`, `.corp`, or a subdomain of a domain you control instead

**Single Label Domains**
- Aliases must contain at least one `.` (e.g., `twingate` is invalid; `twingate.internal` is valid)
- Use `name.internal`, `name.corp`, or `name.yourdomain.com`

## Recommended Alias Patterns
- `resource.internal`
- `resource.corp`
- `resource.yourdomain.com` (subdomain of controlled domain)

## Related Docs
- Resources configuration
- Connector setup
- DNS and split tunneling