# Configuring AWS Exit Nodes for SaaS App Gating

## Summary
Configure Twingate Connectors on AWS EC2 instances to act as exit nodes, enabling IP-based access control to public SaaS applications. Traffic from authorized users is routed through EC2 instances with known public IPs, which are then whitelisted in third-party SaaS apps.

## Key Information
- Enables user-based access control to public SaaS apps via IP whitelisting
- Requires at least one Linux EC2 instance (multiple recommended for redundancy)
- EC2 instances serve as Twingate Connectors and traffic exit points
- Public IP of EC2 instances is what gets whitelisted in third-party apps

## Prerequisites
- AWS account with ability to deploy EC2 instances
- Linux EC2 instance (Ubuntu 22.04 recommended; any Docker-compatible Linux works)
- Docker support on the instance
- Twingate admin console access

## Step-by-Step

1. **Deploy EC2 instance(s)**
   - Minimum: `t3a.micro` (general purpose instance acceptable)
   - OS: Ubuntu 22.04 recommended
   - Deploy multiple instances for redundancy

2. **Configure networking**
   - Allow outbound internet traffic from EC2 instances
   - Block all inbound internet traffic (SSH access optional for setup only)
   - Assign Elastic IP to each EC2 instance

3. **Verify public IP address**
   - Check whether egress routes through NAT gateway or IGW
   - NAT gateway may mask the instance's own public IP
   - The IP that external services see is what you whitelist in SaaS apps

4. **Install Twingate Connector**
   - Follow Linux Connector deployment docs

5. **Create Resource in Twingate**
   - Resource name = FQDN of protected app (e.g., `acme.salesforce.com`)
   - Twingate uses FQDN/IP from connection request for authorization checks

6. **Authorize users**
   - Create a Group in Twingate admin console
   - Add the Resource to the Group
   - Assign users to the Group

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Instance type | `t3a.micro` (minimum) |
| Recommended OS | Ubuntu 22.04 |
| Inbound traffic | Block all (SSH optional) |
| Outbound traffic | Must allow all |
| IP assignment | Elastic IP per instance |

## Gotchas
- **NAT Gateway masking**: If using a NAT gateway, the EC2 instance's Elastic IP may not be the egress IP seen by external services — verify actual outbound IP before whitelisting
- **IP redundancy**: Whitelist public IPs from all EC2 instances in the SaaS app, otherwise failover to a secondary instance will break access
- **Production use**: Guide is illustrative only; apply AWS security best practices for production deployments
- **Image versions**: Code samples may reference outdated container/software versions — check official docs

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs)
- [Deploying Connectors on Linux](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Creating Resources and Groups](https://www.twingate.com/docs)