# Getting Started with Proxmox VE and Twingate

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector on Proxmox VE using the community-maintained ProxmoxVE Helper Scripts repository. The Connector runs as an LXC container and provides secure remote access to private resources on the Proxmox network.

## Key Information
- Connector is deployed as an LXC container via community helper script
- Uses Twingate Access Token + Refresh Token pair for authentication
- Each Connector requires its own unique token set (no reuse)
- Verify deployment by checking Controller and Relay statuses show "connected" in Admin Console

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Existing Remote Network configured in Twingate Admin Console

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
Script prompts for:
- **Network**: your Twingate network name (e.g., `network.twingate.com`)
- **Access Token**: from Step 1
- **Refresh Token**: from Step 1

### 3. Verify
Admin Console → Remote Networks → select network → select Connector → confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values

| Parameter | Description | Example |
|-----------|-------------|---------|
| Network | Twingate network hostname | `network.twingate.com` |
| Access Token | Generated per-connector token | (from Admin Console) |
| Refresh Token | Generated per-connector token | (from Admin Console) |

## Gotchas
- **Do not reuse token sets** — each Connector must have unique Access/Refresh tokens
- Token entry errors are the most common failure cause; paste carefully
- Verify Proxmox web interface is accessible locally before troubleshooting Twingate connectivity

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Community Scripts Repo](https://github.com/community-scripts/ProxmoxVE)