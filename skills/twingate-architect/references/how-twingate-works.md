# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) to enforce zero-trust network access. No single component can independently authorize traffic flow; authorization requires confirmation across multiple components. User authentication is always delegated to a third-party Identity Provider.

## Key Information

### Four Core Components

**Controller** (Twingate-hosted, multi-tenant)
- Stores Admin console configuration
- Delegates authentication to IdP/social identities
- Generates signed ACLs for both Clients and Connectors
- Registers/authenticates Connectors via one-time authorization
- Never participates in data flow

**Client** (installed on user devices)
- Authenticates users via Controller-redirected identity authority
- Holds signed, user-specific ACL from Controller
- Intercepts DNS and TCP/UDP traffic to protected Resources
- Establishes certificate-pinned TLS tunnel to Connector
- Proxies DNS to Connector for local resolution on remote network

**Connector** (deployed behind private network firewall)
- Authenticates with Controller; receives and maintains Connector ACL
- Maintains outbound connections to one or more Relays
- Verifies TLS tunnel integrity, Client signature, and ACL claim validity on every inbound connection
- Performs local DNS resolution for FQDN Resources

**Relay** (equivalent to WebRTC TURN server)
- Stores only hash-based Connector IDs (no network-identifiable information)
- Connects Clients to Connectors without knowing source/destination network details
- No data connections terminate at the Relay; used as fallback when P2P fails

## Security Model

- **Dual ACL check**: Traffic only flows if the destination Resource exists in *both* the Client ACL and the Connector ACL (intersection set)
- **No single point of authorization**: Controller signs ACLs; Connector independently verifies signatures
- **Anonymous Connector identity**: Connectors register with hash-generated IDs; Clients never receive private network information
- **Certificate-pinned TLS**: Client-to-Connector tunnel is pinned to specific Connector via signed connection token from Controller
- **P2P preferred**: Direct Client↔Connector connection attempted first; Relay used as backup

## Prerequisites
- Identity Provider configured (or social identity)
- Connector deployed in private Remote network with outbound internet access
- Client installed on user devices
- Resources defined in Admin console with assigned access policies

## Connection Flow (High Level)
1. User authenticates via Client → Controller → IdP
2. Controller issues signed ACL to Client
3. Client intercepts traffic destined for protected Resource
4. Client requests connection token from Controller
5. Controller returns anonymous Connector ID + signed token
6. Client connects to Relay using Connector ID
7. Relay joins Client to Connector
8. Certificate-pinned TLS tunnel established; Connector verifies Client ACL signature
9. Connector performs DNS resolution and forwards traffic to Resource

## Gotchas
- Connectors require one-time Controller authorization before deployment; cannot self-register
- DNS for protected Resources resolves on the remote network via Connector, not client-side DNS
- Relay holds **no** persistent data; it only brokers the initial connection
- ACL intersection enforcement means misconfigured Connector ACLs can silently block access even if Client ACL permits it

## Related Docs
- Connector deployment guide
- Identity Provider configuration
- Admin console reference
- Relay architecture details
- Client installation guide