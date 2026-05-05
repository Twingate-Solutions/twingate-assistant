## Connector Best Practices

Authoritative guide to Connector deployment, network requirements, hardware sizing, load balancing, and geographic routing.

**Deployment Principles:**
- Deploy as many Remote Networks and Connectors as your architecture requires — no bottleneck advantage to fewer Connectors
- **Always deploy at least 2 Connectors per Remote Network** for HA/failover; they auto-cluster within the same Remote Network
- Each Connector must have its own unique token pair — reusing tokens causes connection failure
- All Connectors in the same Remote Network should have the same network scope and permissions (they are interchangeable)
- Deploy Connectors as physically close to Resources as possible — the last mile to Resources matters for performance

**Network Requirements:**
- Outbound internet only — no inbound access required or recommended
- If restricting outbound: TCP 443 (Controller/Relay), TCP 30000–31000 (Relay fallback), UDP/QUIC 1–65535 (P2P)
- Connectors must have routing and DNS resolution to private Resources they serve
- For ICMP: ensure Connector host has permission to send ICMP to target Resources

**Hardware Recommendations (by platform):**
- AWS: t3a.micro EC2 (sufficient for hundreds of users under typical load)
- GCP: e2-small Compute Engine
- Azure: use Container Instance (no hardware selection needed)
- On-prem/VPS: 1 CPU, 2 GB RAM Linux VM

**Performance Notes:**
- Priority: network bandwidth > memory > CPU
- If resource-bound: add more Connectors (don't add CPU/memory to a single Connector — it won't improve performance)
- Twingate auto-load-balances across all Connectors in a Remote Network

**Load Balancing & Failover:**
- Multiple Connectors in the same Remote Network are automatically clustered
- On Connector failure: clients automatically try the next Connector in their ordered list (~20-second failover delay per attempt)
- Adding/removing Connectors is detected automatically; routing adjusts

**Geographic Routing:**
- Create one Remote Network containing all replicated Resources; deploy Connectors in each geographic location
- Twingate automatically routes users to the nearest active Connector by location

**Related Docs:**
- /docs/connector-placement-best-practices -- Where to place Connectors
- /docs/connector-shutdown-process -- Failover mechanics
- /docs/understanding-connectors -- Conceptual model
