# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) where no single component can independently authorize traffic flow. Authorization requires confirmation across multiple components, with user authentication delegated to a third-party IdP. Users access private Resources via FQDN or IP using addresses local to the remote network.

## Key Information

- **No single point of authorization** — access decisions require intersection of Client ACL and Connector ACL
- **Controller** is the only component that never touches data flow
- **Client** handles all network routing and authorization decisions at the edge
- **Connector** deploys behind the firewall; maintains outbound connections to Relays (never requires inbound firewall rules)
- **Relay** is equivalent to a TURN server — no data terminated or stored there
- Twingate always attempts peer-to-peer (Client↔Connector); Relay is fallback
- DNS for protected Resources is resolved locally on the Remote network via the Connector
- No application configuration required on user devices — transparent proxy handles TCP/UDP

## Component Responsibilities

| Component | Hosted By | Key Role |
|-----------|-----------|----------|
| Controller | Twingate (multi-tenant) | Config, auth delegation, ACL generation, Connector registration |
| Client | User device | Auth proxy, ACL enforcement, DNS/traffic proxying |
| Connector | Customer network (behind firewall) | ACL verification, DNS resolution, traffic forwarding |
| Relay | Twingate | Connector registration point, Client↔Connector matchmaking |

## Authorization Flow (Dual ACL Check)
1. Controller generates **Client ACL** (Resources user can access)
2. Controller generates **Connector ACL** (Resources Connector can forward to)
3. Traffic only flows if destination is in **intersection** of both ACLs

## Security Architecture

- Connector registers with anonymized hash-generated unique ID — only identifier shared with Clients
- Client establishes **certificate-pinned TLS tunnel** to Connector
- Connector verifies: TLS tunnel integrity + Client signature + Client ACL claim validity on every connection
- Controller always delegates authentication to external identity authority (social or IdP)
- Connector cannot be deployed without one-time Controller authorization

## Gotchas

- Connectors make **outbound** connections to Relays — no inbound firewall rules needed on the remote network
- The Relay stores **no** identifying information about source/destination networks, Clients, or Connectors
- Connector ID is the **only** information about Connectors ever shared with Clients
- DNS resolution for FQDN Resources happens on the **remote network** side (via Connector), not the client side

## Related Docs
- Twingate Client installation
- Connector deployment
- Relay configuration
- Identity Provider integration
- Admin console configuration