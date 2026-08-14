---
source: https://www.twingate.com/docs/proxmox-getting-started
type: docs
fetched: 2026-08-14
source_version: c4eef331db1fdddca3689663256537e7db290f40f2c1e0bf95112ea3b4fcc28b
---

# Getting Started with Proxmox VE and Twingate

## Page Title
Getting Started with Proxmox VE and Twingate

## Summary
Deploys a Twingate Connector inside a Proxmox VE LXC container using a community helper script. Enables secure remote access to Proxmox-hosted resources without exposing them publicly.

## Prerequisites
- Running Proxmox VE instance
- Twingate account with Admin Console access
- SSH or web UI access to Proxmox VE server
- Existing Remote Network in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one → choose **Manual** option
3. Scroll to **Step 2** → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy Connector via Helper Script
Run on Proxmox VE head node:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
```
When prompted, enter:
- **Network**: your Twingate network hostname (e.g., `yournetwork.twingate.com`)
- **Access Token**: from Step 1
- **Refresh Token**: from Step 1

### 3. Verify Installation
Admin Console → Remote Networks → select network → select Connector → confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values
| Field | Description | Example |
|-------|-------------|---------|
| Network | Twingate network hostname | `network.twingate.com` |
| Access Token | Generated per-connector token | (from Admin Console) |
| Refresh Token | Generated per-connector token | (from Admin Console) |

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Script deploys Connector as an LXC container, not a VM or native service
- Tokens must be entered accurately; mismatches cause token errors

## Troubleshooting
- **Token Errors**: Re-verify tokens were copied correctly without extra whitespace
- **Connectivity Issues**: Confirm Proxmox web UI is accessible locally and the Twingate LXC container is running
- Extended issues: consult [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources) — configure access to private apps/services post-deployment
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Community Scripts Repo](https://github.com/community-scripts/ProxmoxVE)