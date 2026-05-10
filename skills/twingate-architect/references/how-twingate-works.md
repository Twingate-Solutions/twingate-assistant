# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) where no single component can independently authorize traffic flow. Authorization requires confirmation from multiple components, with user authentication delegated to a third-party IdP. Users access Resources via local FQDNs/IPs without needing network topology knowledge.

## Key Information

- **No single component** can independently allow traffic — all authorization requires multi-component confirmation
- **Four components**: Controller (coordination), Client (user device proxy), Connector (private network gateway), Relay (connection broker)
- Controller is Twingate-hosted, multi-tenant, fully redundant — it never touches data flow
- Client handles all routing/authorization decisions at the edge
- Connector deploys **behind** the firewall; maintains outbound connections to Relays
- Relay is stateless — no data or network-identifiable info stored; equivalent to WebRTC TURN server
- Twingate always attempts **peer-to-peer** Client↔Connector connections; Relay is fallback

## Component Responsibilities

### Controller
- Stores admin config from Admin console
- Delegates auth to IdP; syncs users from IdP
- Generates signed ACLs for Clients (least-privilege Resources per user)
- Generates ACLs for Connectors (authorized forwarding destinations)
- Registers Connectors with one-time authorization; assigns anonymized hash-based Connector ID

### Client
- Authenticates users via identity authority redirect
- Obtains Controller-signed user ACL
- Intercepts network requests; matches destination to ACL
- Proxies DNS to remote Connector (resolves locally on remote network)
- Proxies TCP/UDP transparently (no app config needed on device)
- Establishes certificate-pinned TLS tunnel to Connector using anonymous Connector ID

### Connector
- Authenticates with Controller; receives and maintains Connector ACL
- Maintains outbound connections to one or more Relays
- Verifies: TLS tunnel integrity, Client signature, Client ACL claim validity — on every inbound connection
- Performs local DNS resolution for FQDN Resources before forwarding

### Relay
- Registers Connectors by hash-based Connector ID (only data stored)
- Brokers Client→Connector connections using Connector ID only
- No network-identifiable info about source/destination stored or exposed

## Security Design Gotchas

- **Dual ACL intersection**: Traffic only forwards if Resource appears in **both** Client ACL and Connector ACL — neither alone is sufficient
- Client ACL is **signed by Controller**; Connector verifies signature to prevent tampering
- Connector ID shared with Clients is **anonymized hash** — no private network info exposed via Relay
- Connector deployment requires **one-time authorization** from Controller before it can operate
- DNS for protected Resources resolves on the **remote network**, not the client network

## Prerequisites
- Identity Provider configured (or social identity)
- Connector deployed behind target network firewall
- Twingate Client installed on user devices
- Resources and access policies configured in Admin console

## Related Docs
- Twingate Client installation
- Connector deployment
- Relay configuration
- Identity Provider integration
- Admin console configuration
- Connection flow detail (next article in series)