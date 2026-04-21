## Resources

Comprehensive reference for configuring Twingate Resources -- the network addresses that Twingate secures and routes. Resources can be FQDNs, wildcards, IPs, or CIDR ranges; all must be reachable from the associated Remote Network's Connectors.

**Key Information:**
- Address types: FQDN, wildcard FQDN, IP address, CIDR range, unqualified hostname (with extra config)
- Wildcard rules: `*` matches 0+ characters, `?` matches exactly 1; `*.autoco.internal` matches subdomains but NOT `autoco.internal` itself
- CGNAT subnet `100.96.0.0/12` is reserved by Twingate Client -- cannot be used as Resource addresses
- Resources must be added to at least one Group to be accessible (default deny / zero-trust)
- Default: all TCP, UDP ports, and ICMP (ping) are forwarded; restrict per-Resource as needed
- Address resolution is performed from the Connector -- private DNS and private IPs resolve normally
- Aliases: additional addresses for a Resource; resolved by Connector without separate DNS entries
- Tags: optional metadata for organization; do not affect routing

**Specificity Rules (overlapping addresses):**
- Single IP > CIDR range; smaller CIDR > larger CIDR
- Exact FQDN > wildcard; wildcard with more literal characters > broader wildcard
- Truly ambiguous Resources are chosen arbitrarily -- avoid overlapping where possible

**Port Restriction Details:**
- Requires all Connectors in the Remote Network to be v1.20.0+
- TCP and UDP restricted independently; ICMP can be toggled
- Create two Resources with the same address but different port ranges to grant different Groups different access levels (e.g., `:443` for all users, `:22` for admins only)

**Client Visibility Options:**
- `Standard Address` -- visible in main Client list
- `Browser Address` -- visible + browser shortcut
- `Background Address` -- hidden under "Hidden Resources"
- Minimum Client versions: macOS 1.0.25, Windows 1.0.23, iOS 1.0.25, Android 1.0.22, Linux 1.0.74

**Gotchas:**
- Public FQDNs resolving to private IPs should be configured as DNS Resources (not IP-based) due to DNS rebinding protection in modern resolvers
- Invalid CIDR notation (e.g., `10.1.0.1/16`) returns `Invalid IP or FQDN` -- use the correct network address (e.g., `10.1.0.0/16`)

**Related Docs:**
- /docs/remote-networks -- Remote Network and Connector association
- /docs/how-does-twingate-work -- DNS and routing internals
- /docs/supporting-unqualified-domain-names -- Unqualified hostname configuration
- /docs/resource-aliases -- Alias configuration
- /docs/ip-overlap -- Managing overlapping address spaces
