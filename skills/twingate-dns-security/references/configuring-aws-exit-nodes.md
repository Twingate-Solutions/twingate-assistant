# Configuring AWS Exit Nodes for SaaS App Gating

## Summary
Deploy Twingate Connectors on AWS EC2 instances to control access to public SaaS applications using IP whitelisting. Traffic from authorized users is routed through EC2 instances whose public IPs are whitelisted with third-party applications.

## Key Information
- Pattern: EC2 instances act as exit nodes; their public IPs get whitelisted in SaaS apps
- Minimum viable setup: 1 EC2 instance; recommended: multiple for redundancy
- Instance type: `t3a.micro` sufficient; any general purpose instance acceptable
- OS: Ubuntu 22.04 recommended; any Linux supporting Docker works
- Twingate Resource name must match the exact FQDN/IP of the protected application

## Prerequisites
- AWS account with ability to deploy EC2 instances
- Twingate admin console access
- Outbound internet traffic allowed from EC2 instances
- Elastic IP assigned to each EC2 instance
- Verify actual egress IP — NAT gateway or IGW config may mask instance IP

## Step-by-Step

1. **Deploy EC2 instances**
   - Launch Linux EC2 instances (Ubuntu 22.04, `t3a.micro` or larger)
   - Allow outbound internet traffic
   - Block all inbound internet traffic (SSH access optional for setup only)

2. **Verify public IP**
   - Assign Elastic IPs to each instance
   - Confirm actual egress IP (NAT gateway may substitute a different IP than the instance's Elastic IP)
   - This IP is what gets whitelisted in SaaS apps

3. **Install Twingate Connector**
   - Follow [deploying Connectors on Linux](https://www.twingate.com/docs/linux) documentation

4. **Create Twingate Resource**
   - In admin console, create a Resource named with the exact FQDN of the SaaS app (e.g., `acme.salesforce.com`)

5. **Authorize users**
   - Create a Group
   - Add the Resource to the Group
   - Add users to the Group

6. **Whitelist EC2 public IPs in SaaS application**
   - Configure the third-party SaaS app to allow traffic from the EC2 instance public IPs

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Instance type | `t3a.micro` (minimum) |
| Recommended OS | Ubuntu 22.04 |
| Inbound traffic | Block all (except optional SSH) |
| Outbound traffic | Must allow all |

## Gotchas
- **NAT gateway masks IP**: If using NAT gateway for egress, the EC2 Elastic IP is not the actual egress IP — the NAT gateway IP is. Whitelist the correct egress IP.
- **Resource naming is exact**: Twingate matches on exact FQDN/IP in the connection request; resource name must match precisely
- **Multiple instances for redundancy**: Single instance is a point of failure for all whitelisted SaaS access
- **Production hardening**: This guide is a starting point — apply AWS security best practices for production

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs/whitelisting-traffic)
- [Deploying Connectors on Linux](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Creating Resources and Groups](https://www.twingate.com/docs/resources)