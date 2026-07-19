# Resource Aliases

## Summary
Aliases add extra addresses to Twingate Resources, accessible only through Twingate without requiring DNS record setup. They are protocol-agnostic and work alongside the original Resource address rather than replacing it.

## Key Information
- Aliases act as pseudo-A records resolvable only via Twingate
- Multiple addresses work simultaneously (original + alias)
- No DNS record configuration required
- Protocol-agnostic (works with any protocol)
- Anyone with access to the Resource can use the alias

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
- Set via Twingate Admin Console on a per-Resource basis
- No CLI flags or API params documented on this page

## Gotchas

**HTTPS / TLS**
- Aliases cause certificate errors with HTTPS Resources by default
- Fix: Create and register a TLS certificate for the alias domain (use a controlled domain or distribute a private cert)

**HTTP Host Headers**
- HTTP requests via alias set `Host:` to the alias value (e.g., `Host: router.internal`)
- May affect virtual host routing on the server side

**`.local` TLD**
- Conflicts with mDNS (Bonjour, zeroconf) — avoid `.local` aliases
- Use alternatives: `alias.internal`, `alias.corp`, or a subdomain of a domain you control

**Single Label Domains**
- Aliases must contain at least one `.` (e.g., `twingate` is invalid; `twingate.internal` is valid)

## Recommended Alias Patterns
- `resource.internal`
- `resource.corp`
- `resource.yourdomain.com` (if you control the domain)

## Related Docs
- Resources (general configuration)
- Connector setup and versioning
- DNS and split tunnel configuration