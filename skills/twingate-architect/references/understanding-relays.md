# Understanding Relays

## Summary
Relays facilitate secure connection establishment between Twingate Clients and Connectors for resource access. They act as intermediaries in the end-to-end encrypted TLS tunnel without terminating connections or storing traffic data. Twingate operates a global network of Relay clusters across Google Cloud and DigitalOcean infrastructure.

## Key Information
- Relays serve two functions: connection establishment facilitation and optional traffic routing between Clients and Connectors
- All traffic through Relays is already encrypted (end-to-end TLS with certificate pinning); Relays cannot decrypt it
- Connectors connect to the geographically nearest available Relay automatically
- Each Relay location runs a cluster for redundancy; failover occurs within location first, then to nearest cluster
- Relays do **not** store traffic or network-identifiable information
- No connections are terminated at the Relay

## Relay Cluster Locations

### Google Cloud
| Region | Locations |
|--------|-----------|
| North America | Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia |
| South America | São Paulo |
| Europe | Eemshaven, Finland, Frankfurt, London, Zurich |
| Middle East | Tel Aviv |
| Africa | Johannesburg |
| Asia | Mumbai, Singapore, Tokyo |
| Australia | Sydney |

### DigitalOcean
| Region | Locations |
|--------|-----------|
| North America | Atlanta, New York City, San Francisco, Toronto |
| Europe | Amsterdam, Frankfurt, London |
| Asia | Bengaluru, Singapore |
| Australia | Sydney |

## Architecture Flow
1. Client requests access to a Resource
2. Controller authorizes the Client
3. Client establishes connection to Connector via a Relay
4. Relay facilitates (and if necessary routes) the encrypted tunnel
5. Connector forwards traffic to the Resource

## Gotchas
- Relay selection is automatic; there is no manual Relay selection for Connectors
- Traffic *may* route through Relays—direct Client-to-Connector connections are attempted first when possible
- Relay infrastructure is Twingate-managed; customers cannot self-host Relays

## Configuration Values
None — Relay selection and failover are fully automatic with no user-configurable parameters.

## Prerequisites
- A deployed Connector connected to the Twingate network (Connector handles Relay association automatically)

## Related Docs
- Twingate Connectors documentation
- Twingate Controller documentation
- Network architecture / firewall requirements (for outbound Relay connectivity from Connectors)