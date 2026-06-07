# Getting Started with Unraid and Twingate

## Summary
Deploys a Twingate Connector on an Unraid server using the Community Applications plugin to enable secure remote access. Requires generating connector tokens from the Twingate Admin Console and entering them into the Unraid app configuration form.

## Key Information
- Uses the official Twingate Connector app from the Unraid Community Apps store
- Connector runs as a Community App (Docker container) managed by Unraid
- Each Connector requires its own unique Access/Refresh token pair — never reuse tokens
- Verify deployment by checking Controller and Relay statuses show "connected" in Admin Console

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed on Unraid
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one
3. Choose **Manual** deployment option
4. Scroll to Step 2 → click **Generate Tokens**
5. Copy **Access Token** and **Refresh Token**

### 2. Deploy via Community Apps
1. Go to `http://<your-unraid-ip>/Apps`
2. Search for **Twingate Connector** (select official entry)
3. Click **Install**
4. Fill configuration form, then click **Apply**

### 3. Verify
1. Admin Console → Remote Networks → select network → select connector
2. Confirm **Controller** and **Relay** statuses show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| `Network` | Your Twingate tenant URL (e.g., `network.twingate.com`) |
| `Access Token` | Generated from Admin Console Step 2 |
| `Refresh Token` | Generated from Admin Console Step 2 |

## Gotchas
- **Do not reuse token sets** — each Connector must have its own unique token pair
- Token entry errors are the most common failure point; double-check copy/paste accuracy
- Community Apps store may have non-official Twingate entries — select the official one

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs) — configure access to private services after connector is running
- Home Assistant Setup Guide
- Proxmox Helper Script Guide
- Twingate Troubleshooting Docs