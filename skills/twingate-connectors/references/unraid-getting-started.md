# Getting Started with Unraid and Twingate

## Summary
Deploys a Twingate Connector on Unraid via the Community Applications plugin to enable secure remote access to private resources. Requires generating connector tokens in the Twingate Admin Console and configuring the Unraid app with those credentials.

## Key Information
- Installation method: Unraid Community Apps store (official Twingate Connector entry)
- Each Connector requires its own unique Access/Refresh token pair — never reuse tokens
- Verify connectivity by checking Controller and Relay statuses show "connected" in Admin Console

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one → choose **Manual** option
3. Scroll to **Step 2** → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Community Apps
1. Navigate to `http://<your-unraid-ip>/Apps`
2. Search for **Twingate Connector** → select official entry → click **Install**
3. Fill configuration form:
   - **Network**: `<network-name>.twingate.com`
   - **Access Token**: paste from Admin Console
   - **Refresh Token**: paste from Admin Console
4. Click **Apply**

### 3. Verify
1. Admin Console → **Remote Networks** → select network → select Connector
2. Confirm both **Controller** and **Relay** statuses show `connected`

## Configuration Values

| Field | Value Format |
|-------|-------------|
| Network | `<network-name>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Token reuse is prohibited** — each Connector must have its own unique token set
- Token errors are the most common failure cause; double-check copy/paste accuracy
- Connectivity issues: confirm local Unraid web UI is accessible and Community App is running

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs/proxmox)