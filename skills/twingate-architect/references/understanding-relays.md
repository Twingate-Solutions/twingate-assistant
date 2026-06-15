# Understanding Relays

## Summary
Relays facilitate secure connection establishment between Twingate Clients and Connectors for Resource access. They serve as intermediaries for encrypted tunnel routing without terminating or storing any traffic data. Twingate operates a global network of Relay clusters for low-latency, redundant connectivity.

## Key Information
- Relays facilitate (not terminate) the end-to-end encrypted TLS tunnel between Clients and Connectors
- Connection is certificate-pinned TLS; encryption is applied before reaching the Relay
- Connectors automatically connect to the geographically nearest available Relay
- Failover hierarchy: same-location cluster → next nearest cluster location
- Relays do **not** store traffic or network-identifiable information
- Data passing through Relays is already encrypted — Relays cannot read it

## Relay Cluster Locations

**Google Cloud:** Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia, São Paulo, Eemshaven, Finland, Frankfurt, London, Zurich, Tel Aviv, Johannesburg, Hong Kong, Mumbai, Singapore, Taiwan, Tokyo, Sydney

**DigitalOcean:** Atlanta, New York City, San Francisco, Toronto, Amsterdam, Frankfurt, London, Bengaluru, Singapore, Sydney

## Architecture Notes
- Relays are Twingate-managed infrastructure (no self-hosting required)
- Connectors initiate outbound connections to Relays
- When direct peer-to-peer Client↔Connector path is unavailable, traffic routes through the Relay
- No inbound firewall rules needed for Relay connectivity (Connectors connect outbound)

## Gotchas
- Relay routing is automatic — no configuration required or available for Relay selection
- Traffic *may* route through a Relay but doesn't always (direct connections are preferred when possible)
- Relay clusters are shared infrastructure; no dedicated Relay option exists
- Latency impact depends on geographic distance to nearest cluster — review cluster locations when planning Connector placement

## Prerequisites
- No direct prerequisites; Relay connectivity is handled automatically when a Connector is deployed

## Related Docs
- Connector deployment and configuration
- Understanding Connectors
- Network/firewall requirements (outbound Connector ports)
- Controller documentation