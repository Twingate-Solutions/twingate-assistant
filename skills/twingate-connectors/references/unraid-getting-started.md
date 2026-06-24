# Getting Started with Twingate on Unraid

## Summary
Installs Twingate Connector on Unraid via the Community Applications plugin to enable secure remote access. Requires generating connector tokens from the Twingate Admin Console and configuring them in the Unraid app form.

## Key Information
- Uses Unraid Community Apps store for installation
- Connector runs as a container managed by Unraid
- Each Connector must have its own unique token pair (never reuse tokens)
- Verify success by checking Controller and Relay statuses show "connected" in Admin Console

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed on Unraid
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one → choose **Manual** option
3. Scroll to **Step 2** → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Community Apps
1. Go to `http://<your-unraid-ip>/Apps`
2. Search for **Twingate Connector** → select official entry → click **Install**
3. Fill configuration form:
   - **Network**: `<network-name>.twingate.com`
   - **Access Token**: paste from Admin Console
   - **Refresh Token**: paste from Admin Console
4. Click **Apply**

### 3. Verify
- Admin Console → Remote Networks → select network → select Connector
- Confirm **Controller** and **Relay** statuses are **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<yournetwork>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Do not reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Token entry errors are the most common issue; double-check copy/paste accuracy
- Ensure Unraid web interface is locally accessible before troubleshooting connectivity issues

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs/proxmox)