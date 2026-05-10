# Resource Aliases

## Summary
Aliases add extra addresses to Twingate Resources, accessible to anyone with Resource access. They function as pseudo-A records resolved only through Twingate—no external DNS setup required. Aliases don't replace original addresses; both work simultaneously.

## Key Information
- Aliases are protocol-agnostic (work with any protocol)
- No DNS record configuration needed
- Original Resource address remains functional alongside alias
- Alias resolves only through Twingate (not on public internet)

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
- Alias format: Must be multi-label domain (must contain at least one `.`)
- Example valid aliases: `router.internal`, `alias.corp`, `service.mywebsite.com`

## Gotchas

**HTTPS/TLS Errors**
- Aliases have no built-in HTTPS support → certificate errors will occur
- Fix: Create and register a TLS certificate for the alias domain
  - Option A: Use a subdomain of a domain you control
  - Option B: Create and distribute a private certificate to devices

**HTTP Host Headers**
- HTTP requests via alias set `Host:` header to the alias value (not original address)
- Can affect virtual host routing on web servers

**`.local` TLD — Avoid**
- Reserved for mDNS (Bonjour, zeroconf); causes resolution conflicts on most devices
- Use `.internal`, `.corp`, or a real subdomain instead

**Single Label Domains — Not Supported**
- Aliases must contain a `.` (e.g., `twingate` is invalid; `twingate.internal` is valid)

## Recommended Alias Patterns
- `service.internal`
- `service.corp`
- `service.yourdomain.com`

## Related Docs
- Twingate Resources configuration
- Connector setup and versioning
- TLS/certificate management for private resources