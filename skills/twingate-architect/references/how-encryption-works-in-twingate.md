# Encryption in Twingate

## Page Title
How Encryption Works in Twingate

## Summary
Twingate secures communications between Clients, Connectors, Relays, and Controller using TLS for public-facing components and a custom mutual authentication scheme for Client-Connector traffic. No inbound ports are required because all connections are outbound. Twingate (including Relay operators) cannot decrypt Client-Connector traffic.

## Key Information
- **Two security goals**: Confidentiality (no third-party decryption, including Twingate) and Authentication (components verify legitimacy of peers)
- **Four components**: Client and Connector (customer-hosted); Relay and Controller (Twingate-hosted)
- **Client/Connector → Relay/Controller**: Standard TLS/HTTPS with CA-signed certificates (same as browser-to-bank)
- **Client ↔ Connector**: Custom scheme using Controller as root of trust; encrypted with session key that Relays cannot decrypt
- **Transport agnostic**: Client-Connector encryption applies whether traffic is peer-to-peer or routed through Relays

## Client-Connector Authentication Flow (Step-by-Step)

1. **Connector startup**: Generates RSA public/private key pair; creates self-signed certificate
2. **Connector heartbeat**: Sends SHA-256 digest/fingerprint of its self-signed cert to Controller periodically
3. **Client connects**: Requests self-signed certificate directly from Connector
4. **Client requests Connection Token (CT)**: JWT signed by Controller, containing SHA-256 digest of Connector's certificate
5. **Client validates**: Compares SHA-256 digest in CT (from Controller) against digest received directly from Connector
6. **Trust established**: Client encrypts session key using Connector's public key; sends to Connector
7. **Encrypted session**: All subsequent data encrypted with session key (symmetric)

## Configuration Values
- None exposed to end users; internal to Twingate components
- Certificate digest algorithm: **SHA-256**
- Connection Token format: **JWT** signed by Controller

## Key Cryptographic Details
| Component | Method |
|-----------|--------|
| Relay/Controller auth | TLS with CA-signed certs (standard PKI) |
| Connector identity | Self-signed cert + SHA-256 fingerprint |
| Session establishment | Asymmetric (RSA) key exchange |
| Data transfer | Symmetric session key |
| CT signing | JWT signed by Controller private key |

## Gotchas
- Relays **cannot decrypt** Client-Connector traffic — session key is shared only between Client and Connector
- Connector generates a **new** key pair at each startup — fingerprint in Controller updates via heartbeat
- Controller is the **root of trust**; if Controller is compromised, the authentication chain breaks
- Clients come prepackaged with CA root certificates to validate Relay/Controller TLS certs (standard browser behavior)

## Prerequisites
- No special configuration needed by end users; encryption is automatic
- Connector must have outbound connectivity to Controller to maintain heartbeat/fingerprint registration

## Related Docs
- Twingate architecture overview
- Connector deployment documentation
- Relay documentation
- Zero Trust network access concepts