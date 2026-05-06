# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Documents the 5-step process by which a Twingate Client establishes a secure, proxied connection to a private Resource via a Connector. Uses certificate-pinned TLS tunnels, Controller-signed tokens, and proof-of-possession (RFC 7800) to validate every connection. Non-matching traffic bypasses Twingate entirely.

## Key Information
- Client establishes a local VPN tunnel to `127.0.0.1` for traffic interception only — no remote VPN connection is made
- Whitelist ACL is signed by the Controller and stored locally on the Client
- All tokens are time-bound and connection-specific
- DNS resolution for FQDN Resources occurs **at the Connector**, enabling private/local DNS
- Non-Resource traffic is bypassed to the host's existing routing table and DNS resolvers
- Private Resource traffic never leaves the Client host device unless the user is authorized

## Connection Flow (5 Steps)

1. **Detect connection request** — Client's transparent proxy intercepts TCP/UDP traffic matching the Controller-signed whitelist ACL via local tunnel to `127.0.0.1`

2. **Obtain Connector authorization from Controller** — Controller returns:
   - Relay FQDN (for cert validation)
   - Hash of Connector ID (privacy-preserving Relay lookup)
   - Digest of Connector's TLS certificate (for pinning)

3. **Establish cert-pinned TLS tunnel via Relay** — Steps:
   - Client connects to Relay; Relay validates Controller-signed token
   - Relay confirms requested Connector (by ID hash) is connected
   - Client and Connector negotiate TLS; Connector cert digest must match Controller-provided digest

4. **Present Controller-signed authorization to Connector** — Steps:
   - Client sends its public key to Controller; Controller returns signed ACL + public key
   - Client signs a secret derived from the TLS tunnel context
   - Connector validates: Controller signature, Client public key, TLS session integrity (RFC 7800 proof-of-possession)

5. **Proxy traffic to Resource** — FQDN DNS resolved locally at Connector; proxied connection forwarded to Resource; source application is unaware of proxying

## Configuration Values
| Parameter | Description |
|---|---|
| Whitelist ACL | Delivered by Controller at registration and on updates |
| Relay FQDN | Provided per-connection by Controller authorization response |
| Connector cert digest | Provided per-connection for TLS pinning |
| Client key pair | Generated per Client; public key included in Controller-signed tokens |

## Gotchas
- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is **not** a remote VPN connection
- Requests to Resources are **held** by the transparent proxy until all auth checks complete — adds latency on first connection
- Certificate pinning requires the Connector cert digest to match exactly; cert rotation requires Controller coordination
- Connector ID is exposed to the Relay only as a hash — the Relay cannot identify the Connector directly
- UDP traffic is supported in addition to TCP, regardless of port or protocol

## Related Docs
- Architecture Overview
- Connector Registration Process
- RFC 7800 (Proof-of-Possession Key Semantics for JWTs)
- Resources configuration (Admin console)