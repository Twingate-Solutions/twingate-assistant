# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) to enforce zero-trust network access. No single component can independently authorize traffic flow—authorization requires confirmation across multiple components. User authentication is always delegated to a third-party Identity Provider.

## Key Information

### Four Core Components

**Controller** (Twingate-hosted, multi-tenant)
- Stores Admin console configuration
- Delegates authentication to IdPs
- Generates signed ACLs for both Clients and Connectors
- Registers/authenticates Connectors via one-time authorization
- Never touches data flow

**Client** (installed on user devices)
- Acts as auth/authorization proxy
- Obtains Controller-signed user ACL
- Intercepts connections to protected Resources (IP or FQDN)
- Proxies DNS requests to remote Connector (local resolution semantics)
- Proxies TCP/UDP traffic transparently (no app config required)
- Establishes certificate-pinned TLS tunnel to Connector

**Connector** (deployed behind private network firewall)
- Authenticates with Controller; receives and maintains Connector ACL
- Maintains active outbound connections to Relay(s)
- Verifies inbound Client TLS tunnel integrity, Client signature, and ACL claim validity
- Performs local DNS resolution for FQDN Resources

**Relay** (Twingate-hosted)
- Equivalent to WebRTC TURN server
- Stores only hash-based Connector IDs—no network-identifiable data
- Connects Clients to Connectors via anonymous Connector ID
- Used as fallback; peer-to-peer is attempted first

## Security Model

- **Dual ACL intersection**: Traffic only flows if Resource appears in *both* Client ACL and Connector ACL
- **Signed ACLs**: Controller signs Client ACL; Connector verifies signature on every connection request
- **Anonymous Connector IDs**: Hash-generated; Clients never receive private network topology info
- **Certificate-pinned TLS**: Tunnel pinned to specific Connector via signed connection token from Controller
- **No single point of trust**: Authorization requires multi-component confirmation

## Prerequisites
- Identity Provider configured (or social identity)
- Connector deployed with one-time Controller authorization
- Twingate Client installed on user devices
- Resources defined in Admin console

## Connection Flow (High Level)
1. User authenticates via Client → Controller redirects to IdP
2. Controller issues signed ACL to Client
3. Client detects connection request matching ACL Resource
4. Client contacts Controller for signed connection token
5. Client connects to Relay using anonymous Connector ID
6. Relay bridges Client to Connector
7. Connector verifies Client signature and ACL validity
8. Certificate-pinned TLS tunnel established; traffic proxied

## Gotchas
- Connectors cannot be deployed without initial one-time Controller authorization
- DNS for protected Resources resolves on the remote network, not locally on the client device network
- Peer-to-peer is preferred; Relay is fallback only
- Users see Resources by their remote-network-local FQDN/IP—no knowledge of underlying network topology required

## Related Docs
- Connector deployment guide
- Client installation guide
- Identity Provider configuration
- Relay documentation
- Admin console reference