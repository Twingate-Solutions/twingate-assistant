# Understanding Connectors

## Page Title
Understanding Connectors

## Summary
Connectors are software-defined proxies that form the backbone of Twingate's network access, routing authorized user traffic to protected Resources without exposing them to the public internet. Unlike VPN gateways, Connectors operate transparently to users and never grant broad network access—only permitting connections to explicitly authorized Resources.

## Key Information
- Connectors **must never be publicly accessible**; always deploy behind a firewall within the private network
- Users never directly connect to a Connector—routing happens transparently behind the scenes
- Connectors do **not** allow users to join the private network; they act as narrow, per-Resource proxies
- Name/DNS resolution happens **at the Connector**, not on the user's device—enables private DNS and IP access
- Connectors within the same Remote Network are **automatically clustered** for redundancy
- Only traffic to authorized Resources flows through a Connector (precise split tunneling)
- Multiple Connectors can be deployed across geographic regions; Twingate routes to the nearest one automatically

## Prerequisites
- A defined Twingate Remote Network
- Firewall/private network environment to host the Connector
- Resources defined within the same network segment as the Connector

## Architecture Notes
| Concept | Behavior |
|---|---|
| Public internet exposure | Never—Connector stays internal |
| User awareness of Connector | None—fully transparent |
| DNS resolution | Local to Connector's network |
| Clustering | Automatic within same Remote Network |
| Traffic scope | Only authorized Resource traffic |

## Gotchas
- Deploying multiple Connectors across networks adds **no complexity for users** but improves redundancy and latency
- Network routing/infrastructure changes are **not required** to support remote access—Connectors handle segmentation
- Geographic routing is automatic; no manual configuration needed when Connectors are deployed in multiple regions
- Connectors are software-only—no special hardware required

## Related Docs
- Connector Best Practices (referenced for geographic routing details)
- Access Control for Staging Environments (example multi-network use case)
- Environment-specific Connector deployment guides (cloud and on-prem)