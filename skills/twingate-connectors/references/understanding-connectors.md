# Understanding Connectors

## Page Title
Understanding Connectors

## Summary
Connectors are software-defined proxies that form the backbone of Twingate's network access architecture. Unlike VPN gateways, they never expose the private network to users—instead acting as narrow keyholes routing only authorized traffic to specific Resources. They are automatically clustered for redundancy and require no client-side routing configuration.

## Key Information
- Connectors reside **inside** private networks, never exposed to the public internet
- Users never interact with Connectors directly; routing is handled transparently by Twingate
- DNS/name resolution occurs **at the Connector** (within the Remote network), not on the user's device—enables private DNS names and IPs without direct network access
- Connectors provide precise split tunneling: only traffic to authorized Resources flows through them
- Multiple Connectors on the same Remote network are **automatically clustered** for redundancy
- Geographic routing: traffic is automatically directed to the nearest available Connector
- No limit or complexity penalty for deploying Connectors across multiple private networks

## Prerequisites
- Connector must be deployed within the target private network subnet
- Firewall must block public internet access to the Connector host
- Remote network must be configured in Twingate admin before deploying Connectors

## Architecture Notes
| VPN Gateway | Twingate Connector |
|---|---|
| Users connect directly | Users never see Connectors |
| Joins user to full network | Only passes authorized Resource traffic |
| Single gateway = bottleneck | Auto-clustered, multi-Connector |
| Client-side routing changes needed | No routing changes required |

## Configuration Values
- No specific env vars documented on this page
- Connector clustering is automatic within the same Remote network (no manual config)
- Geographic routing is automatic (no configuration required)

## Gotchas
- Connectors must **never** be accessible from the public internet—always deploy behind a firewall
- DNS resolution happens at the Connector, not the client; misconfigured DNS on the Connector host will break Resource resolution
- Adding Connectors to a Remote network doesn't require user-side changes—safe to scale without coordination
- Connectors do not grant users network-level access; they only proxy connections to explicitly authorized Resources

## Related Docs
- Connectors Best Practices (geographic/redundancy deployment patterns)
- Access Control for Staging Environments (multi-network segmentation use case)
- Environment-specific Connector deployment guides (cloud/on-prem)