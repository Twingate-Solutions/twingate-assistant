# Configuring AWS Exit Nodes for SaaS App Gating

## Summary
Use Twingate Connectors deployed on AWS EC2 instances as exit nodes to control access to public SaaS applications via IP whitelisting. Traffic from authorized users is routed through EC2 instances with known public IPs, which are then whitelisted in target SaaS applications.

## Key Information
- Enables user-based access control to public SaaS apps using IP filtering
- Requires at least one Linux EC2 instance (multiple recommended for redundancy)
- Recommended instance type: `t3a.micro` (any general purpose instance acceptable)
- Recommended OS: Ubuntu 22.04 (any Linux with Docker support works)
- Public IP of EC2 instances is what gets whitelisted in 3rd-party apps

## Prerequisites
- AWS account with ability to deploy EC2 instances
- Docker support on target Linux instances
- Twingate admin console access
- Outbound internet traffic allowed from EC2 instances

## Step-by-Step

1. **Deploy EC2 instances** — Launch at least one Linux EC2 instance (`t3a.micro` or larger)
2. **Configure networking** — Allow outbound internet traffic; block all inbound internet traffic (SSH only if needed during setup)
3. **Assign Elastic IPs** — Attach a public Elastic IP to each EC2 instance
4. **Verify public IP** — Confirm the actual egress IP (NAT gateway vs IGW can mask the instance IP); this IP is what you whitelist
5. **Install Connectors** — Follow Twingate Linux Connector deployment docs on each instance
6. **Create Twingate Resource** — Add the SaaS app FQDN (e.g., `acme.salesforce.com`) as a Resource in admin console
7. **Authorize users** — Create a Group, assign the Resource and users to it
8. **Whitelist IPs in SaaS app** — Add the EC2 instance public Elastic IP(s) to the SaaS application's IP allowlist

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Instance type | `t3a.micro` (minimum) |
| OS | Ubuntu 22.04 (recommended) |
| Inbound traffic | Block all (except SSH if needed) |
| Outbound traffic | Allow all |
| IP type | Public Elastic IP per instance |

## Gotchas
- **NAT gateway masking**: If egress traffic routes through a NAT gateway instead of an IGW, the instance's Elastic IP may not be the actual public egress IP — verify before whitelisting
- **No inbound required**: Twingate Connectors only need outbound connectivity; don't expose instances to inbound internet traffic
- **Redundancy**: Single instance = single point of failure; deploy multiple instances
- **IP stability**: Use Elastic IPs, not auto-assigned public IPs, to prevent IP changes on instance restart

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs)
- [Deploying Connectors on Linux](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Creating Resources and Groups in Twingate Admin Console](https://www.twingate.com/docs)