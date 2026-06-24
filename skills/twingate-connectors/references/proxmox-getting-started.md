# Twingate with Proxmox VE - Getting Started

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector inside a Proxmox VE LXC container using a community helper script. The Connector enables secure remote access to private resources hosted on the Proxmox server without exposing them publicly.

## Key Information
- Uses the [Proxmox VE Community Helper Scripts](https://github.com/community-scripts/ProxmoxVE) to automate Connector deployment
- Connector runs as an LXC container on the Proxmox head node
- Connector must be verified via Admin Console after deployment (Controller + Relay both show "connected")

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- A Remote Network already created in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add a new Connector → select **Manual** option
3. Scroll to **Step 2** → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Helper Script
Run on Proxmox head node:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
```
When prompted, enter:
- **Network**: your Twingate network name (e.g., `yournetwork.twingate.com`)
- **Access Token**: from Step 1
- **Refresh Token**: from Step 1

### 3. Verify
Admin Console → Remote Networks → select network → select Connector → confirm **Controller** and **Relay** both show `connected`

## Configuration Values

| Prompt | Value |
|--------|-------|
| Network | `<yournetwork>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Tokens must be copied immediately after generation; they are not retrievable later
- Script must run on the **head node** of Proxmox VE

## Troubleshooting
- **Token errors**: Re-verify tokens were copied correctly without extra whitespace
- **Connectivity issues**: Confirm Proxmox web UI is accessible locally and the Twingate LXC container is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting) for persistent issues

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources) — configure access to private apps/services
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Twingate Troubleshooting](https://www.twingate.com/docs/troubleshooting)