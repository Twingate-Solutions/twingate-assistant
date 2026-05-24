# Understanding Connectors

## Summary
Twingate Connectors are software-defined proxies that route authorized user traffic to protected Resources within private networks. They differ fundamentally from VPN gateways by never exposing the private network directly to users and handling all name/address resolution locally. Connectors are automatically clustered for redundancy and can be deployed across multiple networks without user-facing complexity.

## Key Information

- **Never internet-accessible**: Connectors must reside behind a firewall within the private network they protect
- **Transparent to users**: Users connect to Resources, not Connectors directly; routing is handled automatically
- **No network join**: Connectors act as narrow proxies—only authorized individual connections pass through, not full network access
- **Local DNS resolution**: Name and address resolution happens at the Connector, not the user's device—enables use of private DNS names and IPs
- **Automatic clustering**: Multiple Connectors on the same Remote network are auto-clustered for redundancy
- **Geographic routing**: Traffic is automatically routed to the nearest available Connector when multiple are deployed across regions
- **Precise split tunneling**: Only traffic destined for authorized Resources routes through a Connector

## Architecture Behavior

| VPN Gateway | Twingate Connector |
|-------------|-------------------|
| Users connect directly | Users never see/choose Connectors |
| Joins user to network | Passes only authorized connections |
| Internet-accessible | Always behind firewall |
| Single point of complexity | Transparent multi-network support |

## Deployment Recommendations

- Deploy Connectors **inside** the private subnet alongside Resources
- Deploy **multiple Connectors** per Remote network for redundancy (auto-clustered)
- Deploy Connectors in **each geographic region** where Resources are replicated
- No routing or infrastructure changes required to support remote access—add Connectors as network segments are defined

## Gotchas

- Connectors should **never** have public internet exposure—this is a security misconfiguration
- Users do not need to know which Connector handles their traffic; do not design workflows around specific Connector selection
- Multiple Connectors add redundancy without adding user-facing complexity—there is no downside to deploying more

## Related Docs

- Connector Best Practices
- Access Control for Staging Environments
- Environment-specific deployment guides (cloud and on-prem)