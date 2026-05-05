## Service Reliability

How Twingate ensures availability, performance, and scalability of its infrastructure. Relevant for customers assessing SLA, uptime, and architectural resilience.

**Availability:**
- Hosted on Google Cloud Platform (GCP) with multi-datacenter, fault-tolerant, geographically distributed architecture
- Automatic failover between data centers; no single point of failure
- DDoS mitigation measures implemented
- 24/7 automated monitoring and alerting
- Service status transparency at status.twingate.com

**Performance & Scalability:**
- No backhaul -- traffic takes a direct route rather than through a central gateway; Clients automatically connect to the nearest Controller/Relay for best performance
- Split tunneling -- non-Twingate traffic bypasses Twingate entirely
- Load balancing at multiple levels: Controllers and Relays are geographically distributed and load-balanced; multiple Connectors per network are automatically load-balanced by Twingate
- Authorization processing is distributed (e.g., at Client level) rather than centralized, reducing bottlenecks
- IaaS co-location -- Controllers and Relays are hosted within the same providers customers use (AWS, Azure, GCP) to minimize latency

**Related Docs:**
- /docs/understanding-relays -- How Twingate Relays work
- /docs/connector-placement-best-practices -- Connector HA and placement
