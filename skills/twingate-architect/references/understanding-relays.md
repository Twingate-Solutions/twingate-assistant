# Understanding Relays

## Summary
Relays facilitate connection establishment between Twingate Clients and Connectors for Resource access. They act as intermediaries in the end-to-end encrypted TLS tunnel but never terminate or store traffic. Twingate operates a global network of Relay clusters for low latency and redundancy.

## Key Information
- Relays are used **after** Controller authorization to establish the Client ↔ Connector data connection
- Connection is end-to-end encrypted via certificate-pinned TLS tunnel
- Relays may route the encrypted tunnel when direct Client-Connector connection isn't possible
- Each Connector connects to the **nearest available Relay** to minimize latency
- Each Relay location runs a **cluster** of multiple Relays for redundancy
- Failover is automatic: same-cluster first, then nearest alternate cluster

## Data Privacy
- Relays are **transit-only** — no traffic storage, no network-identifiable information retained
- Traffic is already encrypted before reaching the Relay
- No connections are terminated at the Relay

## Relay Cluster Locations

| Provider | Regions |
|----------|---------|
| **Google Cloud** | Iowa, Los Angeles, Ohio, Oregon, South Carolina, Toronto, Virginia, São Paulo, Eemshaven, Finland, Frankfurt, London, Zurich, Tel Aviv, Johannesburg, Mumbai, Singapore, Tokyo, Sydney |
| **DigitalOcean** | Atlanta, New York City, San Francisco, Toronto, Amsterdam, Frankfurt, London, Bengaluru, Singapore, Sydney |

## Gotchas
- Relays are Twingate-managed infrastructure — no self-hosting or configuration required
- Connector-to-Relay connectivity must be allowed outbound; check firewall rules if Connectors fail to connect
- Geographic Relay selection is automatic; no manual Relay assignment is available
- If an entire cluster fails, the next nearest cluster is used automatically — expect minor latency increase during failover

## Architecture Flow
1. Client requests Resource access → Controller authorizes
2. Client and Connector establish encrypted tunnel **facilitated by** the nearest Relay
3. If direct connection unavailable, encrypted traffic is **routed through** the Relay
4. Connector forwards traffic to the Resource

## Related Docs
- Twingate Connectors
- Twingate Controller
- Network/firewall requirements for Connectors