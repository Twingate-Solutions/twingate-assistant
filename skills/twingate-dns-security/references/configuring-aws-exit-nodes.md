# Configuring AWS Exit Nodes (SaaS App Gating)

## Summary
Deploy Twingate Connectors on AWS EC2 instances to route user traffic through known IP addresses, enabling IP-based whitelisting for public SaaS applications. Users access IP-restricted resources through Twingate, which proxies traffic via EC2 instances with predictable public IPs.

## Key Information
- Use case: Control access to SaaS apps (e.g., Salesforce) that support IP allowlisting
- Traffic flows: Client → Twingate → EC2 Connector → SaaS app
- Recommended EC2 type: `t3a.micro` (general purpose instances acceptable)
- Recommended OS: Ubuntu 22.04 (any Docker-compatible Linux works)
- Deploy **multiple EC2 instances** for redundancy

## Prerequisites
- AWS account with EC2 provisioning access
- Twingate admin console access
- Docker support on target Linux instances
- Outbound internet access from EC2 instances

## Step-by-Step

1. **Deploy EC2 instances**
   - Launch ≥1 Linux EC2 instance (Ubuntu 22.04 recommended)
   - Instance type: `t3a.micro` minimum

2. **Configure networking**
   - Allow all outbound internet traffic
   - Block all inbound internet traffic (SSH only if needed for setup)
   - Assign **Elastic IPs** to each instance

3. **Verify public IP behavior**
   - Confirm whether egress routes via IGW or NAT Gateway
   - NAT Gateway masks the instance's Elastic IP — the NAT Gateway's IP is what external services see
   - Whitelist the **actual egress public IP** with the SaaS provider

4. **Install Twingate Connector**
   - Follow [deploying Connectors on Linux](https://www.twingate.com/docs/linux) documentation

5. **Create Twingate Resource**
   - Resource name = FQDN of protected app (e.g., `acme.salesforce.com`)

6. **Authorize users**
   - Create a Group
   - Add the Resource to the Group
   - Assign users to the Group

## Configuration Values
| Parameter | Value |
|-----------|-------|
| EC2 instance type | `t3a.micro` (minimum) |
| OS | Ubuntu 22.04 |
| Inbound ports | None required (block all) |
| Outbound ports | All (unrestricted) |
| IP assignment | Elastic IP per instance |

## Gotchas
- **NAT Gateway masking**: If EC2 egress routes through a NAT Gateway instead of IGW, the Elastic IP on the instance is **not** the IP seen by external services — whitelist the NAT Gateway's IP instead
- **IP verification required**: Always confirm the actual public egress IP before whitelisting with SaaS providers
- This guide is not production-hardened; follow AWS security best practices for production deployments
- Image/version references in docs may be outdated — check official sources

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs/saas-app-gating)
- [Deploying Connectors on Linux](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Creating Resources and Groups](https://www.twingate.com/docs/resources-and-groups)