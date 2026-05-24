# How to Replace the AWS VPN with Twingate

## Summary
Twingate replaces AWS Client VPN by deploying a lightweight Connector on an EC2 instance, enabling secure access to AWS resources via private IP addresses without public IPs. Setup takes ~4 minutes using a single generated shell command. Supports hybrid/multi-cloud architectures across AWS, GCP, Azure, and on-prem.

## Key Information
- No public IP addresses required on resources — Twingate connects via private IPs
- Single Connector covers all resources within the same VPC subnet
- Supports Linux, Windows, macOS, iOS, Android clients
- Free Starter plan available for personal/home use
- Multi-network supported: deploy separate Connectors per network (AWS, GCP, on-prem)
- Users can be invited via email from the Team tab in web UI

## Prerequisites
- Running EC2 instance (any major Linux distribution) for Connector deployment
- Twingate account (free Starter plan available)
- Target AWS resources deployed (public IPs not required)

## Step-by-Step

1. **Create Remote Network** — In Twingate web UI, Network page → Add Remote Network → name it (e.g., "AWS")

2. **Add Connector**
   - Select the auto-generated Connector → choose Linux deployment
   - Generate tokens (re-authentication required)
   - Copy the auto-generated shell command

3. **Deploy Connector on EC2**
   - SSH into EC2 instance
   - Paste and run the generated shell command
   - Confirm Connector status turns green in UI

4. **Add Resource**
   - In Remote Network → Add Resource
   - Enter CIDR address or private IP of target resource
   - Assign a label name → Save

5. **Install Twingate Client**
   - Download client for your OS
   - Enter network URL: `[your-network].twingate.com`
   - Authenticate with Twingate account
   - Access resources via private IP

6. **Share Access (optional)** — Team tab → Invite User → send email invitation

## Configuration Values
| Parameter | Value/Notes |
|-----------|-------------|
| Network URL | `[account-name].twingate.com` |
| Connector deployment | Auto-generated shell command from UI |
| Resource address type | Private IP or CIDR block |
| Connector tokens | Two tokens generated via UI (re-auth required) |

## Gotchas
- Connector must be in the **same VPC subnet** as target resources to reach them via private IP
- Tokens are only shown once after re-authentication — copy immediately
- Disconnecting Twingate client should render resources completely inaccessible (good for verification)
- Each separate network (GCP, on-prem) requires its own Connector deployment

## Related Docs
- [GCP Connector deployment](https://www.twingate.com/docs)
- [Azure Connector deployment](https://www.twingate.com/docs)
- Synology NAS and Raspberry Pi deployment guides
- Twingate API (for programmatic configuration of multi-cloud setups)