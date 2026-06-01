# How to Replace the AWS VPN with Twingate

## Summary
Twingate provides Zero Trust network access to AWS resources as an alternative to AWS Client VPN. A single Connector deployed on an EC2 instance grants access to all resources within the same VPC subnet, including resources with no public IP addresses.

## Key Information
- Connector runs on any major Linux distribution on EC2
- Resources need only private IP addresses — no public IPs required
- One Connector covers all resources in the same VPC subnet
- Supports multi-cloud/hybrid: same approach works for GCP, Azure, on-prem
- Free Starter plan available for personal/home use

## Prerequisites
- Existing AWS account with at least one EC2 instance (for Connector deployment)
- Twingate account (free Starter plan available)
- Target resources deployed in same VPC subnet as Connector instance

## Step-by-Step

1. **Create a Remote Network** — In Twingate web UI → Network page → Add Remote Network → name it (e.g., "AWS")

2. **Deploy a Connector**
   - In the Remote Network, click an auto-generated Connector
   - Select **Linux** as deployment method
   - Click **Generate Tokens** (requires re-authentication)
   - Copy the auto-generated shell command
   - SSH into EC2 instance, paste and run the command
   - Verify Connector status turns **green** in the UI

3. **Add a Resource**
   - In Remote Network → click **Add Resource**
   - Enter a label name
   - Enter the **private IP address** (or CIDR block) of the target resource
   - Save

4. **Install Twingate Client** (on user device)
   - Download client for Windows/Mac/Linux/iOS/Android
   - Enter Network URL: `[your-network].twingate.com`
   - Authenticate with Twingate account
   - Access resources via private IP through client

5. **Share Access** (optional)
   - Team tab → **Invite User** → send email invitation

## Configuration Values
- **Network URL format**: `[network-name].twingate.com`
- **Resource address types**: Single private IP or CIDR block
- **Connector install**: Single shell command auto-generated in UI (contains embedded tokens)

## Gotchas
- Connector and target resources must be in the **same VPC subnet** for private IP routing to work
- Tokens are generated during Connector setup — requires re-authentication to reveal
- Resources are inaccessible without Twingate client connected (verify by disconnecting client)
- EC2 instance hosting Connector should remain running; name it to match Connector for easy association

## Related Docs
- [GCP Connector deployment](https://www.twingate.com/docs)
- [Azure Connector deployment](https://www.twingate.com/docs)
- Synology NAS and Raspberry Pi Connector guides
- Twingate API (for programmatic configuration in multi-cloud setups)