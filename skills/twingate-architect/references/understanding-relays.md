# Understanding Relays

## Summary
Relays facilitate secure connection establishment between Twingate Clients and Connectors for Resource access. They act as intermediaries in the end-to-end encrypted TLS tunnel but never terminate connections or store traffic data. Twingate operates a global network of Relay clusters across Google Cloud and DigitalOcean infrastructure.

## Key Information
- Relays facilitate (not terminate) connections between Clients and Connectors
- All traffic through Relays is already encrypted via certificate-pinned TLS tunnel
- Relays do **not** store traffic or network-identifiable information
- Each Connector connects to the geographically nearest available Relay
- Relay clusters provide redundancy: intra-cluster failover first, then nearest alternate cluster

## How Relays Work
1. Controller authorizes Client to access a Resource
2. New connection established between Client and Connector
3. Connection is end-to-end encrypted (certificate-pinned TLS)
4. Relay facilitates connection establishment; may also route encrypted tunnel when necessary
5. No connection termination occurs at the Relay

## Relay Cluster Locations

**Google Cloud**
- North America: Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia
- South America: São Paulo
- Europe: Eemshaven, Finland, Frankfurt, London, Zurich
- Middle East: Tel Aviv
- Africa: Johannesburg
- Asia: Hong Kong, Mumbai, Singapore, Taiwan, Tokyo
- Australia: Sydney

**DigitalOcean**
- North America: Atlanta, New York City, San Francisco, Toronto
- Europe: Amsterdam, Frankfurt, London
- Asia: Bengaluru, Singapore
- Australia: Sydney

## Reliability & Redundancy
- **Latency**: Connectors auto-select nearest available Relay
- **Redundancy tier 1**: Multiple Relays per cluster location
- **Redundancy tier 2**: If entire cluster fails, next nearest cluster activates automatically

## Data Privacy
- Traffic passes through Relays transiently only
- No storage of traffic or network-identifiable information
- Relays are mid-tunnel hops — encryption is already in place before reaching Relay
- No data connections terminated at Relay

## Gotchas
- Relays are Twingate-managed infrastructure; no self-hosted Relay option documented here
- Relay routing is automatic — no manual Relay selection by administrators
- Firewall rules must allow Connector outbound access to Relay endpoints (see related network docs)

## Related Docs
- Twingate Architecture / Controller documentation
- Connector deployment guides
- Network and firewall configuration requirements