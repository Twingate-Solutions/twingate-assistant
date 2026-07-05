# Service Reliability

## Page Title
Service Reliability - Twingate Infrastructure and Service Reliability

## Summary
Twingate ensures high service availability through GCP-hosted redundant multi-region infrastructure. Performance is optimized via direct routing (no backhaul), split tunneling, and distributed authorization processing. Scaling is handled automatically by Twingate rather than requiring customer infrastructure changes.

## Key Information

### Availability
- Hosted on **Google Cloud Platform (GCP)** with multi-datacenter redundancy
- Automatic failover between data centers if one experiences issues
- Geographically separated data centers for disaster resilience
- Service status monitoring: **status.twingate.com**
- DDoS mitigation measures implemented
- 24/7 automated monitoring with alerting

### Performance & Scalability
- **No backhaul**: Traffic takes direct routes rather than through a central gateway; clients auto-select optimal controllers/relays based on user location and target resource
- **Split tunneling**: Non-Twingate traffic bypasses the service entirely, reducing unnecessary hops
- **Load balancing**: Controllers and relays distributed across regions; additional capacity added in high-traffic regions
- **Co-location**: Controllers and relays hosted within AWS, Azure, and GCP to reduce latency for customers on those platforms
- **Multi-connector load balancing**: Multiple connectors per network are automatically load-balanced for inbound access requests
- **Distributed authorization**: Auth processing handled at the client level rather than a centralized bottleneck

## Configuration Values
- No customer-configurable reliability settings documented here
- Multiple connectors per Remote Network enable automatic load balancing (customer-deployable)

## Gotchas
- Load balancing between connectors is **automatic** — no manual configuration required
- Customers are responsible for deploying multiple connectors if they want connector-level redundancy; Twingate handles the balancing logic
- Split tunneling scope is determined by what resources/traffic an organization configures to route through Twingate

## Prerequisites
- None specific to this topic; applies to all Twingate deployments

## Related Docs
- [GCP Infrastructure](https://cloud.google.com/about/locations) (external)
- [status.twingate.com](https://status.twingate.com)
- Connector deployment documentation (for multi-connector load balancing setup)