# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the 5-step process by which a Twingate Client intercepts, authorizes, and proxies traffic to private Resources. The Client uses a local VPN tunnel (to localhost only) for interception, obtains time-bound Controller-signed tokens, and establishes certificate-pinned TLS via a Relay to the Connector.

## Key Information
- Client stores a Controller-signed whitelist ACL; only matching traffic is intercepted
- Non-matching traffic bypasses Twingate entirely via existing host routing table
- Local tunnel is to `127.0.0.1` only — no remote VPN connection is made
- All tokens are time-bound and signed by the Controller
- DNS resolution for FQDN Resources happens at the Connector (enables private/local DNS)
- Client supports transparent proxy for any TCP or UDP traffic regardless of port/protocol
- MITM protection via RFC 7800 proof-of-possession between Client and Connector

## Connection Flow Steps

1. **Detect resource request** — Client intercepts connection requests matching whitelist ACL via local transparent proxy; holds request until authorization completes
2. **Obtain Connector authorization** — Client requests token from Controller; response includes Relay FQDN and Connector certificate digest for pinning
3. **Establish certificate-pinned TLS to Connector** — Client connects through Relay (mutual identity verification), then establishes end-to-end TLS to Connector pinned to the certificate digest
4. **Present Controller-signed ACL** — Client makes second request to Controller for a user-specific signed ACL containing the Client's public key; Connector verifies it matches its own Controller authorization
5. **Proxy traffic** — Connector forwards traffic to Resource; DNS resolved locally at Connector if Resource is FQDN-based

## Security Mechanisms
| Mechanism | Purpose |
|---|---|
| Certificate pinning | Prevents MITM on Client→Connector TLS tunnel |
| Time-bound tokens | Limits validity window of authorization |
| RFC 7800 proof-of-possession | Verifies TLS tunnel integrity |
| Controller-signed ACL with public key | Binds authorization to specific Client |

## Gotchas
- OS may show a VPN notification due to the localhost tunnel — this is expected and does not indicate a remote VPN connection
- Network requests for private Resources **will not leave the device** unless the user is authorized; held by proxy until checks pass
- Port restrictions must be explicitly configured in Admin Console if needed (Client proxies all ports by default)
- Unroutable destination addresses are supported — the Client host does not need to route to the Resource directly

## Prerequisites
- At least one Connector deployed and registered
- At least one Client registered with the network
- Resources configured in Admin Console with access rules assigned

## Related Docs
- Architecture Overview
- Connectors
- Resources
- Admin Console (port restrictions configuration)