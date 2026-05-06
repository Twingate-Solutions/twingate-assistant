# Understanding Connectors

## Page Title
Understanding Connectors

## Summary
Connectors are software-defined proxies that serve as the backbone of Twingate networks, routing authorized traffic to protected Resources without acting as VPN gateways. They reside inside private networks, are never directly accessible from the internet, and automatically cluster for redundancy within a Remote network.

## Key Information
- Connectors **must sit behind a firewall** inside the private network containing protected Resources — never publicly exposed
- Users never connect directly to a Connector; Twingate routes traffic through the appropriate Connector transparently
- Connectors do **not** grant users access to the full private network — only to authorized individual Resources
- Name/DNS resolution happens **at the Connector**, not on the user's device — enables use of private DNS names and IPs
- Multiple Connectors can be deployed across networks without adding complexity for users
- Connectors within the same Remote network are **automatically clustered** for redundancy
- Traffic is automatically routed to the **geographically nearest** Connector when multiple are deployed
- Only traffic destined for authorized Resources is routed through a Connector (precise split tunneling)
- No network routing or infrastructure changes required to support remote access use cases

## Prerequisites
- A Twingate Remote network configured
- Firewall/private network environment to host the Connector
- Resources defined within the same network segment as the Connector

## Architecture Gotchas
- **Connectors ≠ VPN gateways** — do not treat them as such for firewall rules or network design
- Deploying more Connectors does **not** increase user-facing complexity — safe to mirror existing network topology
- Each separate network/subnet requiring access needs its own Connector deployment; this replaces the need for routing rule changes
- Split tunneling is enforced automatically — only authorized Resource traffic flows through the Connector, not general internet traffic

## Configuration Values
No specific env vars or CLI flags documented on this page. See environment-specific deployment guides for configuration parameters.

## Related Docs
- [Connectors Best Practices](https://www.twingate.com/docs/connectors-best-practices) — geographic routing details
- [Access Control for Staging Environments](https://www.twingate.com/docs/access-control-for-staging-environments) — multi-network segmentation use case
- Environment-specific Connector deployment guides (linked in docs section)