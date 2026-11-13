---
source: https://www.twingate.com/docs/exit-networks
type: docs
fetched: 2026-11-13
source_version: edbf76ef1d951c5d9ef3b47afc62e7c1c54480c8a01c55b581594eb861185e01
trust: official
---

# Exit Networks

## Summary
Exit Networks let end users route all traffic (not just Resource traffic) through Twingate, fully encrypting everything that leaves the device. Traffic exits through Connectors acting as exit nodes, selected by geographic proximity. This differs from Twingate's default split-tunnel routing.

## Key Information
- Opt-in feature; available on Home, Business, and Enterprise plans.
- Exit Network = a collection of Connectors acting as exit nodes.
- Resource traffic still routes to Resources; only non-Resource traffic uses the Exit Network.
- Traffic goes through the geographically closest Connector, with automatic failover to another Connector if one goes down.
- Use cases: untrusted networks (hotel or coffee shop Wi-Fi), accessing home-region content while traveling, verifying content localization in other countries.
- DNS filtering continues to work normally while routing all traffic.
- Exit Network use cannot be enforced; users must toggle it manually in the Client.

## Prerequisites
- A plan that includes Exit Networks.
- Admin Console access.
- Ability to deploy Connectors (see the Deploying Connectors guide).

## Step-by-Step
1. In the Admin Console, go to **Internet Security > Exit Networks**.
2. Create a new Exit Network with a unique name (e.g., "United States" or "Coffee Shop Mode").
3. Deploy Connectors inside the Exit Network (at least two recommended).
4. In the Twingate Client, hover over **Route All Traffic Through Twingate** and select the Exit Network. Use the same menu to stop.
5. (Optional) Click **Enabled for Everyone** (or **X Groups**) to restrict Exit Network use to selected Groups. Users outside those Groups cannot use any Exit Network.

## Configuration Values
No env vars, CLI flags, or API parameters are given on this page. Configuration is done through the Admin Console and Client menu.

## Gotchas
- **Session limit:** Exit Network sessions are currently limited to 12 hours.
- **IPv6 is unsupported:** AAAA queries are blocked while routing all traffic, so domains requiring IPv6 are unreachable.
- **Security risk:** If Exit Network Connectors can reach your protected Resources, users routing all traffic could reach Resources without authentication checks. Deploy them outside existing infrastructure (separate VPC or point-of-presence style).
- **Peer-to-peer:** Connectors should be peer-to-peer friendly for lower latency and to stay within the Fair Use Policy for bandwidth. Validate your specific deployment's NAT behavior.
- **Egress costs:** GCP, AWS, and Azure charge high egress prices. Providers with bundled bandwidth (DigitalOcean, Vultr, Linode, Hetzner) can reduce costs, at roughly 0.5-20 TB included depending on provider and instance type or region.
- Some sites may be unreachable depending on Connector deployment or current Exit Network limitations; contact support.

## Related Docs
- Deploying Connectors guide
- Split tunnel routing
- How Connectors are selected for Resources
- Peer-to-peer connections setup and troubleshooting
- Fair Use Policy
- Remote Networks (failover behavior comparison)