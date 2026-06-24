# Understanding Connectors

## Summary
Connectors are software-defined proxies that form the backbone of Twingate's network, routing authorized user traffic to protected Resources without exposing the private network. Unlike VPN gateways, Connectors are never publicly accessible and only pass traffic for explicitly authorized Resources.

## Key Information

- **Not a VPN gateway**: Connectors must reside behind a firewall within the private network—never exposed to the public internet
- **Transparent to users**: Users connect to Resources, not Connectors; routing happens automatically behind the scenes
- **No network join**: Connectors act as narrow keyholes—only authorized individual connections pass through, users never join the private network
- **Name/DNS resolution**: Happens at the Connector (local to the Remote network), not on the user's device—enables use of private DNS names and IPs
- **Automatic clustering**: Multiple Connectors in the same Remote network are auto-clustered for redundancy; no manual configuration required
- **Geographic routing**: Twingate automatically routes users to the nearest available Connector, reducing latency
- **Precise split tunneling**: Only traffic destined for authorized Resources flows through a Connector

## Architecture Behavior

| Behavior | Detail |
|---|---|
| Deployment location | Inside private network, behind firewall |
| User awareness | None—routing is invisible |
| Traffic scope | Only authorized Resource traffic |
| Clustering | Automatic within same Remote network |
| Scalability | Add Connectors as needed for demand |

## Gotchas

- Connectors must **never** have public internet exposure—this is a security requirement, not a recommendation
- DNS/name resolution occurs at the Connector level, so DNS configuration must be correct on the host running the Connector
- Multiple Connectors across different networks add no user-facing complexity—deploy freely to mirror existing network segmentation
- Connectors on separate networks allow multi-network access without routing/infrastructure changes on the network side

## Use Cases Enabled

- Access to staging environments with isolated network segments
- Multi-region deployments with latency-optimized routing
- Private DNS name resolution for remote users without full network access

## Related Docs

- Connectors Best Practices
- Access Control for Staging Environments
- Environment-specific deployment guides (cloud and on-prem)