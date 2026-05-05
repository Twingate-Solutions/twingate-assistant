## Understanding Connectors

Conceptual guide to how Twingate Connectors work and how they differ from VPN gateways. Foundation for making deployment and architecture decisions.

**Connectors Are NOT VPN Gateways:**
- Never accessible from the public internet — always sit behind a firewall within the private network
- Users never choose or directly connect to a Connector — Twingate routes transparently
- Do not grant users access to the full private network — only individual authorized connections pass through
- No downside to deploying across many networks — invisible to users, mirrors your infrastructure

**Connectors as Software-Defined Proxies:**
- Name/address resolution happens at the Connector's network, not on the user's device — enables private DNS names and IPs without VPN
- No infrastructure routing changes needed — Connectors deploy within existing network subnets
- Automatically clustered within a Remote Network — add more Connectors for capacity or redundancy with no user impact
- Precise split tunneling — only traffic destined for authorized Resources routes through the Connector
- Traffic is automatically routed to the geographically nearest Connector for replicated services

**Key Design Principle:**
- Model Connectors as keyholes that pass individual authorized connections, not as gateways that open network segments

**Related Docs:**
- /docs/connector-placement-best-practices -- Placement patterns
- /docs/connector-shutdown-process -- Failover behavior
- /docs/how-twingate-works -- Full architecture
