---
source: https://www.twingate.com/docs/configuring-aws-exit-nodes
type: docs
fetched: 2026-08-05
source_version: f9aee35da28c7ed418d3adf391e841f5d7f410238de3ee1ff0200f74a9923d6a
---

# Configuring AWS Exit Nodes (SaaS App Gating)

## Summary
Use Twingate Connectors deployed on AWS EC2 instances as exit nodes to control access to public SaaS applications via IP whitelisting. Traffic from authorized users routes through EC2 instances, allowing the EC2's public IP to be whitelisted in third-party apps.

## Key Information
- EC2 instances act as exit nodes; their public IPs get whitelisted in SaaS apps
- Minimum one EC2 instance required; multiple recommended for redundancy
- Recommended instance type: `t3a.micro` (any general purpose works)
- Recommended OS: Ubuntu 22.04 (any Linux supporting Docker works)
- Outbound internet traffic must be allowed from EC2 instances
- Inbound internet traffic is **not required** (block all inbound unless SSH needed for setup)

## Prerequisites
- AWS account with ability to deploy EC2 instances
- Elastic IPs assigned to each EC2 instance
- Understanding of your AWS network topology (NAT gateway vs IGW affects public IP)
- Twingate admin console access

## Step-by-Step

### 1. Deploy EC2 Instances
- Launch ≥1 Linux EC2 instance (`t3a.micro` or larger)
- Assign a public **Elastic IP** to each instance
- Configure security groups: allow outbound internet, block inbound internet (except SSH if needed)
- Install Twingate Connector (see Linux Connector deployment docs)

### 2. Verify Public IP Address
- Determine the actual egress public IP — NAT gateways can mask the EC2 instance's Elastic IP
- The IP that appears in SaaS app logs is what you whitelist, not necessarily the Elastic IP
- Whitelist the verified public IP(s) in the target SaaS application

### 3. Create Twingate Resource
- In Twingate admin console, create a Resource using the FQDN or IP of the protected application
- Example: `acme.salesforce.com`

### 4. Authorize Users
- Create a Group in Twingate
- Assign the Resource to the Group
- Add authorized users to the Group

## Configuration Values
| Parameter | Value |
|-----------|-------|
| EC2 instance type | `t3a.micro` (minimum recommended) |
| OS | Ubuntu 22.04 (preferred) |
| Inbound traffic | Block all (except SSH for setup) |
| Outbound traffic | Allow all |
| IP assignment | Elastic IP per instance |

## Gotchas
- **NAT Gateway masking**: If egress traffic routes through a NAT gateway, the Elastic IP on the EC2 instance may not be the public IP seen by external services — verify actual egress IP before whitelisting
- **Production use**: Guide is instructional only; follow AWS security best practices for production
- **Image versions**: Code samples may reference outdated container/software versions — check official docs

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs/whitelisting-traffic-to-public-resources)
- [Deploying Connectors on Linux](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- Twingate Group/Resource authorization docs