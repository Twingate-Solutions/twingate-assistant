# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) to enforce zero-trust network access. No single component can independently authorize traffic flow; decisions require confirmation from multiple components. User authentication is always delegated to a third-party Identity Provider.

## Key Information

### Four Core Components

**Controller** (Twingate-hosted, multi-tenant)
- Central coordination; never touches data flow
- Delegates authentication to IdP/social identities
- Generates signed ACLs for both Clients and Connectors
- Registers/authenticates Connectors via one-time authorization
- Stores all Admin console configuration

**Client** (installed on user devices)
- Acts as authentication + authorization proxy
- Holds user-specific signed ACL from Controller
- Intercepts DNS requests → forwards to Connector for local resolution
- Proxies TCP/UDP traffic transparently (no app config needed)
- Establishes certificate-pinned TLS tunnel to Connector
- Matches destination addresses against ACL before routing

**Connector** (deployed behind private network firewall)
- Maintains outbound connections to Controller and Relay(s)
- Verifies TLS tunnel integrity, Client signature, and ACL validity on every inbound connection
- Performs local DNS resolution for FQDN Resources
- Cannot be deployed without one-time Controller authorization
- Identified only by anonymized hash-generated unique ID

**Relay** (equivalent to WebRTC TURN server)
- Stores only hash-based Connector IDs — no data, no network info
- Primary purpose: enable peer-to-peer Client↔Connector connections
- Relayed connections used as fallback when P2P fails
- No data-carrying connections terminate at Relay

## Security Architecture

- **Dual ACL check**: Traffic only flows if destination exists in *both* Client ACL and Connector ACL (intersection)
- **No single point of authorization**: Controller issues signed tokens; Connector independently verifies them
- **Certificate pinning**: TLS tunnel pinned to specific Connector via signed connection token
- **Anonymous Connector identity**: Only hash-based ID shared with Clients, never network details

## Connection Flow (High Level)
1. User authenticates via IdP (redirected by Controller)
2. Controller issues signed ACL to Client
3. Client detects connection request matching ACL Resource
4. Client contacts Controller for signed connection token referencing Connector ID
5. Client connects to Relay using Connector ID
6. Relay facilitates Client↔Connector tunnel (P2P attempted first)
7. Connector verifies Client signature + ACL claim
8. Traffic forwarded to Resource; DNS resolved locally by Connector

## Prerequisites
- Identity Provider configured (or social identity)
- Connector deployed in target private network with one-time authorization token
- Twingate Client installed on user devices
- Resources defined in Admin console

## Gotchas
- Connector requires outbound connectivity to both Controller and Relay — firewall rules must permit this
- DNS for protected Resources resolves on the remote network, not the client's local network
- Users access Resources using addresses **local to the remote network** — no special client-side network knowledge needed
- Connector ACL acts as a second independent check; misconfigured Connector ACL can block access even if Client ACL permits it

## Related Docs
- Connector deployment guide
- Identity Provider configuration
- Admin console reference
- Relay architecture deep-dive
- Client installation guide