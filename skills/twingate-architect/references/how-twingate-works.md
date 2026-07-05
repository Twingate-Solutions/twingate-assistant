# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) to implement zero-trust network access where no single component can independently authorize traffic flow. Authorization is always confirmed with at least two components, with user authentication delegated to a third-party IdP. Users access private Resources via FQDN or IP using network-local addressing without knowledge of underlying network topology.

## Key Information
- **No single component** can independently allow traffic — all authorization requires multi-component confirmation
- User authentication is always delegated to a third-party identity authority (IdP or social identity)
- Traffic access requires intersection of both Client ACL and Connector ACL — double authorization check
- DNS resolution for protected Resources happens locally on the Remote network (via Connector)
- No application configuration required on user devices — Client uses transparent TCP/UDP proxy
- TLS tunnel is certificate-pinned to a specific Connector using a signed connection token from Controller
- Peer-to-peer connection is always attempted first; Relay is fallback only

## Component Responsibilities

### Controller (Twingate-hosted, multi-tenant)
- Stores Admin console configuration
- Delegates user authentication to IdP
- Generates signed ACLs for Clients (least-privilege per user)
- Generates ACLs for Connectors (authorized forwarding destinations)
- Registers/authenticates Connectors (one-time authorization + hash-based anonymous ID)
- Does **not** interact with any data flow

### Client (installed on user devices)
- Authenticates users via Controller redirect to identity authority
- Obtains Controller-signed user ACL
- Intercepts DNS and TCP/UDP traffic to protected Resources
- Forwards DNS to Remote network Connector for local resolution
- Establishes certificate-pinned TLS tunnel to Connector

### Connector (deployed behind private firewall)
- Authenticates with Controller; receives and maintains Connector ACL
- Maintains outbound connections to one or more Relays
- Verifies TLS tunnel integrity, Client signature, and Client ACL claim on every inbound connection
- Performs local DNS resolution for FQDN Resources before forwarding

### Relay (Twingate-hosted, equivalent to TURN server)
- Stores only anonymous hash-based Connector IDs — no network-identifiable data
- No data-carrying connections terminate at the Relay
- Connects Clients to Connectors by Connector ID without knowing source/destination network details

## Security Design Gotchas
- Connector ACL acts as a **second check** on Client ACL — traffic only flows if destination is in both ACLs
- Connector ID shared with Clients is anonymized (hash-based) — no private network info exposed
- Client ACL signature is verified by Connector on every connection to prevent tampering
- Connectors cannot be deployed without one-time Controller authorization

## Prerequisites
- Configured Identity Provider (or social identity)
- Twingate Admin console access
- Client installed on user devices
- Connector deployed inside target private network

## Related Docs
- Client installation guide
- Connector deployment guide
- Relay documentation
- Identity Provider configuration
- Admin console configuration
- Connection flow detail (referenced as next article in series)