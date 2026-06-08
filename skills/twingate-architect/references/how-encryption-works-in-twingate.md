# Twingate Encryption Architecture

## Summary
Twingate secures communications between Clients, Connectors, Relays, and Controllers using TLS for public-facing components and a custom certificate-pinning scheme for Client-Connector traffic. End-to-end encryption ensures even Twingate's own Relays cannot decrypt user traffic. No inbound ports are required because all connections are outbound-initiated.

## Key Information
- **Two goals**: Confidentiality (traffic unreadable by third parties including Twingate) and Authentication (components verify legitimacy of peers)
- **Four components**: Client (user device), Connector (customer infrastructure), Relay (Twingate-hosted), Controller (Twingate-hosted)
- **Client/Connector → Relay/Controller**: Standard TLS/HTTPS using CA-signed certificates (same as browser-to-website)
- **Client ↔ Connector**: Custom mutual authentication using Controller as root of trust + self-signed certificates
- **Session encryption**: Asymmetric crypto used only for key exchange; symmetric session keys used for actual data transfer
- **Relay cannot decrypt**: Client-Connector traffic is end-to-end encrypted; Relays are transport-only

## Client-Connector Authentication Flow
1. Connector generates public/private key pair + self-signed certificate at startup
2. Connector sends SHA-256 digest of its certificate to Controller via heartbeat
3. Client requests Connector's self-signed certificate directly from Connector
4. Client requests Connection Token (JWT) from Controller
5. Controller issues JWT containing the stored SHA-256 digest of Connector's certificate
6. Client verifies JWT authenticity AND that Connector's cert digest matches Controller's stored digest
7. Trust established → Client encrypts session key using Connector's public key
8. All subsequent traffic encrypted with session key (symmetric)

## Configuration Values
- Certificate digest algorithm: **SHA-256**
- Connection Token format: **JWT** (signed by Controller)
- Connector certificate type: **self-signed** (generated at startup)

## Architecture Notes
| Component | Certificate Type | Trust Source |
|-----------|-----------------|--------------|
| Relay | CA-signed | Public CA infrastructure |
| Controller | CA-signed | Public CA infrastructure |
| Connector | Self-signed | Controller (root of trust) |

## Gotchas
- Connector regenerates its key pair on each startup — Controller tracks current digest via heartbeat
- The Controller is the **root of trust**; if Client cannot reach Controller to get a Connection Token, Client-Connector trust cannot be established
- Relays handle encrypted packets only — they have zero ability to inspect payload content
- Self-signed certificates on Connectors are intentional; CA validation is replaced by Controller-mediated certificate pinning

## Related Docs
- Twingate Relay documentation
- Connector deployment guides
- Controller architecture overview