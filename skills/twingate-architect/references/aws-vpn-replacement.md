# Replace AWS VPN with Twingate

## Summary
Twingate provides Zero Trust network access to AWS resources as an alternative to AWS Client VPN. A single Connector deployed on an EC2 instance grants access to all resources in the same VPC subnet via private IP addresses, without requiring public IPs on target resources.

## Key Information
- Connector deployed on one EC2 instance provides access to entire VPC subnet
- Target resources require **no public IP addresses**
- Supports hybrid/multi-cloud (AWS, GCP, Azure, on-prem) via multiple Connectors
- Free Starter plan available for personal use
- Client apps: Windows, Mac, Linux, iOS, Android

## Prerequisites
- Existing EC2 instance (any major Linux distro) for Connector deployment
- Twingate account (Starter plan is free)
- Target AWS resources running in the same VPC subnet as the Connector

## Step-by-Step

1. **Create Remote Network** — In Twingate web UI → Network → Add Remote Network → name it (e.g., "AWS")

2. **Deploy Connector**
   - Select the auto-generated Connector → Linux → Generate Tokens
   - Copy the auto-generated shell command
   - SSH into EC2 instance → paste and run the command
   - Confirm Connector status turns green in UI

3. **Add Resource**
   - Remote Network → Add Resource
   - Enter private IP address (CIDR supported) and label
   - Resource is now accessible via private IP

4. **Install Client**
   - Download client for your OS
   - Enter network URL (`[yourname].twingate.com`) → Join Network
   - Authenticate with Twingate account
   - Access resource via private IP in browser

5. **Share Access** (optional)
   - Team tab → Invite User → send email invitation

## Configuration Values
| Item | Value |
|------|-------|
| Network URL format | `[networkname].twingate.com` |
| Resource type | IP address or CIDR range |
| Connector install | Auto-generated shell command from UI |
| Connector tokens | Two tokens generated per Connector |

## Gotchas
- Connector must be in the **same VPC subnet** as target resources to reach them via private IP
- Must re-authenticate in Twingate UI when generating Connector tokens
- Disconnecting Twingate client makes resources completely inaccessible (no public IP fallback if configured correctly)
- Each separate network (GCP, on-prem, etc.) requires its own Connector deployment

## Related Docs
- GCP Connector deployment
- Azure Connector deployment
- Synology NAS deployment
- Raspberry Pi deployment
- Twingate API (for programmatic configuration)