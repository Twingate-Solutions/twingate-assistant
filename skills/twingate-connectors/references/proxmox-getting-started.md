# Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector as an LXC container on Proxmox VE using a community helper script. Enables secure remote access to the Proxmox environment through Twingate's zero-trust network. Setup requires generating connector tokens in the Admin Console before running the deployment script.

## Key Information
- Connector runs as an LXC container via the Proxmox VE Community Helper Scripts
- Script is community-maintained (not official Twingate), hosted at `community-scripts/ProxmoxVE`
- Each Connector requires its own unique Access/Refresh token pair — do not reuse tokens
- Verify success by checking `Controller` and `Relay` statuses show `connected` in Admin Console

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Remote Network already created in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one → choose **Manual** option
3. Scroll to **Step 2** → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy Connector
Run on Proxmox VE head node:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
```

When prompted, enter:
- **Network**: Your Twingate network name (e.g., `yournetwork.twingate.com`)
- **Access Token**: From step 1
- **Refresh Token**: From step 1

### 3. Verify
Admin Console → Remote Networks → select network → select Connector → confirm `Controller` and `Relay` both show **connected**

## Configuration Values

| Prompt | Value |
|--------|-------|
| Network | `<networkname>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Never reuse token sets** — each Connector deployment needs unique tokens
- Tokens must be copied accurately; token errors are the most common failure
- Script runs on the **head node** specifically
- Verify the LXC container is running if connectivity issues occur after deployment

## Troubleshooting
- Token errors → re-generate fresh tokens, ensure no extra whitespace when pasting
- Connectivity issues → confirm Proxmox web UI is accessible locally and the Twingate LXC container is running
- Further help: [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Community Scripts GitHub](https://github.com/community-scripts/ProxmoxVE)