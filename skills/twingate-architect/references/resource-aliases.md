---
source: https://www.twingate.com/docs/resource-aliases
type: docs
fetched: 2026-11-22
source_version: 82290ecb081840d61b4fb9dd9f5e8aebfdc89c3363b3214f040ffe800987f440
trust: official
---

# Page Title
Aliases (Twingate Resource Aliases)

## Summary
Aliases add an extra address to a Twingate Resource. They work only through Twingate, need no DNS records, and don't replace the Resource's original address. Anyone with access to the Resource can use the alias.

## Key Information
- An alias is an additional address for a Resource. Example: a router at `10.0.0.1` with alias `router.internal` is reachable at either.
- Aliases are protocol agnostic and work with any protocol. Think of one as a pseudo-A record usable only via Twingate.
- No DNS records need to be set up.
- Access to the alias matches access to the Resource.

## Prerequisites
- An existing Twingate Resource.
- For HTTPS use: a TLS certificate for the alias (see Gotchas).

## Step-by-Step
The source page doesn't include setup steps. It covers only concepts and caveats.

## Configuration Values
None listed (no env vars, CLI flags, or API params in the source).

Alias naming constraints:
- Must not be a single label domain (must contain a `.`).
- Avoid the `.local` TLD.
- Recommended: a subdomain of a domain you control (e.g. `router.mywebsite.com`) or a private domain such as `router.internal` or `router.corp`.

## Gotchas
- **HTTPS:** Accessing HTTPS sites through an alias causes certificate errors, because aliases have no built-in HTTPS support. To fix this, create and register a TLS certificate for the alias. Either use a domain you control (e.g. a subdomain of your corporate domain) or create and distribute a private certificate to your devices.
- **Host header:** For HTTP, the host header is set to the alias (e.g. `Host: router.internal`). This can change which virtual host the server returns.
- **`.local` TLD:** It's reserved for local networking and mDNS (Apple Bonjour, Linux zeroconf, limited Windows support). Aliases using it may not work properly on many devices.
- **Single label domains:** These are not allowed. `twingate` is invalid, while `twingate.com` is valid.

## Related Docs
No related page URLs appear in the source material.