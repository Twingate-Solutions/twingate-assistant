# Service Reliability

## Page Title
Service Reliability – Twingate Infrastructure and Service Reliability

## Summary
Twingate ensures high availability, performance, and scalability through fault-tolerant multi-region GCP infrastructure, distributed architecture, and automatic load balancing. Traffic routing is optimized by avoiding backhauling and supporting split tunneling. Customers are shielded from scaling concerns as Twingate manages infrastructure growth.

## Key Information

### Availability
- Hosted on **Google Cloud Platform (GCP)** across multiple geographically separated data centers
- Automatic failover between data centers if one becomes unavailable
- DDoS mitigation measures in place
- 24/7 automated monitoring with alerting
- Public status page: **status.twingate.com**

### Performance & Scalability
- **No backhauling**: Traffic takes direct routes; clients auto-select nearest/best-performing controllers and relays
- **Split tunneling**: Non-Twingate traffic bypasses the service entirely, reducing unnecessary hops
- **Load balancing**: Controllers and relays distributed globally; additional nodes added in high-traffic regions
- **Co-location**: Controllers and relays hosted within AWS, Azure, and GCP to reduce latency for customers on those platforms
- **Distributed authorization**: Auth processing occurs at the client level, not a central bottleneck
- **Multi-connector support**: Multiple connectors per network with automatic load balancing between them

## Prerequisites
- No customer-side infrastructure scaling required; Twingate manages this automatically
- Customers can deploy multiple connectors within a network to leverage built-in load balancing

## Configuration Values
- No specific env vars or CLI flags for reliability settings
- Deploy multiple Connectors in the same Remote Network to enable automatic load balancing for inbound access requests

## Gotchas
- Split tunneling behavior depends on what traffic the organization configures to route through Twingate — misconfiguration could bypass intended security controls
- Customers using AWS or Azure benefit from co-located relays, but must ensure Connector placement is reasonable relative to protected resources
- Reliability is infrastructure-level; application-level issues within customer networks are outside Twingate's scope

## Related Docs
- [Twingate Status Page](https://status.twingate.com)
- [Google Cloud Platform Overview](https://cloud.google.com)
- Connector deployment documentation (multiple connectors per network)
- Split tunneling configuration