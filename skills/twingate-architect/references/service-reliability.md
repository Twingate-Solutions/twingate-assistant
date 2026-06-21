# Twingate Service Reliability

## Page Title
Service Reliability - How Reliable is Twingate's Infrastructure and Service?

## Summary
Twingate ensures high availability and performance through redundant GCP-hosted infrastructure across geographically separated data centers. Performance is optimized by eliminating backhaul routing, supporting split tunneling, and distributing authorization processing to clients rather than centralizing it.

## Key Information

**Availability:**
- Hosted on Google Cloud Platform (GCP) with multi-datacenter redundancy
- Automatic failover between data centers if one experiences issues
- Geographically separated data centers reduce location-specific disaster risk
- Service status monitoring at `status.twingate.com`
- DDoS mitigation measures in place
- 24/7 automated monitoring with alerting

**Performance & Scalability:**
- No backhaul: traffic takes direct routes rather than through a central gateway
- Clients auto-select best controller/relay based on user location and target resource
- Split tunneling: non-Twingate traffic bypasses the service entirely
- Controllers and relays co-hosted within AWS, Azure, and GCP to reduce latency
- Multiple connectors per network supported; Twingate auto-load-balances between them
- Authorization processing distributed to client level, avoiding central bottleneck

## Configuration Values
- Multiple connectors can be deployed within the same Remote Network for automatic load balancing — no additional configuration required

## Prerequisites
- None specific to reliability architecture; this is managed infrastructure

## Gotchas
- Load balancing between connectors is automatic — deploying multiple connectors in the same network is sufficient, no manual configuration needed
- Organizations must opt into split tunneling; traffic not explicitly excluded will route through Twingate
- Scaling of controllers/relays is handled by Twingate, but connector scaling within customer networks is the customer's responsibility

## Related Docs
- [Twingate Status Page](https://status.twingate.com)
- [Google Cloud Platform](https://cloud.google.com)
- Connector deployment documentation
- Split tunneling configuration