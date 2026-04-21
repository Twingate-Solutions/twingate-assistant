## Remote Network Best Practices

Guidance for structuring Remote Networks, DNS, routing, and firewall rules. One Remote Network per network segment is the standard approach; private DNS is recommended but not required; no routing changes or inbound firewall rules are needed.

**Key Information:**
- Configure one Remote Network per network segment (physical network, VPC, or routable address space)
- Peered VPCs accessible from a shared set of Connectors can be modeled as a single Remote Network; separate VPCs with separate Connectors improve routing performance by eliminating unnecessary hops
- Private DNS is recommended: resources are resolved via the Connector, keeping internal addresses hidden from the public internet
- No changes to network routing rules are required; Connectors resolve local addresses on their own subnet
- Connectors initiate outbound-only connections to Twingate -- no inbound firewall rules are needed for Connectors or Resources

**Key Architecture Pattern (Segmented Subnets):**
- Two subnets (`10.1.0.0/16` and `10.2.0.0/16`) with no cross-subnet routing
- Deploy one Connector on each subnet (`10.1.0.35` and `10.2.0.35`)
- Both subnets are remotely accessible without subnet peering or routing changes

**Gotchas:**
- Connectors within the same Remote Network are assumed to have identical routing rules -- divergent rules cause inconsistent Resource access
- Multiple Remote Networks carry no performance penalty; separating VPCs into dedicated Remote Networks often reduces latency

**Related Docs:**
- /docs/remote-networks -- Remote Network overview
- /docs/connector -- Connector deployment
- /docs/how-does-twingate-work -- DNS and routing internals
