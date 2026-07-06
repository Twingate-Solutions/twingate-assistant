# Getting Started with Unraid and Twingate

## Page Title
Getting Started with Unraid and Twingate

## Summary
Deploys a Twingate Connector on an Unraid server via the Community Applications plugin to enable secure remote access to private resources. Requires generating connector tokens in the Twingate Admin Console and configuring them in the Unraid app form.

## Key Information
- Uses Unraid's Community Applications plugin to install the Twingate Connector
- Connector authenticates to Twingate using an Access Token + Refresh Token pair
- Successful deployment shows `Controller` and `Relay` statuses as **connected** in Admin Console

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
   - **Access Token**: paste generated token
   - **Refresh Token**: paste generated token
4. Click **Apply**

### 3. Verify
1. Admin Console → Remote Networks → select network → select connector
2. Confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<your-network-name>.twingate.com` |
| Access Token | Generated from Admin Console Step 2 |
| Refresh Token | Generated from Admin Console Step 2 |

## Gotchas
- **Never reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- Tokens are only displayed once at generation time; copy immediately
- Use the **official** Twingate Connector entry in Community Apps store (verify it's not a third-party clone)

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs) — configure access to private apps/services after connector is running
- [Home Assistant Setup Guide](https://www.twingate.com/docs) — integrate Twingate with Home Assistant
- [Proxmox Helper Script Guide](https://www.twingate.com/docs) — Proxmox integration
- [Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)