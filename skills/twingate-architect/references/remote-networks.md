---
source: https://www.twingate.com/docs/remote-networks
type: docs
fetched: 2026-11-13
source_version: 9e3d1d4f4af4d2a900b51222d495ad7a3125fdae9a0f0e0b5521c1bad42167cd
trust: official
---

# Page Title
Remote Networks (Twingate Docs)

## Summary
A Remote Network in Twingate is a logical container that groups Resources. Each Remote Network roughly maps to a physical network or VPC you want to give remote access to. At least one Connector must be deployed in a Remote Network for its Resources to be reachable, and two or more are recommended.

## Key Information
- All Resources in a Remote Network must be reachable from every Connector deployed in that same Remote Network.
- Connectors are deployed behind the firewall. They give authenticated, authorized users access to the Remote Network's Resources.
- With no Connector deployed and running, Resources are inaccessible to end users.
- Recommended: at least two Connectors per Remote Network, for:
  - **Load balancing and failover:** Load balancing happens automatically as the number of Connectors changes. If one Connector fails, the others provide redundancy.
  - **Scalability:** Add Connectors as traffic grows. A single Connector can generally handle hundreds of users, depending on usage patterns.
- There is no stated limit on the number of Connectors per Remote Network.

## Prerequisites
- A Twingate account.
- A physical network or VPC to expose.
- The ability to deploy Connectors inside that network, behind the firewall.

## Step-by-Step
The page gives no procedure. The implied workflow is:
1. Create a Remote Network for each physical network or VPC.
2. Define Resources within it.
3. Deploy at least two Connectors in that network.
4. Confirm every Connector can reach every Resource.

## Configuration Values
None listed on this page (no env vars, CLI flags, or API parameters).

## Gotchas
- Connectors in a Remote Network are interchangeable, so they must all have identical network routing and access rules for that network. If they differ, a user's access may succeed or fail depending on which Connector handles the traffic.
- A single Connector is a single point of failure.
- Resources must be reachable from *all* Connectors in the Remote Network, not just one.
- Resources that cannot be reached from a Connector's location should go in a different Remote Network.

## Related Docs
- Connectors (overview and deployment)
- Connector Best Practices
- Remote Network best practices documentation
- Resources