# Getting Started with Proxmox VE and Twingate

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector inside a Proxmox VE LXC container using the community helper script. Enables secure remote access to private resources hosted on Proxmox VE without exposing them publicly.

## Key Information
- Connector runs as an LXC container on the Proxmox VE head node
- Uses the open-source [Proxmox VE Community Helper Scripts](https://github.com/community-scripts/ProxmoxVE)
- Each Connector requires its own unique Access/Refresh token pair (never reuse tokens)
- Verify success by checking Controller and Relay statuses show **connected** in Admin Console

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- An existing Remote Network in Twingate Admin Console

## Step-by-Step

1. **Generate Connector Tokens**
   - Admin Console → Remote Networks → select network → add/select Connector
   - Choose **Manual** deployment option
   - Click **Generate Tokens** (Step 2 of connector setup)
   - Copy Access Token and Refresh Token

2. **Deploy via Helper Script** (run on Proxmox VE head node):
   ```bash
   bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
   ```
   When prompted, enter:
   - **Network**: your Twingate network hostname (e.g., `network.twingate.com`)
   - **Access Token**: from step 1
   - **Refresh Token**: from step 1

3. **Verify Installation**
   - Admin Console → Remote Networks → select network → select Connector
   - Confirm **Controller** and **Relay** both show `connected`

## Configuration Values

| Prompt | Value |
|--------|-------|
| Network | `<tenant>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Never reuse token sets** — each Connector must have its own unique Access + Refresh token pair
- Token entry errors are the most common failure; double-check copy/paste accuracy
- Verify the Twingate Connector LXC container is running if connectivity issues occur

## Troubleshooting
- Token errors → re-generate and re-enter tokens
- Connectivity issues → confirm Proxmox VE web interface is locally accessible and LXC container is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting) for persistent issues

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources) — configure access to private services post-install
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)