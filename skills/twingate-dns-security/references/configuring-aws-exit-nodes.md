# Configuring AWS Exit Nodes for SaaS App Gating

## Summary
Deploy Twingate Connectors on AWS EC2 instances to route user traffic through known public IPs, enabling IP-based allowlisting for public SaaS applications. Users access IP-restricted resources through Twingate regardless of their physical network location.

## Key Information
- Uses AWS EC2 instances as "exit nodes" — traffic egresses from known public IPs
- Enables IP allowlisting with third-party SaaS apps (e.g., Salesforce) combined with Twingate user-based access control
- Requires at least one EC2 instance; multiple recommended for redundancy
- Only outbound internet traffic required from EC2 instances; inbound can be blocked

## Prerequisites
- AWS account with ability to deploy EC2 instances and assign Elastic IPs
- Twingate admin console access
- Linux EC2 instance with Docker support (Ubuntu 22.04 recommended)
- Understanding of your AWS network egress path (NAT gateway vs. IGW affects public IP)

## Step-by-Step

### 1. Deploy EC2 Exit Node(s)
- Launch Linux EC2 instance (Ubuntu 22.04 recommended)
- Instance type: `t3a.micro` minimum; any general purpose acceptable
- Allow outbound internet traffic; block all inbound internet traffic
- Assign an **Elastic IP** to each instance

### 2. Verify Public IP
- Confirm which public IP egress traffic uses — NAT gateway may mask the instance's Elastic IP
- This public IP is what gets allowlisted in the SaaS application

### 3. Install Twingate Connector
- Follow [deploying Connectors on Linux](https://www.twingate.com/docs/connector) documentation
- Install on each EC2 exit node instance

### 4. Create Twingate Resource
- In Twingate admin console, create a Resource using the SaaS app's FQDN (e.g., `acme.salesforce.com`)

### 5. Authorize Users
- Create a Group in Twingate
- Add the Resource to the Group
- Assign users to the Group — these users will route through the exit node when accessing the resource

### 6. Configure SaaS Application
- Add the EC2 instance(s) public IP(s) to the SaaS app's IP allowlist

## Configuration Values
| Parameter | Value |
|-----------|-------|
| EC2 instance type | `t3a.micro` (minimum) |
| Recommended OS | Ubuntu 22.04 |
| Inbound traffic | Not required (block all) |
| Outbound traffic | Must be allowed |
| IP assignment | Elastic IP per instance |

## Gotchas
- **NAT Gateway masking**: If traffic egresses via NAT gateway rather than IGW, the Elastic IP on the instance may not be the public IP seen by external services — verify actual egress IP before allowlisting
- **No inbound required**: Do not open inbound ports unless needed for SSH setup; close after configuration
- **Multiple instances for redundancy**: Single instance is a SPOF; deploy at least two
- Twingate routes based on FQDN/IP in the request — Resource name must exactly match the domain being protected

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs/whitelisting-traffic)
- [Deploying Connectors on Linux](https://www.twingate.com/docs/connector)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Creating Resources and Groups](https://www.twingate.com/docs/resources)