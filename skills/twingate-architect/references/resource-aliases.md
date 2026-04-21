## Resource Aliases

Aliases add a secondary address to any Resource, accessible alongside the primary address. Aliases are resolved by the Connector and do not require DNS records; they are protocol-agnostic but have specific limitations around HTTPS and special TLDs.

**Key Information:**
- An alias is an additional address for a Resource; both the original address and the alias work simultaneously
- Aliases are Twingate-only -- no external DNS registration required
- Protocol-agnostic: works with any protocol (effectively a virtual A record within Twingate)
- Access to the alias is automatically granted to anyone with access to the Resource

**Version Requirements:**
- Connector: 1.50.0+
- macOS Client: 1.0.27+
- Windows Client: 1.0.29+
- Linux Client: 1.0.79+
- iOS: 1.0.27+
- Android: 1.0.24+

**Gotchas:**
- **HTTPS:** Aliases cause TLS certificate errors unless a valid cert is issued for the alias domain. Use a subdomain of a domain you control or distribute a private CA cert.
- **Host headers:** HTTP requests to an alias set `Host: <alias>` -- this may affect virtual host routing on the backend server
- **`.local` TLD:** Avoid -- conflicts with mDNS (Bonjour/zeroconf); use `.internal`, `.corp`, or a subdomain of a controlled domain instead
- **Single-label domains:** Not supported (alias must contain a `.`); use `twingate.internal` instead of `twingate`

**Related Docs:**
- /docs/resources -- Resource configuration and address types
- /docs/supporting-unqualified-domain-names -- Alternative for short hostname access
