# Understanding Relays

## Page Title
Understanding Relays

## Summary
Relays facilitate connection establishment between Twingate Clients and Connectors for Resource access. They operate as hops within end-to-end encrypted TLS tunnels and may route encrypted traffic when direct connections aren't possible. Relays are Twingate-managed infrastructure requiring no customer configuration.

## Key Information
- Relays facilitate (and sometimes route) the encrypted tunnel between Client and Connector
- Connections are end-to-end encrypted via certificate-pinned TLS tunnels
- Relays do **not** terminate connections or decrypt traffic
- Relays do **not** store traffic or network-identifiable information
- Each Connector connects to the geographically nearest available Relay
- Relay clusters provide redundancy: failure within a cluster falls over to another node; full cluster failure falls over to next nearest cluster

## Prerequisites
- No customer action required — Relays are fully managed by Twingate
- Connectors must be able to reach Twingate Relay infrastructure (outbound connectivity required)

## Relay Cluster Locations

| Provider | Regions |
|---|---|
| **Google Cloud** | Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia, São Paulo, Eemshaven, Finland, Frankfurt, London, Zurich, Tel Aviv, Johannesburg, Hong Kong, Mumbai, Singapore, Taiwan, Tokyo, Sydney |
| **DigitalOcean** | Atlanta, New York City, San Francisco, Toronto, Amsterdam, Frankfurt, London, Bengaluru, Singapore, Sydney |

## Configuration Values
None — Relay selection is automatic. No environment variables, CLI flags, or API parameters are exposed for Relay configuration.

## Gotchas
- Traffic **may** pass through a Relay (not guaranteed direct); depends on network topology between Client and Connector
- Relay routing is transparent to the end-to-end encryption — Relays cannot inspect payload data
- Connector connects to nearest Relay at startup; no manual override documented

## Related Docs
- Connector deployment documentation
- Controller/authorization flow documentation
- Network architecture / firewall requirements (outbound ports for Relay connectivity)