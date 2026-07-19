# Understanding Connectors

## Summary
Twingate Connectors are software-defined proxies that route authorized user traffic to protected Resources within private networks. Unlike VPN gateways, they never expose the private network directly to users and handle name/address resolution locally. They cluster automatically for redundancy and support precise split tunneling.

## Key Information
- Connectors must reside **behind a firewall** within the private network — never exposed to the public internet
- Users never directly connect to a Connector; routing happens transparently behind the scenes
- Connectors do **not** grant users access to the broader private network — only to authorized Resources
- DNS/IP resolution occurs at the Connector level (within the Remote network), not on the user's device
- Connectors within the same Remote network are **automatically clustered** for redundancy
- Traffic is routed to the **geographically nearest** available Connector automatically
- Only traffic destined for authorized Resources is routed through a Connector (precise split tunneling)

## Deployment Considerations
- Deploy multiple Connectors across private networks without adding user-facing complexity
- No network routing or infrastructure changes required to support remote access
- Deploy Connectors in each geographic region when services are replicated across regions
- Add Connectors as needed to scale with demand — no reconfiguration required

## Architecture Differences vs. VPN
| VPN Gateway | Twingate Connector |
|---|---|
| Internet-accessible | Never internet-accessible |
| User selects gateway | Routing is automatic/transparent |
| Grants network-level access | Grants Resource-level access only |
| Complex multi-network setup | Deploy per-subnet, no user impact |

## Gotchas
- Connectors **must** be inside the private network they protect — placing them in a DMZ or public subnet breaks the security model
- Private DNS names and IPs work for users **because** resolution is forwarded to the Connector's network — this only works if the Connector has proper DNS access within its subnet
- Automatic clustering only applies to Connectors within the **same Remote network**; cross-network routing is not automatic

## Related Docs
- Connectors Best Practices (geographic routing details)
- Access Control for Staging Environments (multi-network segmentation example)
- Environment-specific Connector deployment guides (cloud/on-prem)