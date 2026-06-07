# Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector on Proxmox VE using the community helper script, which creates an LXC container running the Connector. Enables secure remote access to private resources hosted on Proxmox VE infrastructure.

## Key Information
- Uses the open-source [Proxmox VE Helper Scripts](https://github.com/community-scripts/ProxmoxVE) community repository
- Connector runs as an LXC container on the Proxmox head node
- Each Connector requires its own unique Access/Refresh token pair (never reuse tokens)

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Existing Remote Network in Twingate Admin Console

## Step-by-Step

1. **Generate Connector Tokens** in Admin Console:
   - Navigate to **Remote Networks** → select target network
   - Add new Connector or select undeployed Connector
   - Choose **Manual** deployment option
   - Click **Generate Tokens** (Step 2) → authenticate → copy both tokens

2. **Deploy Connector** — run on Proxmox head node:
   ```bash
   bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
   ```

3. **Enter when prompted:**
   - **Network**: Your Twingate network name (e.g., `yournetwork.twingate.com`)
   - **Access Token**: From Admin Console
   - **Refresh Token**: From Admin Console

4. **Verify** in Admin Console: Remote Networks → select network → select Connector → confirm **Controller** and **Relay** statuses show `connected`

## Configuration Values

| Field | Format/Example |
|-------|---------------|
| Network | `<name>.twingate.com` |
| Access Token | Generated per-Connector in Admin Console |
| Refresh Token | Generated per-Connector in Admin Console |

## Gotchas
- **Do not reuse token sets** — each Connector must have unique Access/Refresh tokens
- Token entry errors are the most common failure cause — paste carefully
- Verify the LXC container is running if connectivity fails
- Script must be run on the **head node** of the Proxmox cluster

## Troubleshooting
- Token errors: Re-generate and re-enter tokens
- Connectivity issues: Confirm Proxmox web UI is accessible locally and LXC is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Twingate Troubleshooting](https://www.twingate.com/docs/troubleshooting)