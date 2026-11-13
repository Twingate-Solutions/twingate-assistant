---
source: https://www.twingate.com/docs/remote-network-best-practices
type: docs
fetched: 2026-11-13
source_version: be71a88a78c6b0a05ba1dfc4f52f845a131d2b22be6f4f27231dc27dc348cdcc
trust: official
---

# Remote Network Best Practices

## Summary
Guidance on structuring Twingate Remote Networks, DNS, routing, and firewall rules. A Remote Network should map to an address space reachable from a set of Connectors. No routing or inbound firewall changes are needed to deploy Twingate.

## Key Information
- **One Remote Network per network segment.** A "segment" is any address space reachable from the deployed Connectors, regardless of physical layout.
- Two peered AWS VPCs can be modeled as a single Remote Network if the Connectors can reach the combined address space.
- **No performance penalty** for multiple Remote Networks. If VPCs are peered only for remote access, treat each as its own Remote Network with its own Connectors so traffic goes directly to the Resource with no network traversal.
- **Private DNS** is recommended but not required. It improves the user experience and avoids address space collisions as the deployment grows. Twingate needs no public DNS entries, and Connectors resolve local addresses, so the internal network stays hidden from the Internet.
- Private DNS names (e.g. `resource.company.int`) resolve only while Twingate is connected and the user has access. They become unresolvable if Twingate is disconnected or access is revoked.
- **Routing:** Existing routing rules don't need to change for remote access. Set routing purely on security and infrastructure best practices.
- **Firewall:** No inbound traffic from the Internet or any other source is needed for Connectors or Resources. Connectors only initiate outbound connections to Twingate to authenticate and receive their authorized Resource list. User-to-Resource traffic flows over that established connection.

## Prerequisites
- Deployed Twingate Connectors with network reachability to the target Resources.
- Outbound connectivity from Connectors to Twingate (see Connector Best Practices for network requirements).

## Step-by-Step (Example: Isolated Subnets)
1. Identify subnets, e.g. `10.1.0.0/16` and `10.2.0.0/16`, that cannot route to each other.
2. Deploy one Connector on each subnet (e.g. `10.1.0.35` and `10.2.0.35`).
3. Each Connector resolves addresses local to its own subnet, so both subnets are reachable remotely without cross-subnet traffic.

## Configuration Values
None. This page is architectural guidance only, with no env vars, CLI flags, or API parameters.

## Gotchas
- Don't peer networks or open routes between segments just for remote access. It adds unnecessary traversal.
- Without private DNS, address space collisions are more likely as the deployment expands.
- Private DNS names stop resolving when the client is disconnected, which is expected behavior.
- Don't open inbound firewall ports for Connectors or Resources. They aren't needed.

## Related Docs
- How DNS works with Twingate
- Connector Best Practices (Connector network requirements)