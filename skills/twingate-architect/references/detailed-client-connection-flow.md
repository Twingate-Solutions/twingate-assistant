# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Documents the 5-stage process by which a Twingate Client establishes a secure, authorized connection to a private Resource via a Connector. Each stage involves cryptographic verification to ensure only authorized clients access resources without exposing traffic prematurely.

## Key Information
- Client intercepts traffic via local tunnel to `127.0.0.1` — this is **not** a VPN to any remote destination
- Non-matching traffic bypasses Twingate entirely (existing routing/DNS used)
- Network requests for private Resources **never leave the client device** unless authorization succeeds
- DNS for FQDN-based Resources resolves **at the Connector** (enables private/local DNS)
- Certificate pinning is enforced end-to-end (Client → Relay → Connector)
- Implements RFC 7800 proof-of-possession to prevent MITM

## Connection Flow Steps

1. **Detect Resource Request** — Client intercepts TCP/UDP traffic matching whitelist ACL (signed by Controller); holds connection pending auth
2. **Obtain Connector Authorization** — Client requests token from Controller; receives Relay FQDN, Connector ID hash, and Connector certificate digest
3. **Establish Certificate-Pinned TLS to Connector** — Client connects to Relay → Relay validates Controller-signed token → Relay verifies Connector is connected → Client and Connector negotiate TLS pinned to expected cert digest
4. **Present Controller-Signed Authorization** — Client requests connection-specific token (includes Client public key) → Controller returns signed ACL + Client public key → Client signs TLS tunnel-derived secret → sends both to Connector for validation
5. **Proxy Traffic** — Connector forwards DNS (if FQDN) and proxied TCP/UDP to Resource; source application unaware of proxying

## Configuration Values
| Item | Value |
|------|-------|
| Local tunnel destination | `127.0.0.1` |
| Protocols proxied | TCP and UDP (all ports) |
| Token type | Time-bound, Controller-signed |
| Key binding | Client public/private key pair per client |
| Proof-of-possession spec | RFC 7800 |

## Gotchas
- OS may show a VPN notification — this refers only to the local `127.0.0.1` tunnel, **not** a remote VPN
- Resource destination address does **not** need to be routable from the client device
- Token is bound to the specific TLS session — replay/MITM attacks are blocked via tunnel-derived secret signing
- Each connection request requires a fresh Controller token; tokens are time-bound
- Connector certificate digest is provided by Controller — pinning is automatic, not manually configured

## Prerequisites
- At least one Connector registered and running
- Twingate Client installed and user-authenticated
- Resources configured in Admin console with access rules assigned

## Related Docs
- Architecture Overview
- Connector Registration Process
- Relay documentation
- Resource and ACL configuration (Admin console)