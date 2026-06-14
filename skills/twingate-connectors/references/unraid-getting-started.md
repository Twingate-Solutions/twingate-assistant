# Twingate on Unraid - Getting Started

## Summary
Installs a Twingate Connector on Unraid via the Community Applications plugin to enable secure remote access to the Unraid environment. Requires generating connector tokens in the Twingate Admin Console before deploying through Unraid's app store.

## Key Information
- Uses the official Twingate Connector from the Unraid Community Apps store
- Connector runs as a plugin managed through Unraid's web UI
- Each Connector must have its own unique token set — never reuse tokens across Connectors

## Prerequisites
- Running Unraid instance with web UI access (`http://<unraid-ip>/Apps`)
- Community Applications plugin installed on Unraid
- Twingate account with Admin Console access
- Existing Remote Network in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed Connector → choose **Manual** option
3. Scroll to Step 2 → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Community Apps
1. Unraid web UI → **Apps** tab
2. Search for **Twingate Connector** → select official entry → click **Install**
3. Fill configuration form:
   - **Network**: `<network-name>.twingate.com`
   - **Access Token**: paste from Admin Console
   - **Refresh Token**: paste from Admin Console
4. Click **Apply**

### 3. Verify
1. Admin Console → **Remote Networks** → select network → select Connector
2. Confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<your-network-name>.twingate.com` |
| Access Token | Generated from Admin Console (unique per Connector) |
| Refresh Token | Generated from Admin Console (unique per Connector) |

## Gotchas
- **Do not reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Token errors are the most common issue; double-check copy/paste accuracy
- Connectivity issues may indicate the Community App isn't running — verify via Unraid web UI

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Setting Up Resources (configure access to private apps/services)
- Home Assistant Setup Guide
- Proxmox Helper Script Guide