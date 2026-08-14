---
source: https://www.twingate.com/docs/detailed-client-connection-flow
type: docs
fetched: 2026-08-14
source_version: b8ff5889ead92140b465ef0fe5c27a84588afeff7b8d2883ca471ffe59b236c0
---

# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the five-stage process by which a Twingate Client establishes a secure, authorized connection to a Resource via a Connector. Each stage involves cryptographic verification between Client, Controller, Relay, and Connector components. No traffic reaches the destination Resource until all authorization checks pass.

## Key Information

- Client intercepts traffic via a local VPN tunnel to `127.0.0.1` (localhost only — not a remote VPN)
- Whitelist ACL is signed by the Controller and stored on the Client; updated on registration and changes
- Non-matching traffic is bypassed to the existing routing table transparently
- DNS resolution for FQDN Resources occurs **at the Connector** (enables private/local DNS)
- Certificate pinning is enforced end-to-end (Client → Connector) via digest provided by Controller
- Proof-of-possession per [RFC 7800](https://www.rfc-editor.org/rfc/rfc7800) prevents intermediary interference

## Prerequisites

- At least one Connector registered with the Twingate network
- At least one Client registered with the Twingate network
- Resources configured in the Admin console with access rules

## Step-by-Step: Connection Flow

1. **Detect resource request** — Client's local transparent proxy intercepts TCP/UDP traffic matching the Controller-signed whitelist ACL; holds the connection pending authorization
2. **Obtain Connector authorization from Controller** — Controller returns:
   - Relay FQDN for the relevant Connector
   - Hash of Connector ID (opaque to Relay)
   - Digest of Connector's TLS certificate (for pinning)
3. **Establish cert-pinned TLS tunnel via Relay**:
   - Client connects to Relay; validates Relay cert against FQDN
   - Relay verifies Client's Controller-signed token
   - Relay verifies target Connector is connected (by Connector ID hash)
   - Client and Connector establish TLS tunnel; Client pins against provided cert digest
4. **Present Controller-signed authorization to Connector**:
   - Client sends its public key to Controller; receives signed time-bound token containing ACL + Client public key
   - Client signs a secret derived from the TLS tunnel context
   - Client sends token + signed secret to Connector over the TLS tunnel
   - Connector validates: (a) Controller signature on token, (b) Client public key matches signed secret, (c) no TLS session tampering (RFC 7800)
5. **Proxy traffic to Resource**:
   - If FQDN Resource: DNS query forwarded to Connector; resolved locally at Connector
   - Connection forwarded from Client host to Resource via Connector
   - Application-layer connection (including any encryption) proceeds normally, unaware of proxying

## Configuration Values

| Item | Value/Notes |
|------|-------------|
| Local tunnel address | `127.0.0.1` (localhost) |
| Supported traffic | TCP and UDP, any port or protocol |
| Token lifetime | Time-bound (short-lived, connection-specific) |
| Client key pair | Generated per Client; public key included in Controller-signed tokens |

## Gotchas

- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is **not** a remote VPN connection
- Traffic for private Resources is **held at the Client** and never leaves the device unless the user is authorized
- DNS for FQDN Resources resolves at the Connector's network, not the Client's — ensures private DNS works off-network
- Each connection requires a fresh Controller-issued token; no caching of connection tokens

## Related Docs

- Architecture Overview
- Connector Registration Process
- Resources configuration
- RFC 7800 (Proof-of-Possession Key Semantics for JWTs)