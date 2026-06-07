# Understanding Relays

## Summary
Relays facilitate connection establishment between Twingate Clients and Connectors for accessing Resources. They act as intermediaries in the end-to-end encrypted TLS tunnel, routing traffic when direct connections aren't possible. Relays are Twingate-managed infrastructure and require no customer configuration.

## Key Information
- Relays facilitate (and sometimes carry) encrypted traffic between Clients and Connectors
- Connections are end-to-end encrypted via certificate-pinned TLS tunnels
- Relays do **not** terminate connections — encryption is maintained end-to-end
- Relays do **not** store traffic or network-identifiable information
- Traffic through Relays is already encrypted before reaching the Relay
- Connectors automatically connect to the geographically nearest available Relay
- Failover is automatic: within a cluster first, then to next nearest cluster

## Relay Cluster Locations

**Google Cloud:** Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia, São Paulo, Eemshaven, Finland, Frankfurt, London, Zurich, Tel Aviv, Johannesburg, Hong Kong, Mumbai, Singapore, Taiwan, Tokyo, Sydney

**DigitalOcean:** Atlanta, New York City, San Francisco, Toronto, Amsterdam, Frankfurt, London, Bengaluru, Singapore, Sydney

## Prerequisites
- None (customer-managed) — Relays are fully managed by Twingate
- Connectors must be able to reach Twingate Relay infrastructure (outbound)

## Configuration Values
- No customer-configurable parameters for Relays
- Relay selection is automatic based on Connector geography

## How It Works
1. Client requests access to a Resource → Controller authorizes
2. Client establishes connection to Connector via a Relay
3. Connector forwards traffic to the Resource
4. If direct Client↔Connector path unavailable, encrypted traffic routes through the Relay

## Gotchas
- Relay routing adds latency only when direct connection isn't possible; nearest Relay is always selected to minimize this
- Relays are shared Twingate infrastructure — not deployed per-customer
- If an entire Relay cluster location fails, the next nearest cluster is used automatically (no manual intervention)
- Data privacy: transient relay traffic is pre-encrypted and never stored or logged by the Relay

## Related Docs
- Twingate Architecture / Controller documentation
- Connector deployment guides
- Network requirements (firewall/egress rules for Relay endpoints)