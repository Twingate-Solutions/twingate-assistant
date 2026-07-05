# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes how Twingate Clients establish secure connections to Resources through a multi-step authorization and tunneling process. Clients intercept matching traffic via a local VPN tunnel, obtain Controller-signed tokens, establish certificate-pinned TLS connections through a Relay to a Connector, then proxy traffic to the Resource.

## Key Information
- Client establishes a **local VPN tunnel to 127.0.0.1** solely for traffic interception — this is NOT a remote VPN connection
- Access rules stored as a **signed whitelist ACL** delivered from Controller to Client at registration and on updates
- Connection requests for private Resources are **held** at the Client until all security checks pass — traffic never leaves the device if unauthorized
- **DNS resolution** for FQDN-based Resources occurs at the Connector (enables private/local DNS for off-network users)
- Non-matching traffic is **bypassed** through the host's existing routing table transparently

## Connection Flow Steps

1. **Detect request** — Client intercepts TCP/UDP traffic matching the Controller-signed whitelist ACL via local transparent proxy
2. **Obtain Connector authorization** — Client requests a time-bound token from Controller; response includes Relay FQDN and Connector certificate digest
3. **Establish cert-pinned TLS tunnel** — Client connects to Relay (mutual verification: Client validates Relay's public cert; Relay validates Client's Controller-signed token), then end-to-end TLS tunnel established to Connector, pinned to the Connector certificate digest
4. **Present signed ACL to Connector** — Client obtains a second Controller-signed token (user-specific ACL + Client public key); Connector verifies shared Controller trust; proof-of-possession (RFC 7800) used to confirm TLS tunnel integrity
5. **Proxy traffic** — Connector forwards connections to Resource; DNS resolved locally at Connector if Resource is FQDN-based

## Configuration Values
- Port restrictions configurable via Admin Console (optional, applies to proxied Resources)
- No environment variables or CLI flags specific to this flow (managed by Controller policy)

## Gotchas
- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is expected and does not indicate a remote VPN connection
- Resource destination addresses **do not need to be routable** from the Client device
- Authorization tokens are **time-bound** — expired tokens will require re-authorization
- MITM protection is enforced via RFC 7800 proof-of-possession in addition to certificate pinning
- Both TCP and UDP traffic is proxied regardless of port/protocol unless port restrictions are configured

## Prerequisites
- At least one Connector deployed and registered
- At least one Client registered with the Twingate network
- Resources defined in Admin Console with access rules assigned

## Related Docs
- Architecture Overview
- Connectors
- Resources
- Admin Console (access rules, port restrictions)
- RFC 7800 (proof-of-possession for JWTs)