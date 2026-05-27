# Service Reliability

## Page Title
Service Reliability — How Twingate Ensures Infrastructure and Service Reliability

## Summary
Twingate ensures high availability, performance, and scalability through GCP-hosted redundant infrastructure across multiple geographic data centers. Unlike traditional VPN solutions, Twingate distributes traffic routing and authorization processing to reduce latency and eliminate single points of failure. Customers are offloaded from managing scaling infrastructure entirely.

## Key Information

**Availability Mechanisms:**
- Hosted on Google Cloud Platform (GCP) with multi-datacenter redundancy
- Automatic failover between data centers if one has issues
- Geographically separated data centers for disaster resilience
- DDoS mitigation measures in place
- 24/7 automated monitoring with alerting
- Public status page: `status.twingate.com`

**Performance Mechanisms:**
- No traffic backhauling — clients connect directly to nearest controllers/relays
- Split tunneling supported — non-Twingate traffic bypasses the service entirely
- Controllers and relays hosted within customer IaaS providers (AWS, Azure, GCP) to reduce latency
- Load balancing across controllers and relays by region; additional nodes added in high-traffic regions
- Distributed authorization processing (partially client-side) avoids centralized bottlenecks

**Scalability Mechanisms:**
- Multiple Connectors per network supported; Twingate auto-load-balances between them
- Twingate manages infrastructure scaling — no customer-side VPN gateway scaling required

## Configuration Values

| Feature | Details |
|---|---|
| Multiple Connectors | Deploy multiple Connectors in the same Remote Network for automatic load balancing |
| Split tunneling | Configurable per resource/policy — traffic not routed through Twingate is handled directly by the device |

## Prerequisites
- None specific to reliability features — these are platform-level guarantees
- For Connector redundancy: deploy multiple Connectors within the same Remote Network in Twingate admin console

## Gotchas
- Load balancing between Connectors is automatic — no manual configuration needed, but requires multiple Connectors to be deployed in the same Remote Network
- Split tunneling scope depends on what resources are defined in Twingate; undefined traffic bypasses Twingate by default
- Customers are responsible for deploying Connectors with sufficient redundancy on their own infrastructure; Twingate handles cloud-side reliability only

## Related Docs
- [GCP Infrastructure](https://cloud.google.com/about/locations) — underlying infrastructure details
- [status.twingate.com](https://status.twingate.com) — live service status
- Twingate Connectors documentation — for deploying redundant Connectors
- Twingate Architecture documentation — for understanding Controller/Relay topology