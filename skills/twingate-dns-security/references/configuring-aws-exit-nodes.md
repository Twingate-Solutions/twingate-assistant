# Configuring AWS Exit Nodes for SaaS App Gating

## Page Title
How to SaaS App Gate with AWS Exit Nodes

## Summary
This guide explains how to use Twingate Connectors deployed on AWS EC2 instances as exit nodes to provide user-based access control to public SaaS applications via IP whitelisting. Traffic from users routes through the EC2 instances, allowing their public IPs to be whitelisted with third-party applications. This is a production-capable pattern requiring additional security hardening beyond what's documented here.

## Key Information
- EC2 instances act as egress points; the instance's public IP is what gets whitelisted with SaaS providers
- Minimum recommended instance type: `t3a.micro` (general purpose)
- Recommended OS: Ubuntu 22.04 (any Docker-compatible Linux works)
- Deploy **multiple instances** for redundancy
- Twingate uses FQDN or IP from the connection request to determine access authorization

## Prerequisites
- AWS account with ability to deploy EC2 instances
- Twingate admin console access
- Docker support on target Linux instances
- Elastic IPs assigned to each EC2 instance
- Understanding of whether egress traffic leaves via NAT Gateway or IGW (affects which public IP to whitelist)

## Step-by-Step

1. **Deploy EC2 instances**
   - Launch one or more Linux EC2 instances (`t3a.micro` or larger)
   - Use Ubuntu 22.04 or any Docker-compatible Linux
   - Assign an **Elastic IP** to each instance

2. **Configure security groups**
   - Allow outbound internet traffic from instances
   - Block all inbound internet traffic (SSH inbound only if needed for setup)

3. **Verify public IP behavior**
   - Confirm whether egress goes through IGW (uses Elastic IP) or NAT Gateway (uses NAT Gateway IP)
   - Whitelist the correct public IP(s) with your SaaS application

4. **Install Twingate Connector**
   - Follow [deploying Connectors on Linux](https://www.twingate.com/docs/connectors-linux) documentation

5. **Create a Twingate Resource**
   - Name the Resource using the FQDN of the protected application (e.g., `acme.salesforce.com`)

6. **Authorize users**
   - Create a Group, add the Resource to the Group, assign users to the Group

## Configuration Values
- Instance type: `t3a.micro` (minimum recommended)
- OS: Ubuntu 22.04 (recommended)
- Inbound ports: none required (block all)
- Outbound: all allowed

## Gotchas
- **NAT Gateway masking**: If EC2 egress goes through a NAT Gateway, the Elastic IP on the instance is NOT the public IP seen by external services—whitelist the NAT Gateway IP instead
- **Multiple IPs to whitelist**: Each EC2 instance (or NAT Gateway) IP must be whitelisted separately in the SaaS application
- **Guide is non-exhaustive**: Explicitly not a complete production security guide; follow AWS security best practices separately
- Software/image versions in examples may be outdated; check official docs for current versions

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs/whitelisting-traffic)
- [Deploying Connectors on Linux](https://www.twingate.com/docs/connectors-linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Creating Resources and Groups](https://www.twingate.com/docs/resources)