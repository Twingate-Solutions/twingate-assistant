# How to Replace the AWS VPN with Twingate

## Summary
Twingate provides a Zero Trust alternative to AWS Client VPN for securing access to AWS resources. A Connector deployed on a single EC2 instance grants access to all resources in the same VPC subnet, including those without public IP addresses. Setup takes approximately 4 minutes using a single auto-generated shell command.

## Key Information
- Connector deployed on one EC2 instance covers all resources in the same VPC subnet
- Resources do **not** need public IP addresses — access via private IPs only
- Supports multi-cloud and hybrid setups (AWS, GCP, Azure, on-prem) from a single solution
- Free Starter plan available for personal/home use
- Client apps: Windows, Mac, Linux, iOS, Android

## Prerequisites
- An EC2 instance (any major Linux distro) to host the Connector
- Twingate account (sign up at twingate.com)
- Target resources deployed in AWS (public IPs not required)

## Step-by-Step

1. **Create a Remote Network** — In Twingate web UI → Network page → Add Remote Network → name it (e.g., "AWS")

2. **Add a Connector**
   - Select the auto-named Connector → deployment method: Linux
   - Generate tokens (re-authentication required)
   - Copy the auto-generated shell command

3. **Deploy Connector on EC2**
   - SSH into EC2 instance
   - Paste and run the auto-generated shell command
   - Verify: Connector status turns green in UI

4. **Add a Resource**
   - Remote Network → Add Resource
   - Enter CIDR Address or private IP of target resource
   - Assign a label name → Save

5. **Install Twingate Client**
   - Download client for your OS
   - Enter Network URL (`[yourname].twingate.com`) → Join Network
   - Authenticate with Twingate account credentials
   - Access resource via private IP through client

6. **Share Access (Optional)**
   - Team tab → Invite User → send email invitation

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Network URL format | `[yourname].twingate.com` |
| Resource address type | CIDR Address or private IP |
| Connector deployment | Auto-generated shell command from UI |

## Gotchas
- Connector must be on the **same VPC subnet** as the resources it proxies
- Tokens are generated once — copy the shell command before leaving the UI
- Re-authentication is required during token generation step
- Resources are inaccessible when Twingate client is disconnected (by design)
- AWS Client VPN has hidden costs; Twingate Starter is free for personal use

## Related Docs
- Twingate on GCP deployment
- Twingate on Azure deployment
- Synology NAS Connector setup
- Raspberry Pi Connector setup
- Twingate API (for programmatic configuration)