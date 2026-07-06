# Encryption in Twingate

## Page Title
How Encryption Works in Twingate

## Summary
Twingate secures communications between Clients, Connectors, Relays, and Controller using TLS/HTTPS for public component authentication and a custom certificate-pinning scheme for Client-Connector trust. No inbound ports are required. Traffic between Clients and Connectors cannot be decrypted by Twingate or any intermediary, including Relays.

## Key Information

- **Four components**: Client (user device), Connector (customer infrastructure), Relay (Twingate-hosted), Controller (Twingate-hosted)
- **Two security goals**: Confidentiality (end-to-end encryption) and Authentication (verify legitimacy of components)
- **Client/Connector → Relay/Controller**: Standard TLS/HTTPS using CA-signed certificates (same as browser-to-bank)
- **Client ↔ Connector**: Custom trust chain using Controller as "root of trust" and Connector's self-signed certificate
- **Session encryption**: Asymmetric encryption used for key exchange only; symmetric session keys used for actual data transfer
- **Twingate CA**: Uses Let's Encrypt to sign certificates for `twingate.com` and hosted infrastructure

## Client-Connector Trust Flow (Step-by-Step)

1. **Connector startup**: Generates a public/private key pair and creates a self-signed certificate
2. **Connector heartbeat**: Sends SHA-256 digest/fingerprint of its self-signed certificate to Controller periodically
3. **Client connects**: Requests self-signed certificate directly from Connector
4. **Client requests Connection Token (CT)**: Asks Controller for a JWT signed by the Controller
5. **Controller issues CT**: JWT contains the SHA-256 digest of Connector's self-signed certificate (sourced from heartbeat)
6. **Client validates**: Verifies CT authenticity AND checks that the SHA-256 digest in CT matches the certificate received directly from Connector
7. **Trust established**: Client encrypts a session key using Connector's public key and shares it
8. **Data transfer**: All subsequent traffic encrypted with the symmetric session key

## Configuration Values

- **Connection Token format**: JWT signed by Controller
- **Certificate digest algorithm**: SHA-256
- **Applies to**: Both peer-to-peer and Relay-mediated Client-Connector connections

## Gotchas

- Relays **cannot decrypt** Client-Connector traffic — session key is only shared between Client and Connector
- Connector self-signed certificates are **not CA-signed**; trust is established via Controller's JWT (Controller is the root of trust, not a CA)
- The Controller must be reachable and trusted for any Client-Connector session to be established
- Compromising a Relay does not expose traffic content — it only carries encrypted packets

## Related Docs

- Twingate architecture overview (Clients, Connectors, Relays, Controller roles)
- Connector deployment documentation
- Network requirements / firewall configuration (no inbound ports needed)