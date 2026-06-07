# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) where no single component can independently authorize traffic flow. Authorization requires confirmation from multiple components, with user authentication delegated to third-party Identity Providers. The result is zero-trust network access where users connect to resources using local FQDNs/IPs without knowing underlying network topology.

## Key Information

### Four Core Components

**Controller** (Twingate-hosted, multi-tenant)
- Stores admin configuration; delegates auth to IdP
- Generates signed ACLs for both Clients and Connectors
- Registers/authenticates Connectors via one-time authorization
- Only component that never touches data flow
- Issues signed connection tokens to Clients

**Client** (installed on user devices)
- Acts as auth + authorization proxy for private resource access
- Intercepts DNS requests → forwards to Connector for local resolution
- Transparent proxy for TCP/UDP (no app config needed on device)
- Establishes certificate-pinned TLS tunnel to Connector
- Verifies signed ACL from Controller before routing decisions

**Connector** (deployed behind private network firewall)
- Maintains outbound connections to Controller and Relay(s)
- Verifies TLS tunnel integrity, Client signature, and ACL validity on every inbound connection
- Performs local DNS resolution for FQDN resources
- Cannot be deployed without one-time Controller authorization

**Relay** (equivalent to WebRTC TURN server)
- No data stored; no data connections terminated here
- Registers Connectors by anonymous hash-based ID only
- Connects Clients to Connectors without knowing source/destination network details
- Fallback when peer-to-peer Client↔Connector is unavailable

## Security Model

- **Dual ACL check**: Traffic only flows if destination falls in the intersection of Client ACL AND Connector ACL
- **Anonymized Connector IDs**: Hash-generated; only identifier shared with Clients
- **ACL signature verification**: Connector verifies Controller's signature on Client ACL to prevent tampering
- **P2P preferred**: Twingate always attempts direct Client↔Connector connection; Relay used as backup

## Prerequisites
- Identity Provider (IdP) configured or social identity available
- Connectors deployed behind remote network firewalls
- Twingate Client installed on user devices
- One-time authorization from Controller to deploy each Connector

## Connection Flow (High Level)
1. User authenticates via Client → redirected to IdP by Controller
2. Controller issues signed, user-specific ACL to Client
3. Client detects connection request matching ACL resource
4. Client requests signed connection token from Controller for specific Connector
5. Client connects to Relay using anonymous Connector ID
6. Relay bridges Client↔Connector
7. Certificate-pinned TLS tunnel established
8. Connector verifies Client ACL signature and tunnel integrity
9. Traffic proxied to resource; DNS resolved locally by Connector

## Gotchas
- Connector ACL intersection with Client ACL is a **second enforcement layer** — misconfigured Connector ACLs will silently block access even if Client ACL permits it
- DNS for protected resources is always resolved on the remote network (local to resource), not on the user's network
- Peer-to-peer is attempted first; Relay is fallback only — latency characteristics differ between the two paths
- Connector registration requires outbound connectivity to both Controller and at least one Relay

## Related Docs
- Connector deployment guide
- Identity Provider configuration
- Relay architecture details
- Admin console configuration
- Client installation