# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) where no single component can independently authorize traffic flow. Authorization requires confirmation across multiple components, with user authentication delegated to a third-party IdP. Users access private Resources via FQDN or IP using local addressing without needing network configuration knowledge.

## Key Information

- **No single-component authorization**: Access decisions always require cross-component verification
- **Four components**: Controller (coordination), Client (user device proxy), Connector (remote network agent), Relay (connection broker)
- **Controller is data-plane isolated**: Only component that never touches actual data flow
- **Dual ACL intersection check**: Traffic only flows if destination Resource exists in *both* Client ACL and Connector ACL
- **Peer-to-peer preferred**: Client↔Connector P2P connections attempted first; Relay used as fallback (equivalent to TURN server)
- **Connector IDs are anonymized**: Only hash-generated IDs shared with Clients; no private network info exposed

## Component Responsibilities

| Component | Hosted By | Key Role |
|-----------|-----------|----------|
| Controller | Twingate (multi-tenant, clustered) | Config storage, ACL generation, Connector registration, auth delegation |
| Client | User device (installed software) | Auth proxy, DNS proxying, TCP/UDP proxying, ACL enforcement |
| Connector | Customer (behind firewall) | Traffic forwarding, local DNS resolution, Client verification |
| Relay | Twingate | Connector registration point, Client↔Connector matchmaking |

## Security Architecture Details

- **ACL signing**: Client ACLs are signed by Controller; Connector verifies signature on every inbound connection request (prevents tampering)
- **Certificate-pinned TLS**: Client establishes TLS tunnel to Connector pinned via signed connection token from Controller
- **Connector deployment**: Requires one-time Controller authorization; authenticates with anonymized hash ID thereafter
- **DNS resolution**: DNS lookups for protected Resources forwarded to Connector and resolved *locally* on the remote network
- **No application config needed**: Transparent proxy handles all TCP/UDP—apps behave as if connecting directly to Resources

## Connection Verification (Connector-side)
For every inbound Client connection, Connector verifies:
1. TLS tunnel integrity
2. Client signature validity
3. Client ACL claim validity

## Gotchas

- Connector must be deployed *behind* the remote network firewall—it uses outbound connections to Relay(s), not inbound
- The Relay stores **no** network-identifiable information and terminates **no** data-carrying connections
- User sync from IdP goes to Controller; authentication is always delegated externally (social identity or configured IdP)
- Connector ACL intersection with Client ACL acts as a second authorization check—misconfigured Connector ACLs can block authorized users

## Related Docs
- Connector deployment guide
- Identity Provider configuration
- Admin console configuration
- Relay documentation
- Client installation guide