# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) where no single component independently authorizes traffic flow. Authorization requires confirmation from multiple components, with user authentication delegated to a third-party IdP. Users access Resources via local FQDNs/IPs without needing network topology knowledge.

## Key Information

- **No single point of authorization** — traffic allowed only at intersection of Client ACL and Connector ACL
- **Controller** is the only component that never touches data flow
- **Four components**: Controller (hosted SaaS), Client (user device), Connector (behind firewall), Relay (connection broker)
- **Connector ACL ∩ Client ACL** = actual accessible Resources (double-check mechanism)
- Relay is equivalent to a TURN server; stores no data, no network-identifiable info
- Twingate always attempts peer-to-peer (Client↔Connector); Relay used as fallback
- DNS for protected Resources resolves locally via Connector (not public DNS)

## Component Responsibilities

| Component | Key Role |
|-----------|----------|
| Controller | Config storage, ACL generation, Connector registration, IdP delegation |
| Client | Auth proxy, ACL enforcement, DNS proxying, TLS tunnel establishment |
| Connector | ACL verification, Relay connectivity, inbound connection validation, local DNS resolution |
| Relay | Connector registration point, Client-to-Connector connection broker |

## Architecture Flow

1. Controller delegates user auth to IdP
2. Controller issues signed user ACL to Client
3. Controller issues Connector ACL to Connector
4. Connector registers anonymous hash-based ID with Relay
5. Client detects connection request to protected Resource
6. Client requests connection token from Controller
7. Client connects to Relay using Connector ID (no private network info exposed)
8. Relay brokers single certificate-pinned TLS tunnel between Client and Connector
9. Connector verifies TLS integrity, Client signature, and ACL claim validity
10. Connector performs local DNS resolution and forwards traffic

## Security Properties

- Connectors cannot deploy without one-time Controller authorization
- Connector identified only by anonymized hash-based ID (no IP/network info shared with Clients)
- Client ACL is Controller-signed; signature verified by Connector on every connection
- TLS tunnel is certificate-pinned to specific Connector
- Connector ACL serves as independent second check on Client ACL claims

## Gotchas

- Connector must be deployed **behind** the firewall of the private network — it makes outbound connections to Relay, not inbound
- Relay never terminates data-carrying connections — it only brokers the tunnel establishment
- Controller is multi-tenant SaaS (Twingate-hosted); not self-hostable
- Connector ID shared with Clients is anonymized — Clients never learn actual Connector network location

## Related Docs
- Identity Provider configuration
- Admin console
- Client installation
- Connector deployment
- Relay configuration