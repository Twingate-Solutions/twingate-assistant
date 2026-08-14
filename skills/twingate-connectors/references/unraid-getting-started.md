---
source: https://www.twingate.com/docs/unraid-getting-started
type: docs
fetched: 2026-08-14
source_version: 3e6e9e66dbfeb4a2f29504136e38b3e7cc612b4cf2565b57d891f2c69584c8a8
---

# Getting Started with Twingate on Unraid

## Page Title
Getting Started with Unraid and Twingate

## Summary
Installs a Twingate Connector on Unraid via the Community Applications plugin to enable secure remote access. Requires generating connector tokens from the Twingate Admin Console and entering them into the Community App configuration form.

## Key Information
- Uses Unraid's Community Applications plugin to deploy the Twingate Connector as a container
- Each Connector requires its own unique Access Token + Refresh Token pair (never reuse token sets)
- Connector health verified in Admin Console by checking Controller and Relay statuses show "connected"

## Prerequisites
- Running Unraid instance with web UI access
- Community Applications plugin installed
- Twingate account with Admin Console access
- An existing Remote Network in Twingate Admin Console

## Step-by-Step

**1. Generate Connector Tokens**
1. Admin Console → Remote Networks → select target network
2. Add new Connector or select undeployed one → choose **Manual** option
3. Scroll to Step 2 → click **Generate Tokens** → authenticate
4. Copy both **Access Token** and **Refresh Token**

**2. Deploy via Community App**
1. Go to `http://<unraid-ip>/Apps`
2. Search "Twingate Connector" → select official entry → click **Install**
3. Fill configuration form:
   - **Network**: your Remote Network name (e.g., `network.twingate.com`)
   - **Access Token**: paste from Step 1
   - **Refresh Token**: paste from Step 1
4. Click **Apply**

**3. Verify**
1. Admin Console → Remote Networks → select network → select Connector
2. Confirm **Controller** and **Relay** both show **connected**

## Configuration Values

| Field | Value |
|-------|-------|
| Network | `<network-name>.twingate.com` |
| Access Token | Generated from Admin Console |
| Refresh Token | Generated from Admin Console |

## Gotchas
- **Do not reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- Token entry errors are the most common failure cause; double-check copy/paste
- Verify local Unraid web UI accessibility before troubleshooting Twingate connectivity

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs) — configure access to private apps/services
- [Home Assistant Setup Guide](https://www.twingate.com/docs)
- [Proxmox Helper Script Guide](https://www.twingate.com/docs)
- [Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)