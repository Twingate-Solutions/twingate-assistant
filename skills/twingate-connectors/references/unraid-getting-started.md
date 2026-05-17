# Getting Started with Twingate on Unraid

## Summary
Deploys a Twingate Connector on Unraid using the Community Applications plugin to enable secure remote access. Requires generating tokens from the Twingate Admin Console and configuring them in the Unraid app form.

## Key Information
- Uses the official Twingate Connector app from the Unraid Community Apps store
- Connector authenticates via Access Token + Refresh Token pair
- Each Connector must have its own unique token set (no reuse)
- Verify success by checking Controller and Relay statuses show "connected" in Admin Console

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed on Unraid
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one
3. Select **Manual** deployment option
4. Scroll to **Step 2** → click **Generate Tokens**
5. Authenticate when prompted
6. Copy both **Access Token** and **Refresh Token**

### 2. Install via Community Apps
1. Go to `http://<your-unraid-ip>/Apps`
2. Search for **Twingate Connector** → select official entry → click **Install**
3. Fill in configuration form:
   - **Network**: Your Twingate Remote Network name (e.g., `network.twingate.com`)
   - **Access Token**: Paste from Admin Console
   - **Refresh Token**: Paste from Admin Console
4. Click **Apply**

### 3. Verify
1. Admin Console → **Remote Networks** → select network → select Connector
2. Confirm **Controller** and **Relay** statuses both show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network-name>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Token entry errors are the most common failure cause; double-check copy/paste
- Connectivity issues: confirm Unraid web UI is accessible locally before troubleshooting Twingate

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs/proxmox)