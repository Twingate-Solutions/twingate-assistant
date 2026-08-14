---
source: https://www.twingate.com/docs/aws-vpn-replacement
type: docs
fetched: 2026-08-14
source_version: 94a059028bbb848a010115b70c22d996477b70263cfa475c6f855cfddaa67d73
---

# How to Replace the AWS VPN with Twingate

## Summary
Twingate provides a Zero Trust alternative to AWS Client VPN for securing access to AWS resources. A single Connector deployed on an EC2 instance grants access to all resources within the same VPC subnet via private IP addresses only. Supports hybrid/multi-cloud setups across AWS, GCP, Azure, and on-prem.

## Key Information
- No public IP addresses required on resources — Twingate routes via private IPs
- Single Connector covers all resources in the same VPC subnet
- Supports Linux, Windows, macOS, iOS, Android clients
- Free Starter plan available for home/personal use
- Multi-network supported: deploy separate Connectors per network (AWS, GCP, on-prem)

## Prerequisites
- Running EC2 instance (any major Linux distro) for Connector deployment
- Twingate account (sign up at twingate.com)
- Target resources deployed in AWS (public IPs not required)

## Step-by-Step

### 1. Create a Remote Network
- In Twingate web UI → **Network** page → **Add Remote Network**
- Name it (e.g., "AWS")

### 2. Deploy a Connector
- In the Remote Network, click an auto-generated Connector name
- Select **Linux** as deployment method
- Click **Generate Tokens** (re-authenticate when prompted) → two tokens generated
- Copy the auto-generated shell command
- SSH into EC2 instance, paste and run the command
- Connector status turns green when successful

### 3. Add a Resource
- In Remote Network → **Add Resource**
- Select **CIDR Address**, enter a label and the resource's **private IP address**
- Save — resource is now accessible via Twingate

### 4. Install Twingate Client
- Download client for your OS
- Enter your Network URL: `[yournetwork].twingate.com`
- Click **Join Network** → authenticate
- Access resource via private IP through the client

### 5. Share Access (Optional)
- **Team** tab → **Invite User** → send email invitation
- Invitee installs client and joins the same network

## Configuration Values
| Item | Value/Note |
|------|-----------|
| Network URL format | `[subdomain].twingate.com` |
| Connector install | Auto-generated shell command from UI |
| Resource type | CIDR Address (private IP) |
| Connector tokens | Two tokens generated per Connector |

## Gotchas
- Connector must be in the **same VPC subnet** as resources it proxies
- Tokens are shown once — copy immediately after generation
- Resources with no public IP are unreachable without Twingate connected (verify by disconnecting client)
- Each separate network (GCP, on-prem) requires its own Connector deployment

## Related Docs
- GCP Connector deployment
- Azure Connector deployment
- Synology NAS / Raspberry Pi Connector
- Twingate API (for programmatic multi-network configuration)