# How to Replace the AWS VPN with Twingate

## Summary
Twingate provides Zero Trust network access to AWS resources as an alternative to AWS Client VPN. A single Connector deployed on an EC2 instance grants access to all resources in the same VPC subnet via private IP addresses, without requiring public IPs on target resources.

## Key Information
- Single Connector on one EC2 instance covers all resources in the same VPC subnet
- Resources do not need public IP addresses
- Works across hybrid/multi-cloud (AWS, GCP, Azure, on-prem) with separate Connectors per network
- Free Starter plan available for personal/home use
- Clients available: Windows, macOS, Linux, iOS, Android

## Prerequisites
- An EC2 instance (Linux) to host the Connector
- Twingate account (sign up at twingate.com)
- Target AWS resources running in the same VPC subnet as the Connector

## Step-by-Step

1. **Create a Remote Network** — In Twingate Admin UI > Network, add a Remote Network named for your AWS environment

2. **Add a Connector**
   - Select the auto-generated Connector → Linux deployment method
   - Generate tokens (re-authentication required)
   - Copy the auto-generated shell command

3. **Deploy Connector on EC2**
   - SSH into your EC2 instance
   - Paste and run the generated shell command
   - Confirm Connector status turns green in Admin UI

4. **Add a Resource**
   - In the Remote Network, click "Add Resource"
   - Enter a label and the **private IP address** (or CIDR) of the target resource
   - Save

5. **Install Twingate Client**
   - Download client for your OS
   - Enter your Network URL (`[account].twingate.com`)
   - Authenticate and connect
   - Access resources via private IP in browser

6. **Share Access (Optional)**
   - Team tab → Invite User → send email invitation

## Configuration Values
- **Network URL format**: `[account].twingate.com`
- **Connector tokens**: Two tokens auto-generated in Admin UI (used in the install command)
- **Resource address types**: Single private IP or CIDR block

## Gotchas
- Connector must be in the **same VPC subnet** as target resources to reach them via private IP
- Tokens are only shown once after re-authentication — copy the shell command immediately
- Resources are inaccessible without an active Twingate client connection (verify by disconnecting)
- AWS Client VPN has hidden costs not present with Twingate Starter

## Related Docs
- GCP Connector deployment
- Azure Connector deployment
- Synology NAS / Raspberry Pi Connector
- Twingate API (for programmatic configuration in multi-cloud setups)