# Service Reliability

## Page Title
Service Reliability – Twingate Infrastructure and Service Reliability

## Summary
Twingate ensures high availability, performance, and scalability through a distributed, fault-tolerant architecture hosted on GCP with multiple geographically separated data centers. Traffic routing is optimized by eliminating backhauling, supporting split tunneling, and distributing authorization processing to reduce latency and bottlenecks.

## Key Information

### Availability
- **Infrastructure**: Hosted on Google Cloud Platform (GCP)
- **Redundancy**: Multiple mirrored data centers with automatic failover
- **Geographic separation**: Mitigates location-specific disaster risk
- **Status page**: [status.twingate.com](https://status.twingate.com)
- **DDoS mitigation**: Built-in protective measures
- **Monitoring**: 24/7 automated monitoring with alerting

### Performance & Scalability
- **No backhauling**: Clients connect directly via optimal controllers/relays based on user location and target resource
- **Split tunneling**: Non-Twingate traffic bypasses the service entirely, reducing unnecessary hops
- **Load balancing**: Handled at multiple levels — controllers, relays, and connectors
- **Multi-cloud relay hosting**: Controllers and relays co-hosted within AWS, Azure, and GCP to reduce latency
- **Distributed authorization**: Processing occurs at the client level rather than a centralized bottleneck
- **Connector load balancing**: Multiple connectors per network are automatically load-balanced by Twingate

## Prerequisites
- None specific to this document; architectural information only

## Configuration Values
- **Multiple Connectors**: Deploy more than one Connector per remote network to enable automatic load balancing across connectors

## Gotchas
- Scaling infrastructure (controllers/relays) is managed by Twingate, not the customer — no action required from admins
- Load balancing between connectors is automatic but requires multiple connectors to be deployed within the same network
- Split tunneling behavior depends on what traffic the organization configures to route through Twingate

## Related Docs
- [GCP Infrastructure Overview](https://cloud.google.com/docs)
- [Twingate Status Page](https://status.twingate.com)
- Connector deployment documentation (multiple connectors per network)