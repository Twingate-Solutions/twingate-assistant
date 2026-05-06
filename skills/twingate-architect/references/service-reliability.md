# Service Reliability

## Page Title
Service Reliability - How Reliable is Twingate's Infrastructure and Service?

## Summary
Twingate ensures high service availability, performance, and scalability through fault-tolerant GCP-hosted infrastructure across multiple geographic data centers. Traffic routing is optimized by eliminating backhauling, supporting split tunneling, and distributing authorization processing. Customers are shielded from scaling complexity as Twingate handles infrastructure scaling automatically.

## Key Information

### Availability
- **Infrastructure**: Hosted on Google Cloud Platform (GCP) with multi-data-center redundancy
- **Failover**: Automatic load redistribution if one data center has issues
- **Status page**: `status.twingate.com` for real-time monitoring
- **DDOS mitigation**: Active measures in place
- **Monitoring**: 24/7 automated alerting

### Performance & Scalability
- **No backhauling**: Traffic takes direct routes; clients auto-select optimal controllers/relays based on user location
- **Split tunneling**: Non-Twingate traffic bypasses the service entirely, reducing unnecessary hops
- **Load balancing**: Operates at multiple levels—controllers, relays, and connectors
- **Co-location**: Controllers and relays hosted within AWS, Azure, and GCP to reduce latency for customers on those platforms
- **Connector load balancing**: Multiple connectors per network are automatically load-balanced
- **Distributed authorization**: Processing handled at the client level rather than a central bottleneck

## Configuration Values
- **Multiple connectors**: Deploy more than one connector within the same Remote Network to enable automatic load balancing for inbound access requests

## Gotchas
- Load balancing between connectors is **automatic**—no manual configuration required, but requires multiple connectors deployed in the same network
- Split tunneling behavior depends on what resources are configured to route through Twingate; non-configured traffic bypasses Twingate by default
- Customers do **not** manage scaling of Twingate infrastructure—this is fully handled by Twingate

## Prerequisites
- None specific to reliability features; behavior is inherent to Twingate's architecture

## Related Docs
- [GCP Infrastructure](https://cloud.google.com/about/locations) (external)
- [Twingate Status Page](https://status.twingate.com)
- Connector deployment documentation (for multi-connector load balancing setup)