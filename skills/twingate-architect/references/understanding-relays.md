# Understanding Relays

## Page Title
Understanding Relays

## Summary
Relays facilitate secure connections between Twingate Clients and Connectors for Resource-bound traffic. They act as intermediaries in the end-to-end encrypted TLS tunnel but never terminate connections or store traffic data. Twingate operates a global Relay network across Google Cloud and DigitalOcean infrastructure.

## Key Information
- Relays are used **only when necessary** to route the encrypted tunnel between Client and Connector
- Connections are end-to-end encrypted via certificate-pinned TLS tunnels
- Relays do **not** terminate connections — they are a transit hop only
- Relays do **not** store traffic or network-identifiable information
- Each Connector connects to the **geographically nearest** available Relay
- Multiple Relays per cluster location provide redundancy; if a cluster fails, next-nearest cluster is used automatically

## Relay Cluster Locations

**Google Cloud:** Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia, São Paulo, Eemshaven, Finland, Frankfurt, London, Zurich, Tel Aviv, Johannesburg, Hong Kong, Mumbai, Singapore, Taiwan, Tokyo, Sydney

**DigitalOcean:** Atlanta, New York City, San Francisco, Toronto, Amsterdam, Frankfurt, London, Bengaluru, Singapore, Sydney

## Data Privacy
- Traffic passing through Relays is already encrypted before it arrives
- No connection termination at Relay layer
- No persistent storage of traffic or network metadata

## Gotchas
- Relays are Twingate-managed infrastructure — no self-hosting option mentioned
- Relay routing is automatic; no manual selection of Relay cluster by operators
- Firewall rules must allow Connector outbound access to Relay endpoints (see network requirements docs)

## Related Docs
- Connector setup and configuration
- Controller documentation
- Network/firewall requirements for Connector-to-Relay communication