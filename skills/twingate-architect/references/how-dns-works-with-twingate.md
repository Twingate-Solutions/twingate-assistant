## Page Title
How DNS Works with Twingate

## Summary
Explains how the Twingate Client intercepts DNS for private resources and resolves them transparently without exposing the private DNS resolver to users. The Client assigns CGNAT addresses to resources and uses a local proxy to forward traffic through the Connector, which performs the actual DNS resolution.

## Key Information
- Client adds itself as the primary DNS resolver on the device (`100.95.0.251–254`)
- Private resource FQDNs resolve to CGNAT addresses (`100.64.0.0/10`, routing range `100.96/12`)
- Client modifies routing table: all traffic to CGNAT range routes through Twingate's virtual network interface (`utun` on macOS/Linux)
- Connector performs real DNS resolution against the private DNS server on the remote network
- Destination private IP is never exposed to the Client — it stays behind the Connector's transparent proxy
- Three proxies in the Client: TCP, UDP, ICMP (ping only)
- Same flow applies for resources with public DNS entries — resolution still passes through Connector, overriding direct DNS lookup
- Traffic is encrypted client-side — Twingate cannot decrypt network traffic

## Prerequisites
None — reference/overview page.

## Step-by-Step
Not applicable — see `dig` examples in the doc for diagnostic reference.

## Configuration Values
- CGNAT DNS resolvers added by Client: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- CGNAT routing range: `100.96/12`
- CGNAT assignment range: `100.64.0.0/10`

## Gotchas
- If a resource uses a public FQDN but you define it in Twingate, DNS still resolves through the Connector — the Connector's local DNS is authoritative, not the client's public resolver
- Split-tunnel: only traffic for Twingate resources routes through the virtual interface; all other traffic uses normal routing
- ICMP proxy supports ping only — other ICMP types are not proxied

## Related Docs
- `/docs/how-twingate-works` — full architecture overview
- `/docs/introduction-to-dns` — DNS primer
- `/docs/how-twingate-forwards-dns` — Connector-side DNS forwarding detail
- `/docs/private-dns-best-practices` — private DNS configuration recommendations
- `/docs/supporting-unqualified-domain-names` — search domain configuration
