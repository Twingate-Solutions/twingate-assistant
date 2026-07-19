# Replace AWS VPN with Twingate

## Page Title
How to Replace the AWS VPN

## Summary
Twingate provides a Zero Trust alternative to AWS Client VPN for securing access to AWS resources. A Connector deployed on an EC2 instance enables private IP access to any resource in the same VPC without requiring public IP addresses. Setup takes approximately 4 minutes using a single shell command.

## Key Information
- Connector grants access to all resources in the same VPC subnet via private IP only
- No public IP addresses required on protected resources
- Supports hybrid/multi-cloud: AWS, GCP, Azure, on-prem
- Free Starter plan available for personal/home use
- Client apps: Windows, Mac, Linux, iOS, Android

## Prerequisites
- An EC2 instance running a major Linux distribution (for Connector deployment)
- Twingate account (Starter plan is free)
- Target resources deployed in AWS (Jenkins, Grafana, MongoDB, etc.)

## Step-by-Step

1. **Create Remote Network** — In Twingate web UI → Network page → Add Remote Network → name it (e.g., "AWS")

2. **Deploy Connector**
   - Select the auto-generated Connector → choose Linux deployment
   - Generate tokens (re-authentication required)
   - Copy the auto-generated shell command
   - SSH into EC2 instance → paste and run the shell command
   - Confirm Connector status turns green in UI

3. **Add Resource**
   - In Remote Network → click "Add Resource"
   - Select CIDR Address, enter private IP of target VM, assign a label
   - Resource is now accessible via Twingate

4. **Install Client**
   - Download client for your OS
   - Enter Network URL: `[your-network].twingate.com`
   - Authenticate with Twingate account
   - Access resource via private IP through the client

5. **Share Access (optional)** — Team tab → Invite User → send email invitation

## Configuration Values
- **Network URL format**: `[network-name].twingate.com`
- **Connector install**: Auto-generated shell command from UI (contains embedded tokens)
- **Resource address type**: CIDR Address (private IP of target VM)

## Gotchas
- Connector and target resources must be in the **same VPC subnet** for Connector to reach them
- Tokens are generated per-Connector; re-authentication is required during token generation step
- Disconnecting Twingate client should render resources completely inaccessible (verify this post-setup)
- AWS Client VPN has hidden costs not present with Twingate Starter

## Related Docs
- GCP Connector deployment
- Azure Connector deployment
- Synology NAS Connector deployment
- Raspberry Pi Connector deployment
- Twingate API (for programmatic/multi-network configuration)