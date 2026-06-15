# Understanding Connectors

## Page Title
Understanding Connectors

## Summary
Connectors are software-defined proxies that form the backbone of Twingate's network, enabling secure access to protected Resources without acting as VPN gateways. They reside inside private networks, handle name/address resolution locally, and are automatically clustered for redundancy. Users never interact with Connectors directly—Twingate routes traffic transparently.

## Key Information
- Connectors must **never** be exposed to the public internet; always deploy behind a firewall within the private network
- Users never connect directly to a Connector—routing is transparent and automatic
- Connectors do **not** join users to the private network; they act as narrow proxies for authorized Resources only
- DNS and IP resolution happens **at the Connector**, not on the user's device—enables private DNS names and IPs
- Multiple Connectors across networks add no user-facing complexity
- Connectors within the same Remote Network are **automatically clustered** for redundancy
- Traffic is routed to the **geographically nearest** Connector automatically
- Precise split tunneling: only authorized Resource traffic flows through a Connector

## Prerequisites
- A private network (cloud or on-prem) to deploy Connectors within
- Firewall in place to prevent public internet exposure of Connectors
- Twingate Remote Network configured

## Architecture Gotchas
- **Not a VPN gateway**: Do not treat Connectors like traditional VPN endpoints—no network-level access is granted to users
- **Firewall requirement**: Connectors initiate outbound connections; inbound access from the internet is not needed and should be blocked
- **Separate Connectors per subnet**: Deploy individual Connectors within each network segment rather than routing across subnets to a single Connector
- **Redundancy requires same Remote Network**: Auto-clustering only applies to Connectors within the same Twingate Remote Network
- **No routing changes needed**: Twingate handles multi-network routing automatically; no infrastructure changes required for remote access segmentation

## Configuration Values
| Concern | Guidance |
|---|---|
| Network placement | Inside private subnet, behind firewall |
| Internet exposure | None (outbound only) |
| Redundancy | Deploy 2+ Connectors per Remote Network |
| Geographic routing | Deploy one Connector per region for replicated services |

## Related Docs
- Connectors Best Practices
- Access Control for Staging Environments
- Environment-specific deployment guides (cloud and on-prem)