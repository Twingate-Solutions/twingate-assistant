# Understanding Connectors

## Page Title
Understanding Connectors

## Summary
Connectors are software-defined proxies that form the backbone of Twingate's network access architecture. They route authorized user traffic to protected Resources without exposing the private network or requiring VPN-style direct connections. Connectors are automatically clustered for redundancy and handle routing transparently to end users.

## Key Information
- Connectors must **never** be publicly accessible — always deploy behind a firewall within the private network
- Users never directly connect to Connectors; routing is handled automatically by Twingate
- Connectors do not grant private network access — only allow individual authorized connections to specific Resources
- DNS/name resolution occurs **at the Connector** (local to the Remote network), not on the user's device — enables private DNS names and IPs
- Connectors within the same Remote network are **automatically clustered** for redundancy
- Traffic is routed to the **geographically nearest** Connector automatically
- Precise split tunneling: only traffic destined for authorized Resources flows through a Connector

## Prerequisites
- Firewall in place to block public internet access to Connector hosts
- Connector deployed within the same subnet/network as the Resources it serves

## Architecture Notes
- Deploy one Connector per private network/subnet as needed — no user-facing complexity added
- Multiple Connectors in the same Remote network = automatic clustering (no manual configuration)
- For geographically replicated services, deploy Connectors in each region for latency optimization
- No routing table or infrastructure changes required on the network to support remote access

## Gotchas
- Connectors are **not** VPN gateways — do not expose them to the internet or treat them as network entry points
- Name resolution happens at the Connector, not the client — misconfigured DNS on the Connector host will break Resource access
- Users never see or select Connectors — do not design workflows that assume user Connector awareness
- Each Connector is scoped to its Remote network; cross-network access requires separate Connectors per network

## Configuration Values
No specific env vars or CLI flags documented on this page. See environment-specific deployment guides for configuration details.

## Related Docs
- Connectors Best Practices (geographic routing details)
- Access Control for Staging Environments (multi-network segmentation example)
- Environment-specific Connector deployment guides (cloud/on-prem)