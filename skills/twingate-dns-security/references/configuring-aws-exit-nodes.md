# Configuring AWS Exit Nodes for SaaS App Gating

## Summary
Use Twingate Connectors deployed on AWS EC2 instances as exit nodes to control access to public SaaS applications via IP whitelisting. Traffic from authorized users routes through the EC2 instances, allowing the EC2's public IP to be whitelisted with third-party applications.

## Key Information
- Enables user-based access control to public SaaS apps using app-native IP filtering
- Requires at least one Linux EC2 instance (recommend multiple for redundancy)
- Recommended instance type: `t3a.micro` (any general purpose works)
- Recommended OS: Ubuntu 22.04 (any Linux with Docker support works)
- The EC2's public IP is what gets whitelisted with third-party apps

## Prerequisites
- AWS account with ability to deploy EC2 instances
- Twingate admin console access
- Docker-compatible Linux on EC2
- Outbound internet traffic allowed from EC2 instances

## Step-by-Step

1. **Deploy EC2 instances**
   - Launch at least one Linux EC2 instance (`t3a.micro` or larger)
   - Deploy multiple instances for redundancy

2. **Configure networking**
   - Allow outbound internet traffic from instances
   - Block all inbound internet traffic (SSH inbound only needed during setup)
   - Assign an Elastic IP to each EC2 instance

3. **Verify public IP**
   - Confirm whether egress traffic leaves via NAT Gateway or IGW
   - If using NAT Gateway, the NAT Gateway's IP is what external services see (not the instance's Elastic IP)
   - Whitelist the correct public IP(s) with the target SaaS application

4. **Install Twingate Connector**
   - Follow [deploying Connectors on Linux](https://www.twingate.com/docs) documentation

5. **Create Twingate Resource**
   - In admin console, create a Resource using the FQDN of the protected application (e.g., `acme.salesforce.com`)

6. **Authorize users**
   - Create a Group, add the Resource to the Group
   - Assign users to the Group

## Configuration Values
- Instance type: `t3a.micro` minimum
- OS: Ubuntu 22.04 recommended
- Inbound ports: None required (block all)
- Outbound: All traffic allowed

## Gotchas
- **NAT Gateway masking**: If EC2 egress goes through a NAT Gateway, the NAT Gateway's public IP is what third-party apps see—not the Elastic IP assigned to the instance. Whitelist the correct IP.
- **Elastic IP required**: Without an Elastic IP, the instance's public IP may change on restart
- **Production warning**: This guide is not a complete security hardening guide; follow AWS security best practices for production deployments
- Software versions in examples may be outdated; check official docs for current versions

## Related Docs
- [Whitelisting Traffic to Public Resources](https://www.twingate.com/docs)
- [Deploying Connectors on Linux](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Creating Resources and Groups](https://www.twingate.com/docs)