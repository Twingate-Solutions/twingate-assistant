# Getting Started with Unraid and Twingate

## Summary
Installs Twingate Connector on Unraid via the Community Applications plugin to enable secure remote access. Requires generating connector tokens from the Twingate Admin Console and entering them into the Unraid app configuration form.

## Key Information
- Uses Unraid Community Apps store (official Twingate Connector entry)
- Connector authenticates via Access Token + Refresh Token pair
- Each Connector must have its own unique token set — never reuse tokens
- Verify setup by checking Controller and Relay statuses show "connected" in Admin Console

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed on Unraid
- Twingate account with Admin Console access
- Existing Remote Network in Twingate

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one → choose **Manual** option
3. Scroll to Step 2 → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Community Apps
1. Go to `http://<your-unraid-ip>/Apps`
2. Search for **Twingate Connector** → select official entry → click **Install**
3. Fill configuration form:
   - **Network**: `<network>.twingate.com`
   - **Access Token**: paste from Admin Console
   - **Refresh Token**: paste from Admin Console
4. Click **Apply**

### 3. Verify
1. Admin Console → Remote Networks → select network → select Connector
2. Confirm **Controller** and **Relay** statuses are **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<your-network-name>.twingate.com` |
| Access Token | Generated from Admin Console (unique per connector) |
| Refresh Token | Generated from Admin Console (unique per connector) |

## Gotchas
- **Do not reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Token errors are the most common failure; double-check copy/paste accuracy
- Connectivity issues may indicate the Community App isn't running or local web UI is unreachable

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs) — configure access to private apps/services
- [Home Assistant Setup Guide](https://www.twingate.com/docs)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs)
- [Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)