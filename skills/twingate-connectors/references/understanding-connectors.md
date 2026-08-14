---
source: https://www.twingate.com/docs/understanding-connectors
type: docs
fetched: 2026-08-14
source_version: e4b3ed2d89fbb68fc3fc2683bc1c0fea0a9917b7ce15890301a1f1de1b38e5e7
---

# Understanding Connectors

## Summary
Twingate Connectors are software-defined proxies that route authorized user traffic to protected Resources within private networks. Unlike VPN gateways, Connectors never expose the private network to users—they act as narrow access points for individual authorized connections only.

## Key Information

- Connectors **must reside behind a firewall** within the private network—never exposed to the public internet
- Users never directly connect to Connectors; routing happens transparently behind the scenes
- Connectors do **not** grant users access to the entire private network—only to authorized Resources
- Name/DNS resolution occurs **at the Connector**, not on the user's device—enables use of private DNS names and IPs
- Connectors are **automatically clustered** for redundancy within the same Remote network
- Traffic is automatically routed to the **geographically nearest** Connector when multiple are deployed
- Only traffic destined for authorized Resources flows through a Connector (precise split tunneling)
- No limit on deploying Connectors across multiple private networks—users see no added complexity

## Architecture Behavior

| Behavior | VPN Gateway | Twingate Connector |
|---|---|---|
| Public internet exposure | Often required | Never |
| User joins private network | Yes | No |
| DNS resolution location | User device | Connector |
| Traffic scope | All network traffic | Authorized Resources only |

## Deployment Recommendations

- Deploy **multiple Connectors per Remote network** for redundancy (automatic clustering)
- Deploy Connectors **per geographic region** when services are replicated, to minimize latency
- Deploy Connectors **per network subnet** to segment access without infrastructure routing changes
- No need to modify network routing or firewall rules to support remote access use cases

## Gotchas

- Connectors should never be reachable from the public internet—placing one in a DMZ or with a public IP is a misconfiguration
- Users cannot be routed to a Connector they "choose"—routing is automatic and opaque to users
- Split tunneling is enforced by design: non-Resource traffic is never routed through Connectors
- Multiple Connectors on the same Remote network cluster automatically—no manual clustering configuration needed

## Prerequisites

- Private network infrastructure where Connector will reside
- Firewall rules allowing outbound Connector connections (to Twingate control plane), but **no inbound rules required**

## Related Docs

- Connectors Best Practices (geographic routing details)
- Access Control for Staging Environments (multi-network segmentation example)
- Environment-specific deployment guides (cloud/on-prem)