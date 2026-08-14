---
source: https://www.twingate.com/docs/how-encryption-works-in-twingate
type: docs
fetched: 2026-08-14
source_version: 6d1f3edc17af9af7edc26bea53118d7741fe23fa1c93aa5c819ee23820b034f2
---

# Encryption in Twingate

## Summary
Twingate secures communications between Clients, Connectors, Relays, and Controller using TLS for public-facing components and a custom certificate-pinning scheme for Client-Connector traffic. No inbound ports are required because all connections are outbound. Twingate (including its own Relays) cannot decrypt Client-Connector traffic.

## Key Information

- **Four components**: Client (end-user device), Connector (behind firewall) — customer-hosted; Relay and Controller — Twingate-hosted
- **Two security goals**: Confidentiality (no third-party decryption, including Twingate) and Authentication (verify legitimacy of all components)
- **Client/Connector → Relay/Controller**: Standard TLS/HTTPS with CA-signed certificates (same as browser-to-bank)
- **Client ↔ Connector**: Custom trust chain using Controller as root of trust; session key encrypted with Connector's self-signed cert public key
- **Relay cannot decrypt** Client-Connector traffic; it only relays encrypted packets

## Client-Connector Trust Establishment (Step-by-Step)

1. Connector generates a public/private key pair and self-signed certificate at startup
2. Connector sends SHA-256 digest/fingerprint of its certificate to Controller via periodic heartbeat
3. Client connects → requests Connector's self-signed certificate
4. Client requests a **Connection Token (CT)** from Controller (JWT signed by Controller)
5. CT contains the SHA-256 digest of the Connector's certificate (sourced from heartbeat)
6. Client verifies CT authenticity and compares the digest from CT against digest received directly from Connector
7. On match, Client encrypts a session key using Connector's public key and shares it
8. All subsequent traffic encrypted via session key (symmetric)

## Encryption Flow Summary

| Communication Path | Method |
|---|---|
| Client → Controller | TLS (CA-signed cert) |
| Connector → Controller | TLS (CA-signed cert) |
| Client → Relay | TLS (CA-signed cert) |
| Client ↔ Connector (data) | Symmetric encryption via session key |

## Configuration Values
- None required; encryption is automatic and built into the Twingate components

## Gotchas

- **Relays are transit-only**: Even when traffic routes through Relays, the session key is never shared with them — Relays cannot inspect payload
- **Controller is root of trust**: Both Client and Connector must trust the Controller for the Client-Connector authentication to work
- **Self-signed certs are valid here**: Connector uses a self-signed certificate, but trust is established via Controller-signed JWT containing the cert digest — not CA validation
- **Heartbeat is security-critical**: The Connector's periodic heartbeat to Controller keeps the cert digest current; stale or missing heartbeats would break trust establishment

## Related Docs
- Twingate architecture overview
- Connector deployment documentation
- Relay configuration