# Getting Started with Unraid and Twingate

## Summary
Deploys a Twingate Connector on an Unraid server via the Community Applications plugin to enable secure remote access. Requires generating connector tokens in the Twingate Admin Console and configuring them in the Unraid app form.

## Key Information
- Uses the official Twingate Connector app from Unraid Community Apps store
- Connector runs as a container managed through Unraid's web UI
- Each connector requires its own unique Access/Refresh token pair (never reuse tokens)
- Verify deployment by checking Controller and Relay statuses show "connected" in Admin Console

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed
- Twingate account with Admin Console access
- An existing Remote Network in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one → choose **Manual** option
3. Scroll to Step 2 → click **Generate Tokens** → authenticate
4. Copy both **Access Token** and **Refresh Token**

### 2. Deploy via Community Apps
1. Go to `http://<your-unraid-ip>/Apps`
2. Search for **Twingate Connector** → select official entry → click **Install**
3. Fill configuration form:
   - **Network**: `<network-name>.twingate.com`
   - **Access Token**: paste from Admin Console
   - **Refresh Token**: paste from Admin Console
4. Click **Apply**

### 3. Verify
- Admin Console → Remote Networks → select network → select connector
- Confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values

| Field | Value Format |
|-------|-------------|
| Network | `<network>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Never reuse token sets** — each connector must have its own unique tokens
- Token entry errors are the most common failure cause; double-check copy/paste
- Ensure Community Applications plugin is installed before searching for the app
- Select the official Twingate Connector entry in the store (not community forks)

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs) — configure access to private services post-install
- [Home Assistant Setup Guide](https://www.twingate.com/docs)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs)
- [Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)