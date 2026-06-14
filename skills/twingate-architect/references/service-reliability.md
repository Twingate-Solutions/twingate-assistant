# Service Reliability

## Page Title
Service Reliability – How Twingate Ensures Infrastructure and Service Reliability

## Summary
Twingate provides high availability, performance, and scalability through GCP-hosted infrastructure, multi-region redundancy, and a distributed architecture. Unlike traditional VPNs, traffic takes direct routes without backhauling, and authorization processing is distributed rather than centralized. Customers are abstracted from scaling concerns.

## Key Information

**Availability:**
- Hosted on Google Cloud Platform (GCP) with multi-datacenter redundancy
- Automatic failover if one datacenter experiences issues
- Geographically separated datacenters to mitigate location-specific disasters
- Service status monitoring: [status.twingate.com](https://status.twingate.com)
- DDoS mitigation measures in place
- 24/7 automated monitoring with alerting

**Performance & Scalability:**
- **No backhauling**: Traffic routes directly between endpoints; clients auto-select lowest-latency controllers/relays based on user location
- **Split tunneling**: Non-Twingate traffic bypasses the service entirely, reducing unnecessary hops
- **Load balancing**: Controllers and relays distributed across regions; co-hosted within AWS, Azure, and GCP to reduce latency
- **Connector-level load balancing**: Deploy multiple Connectors per network; Twingate auto-balances access requests across them
- **Distributed authorization**: Auth processing occurs at the client level, not a central bottleneck

## Configuration Values
- Multiple Connectors per Remote Network supported for load balancing (no special flag; deploy additional Connectors to same network)

## Prerequisites
- None specific to reliability configuration; multi-connector load balancing is automatic

## Gotchas
- Load balancing between Connectors is automatic — no manual configuration required, but you must deploy multiple Connectors to the same Remote Network to enable it
- Split tunneling must be explicitly configured; by default, only resources defined in Twingate are routed through the service
- Twingate manages infrastructure scaling; customers do not need to provision relay/controller capacity

## Related Docs
- [GCP Infrastructure](https://cloud.google.com/docs) (external)
- [status.twingate.com](https://status.twingate.com) – live service status
- Connector deployment documentation (multiple Connectors per network)
- Split tunneling configuration