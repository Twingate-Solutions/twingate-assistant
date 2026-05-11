# Service Reliability

## Page Title
Service Reliability – How Reliable is Twingate's Infrastructure and Service?

## Summary
Twingate provides high availability, performance, and scalability through distributed infrastructure hosted on GCP with multi-region redundancy. Traffic routing is optimized via split tunneling and direct paths (no backhauling), with load balancing handled automatically at multiple levels. Customers are abstracted from scaling concerns entirely.

## Key Information

**Availability:**
- Hosted on Google Cloud Platform (GCP) with multi-datacenter redundancy
- Automatic failover between data centers if one becomes unavailable
- Geographically separated data centers mitigate location-specific disasters
- DDoS mitigation measures in place
- 24/7 automated monitoring with alerting
- Service status page: **status.twingate.com**

**Performance & Scalability:**
- No backhauling: traffic takes direct routes rather than through a central gateway
- Clients automatically select the best-performing controllers and relays based on user location and target resource
- Split tunneling: non-Twingate traffic bypasses the service entirely
- Controllers and relays co-hosted with major IaaS providers (AWS, Azure, GCP) to reduce latency
- Load balancing operates at multiple levels: across regional controllers/relays and across customer-deployed connectors
- Authorization processing is distributed (partially at client level) to avoid centralized bottlenecks

## Prerequisites
- None for reliability features; they are platform-managed
- Multiple connectors can be deployed per network to enable connector-level load balancing

## Configuration Values
| Feature | Customer Action Required |
|---|---|
| Connector load balancing | Deploy multiple Connectors in same network — Twingate handles balancing automatically |
| Split tunneling | Configure which resources route through Twingate vs. bypass |
| Regional relay selection | Automatic; no configuration needed |

## Gotchas
- Load balancing between connectors within a network is automatic, but requires **multiple connectors deployed** to take effect
- Split tunneling scope is determined by what resources/policies are configured — unrouted traffic bypasses Twingate entirely (desired behavior, but verify policy coverage)
- Twingate manages infrastructure scaling; customers do not deploy or scale relay/controller infrastructure themselves

## Related Docs
- [GCP Infrastructure Overview](https://cloud.google.com/docs) (external)
- status.twingate.com – live service status
- Connector deployment documentation (for multi-connector load balancing setup)
- Split tunneling configuration