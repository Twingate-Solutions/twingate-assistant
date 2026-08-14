---
source: https://www.twingate.com/docs/service-reliability
type: docs
fetched: 2026-08-14
source_version: 4833f88822dbaa7d90049690092b931e16d53acfd048e2dbb73688d97af99243
---

# Service Reliability

## Page Title
Twingate Service Reliability

## Summary
Twingate's infrastructure is hosted on GCP with multi-region redundancy, fault tolerance, and 24/7 monitoring. Performance is optimized through direct routing (no backhaul), split tunneling, and distributed authorization processing. Scaling is handled automatically by Twingate rather than requiring customer-managed infrastructure.

## Key Information

**Availability:**
- Hosted on Google Cloud Platform (GCP) with multi-datacenter redundancy
- Automatic failover between data centers if one becomes unavailable
- Geographically separated data centers reduce location-specific disaster risk
- DDoS mitigation measures implemented
- Service status visible at [status.twingate.com](https://status.twingate.com)
- 24/7 automated monitoring with alerting

**Performance:**
- Traffic takes direct routes instead of backhauling through a central gateway
- Clients automatically select optimal controllers and relays based on user location and target resource
- Split tunneling bypasses Twingate entirely for non-routed traffic
- Controllers and relays co-hosted with AWS, Azure, and GCP to reduce latency
- Authorization processing is distributed (partially at client level) to avoid centralized bottlenecks

**Scalability:**
- Load balancing handled automatically across controllers, relays, and connectors
- Multiple connectors can be deployed in the same network; Twingate auto-balances between them
- Twingate manages infrastructure scaling — no customer-side VPN gateway scaling required
- Additional controllers/relays added in high-traffic regions as needed

## Configuration Values
- **Multiple Connectors per network**: Supported; Twingate auto-load-balances between them — no additional configuration required

## Prerequisites
- None specific to reliability; features are built into the platform

## Gotchas
- No explicit SLA percentage is stated in this document — check separate SLA documentation for uptime commitments
- Split tunneling scope is determined by administrator policy; traffic not explicitly routed through Twingate bypasses it entirely

## Related Docs
- [GCP Infrastructure](https://cloud.google.com/docs)
- [status.twingate.com](https://status.twingate.com)
- Twingate Connector deployment docs (for multi-connector load balancing setup)