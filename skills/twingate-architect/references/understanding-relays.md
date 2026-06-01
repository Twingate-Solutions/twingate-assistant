# Understanding Relays

## Summary
Relays facilitate connection establishment between Twingate Clients and Connectors for Resource access. They serve as infrastructure hops in the end-to-end encrypted TLS tunnel but do not terminate connections or store traffic. When direct Client-Connector connections aren't possible, traffic is routed through a Relay.

## Key Information
- Relays facilitate (not terminate) connections between Clients and Connectors
- All traffic through Relays is already encrypted via certificate-pinned TLS tunnel
- Relays do **not** store traffic or network-identifiable information
- Connectors automatically connect to the geographically nearest available Relay
- Each Relay location runs a cluster for redundancy; failover is automatic

## How Relays Fit in the Connection Flow
1. Client requests access to a Resource
2. Controller authorizes the Client
3. Client establishes encrypted tunnel to a Connector via a Relay
4. Connector forwards traffic to the Resource
5. Data passes through Relay transiently (encrypted, not inspected or stored)

## Relay Cluster Locations

### Google Cloud
- **North America:** Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia
- **South America:** São Paulo
- **Europe:** Eemshaven, Finland, Frankfurt, London, Zurich
- **Middle East:** Tel Aviv
- **Africa:** Johannesburg
- **Asia:** Hong Kong, Mumbai, Singapore, Taiwan, Tokyo
- **Australia:** Sydney

### DigitalOcean
- **North America:** Atlanta, New York City, San Francisco, Toronto
- **Europe:** Amsterdam, Frankfurt, London
- **Asia:** Bengaluru, Singapore
- **Australia:** Sydney

## Reliability Behavior
| Failure Scenario | Behavior |
|---|---|
| Single Relay fails | Another Relay in same cluster used |
| Entire cluster location fails | Next nearest cluster location used automatically |

## Gotchas
- Relays are Twingate-managed infrastructure — no customer configuration required or available
- Traffic **may** route through a Relay (not always); direct peer connections are attempted first
- Relay selection is automatic based on Connector geography, not Client geography
- No egress IPs to allowlist for Relay traffic (managed by Twingate)

## Related Docs
- Twingate Architecture / Controller documentation
- Connector deployment guides
- Network requirements / firewall configuration (ports needed for Relay communication)