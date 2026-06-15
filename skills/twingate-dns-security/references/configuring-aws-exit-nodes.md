# Configuring AWS Exit Nodes for SaaS App Gating

## Summary
Deploy Twingate Connectors on AWS EC2 instances to route user traffic through known public IPs, enabling IP-based allowlisting for SaaS applications. Users authenticate via Twingate and their traffic exits through the EC2 instances' Elastic IPs, which are whitelisted in the target application.

## Key Information
- Enables user-based access control to public SaaS apps using IP filtering
- EC2 instances act as exit nodes — traffic egresses through their public IPs
- Minimum one EC2 instance required; multiple recommended for redundancy
- No inbound internet traffic required on EC2 instances post-setup

## Prerequisites
- AWS account with ability to deploy EC2 instances and assign Elastic IPs
- Twingate admin access to create Resources and Groups
- Target SaaS app must support IP allowlisting

## Step-by-Step

### 1. Deploy EC2 Exit Nodes
- Launch one or more Linux EC2 instances (Ubuntu 22.04 recommended)
- Minimum instance type: `t3a.micro` (any general purpose works)
- Assign an **Elastic IP** to each instance
- Confirm outbound internet traffic is permitted
- Block all inbound internet traffic (SSH only needed during setup, then block)
- Verify actual public egress IP — NAT gateway may mask instance IP

### 2. Install Twingate Connector
- Follow [deploying Connectors on Linux](https://www.twingate.com/docs/connectors) documentation
- Install on each EC2 instance

### 3. Whitelist EC2 Public IPs in SaaS App
- Whitelist the Elastic IP(s) of EC2 instances in the target application's IP allowlist
- If using NAT gateway, whitelist the NAT gateway's public IP instead

### 4. Create Twingate Resource
- In Twingate admin console, create a Resource using the FQDN of the protected app (e.g., `acme.salesforce.com`)

### 5. Authorize Users
- Create a Group in Twingate
- Add the Resource to the Group
- Assign users to the Group — they can now access the IP-allowlisted app from any network

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Recommended instance type | `t3a.micro` |
| Recommended OS | Ubuntu 22.04 |
| Inbound traffic | Block all (except SSH during setup) |
| Outbound traffic | Must be allowed |
| IP assignment | Elastic IP per instance |

## Gotchas
- **NAT Gateway masking**: If egress routes through a NAT gateway rather than IGW, the EC2 instance's Elastic IP is not the public IP seen by external services — whitelist the NAT gateway IP instead
- **Elastic IP required**: Without an Elastic IP, the public IP may change on instance restart
- **Multiple instances**: Each instance gets a different Elastic IP; all must be whitelisted in the SaaS app
- Resource name in Twingate must exactly match the FQDN users connect to

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs/whitelisting-traffic)
- [Deploying Connectors on Linux](https://www.twingate.com/docs/connectors)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Creating Resources and Groups](https://www.twingate.com/docs/resources)