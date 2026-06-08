# Understanding Connectors

## Page Title
Understanding Connectors

## Summary
Connectors are software-defined proxies that form the backbone of Twingate's network access, routing authorized user traffic to protected Resources without exposing them to the public internet. They differ fundamentally from VPN gateways by acting as narrow, centrally-coordinated proxies rather than network gateways. Connectors handle name/address resolution locally and are automatically clustered for redundancy.

## Key Information
- Connectors must reside **behind a firewall** within the private network—never publicly accessible
- Users never directly connect to Connectors; routing is handled transparently by Twingate
- Connectors do **not** allow users to join the private network—only specific authorized connections pass through
- DNS/IP resolution happens at the Connector (Remote network side), not on the user's device
- Connectors are automatically clustered within the same Remote network for redundancy
- Traffic is routed to the **geographically nearest** Connector automatically
- Only traffic destined for authorized Resources flows through a Connector (precise split tunneling)
- Multiple Connectors across networks add no user-facing complexity

## Architecture Implications
- Deploy Connectors **inside** private subnets alongside the Resources they protect
- Multiple Connectors on separate networks = users can access multiple networks without routing changes
- Connectors scale horizontally—add more as demand grows, no reconfiguration required
- Replicated services across regions: deploy one Connector per region for latency optimization

## Gotchas
- Connectors are **not** VPN gateways—do not place them in DMZs or expose them publicly
- Network infrastructure changes are not required to support remote access; Connectors handle routing internally
- Users are unaware of which Connector handles their connection—don't design workflows assuming Connector visibility
- Private DNS names/IPs work for users without direct network connectivity because resolution is forwarded to the Connector's network

## Prerequisites
- Firewall/private network environment for Connector placement
- Twingate Remote network configured before deploying Connectors
- See environment-specific deployment guides for cloud or on-prem setup

## Related Docs
- Connectors Best Practices (geographic routing details)
- Access Control for Staging Environments (multi-network segmentation example)
- Environment-specific Connector deployment guides (cloud/on-prem)