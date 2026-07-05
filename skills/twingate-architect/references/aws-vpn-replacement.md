# How to Replace the AWS VPN with Twingate

## Summary
Twingate provides a Zero Trust alternative to AWS Client VPN for securing access to AWS resources. A Connector deployed on a single EC2 instance grants access to all resources within the same VPC subnet, including those without public IP addresses. Setup takes approximately 4 minutes using a single shell command.

## Key Information
- No public IP addresses required on resources — access via private IPs only
- One Connector per VPC subnet covers all resources in that subnet
- Works across hybrid/multi-cloud (AWS, GCP, Azure, on-prem) from a single control plane
- Supports Windows, Mac, Linux, iOS, Android clients
- Free Starter plan available for personal/home use

## Prerequisites
- An EC2 instance (any major Linux distro) to host the Connector
- Twingate account (sign up at twingate.com)
- AWS resources deployed in a VPC (public IPs not required)

## Step-by-Step

1. **Create a Remote Network**
   - In Twingate dashboard → Network page → Add Remote Network
   - Name it (e.g., "AWS")

2. **Add a Connector**
   - Select the auto-generated Connector within the Remote Network
   - Choose Linux as deployment method
   - Generate tokens (requires re-authentication)
   - Copy the auto-generated shell command

3. **Deploy the Connector on EC2**
   - SSH into your EC2 instance
   - Paste and run the copied shell command
   - Confirm Connector status turns green in dashboard

4. **Add a Resource**
   - In Remote Network → Add Resource
   - Enter a Label and the private IP address (CIDR format supported)
   - Save — resource is now accessible via Twingate

5. **Install Twingate Client**
   - Download client for your OS
   - Enter your network URL: `[yournetwork].twingate.com`
   - Authenticate with your Twingate account
   - Access resources via private IP through the client

6. **Share Access (Optional)**
   - Team tab → Invite User → send email invitation
   - Invitee installs client and joins network

## Configuration Values
- **Network URL format**: `[subdomain].twingate.com`
- **Resource type**: CIDR Address or specific private IP
- **Connector tokens**: Two tokens auto-generated per Connector (used in the deploy command)

## Gotchas
- Connector must be in the same VPC subnet as the resources it proxies
- Disconnecting Twingate client should render resources completely inaccessible (verify this works as a sanity check)
- Tokens are only shown once after re-authentication — copy them before closing
- EC2 instance hosting the Connector must remain running for access to work

## Related Docs
- [GCP Connector deployment](https://www.twingate.com/docs/gcp)
- [Azure Connector deployment](https://www.twingate.com/docs/azure)
- [Synology NAS Connector](https://www.twingate.com/docs/synology-nas)
- [Raspberry Pi Connector](https://www.twingate.com/docs/raspberry-pi)
- [Twingate API (programmatic config)](https://www.twingate.com/docs/api)