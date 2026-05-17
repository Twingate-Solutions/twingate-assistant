# Service Reliability

## Page Title
Service Reliability – Twingate Infrastructure and Service Reliability

## Summary
Twingate describes its reliability architecture covering availability, performance, and scalability. The service runs on GCP with multi-datacenter redundancy and uses a distributed architecture to avoid traditional VPN bottlenecks. Customers can monitor uptime at status.twingate.com.

## Key Information

**Availability:**
- Hosted on Google Cloud Platform (GCP) with multi-datacenter redundancy
- Automatic failover between data centers if one becomes unavailable
- Geographically separated data centers to mitigate location-specific disasters
- DDoS mitigation measures implemented
- 24/7 automated monitoring with alerting
- Public status page: **status.twingate.com**

**Performance:**
- No traffic backhauling — traffic takes direct routes between endpoints
- Clients auto-select controllers/relays with best performance based on user location and target resource
- Split tunneling supported — non-Twingate traffic bypasses the service entirely
- Authorization processing distributed (partially to client level) to avoid centralized bottlenecks

**Scalability:**
- Load balancing across controllers and relays in multiple regions and IaaS providers (AWS, Azure, GCP)
- High-traffic regions get additional controllers/relays
- Multiple connectors per customer network supported; Twingate auto-balances between them
- Twingate handles infrastructure scaling — no customer-side VPN gateway scaling required

## Prerequisites
- None specific; applies to all Twingate deployments

## Configuration Values
- **Multiple Connectors per network**: Deploy additional connectors in the same Remote Network — Twingate handles load balancing automatically (no extra config required)
- **Split tunneling**: Configured at the policy/resource level — traffic not explicitly routed through Twingate bypasses it

## Gotchas
- Load balancing between connectors is automatic, but connectors must be deployed in the same Remote Network to be treated as equivalent endpoints
- Performance benefits of co-located relays (within AWS/Azure/GCP) depend on Twingate's infrastructure placement decisions, not customer configuration
- Customers are responsible for connector-level availability within their own networks; Twingate manages cloud infrastructure only

## Related Docs
- [GCP Infrastructure](https://cloud.google.com/docs)
- [status.twingate.com](https://status.twingate.com) — live service status
- Connector deployment documentation (multiple connectors per network)
- Split tunneling configuration