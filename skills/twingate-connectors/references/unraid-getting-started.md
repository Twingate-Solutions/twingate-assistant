# Getting Started with Twingate on Unraid

## Page Title
Getting Started with Unraid and Twingate

## Summary
Installs Twingate Connector on Unraid via the Community Applications plugin to enable secure remote access. Requires generating connector tokens from the Twingate Admin Console and entering them into the Unraid app configuration form.

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed
- Twingate account with Admin Console access
- Existing Remote Network in Twingate

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → Remote Networks → select target network
2. Add new Connector (or select undeployed one) → choose **Manual** option
3. Scroll to Step 2 → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Community Apps
1. Go to `http://<your-unraid-ip>/Apps`
2. Search for **Twingate Connector** → select official entry → click **Install**
3. Fill configuration form:
   - **Network**: `<network>.twingate.com`
   - **Access Token**: paste from step 1
   - **Refresh Token**: paste from step 1
4. Click **Apply**

### 3. Verify
- Admin Console → Remote Networks → select network → select connector
- Confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<your-network-name>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access + Refresh token pair
- Token errors are the most common failure; double-check copy/paste accuracy
- Verify local web UI access to Unraid before troubleshooting connectivity issues

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- Home Assistant Setup Guide
- Proxmox Helper Script Guide