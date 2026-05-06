# Understanding Relays

## Summary
Relays facilitate connection establishment between Twingate Clients and Connectors for authorized Resource access. They act as intermediaries in the end-to-end encrypted TLS tunnel without terminating or storing any traffic. Twingate operates a global network of Relay clusters across multiple cloud providers for low-latency, redundant connectivity.

## Key Information
- Relays facilitate (not terminate) connections between Clients and Connectors
- Connections use certificate-pinned TLS tunnels that are end-to-end encrypted
- Encrypted traffic may route *through* a Relay when direct connection isn't possible
- Relays do **not** store traffic or network-identifiable information
- Data passing through Relays is already encrypted — Relay cannot decrypt it
- Connectors automatically connect to the **geographically nearest** available Relay
- Failover is automatic: within a cluster first, then to the next nearest cluster

## Architecture Role
- **Controller**: Authorizes Client access to Resources
- **Relay**: Facilitates/routes the encrypted tunnel between Client and Connector
- **Connector**: Forwards traffic to the actual Resource
- No connections are terminated at the Relay layer

## Relay Cluster Locations

### Google Cloud
- **North America**: Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia
- **South America**: São Paulo
- **Europe**: Eemshaven, Finland, Frankfurt, London, Zurich
- **Middle East**: Tel Aviv
- **Africa**: Johannesburg
- **Asia**: Mumbai, Singapore, Tokyo
- **Australia**: Sydney

### DigitalOcean
- **North America**: Atlanta, New York City, San Francisco, Toronto
- **Europe**: Amsterdam, Frankfurt, London
- **Asia**: Bengaluru, Singapore
- **Australia**: Sydney

## Reliability
- Each location runs a **cluster** of multiple Relays (not single points of failure)
- Failure handling: same-cluster Relay → next nearest cluster (automatic)
- No manual configuration required for failover

## Gotchas
- Relays are Twingate-managed infrastructure — no self-hosted Relay option documented here
- Traffic routing through a Relay adds latency; geographic proximity of Connector deployment affects performance
- Relay involvement is only for connection *facilitation* — direct Client-to-Connector paths bypass Relay routing when possible

## Prerequisites
- None for understanding; Relays are automatically used by deployed Connectors
- Connector placement near target Resources minimizes Relay-introduced latency

## Related Docs
- Connector deployment documentation
- Controller and authorization flow
- Network architecture overview