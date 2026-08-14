---
source: https://www.twingate.com/docs/configuring-aws-exit-nodes
type: docs
fetched: 2026-08-14
source_version: 919054f4dfb7ccf31d11927ced270aa6404303d4add4cc3112880539600c2179
---

# Configuring AWS Exit Nodes for SaaS App Gating

## Page Title
How to SaaS App Gate with AWS Exit Nodes

## Summary
Use Twingate Connectors deployed on AWS EC2 instances to provide user-based access control to public SaaS applications via IP whitelisting. Traffic from authorized users is routed through EC2 instances with known public IPs, which are then whitelisted in third-party SaaS applications.

## Key Information
- EC2 instances act as exit nodes; their public IPs are whitelisted in SaaS apps
- Requires at least one EC2 instance (multiple recommended for redundancy)
- Recommended instance type: `t3a.micro` (any general-purpose instance works)
- Recommended OS: Ubuntu 22.04 (any Linux supporting Docker is acceptable)
- Outbound internet traffic must be allowed from EC2 instances
- Inbound internet traffic is **not required** (block all inbound unless SSH needed for setup)

## Prerequisites
- AWS account with ability to launch EC2 instances
- Twingate admin access
- Docker-compatible Linux on EC2
- Elastic IPs assigned to EC2 instances
- Access to whitelist IPs in target SaaS application

## Step-by-Step

1. **Deploy EC2 instances**
   - Launch one or more Linux EC2 instances (`t3a.micro` minimum)
   - Use Ubuntu 22.04 or any Docker-compatible Linux
   - Allow outbound internet traffic; block all inbound (except SSH if needed)

2. **Verify public IP addresses**
   - Assign Elastic IPs to each EC2 instance
   - Confirm the actual egress public IP — NAT gateway may mask the instance IP
   - These public IPs are what you whitelist in third-party SaaS apps

3. **Install Twingate Connectors**
   - Follow [deploying Connectors on Linux](https://www.twingate.com/docs/linux) documentation

4. **Create a Twingate Resource**
   - In Twingate admin console, create a Resource using the FQDN or IP of the SaaS app (e.g., `acme.salesforce.com`)

5. **Authorize users**
   - Create a Group, add the Resource to the Group, assign users to the Group
   - Users in the Group can access the whitelisted app from any network via Twingate

## Configuration Values
- Instance type: `t3a.micro` (minimum recommended)
- OS: Ubuntu 22.04 (preferred)
- Network: Elastic IP per instance; egress via IGW or NAT gateway

## Gotchas
- **NAT Gateway masking**: If egress traffic routes through a NAT gateway, the NAT gateway's IP (not the EC2 instance's Elastic IP) will be the actual public egress IP — whitelist the correct one
- Multiple EC2 instances needed for redundancy; single instance is a SPOF
- This is a guide, not hardened production config — follow AWS security best practices separately
- Software/image versions in examples may be outdated; check official docs

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs/whitelisting-traffic)
- [Deploying Connectors on Linux](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Creating Resources and Groups](https://www.twingate.com/docs/resources)