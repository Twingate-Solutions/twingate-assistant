# Twingate + Proxmox VE Getting Started

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector as an LXC container on Proxmox VE using a community helper script. The Connector enables secure remote access to private resources hosted on the Proxmox server without exposing them publicly.

## Key Information
- Connector is deployed via a community-maintained script (not official Twingate tooling)
- Script creates an LXC container running the Twingate Connector
- Each Connector requires its own unique Access/Refresh token pair — never reuse tokens
- Verify deployment by confirming both **Controller** and **Relay** statuses show `connected` in Admin Console

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Existing Remote Network configured in Twingate Admin Console

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens → copy Access Token and Refresh Token
2. **Run helper script** on Proxmox head node:
   ```bash
   bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
   ```
3. **Enter prompted values** when script asks:
   - Network name (e.g., `yournetwork.twingate.com`)
   - Access Token
   - Refresh Token
4. **Verify**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay show `connected`

## Configuration Values

| Prompt | Value |
|--------|-------|
| Network | `<network-name>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Do not reuse token sets** — each Connector must have unique tokens
- Script is community-maintained (`community-scripts/ProxmoxVE`), not from Twingate's official repo
- Must run script on the **head node** of Proxmox VE
- Token entry errors are a common failure point — paste carefully

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- [Community Scripts GitHub](https://github.com/community-scripts/ProxmoxVE)