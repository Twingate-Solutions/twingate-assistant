# Understanding Relays

## Page Title
Understanding Relays

## Summary
Relays facilitate secure connection establishment between Twingate Clients and Connectors for resource access. They serve as routing hops within end-to-end encrypted TLS tunnels but do not terminate connections or store traffic data. Twingate operates a global network of Relay clusters across Google Cloud and DigitalOcean infrastructure.

## Key Information
- Relays facilitate (not terminate) connections between Clients and Connectors
- Connection tunnel is end-to-end encrypted, certificate-pinned TLS
- Relay involvement: connection establishment always; data routing when necessary
- Each Connector connects to the geographically nearest available Relay
- Relay clusters provide redundancy: failover within location first, then next nearest cluster
- Relays are Twingate-managed infrastructure (not self-hosted)
- No traffic data or network-identifiable information is stored at Relays
- Traffic passing through Relays is already encrypted end-to-end

## Prerequisites
- None (Relays are fully managed by Twingate — no user configuration required)

## Configuration Values
- None — Relay selection and failover are automatic; no user-configurable parameters

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
- North America: Atlanta, Richmond (VA), New York City, San Francisco, Toronto
- Europe: Amsterdam, Frankfurt, London
- Asia: Bengaluru, Singapore
- Australia: Sydney

## Gotchas
- Relays are on the data path only "when necessary" — direct Client-to-Connector connections are preferred when possible
- Relay routing adds potential latency; geographic proximity is used to minimize this
- Encrypted data does traverse Twingate-controlled Relay infrastructure transiently (relevant for compliance considerations)
- No self-hosted Relay option documented here

## Related Docs
- Twingate Controllers (authorization component referenced)
- Twingate Connectors (paired component that connects to Relays)
- Twingate Clients (endpoint component)
- Network architecture / security model documentation