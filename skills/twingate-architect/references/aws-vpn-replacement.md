# How to Replace the AWS VPN with Twingate

## Summary
Twingate provides Zero Trust network access to AWS resources as an alternative to AWS Client VPN. A single Connector deployed on an EC2 instance grants access to all resources in the same VPC subnet via private IP addresses, without requiring public IPs on target resources.

## Key Information
- Single EC2 instance runs the Twingate Connector for the entire VPC subnet
- Target resources do **not** need public IP addresses
- Supports multi-cloud/hybrid: same approach works for GCP, Azure, on-prem
- Client apps available: Windows, macOS, Linux, iOS, Android
- Free Starter plan available for home/personal use

## Prerequisites
- Existing AWS account with EC2 instance (Linux, any major distro) for Connector deployment
- Twingate account (sign up at twingate.com)
- SSH or other access method to the EC2 instance

## Step-by-Step

1. **Create Remote Network** — In Twingate admin UI under "Network," add a Remote Network representing your AWS environment

2. **Generate Connector Tokens** — Click the auto-generated Connector → select Linux → Generate tokens → copy the auto-generated shell command

3. **Deploy Connector on EC2** — SSH into EC2 instance, paste and run the generated shell command; Connector status turns green when successful

4. **Add Resource** — In Remote Network, click "Add Resource" → select CIDR Address → enter private IP of target VM → assign label

5. **Install Twingate Client** — Download client for your OS → enter your network URL (`[yourname].twingate.com`) → authenticate → access resources via private IP

6. **Invite Users (optional)** — "Team" tab → "Invite User" → send email invitation

## Configuration Values
| Item | Value |
|------|-------|
| Network URL format | `[yourname].twingate.com` |
| Connector install method | Auto-generated shell command from UI |
| Resource address type | Private IP or CIDR block |
| Connector deployment | One per VPC/Remote Network |

## Gotchas
- Connector must be in the **same VPC subnet** as the resources it proxies
- Two tokens are generated during Connector setup — embedded in the auto-generated command
- Re-authentication required during token generation step
- Disconnecting Twingate client should make resources completely inaccessible (good for verification)
- AWS Client VPN has hidden costs; Twingate Starter is free for personal use

## Related Docs
- GCP Connector deployment
- Azure Connector deployment
- Synology NAS Connector
- Raspberry Pi Connector
- Twingate API (for programmatic configuration)
- Twingate community subreddit