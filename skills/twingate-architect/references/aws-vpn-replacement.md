# Replace AWS VPN with Twingate

## Page Title
How to Replace the AWS VPN

## Summary
Twingate provides a Zero Trust alternative to AWS Client VPN, enabling secure access to AWS resources via private IP addresses without public IPs. Setup requires deploying a Connector on an EC2 instance and takes approximately 4 minutes. Supports hybrid/multi-cloud architectures (AWS, GCP, Azure, on-prem) from a single solution.

## Key Information
- Connector deployed on one EC2 instance grants access to all resources on the same VPC subnet
- Resources do **not** need public IP addresses — access via private IPs only
- Single Connector serves entire VPC; additional resources just need to be added as Twingate Resources
- Multi-cloud: deploy separate Connectors per network, managed from one Twingate account
- Client apps: Windows, Mac, Linux, iOS, Android

## Prerequisites
- Existing EC2 instance (any major Linux distro) for Connector deployment
- Twingate account (Starter plan is free)
- AWS resources running in same VPC subnet as Connector instance

## Step-by-Step

1. **Create Remote Network** — In Twingate web UI → Network page → Add Remote Network → name it (e.g., "AWS")

2. **Add Connector**
   - Select the auto-generated Connector → choose Linux deployment
   - Generate tokens (re-authentication required)
   - Copy the auto-generated shell command

3. **Deploy Connector on EC2**
   - SSH into EC2 instance
   - Paste and run the generated shell command
   - Verify Connector status turns green in UI

4. **Add Resource**
   - Remote Network → Add Resource
   - Enter private IP address (CIDR supported) and label
   - Resource is now accessible via Twingate

5. **Install Twingate Client**
   - Download client for your OS
   - Enter network URL (`[yourname].twingate.com`)
   - Authenticate and connect

6. **Share Access (optional)** — Team tab → Invite User → send email invitation

## Configuration Values
| Item | Value |
|------|-------|
| Network URL format | `[subdomain].twingate.com` |
| Connector install | Auto-generated shell command from UI |
| Resource address type | Private IP or CIDR block |
| Deployment method | Linux (for EC2) |

## Gotchas
- Tokens are generated during Connector setup and require re-authentication — save them immediately
- Connector must be on the **same VPC subnet** as target resources to reach them via private IP
- Disconnecting Twingate client renders resources completely inaccessible (no public IP fallback if configured correctly)
- EC2 Connector instance itself needs network connectivity to Twingate control plane (outbound internet access)

## Related Docs
- GCP Connector deployment
- Azure Connector deployment
- Synology NAS deployment
- Raspberry Pi deployment
- Twingate API (programmatic configuration)
- Twingate community subreddit