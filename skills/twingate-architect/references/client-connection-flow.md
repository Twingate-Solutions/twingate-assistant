# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the 5-step process by which a Twingate Client establishes a secure, authorized connection to a Resource. The Client intercepts matching traffic via a local VPN tunnel, obtains time-bound Controller-signed tokens, and establishes a certificate-pinned TLS tunnel through a Relay to a Connector before proxying traffic.

## Key Information
- Client stores a Controller-signed whitelist ACL; only traffic matching this ACL is intercepted
- Local tunnel to `127.0.0.1` enables traffic interception — this is **not** a VPN to any remote destination
- Non-matching traffic bypasses Twingate entirely (uses host's existing routing table)
- All authorization tokens are time-bound
- DNS for FQDN-based Resources resolves **at the Connector** (supports private/local DNS)
- MITM protection via RFC 7800 proof-of-possession between Client and Connector

## Connection Flow Steps

1. **Detect resource request** — Local tunnel intercepts TCP/UDP traffic matching whitelist ACL; holds connection until authorization completes
2. **Obtain Connector authorization** — Client requests token from Controller; response includes Relay FQDN and Connector certificate digest
3. **Establish certificate-pinned TLS to Connector** — Via Relay: Client validates Relay's public cert; Relay validates Client's Controller-signed token; Client↔Connector TLS tunnel pinned to Connector cert digest
4. **Present signed ACL to Connector** — Second Controller request returns user-specific signed ACL containing Client's public key; Connector verifies shared Controller trust + proof-of-possession
5. **Proxy traffic** — FQDN DNS resolved at Connector; traffic forwarded to Resource; source application unaware of proxying

## Configuration Values
- Port restrictions configurable via Admin Console (optional, for TCP/UDP)
- No client-side env vars or flags documented on this page

## Gotchas
- OS may display a VPN notification when Client starts — this refers only to the local `127.0.0.1` tunnel, not a remote VPN
- Network requests for private Resources **will not leave the device** if the user lacks authorization
- Certificate pinning is based on digest obtained from Controller — Connector cert changes require Controller coordination
- DNS resolution is remote (at Connector side), so client-side DNS config does not apply to FQDN Resources

## Prerequisites
- At least one Connector deployed and registered
- At least one Client registered with the Twingate network
- Resources configured in Admin Console with access rules assigned to users

## Related Docs
- Architecture Overview
- Connectors
- Resources
- Admin Console (port restrictions)
- RFC 7800 (proof-of-possession key semantics for JWTs)