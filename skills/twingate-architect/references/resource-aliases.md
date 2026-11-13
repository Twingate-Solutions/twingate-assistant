---
source: https://www.twingate.com/docs/resource-aliases
type: docs
fetched: 2026-11-13
source_version: ce73ce64c21335abe5ef524caa82af9ba1e98df31c0ee834a8de362ce3d747dc
trust: official
---

# Page Title
Aliases (Twingate Resource Aliases)

## Summary
Aliases add an extra address to a Twingate Resource. Anyone with access to the Resource can use the alias, and it does not replace the original address. Aliases work only through Twingate, need no DNS records, and are protocol agnostic (a pseudo-A record usable only via Twingate).

## Key Information
- An alias is an additional address for a Resource, e.g. Resource `10.0.0.1` with alias `router.internal`. Both addresses work.
- Access to the alias follows access to the Resource.
- No DNS record setup is required.
- Works with any protocol.
- Minimum versions:
  - Connector: 1.50.0+
  - macOS: 1.0.27+
  - Windows: 1.0.29+
  - Linux: 1.0.79+
  - iOS: 1.0.27+
  - Android: 1.0.24+

## Prerequisites
- A Twingate Resource.
- Connector and Clients at or above the minimum versions listed above.

## Step-by-Step
The page doesn't describe configuration steps. It covers concepts, version requirements, and caveats only.

## Configuration Values
None are listed on this page. Alias naming guidance:
- Use a subdomain of a domain you control (e.g. `router.mywebsite.com`).
- Or use a private/internal name (e.g. `router.internal`, `router.corp`).

## Gotchas
- **HTTPS:** Accessing an HTTPS site via an alias causes certificate errors, because aliases have no built-in HTTPS support. To fix this, create and register a TLS certificate for the alias. Either use a domain you control or distribute a private certificate to your devices.
- **Host header:** HTTP requests to an alias set `Host: <alias>` (e.g. `Host: router.internal`). This can change which virtual host the server returns.
- **`.local` TLD:** Reserved for mDNS (Bonjour, zeroconf, limited Windows support). Aliases ending in `.local` may not work on many devices. Use an owned domain or `.internal`/`.corp` instead.
- **Single-label domains:** Aliases cannot be single-label (no `.`), e.g. `twingate` is invalid and `twingate.com` is valid.

## Related Docs
- Twingate Resources documentation
- Twingate Connector and Client release/version documentation