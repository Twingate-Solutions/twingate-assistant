# Configuring AWS Exit Nodes for SaaS App Gating

## Summary
Deploy Twingate Connectors on AWS EC2 instances to act as exit nodes, enabling IP-based access control to public SaaS applications. Outbound traffic routes through EC2 instances with known Elastic IPs, which are whitelisted in third-party SaaS apps. Users are granted access via Twingate Groups and Resources.

## Key Information
- Use case: Control access to public SaaS apps via IP whitelisting combined with Twingate user authentication
- Requires at least one Linux EC2 instance (multiple recommended for redundancy)
- EC2 instances serve as Twingate Connectors and traffic exit points
- Recommended instance type: `t3a.micro` (any general purpose works)
- Recommended OS: Ubuntu 22.04 (any Linux supporting Docker works)

## Prerequisites
- AWS account with ability to launch EC2 instances
- Twingate admin console access
- Elastic IPs assignable to EC2 instances
- Understanding of your AWS network topology (NAT gateway vs IGW affects public IP)

## Step-by-Step

### 1. Deploy EC2 Exit Nodes
- Launch one or more Linux EC2 instances (`t3a.micro` minimum)
- Assign an **Elastic IP** to each instance
- Verify actual public egress IP — if traffic exits via NAT gateway, the instance's Elastic IP may be masked; confirm which IP external services will see
- Allow outbound internet traffic from instances
- Block all inbound internet traffic (SSH access optional/temporary only)
- Install Twingate Connector on each instance per [Linux Connector deployment docs]

### 2. Whitelist EC2 Public IPs in SaaS Application
- Use the confirmed public egress IP(s) from Step 1
- Add these IPs to the IP allowlist in the target SaaS application (e.g., Salesforce, GitHub)

### 3. Create Twingate Resource
- In Twingate admin console, create a Resource using the FQDN or IP of the protected application
- Example: `acme.salesforce.com`
- Twingate uses this FQDN/IP to evaluate authorization on each connection request

### 4. Authorize Users
- Create a new Group in Twingate
- Add the Resource to the Group
- Assign users to the Group
- Users in the Group can access the SaaS app from any network via Twingate

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Instance type | `t3a.micro` (minimum) |
| OS | Ubuntu 22.04 (recommended) |
| Inbound ports | None required (block all) |
| Outbound | All allowed |

## Gotchas
- **NAT Gateway masking**: If EC2 egress routes through a NAT gateway, the Elastic IP on the instance is NOT the IP seen by external services — verify actual egress IP before whitelisting
- **Multiple instances**: Each instance has its own public IP; all must be whitelisted in the SaaS app
- **Production use**: This guide is a reference only; apply AWS security best practices for production deployments
- Software/image versions in examples may not be current; check official docs for latest versions

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs)
- [Deploying Connectors on Linux](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Creating Resources and Groups](https://www.twingate.com/docs)