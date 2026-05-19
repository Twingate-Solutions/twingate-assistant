# Twingate Encryption Architecture

## Page Title
How Encryption Works in Twingate

## Summary
Twingate secures communications across four components: client-hosted Clients and Connectors, and Twingate-hosted Relays and Controller. All inter-component traffic is encrypted for confidentiality and authenticated to prevent impersonation. Notably, even Twingate's own Relays cannot decrypt Client-Connector traffic.

## Key Information
- **Four components**: Client (end-user device), Connector (behind firewall), Relay (Twingate-hosted), Controller (Twingate-hosted)
- **No inbound ports required** — Clients and Connectors initiate outbound connections only
- **Two encryption goals**: Confidentiality (no third-party decryption, including Twingate) + Authentication (verify legitimacy of Relays/Controller)
- **Client↔Relay/Controller**: Standard TLS/HTTPS with CA-signed certificates (same as browser-to-bank)
- **Client↔Connector**: Custom trust chain using Controller as root of trust; session key encrypted with Connector's self-signed cert public key
- **Relay cannot decrypt** Client↔Connector packets — session key is shared only between Client and Connector

## Client-to-Connector Trust Establishment (Step-by-Step)

1. Connector generates a public/private key pair and self-signed certificate at startup
2. Connector sends SHA-256 digest of its self-signed cert to Controller via regular heartbeat
3. Client requests Connector's self-signed certificate directly from Connector
4. Client requests a Connection Token (CT) from Controller
5. Controller issues a JWT (signed by Controller) containing the SHA-256 digest of Connector's cert
6. Client verifies CT authenticity and checks that Connector's cert digest matches the CT value
7. Client generates session key and shares it with Connector encrypted via Connector's public key
8. All subsequent traffic encrypted symmetrically with session key

## Configuration Values
None exposed to operators — encryption is handled automatically by Twingate components.

## Gotchas
- **Self-signed certs on Connectors are intentional** — trust is established via Controller-issued JWT, not CA chain
- **Connector restart regenerates key pair** — new self-signed cert and new heartbeat digest sent to Controller
- **Session key is ephemeral and client-generated** — Relays are transparent forwarders with no decryption capability
- The Controller is the **root of trust** for Client↔Connector authentication; Controller compromise would undermine this chain
- Twingate uses **Let's Encrypt** for signing Controller/Relay certificates

## Prerequisites
- Understanding of TLS/HTTPS helps but is not required for operators
- No operator configuration needed — encryption is built into all components

## Related Docs
- Twingate Client deployment
- Connector deployment and configuration
- Relay architecture
- Zero Trust Network Access overview