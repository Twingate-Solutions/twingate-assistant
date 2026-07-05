# Understanding Connectors

## Summary
Connectors are software-defined proxies that form the backbone of Twingate networks, enabling secure access to private Resources without exposing them to the public internet. Unlike VPN gateways, Connectors never allow users to join the private network directly—they act as narrow keyholes routing only authorized traffic to specific Resources.

## Key Information

- **Never internet-facing**: Connectors must reside behind a firewall within the private network they protect
- **Transparent to users**: Users connect to Resources, not Connectors; routing happens automatically behind the scenes
- **No network join**: Connectors only permit individual authorized connections to specific Resources, not full network access
- **Local name/address resolution**: DNS and IP resolution occurs at the Connector's Remote network, enabling use of private DNS names and IPs without direct network access
- **Auto-clustering**: Multiple Connectors within the same Remote network are automatically clustered for redundancy—no manual configuration required
- **Geo-routing**: Twingate automatically routes users to the nearest available Connector when multiple are deployed across regions
- **Precise split tunneling**: Only traffic destined for authorized Resources routes through a Connector; all other traffic goes direct

## Architecture Behavior

| VPN Gateway | Twingate Connector |
|---|---|
| User selects/connects to gateway | Routing is automatic and invisible |
| User joins the private network | User only reaches specific Resources |
| Public-facing endpoint | Always behind firewall |
| Manual clustering/HA setup | Automatic clustering within Remote network |

## Deployment Recommendations

- Deploy Connectors **inside** the subnet containing the Resources they serve
- Deploy **multiple Connectors per Remote network** for redundancy (auto-clustered)
- Deploy Connectors in **each geographic region** where replicated services exist
- No need to modify network routing or firewall rules to support remote access use cases—segment networks per best practices and add Connectors as needed

## Prerequisites

- A firewall/private network boundary for the Connector to reside behind
- A Twingate Remote network configured before deploying Connectors

## Gotchas

- Connectors should **never** have a public IP or be reachable from the internet
- DNS resolution for Resources happens at the Connector, not the client—private DNS names work, but the Connector must be able to resolve them
- Each Connector auto-clusters only within the **same Remote network**; Connectors in different Remote networks are independent
- Traffic isolation is automatic: only authorized Resource traffic flows through a given Connector

## Related Docs

- Connectors Best Practices (geo-routing, scaling)
- Access Control for Staging Environments (multi-network segmentation use case)
- Environment-specific deployment guides (cloud/on-prem)