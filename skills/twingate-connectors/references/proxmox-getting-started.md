# Getting Started with Proxmox VE and Twingate

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector on Proxmox VE using a community helper script that creates an LXC container. Requires generating unique Access/Refresh token pairs from the Twingate Admin Console before running the script.

## Key Information
- Uses [Proxmox VE Community Helper Scripts](https://github.com/community-scripts/ProxmoxVE) to deploy Connector as an LXC container
- Script runs on the Proxmox **head node**
- Each Connector must have its own unique token set — never reuse tokens

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Existing Remote Network configured in Twingate Admin Console

## Step-by-Step

1. **Generate Tokens** in Admin Console:
   - Navigate to **Remote Networks** → select network → add/select undeployed Connector
   - Choose **Manual** deployment option
   - Click **Generate Tokens** (Step 2), authenticate, copy both tokens

2. **Run helper script** on Proxmox head node:
   ```bash
   bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
   ```

3. **Enter prompted values** when script runs:
   - Network name (e.g., `yournetwork.twingate.com`)
   - Access Token
   - Refresh Token

4. **Verify** in Admin Console: Remote Networks → select network → select Connector → confirm **Controller** and **Relay** show `connected`

## Configuration Values

| Prompt | Value |
|--------|-------|
| Network | `<network-name>.twingate.com` |
| Access Token | Generated from Admin Console Step 2 |
| Refresh Token | Generated from Admin Console Step 2 |

## Gotchas
- **Do not reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Tokens must be copied immediately after generation; they won't be shown again
- Script must run on the head node, not a VM or container

## Troubleshooting
- **Token errors**: Re-verify tokens were copied correctly without extra whitespace
- **Connectivity issues**: Confirm Proxmox web UI is accessible locally and the Twingate LXC container is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting) for persistent issues

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)