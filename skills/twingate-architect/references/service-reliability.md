# Service Reliability

## Page Title
Service Reliability – How Reliable is Twingate's Infrastructure and Service?

## Summary
Twingate ensures high availability, performance, and scalability through GCP-hosted redundant multi-region infrastructure and a distributed architecture. Unlike traditional VPN-based solutions, Twingate eliminates backhauling and centralizes scaling management on behalf of customers. Authorization processing is distributed (partially client-side) to avoid bottlenecks.

## Key Information

- **Infrastructure provider**: Google Cloud Platform (GCP)
- **Status page**: [status.twingate.com](https://status.twingate.com)
- **Multi-region**: Multiple geographically separated data centers with automatic failover
- **DDoS mitigation**: Built-in measures implemented at infrastructure level
- **Monitoring**: 24/7 automated monitoring with alerting
- **Controller/relay placement**: Hosted within AWS, Azure, and GCP to reduce latency for customers on those platforms
- **Connector load balancing**: Multiple connectors in the same network are automatically load balanced by Twingate

## Architecture Details (Performance & Scalability)

| Feature | Behavior |
|---|---|
| Traffic routing | Direct path between client and resource (no backhauling) |
| Split tunneling | Non-Twingate traffic bypasses Twingate entirely |
| Load balancing | Handled at controller, relay, and connector levels |
| Authorization processing | Distributed; partially handled at the client level |
| Scaling | Managed by Twingate, not the customer |

## Prerequisites
- No customer action required for infrastructure reliability features
- For connector-level load balancing: deploy multiple Connectors within the same Remote Network

## Configuration Values
- **Multiple Connectors per network**: Deploy ≥2 Connectors in the same Remote Network to enable automatic load balancing for inbound access requests

## Gotchas

- Load balancing between connectors is **automatic** — no manual configuration needed, but requires multiple connectors to be deployed in the same network
- Split tunneling must be **configured by the admin** — traffic not explicitly routed through Twingate bypasses it; this is intentional but requires policy planning
- Twingate clients **automatically select** the best controller/relay based on user location — no client-side configuration needed

## Related Docs
- GCP infrastructure overview (linked externally on page)
- Twingate Connector deployment documentation
- Remote Networks configuration
- Split tunneling configuration