# Resource Aliases

## Summary
Aliases add extra addresses to Twingate Resources, accessible to anyone with Resource access without replacing the original address. They function as pseudo-A records that only work via Twingate and require no DNS setup. Aliases are protocol agnostic but have caveats for HTTPS and certain domain formats.

## Key Information
- Aliases are additional addresses on top of existing Resource addresses (both work simultaneously)
- Only accessible via Twingate — no external DNS records needed
- Protocol agnostic: works with any protocol
- All users with Resource access can use the alias

## Prerequisites
Minimum versions required:
- **Connector**: 1.50.0+
- **macOS Client**: 1.0.27+
- **Windows Client**: 1.0.29+
- **Linux Client**: 1.0.79+
- **iOS**: 1.0.27+
- **Android**: 1.0.24+

## Configuration Values
- Aliases must be multi-label domains (must contain a `.`)
- Avoid `.local` TLD (conflicts with mDNS/Bonjour/zeroconf)
- Recommended formats: `alias.internal`, `alias.corp`, `alias.yourcompany.com`

## Gotchas

**HTTPS Certificate Errors**
- Aliases have no built-in HTTPS support → browser certificate errors will occur
- Fix: Create and register a TLS certificate for the alias domain
  - Option A: Use a subdomain of a domain you control
  - Option B: Create and distribute a private/internal certificate

**Host Header Behavior**
- HTTP connections set `Host:` header to the alias value (not original address)
- May affect virtual host routing on servers

**`.local` TLD**
- Reserved for mDNS (Bonjour, zeroconf) — alias may not resolve correctly on many devices
- Avoid `.local`; use `.internal`, `.corp`, or a controlled subdomain instead

**Single Label Domains**
- Aliases cannot be single-label (no `.` in name, e.g., `router`)
- Must use format like `router.internal` or `router.corp`

## Related Docs
- Twingate Resources configuration
- Connector setup and versioning
- TLS certificate management (external)