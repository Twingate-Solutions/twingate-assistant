# Getting Started with Unraid and Twingate

## Summary
Install the Twingate Connector on Unraid via the Community Applications plugin to enable secure remote access. Requires generating connector tokens in the Twingate Admin Console and entering them into the Unraid app configuration form.

## Key Information
- Uses Unraid Community Applications plugin for installation
- Each Connector requires its own unique Access/Refresh token pair (never reuse tokens)
- Connector status verified in Admin Console (Controller + Relay both show "connected")

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed on Unraid
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one
3. Choose **Manual** option
4. Scroll to **Step 2** → click **Generate Tokens** → authenticate
5. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Community Apps
1. Go to `http://<your-unraid-ip>/Apps`
2. Search for **Twingate Connector** (select official entry)
3. Click **Install**
4. Fill in the configuration form:
   - **Network**: `<network>.twingate.com`
   - **Access Token**: paste token from Step 1
   - **Refresh Token**: paste token from Step 1
5. Click **Apply**

### 3. Verify
1. Admin Console → Remote Networks → select network → select Connector
2. Confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<your-network-name>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Do not reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- Search specifically for the official Twingate Connector entry in Community Apps

## Troubleshooting
- Token errors: verify tokens are copied correctly with no extra whitespace
- Connectivity issues: confirm local Unraid web UI is accessible and the Community App is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs/proxmox)