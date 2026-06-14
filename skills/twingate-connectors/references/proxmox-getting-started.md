# Getting Started with Proxmox VE and Twingate

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector as an LXC container on Proxmox VE using a community helper script. Enables secure remote access to private Proxmox resources without exposing them publicly.

## Key Information
- Connector runs as an LXC container via the Proxmox VE Community Helper Scripts
- Requires unique Access Token + Refresh Token pair per Connector
- Script handles full Connector installation and startup automatically

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Remote Network already created in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Log in to Twingate Admin Console → **Remote Networks**
2. Select target Remote Network → Add or select an undeployed Connector
3. Choose **Manual** deployment option
4. Scroll to **Step 2** → click **Generate Tokens** → authenticate
5. Copy **Access Token** and **Refresh Token**

### 2. Deploy Connector via Helper Script
Run on the Proxmox VE head node:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
```

When prompted, provide:
| Field | Value |
|-------|-------|
| Network | `<network>.twingate.com` |
| Access Token | Token from Admin Console |
| Refresh Token | Token from Admin Console |

### 3. Verify Installation
1. Admin Console → **Remote Networks** → select the network
2. Select the new Connector
3. Confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values
- **Network**: Your Twingate network subdomain (format: `<name>.twingate.com`)
- **Access Token**: Generated per-connector in Admin Console
- **Refresh Token**: Generated per-connector in Admin Console

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access Token + Refresh Token pair
- Token entry errors are the most common failure; double-check copy/paste accuracy
- Verify Proxmox VE web interface is accessible locally before troubleshooting Connector issues
- Ensure the Twingate Connector LXC container is running if connectivity fails

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Community Scripts GitHub](https://github.com/community-scripts/ProxmoxVE)