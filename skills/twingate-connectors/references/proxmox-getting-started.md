# Twingate with Proxmox VE - Getting Started

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector inside a Proxmox VE LXC container using the community helper script. Enables secure remote access to private Proxmox resources without exposing them publicly.

## Key Information
- Connector runs as an LXC container on Proxmox VE
- Uses the open-source [Proxmox VE Helper Scripts](https://github.com/community-scripts/ProxmoxVE) community repository
- Connector requires unique Access + Refresh token pair per deployment

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Remote Network already created in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one
3. Choose **Manual** deployment option
4. Scroll to Step 2 → click **Generate Tokens**
5. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Helper Script
Run on Proxmox VE head node:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
```

Script prompts for:
- **Network**: your Twingate network name (e.g., `network.twingate.com`)
- **Access Token**: from Admin Console
- **Refresh Token**: from Admin Console

### 3. Verify
Admin Console → Remote Networks → select network → select Connector → confirm **Controller** and **Relay** statuses show `connected`

## Configuration Values

| Prompt | Value Format | Notes |
|--------|-------------|-------|
| Network | `<name>.twingate.com` | Your tenant name only |
| Access Token | string | From Admin Console token generation |
| Refresh Token | string | From Admin Console token generation |

## Gotchas
- **Never reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- Tokens must be captured immediately after generation; they are not retrievable afterward
- Script must run on the **head node** of Proxmox VE
- Troubleshoot by verifying the Twingate Connector LXC container is running

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)