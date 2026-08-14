---
source: https://www.twingate.com/docs/zimaos-getting-started
type: docs
fetched: 2026-08-14
source_version: 7aec958636fc032d279aacc679728c8ae231e1b5de49a245a27761695271668d
---

# Getting Started with ZimaOS and Twingate

## Summary
Deploys a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to ZimaOS resources. Connector is configured through ZimaOS app settings using tokens generated from the Twingate Admin Console.

## Prerequisites
- Running ZimaOS instance
- Twingate account with Admin Console access

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → Remote Networks → select target network
2. Add new Connector or select undeployed one
3. Select **ZimaOS** as connector type
4. Click **Generate Tokens** (Step 2 of connector setup)
5. Copy **Access Token** and **Refresh Token**

> Each Connector must have its own unique token set — do not reuse tokens.

### 2. Deploy Connector via ZimaOS App Store
1. Open ZimaOS web UI → App Store
2. Search "Twingate" → install **Twingate Connector** app
3. On dashboard, hover over app tile → click `...` → **Settings**
4. Set Web UI: `https` + `{network_name}.twingate.com/networks/overview`
5. Fill **Environment Variables** with tokens and network name
6. Click **Save** — container starts automatically

### 3. Verify Installation
- Admin Console → Remote Networks → select network → select connector
- Confirm **Controller** and **Relay** statuses show **Connected**

### 4. Add ZimaOS as a Resource
1. Admin Console → Resources → **+ Resource**
2. Select the remote network with the new Connector
3. Name the resource (e.g., "ZimaOS")
4. Enter dashboard's private IP (format: `192.168.x.x`)
5. Assign a group and click **Grant Access**

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `TWINGATE_NETWORK` | Subdomain from `https://{name}.twingate.com` |
| `ACCESS_TOKEN` | Generated from Admin Console Step 2 |
| `REFRESH_TOKEN` | Generated from Admin Console Step 2 |
| Web UI URL | `https://{network_name}.twingate.com/networks/overview` |

## Gotchas
- Install app first, **then** configure — app won't connect successfully until environment variables are set
- Network name = subdomain only (e.g., `example` from `example.twingate.com`)
- Token reuse across connectors will cause errors

## Troubleshooting
- **Token Errors**: Verify exact copy/paste of Access and Refresh tokens
- **Connectivity**: Confirm ZimaOS web UI is locally accessible and container is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- CasaOS Setup Guide
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- Twingate Resources configuration