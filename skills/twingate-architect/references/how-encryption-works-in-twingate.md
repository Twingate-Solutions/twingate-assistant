# Twingate Encryption Architecture

## Page Title
How Encryption Works in Twingate

## Summary
Twingate secures communications between four components: customer-hosted Clients and Connectors, and Twingate-hosted Relays and Controller. The system provides confidentiality and authentication using TLS for public-facing components and a custom certificate-pinning scheme for Client-Connector traffic. Notably, even Twingate's own Relays cannot decrypt Client-Connector traffic.

## Key Information
- **Four components**: Client (end-user device), Connector (behind firewall), Relay (Twingate-hosted), Controller (Twingate-hosted)
- **No open inbound ports required** for operation
- **Two encryption layers**: TLS for Client/Connector→Relay/Controller; session key encryption for Client↔Connector
- **Controller is the root of trust** for Client-Connector authentication
- Twingate uses Let's Encrypt as its CA for `twingate.com` certificates
- End-to-end encryption: Relays cannot decrypt Client-Connector packets

## Client↔Connector Authentication Flow

1. Connector generates public/private key pair + self-signed certificate at startup
2. Connector sends SHA-256 digest of its certificate to Controller via heartbeat
3. Client connects → requests Connector's self-signed certificate
4. Client requests Connection Token (JWT) from Controller
5. Controller issues JWT containing the stored SHA-256 digest of Connector's certificate
6. Client verifies JWT authenticity AND matches digest against Connector's presented certificate
7. Trust established → Client encrypts a session key using Connector's public key
8. All subsequent Client↔Connector traffic uses symmetric session key encryption

## Configuration Values
- Connection Token format: **JWT signed by Controller**
- Certificate fingerprint algorithm: **SHA-256**
- Certificate type on Connector: **self-signed**, generated at startup

## Architecture Notes

| Component Pair | Encryption Method |
|---|---|
| Client/Connector → Controller/Relay | TLS (standard CA-signed certificates) |
| Client ↔ Connector | Session key via Connector's self-signed cert + Controller-issued JWT |

## Gotchas
- Connector generates a **new key pair at each startup** — the Controller tracks the current digest via heartbeat
- The self-signed certificate is **not CA-signed**; trust is established through the Controller's JWT, not a CA chain
- Relay transport is transparent to encryption — Client-Connector session key is opaque to Relays
- Both peer-to-peer and Relay-routed traffic use **identical** Client-Connector encryption process

## Related Docs
- Connector deployment documentation
- Controller architecture
- Relay configuration
- Zero Trust Network Access concepts