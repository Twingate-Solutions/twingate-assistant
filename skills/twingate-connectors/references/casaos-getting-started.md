---
source: https://www.twingate.com/docs/casaos-getting-started
type: docs
fetched: 2026-08-14
source_version: 4dc4957994028b2ccf0ce3f43ab5bfaf37a0fd5c3b9772a3ac0dd2feacb7e43e
---

# Getting Started with CasaOS and Twingate

## Summary
Deploys a Twingate Connector on CasaOS via Docker Compose to enable secure remote access to self-hosted resources. Uses CasaOS's custom app install flow to import connector configuration directly from the Twingate Admin Console.

## Key Information
- Connector is deployed as a Docker Compose app via CasaOS App Store custom install
- Each Connector requires its own unique Access/Refresh token pair (never reuse tokens)
- Verification requires both Controller and Relay statuses showing "Connected"
- CasaOS dashboard accessible remotely via its local private IP (typically `192.168.x.x`)

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add or select an undeployed Connector
3. Select **Homelab** → **CasaOS** option
4. Scroll to Step 2 → click **Generate Tokens** → authenticate
5. Copy the full Docker Compose configuration (contains network name, access token, refresh token)

### 2. Deploy via CasaOS Custom Install
1. Open CasaOS web UI → **App Store**
2. Click **Custom Install** (top right)
3. Click **Import** on the Manual App Install page
4. Paste Docker Compose config → **Submit** → dismiss popup → **Install**

### 3. Verify Connector
- Admin Console → **Remote Networks** → select network → select Connector
- Confirm **Controller** and **Relay** both show **Connected**

### 4. Add CasaOS Resource
1. Admin Console → **Resources** → **+ Resource**
2. Select the Remote Network
3. Name the resource (e.g., "CasaOS Dashboard")
4. Enter dashboard's private IP address (`192.168.x.x`)
5. Select a group → **Grant Access**

## Configuration Values
| Item | Source | Notes |
|------|--------|-------|
| Access Token | Generated in Admin Console | Unique per Connector |
| Refresh Token | Generated in Admin Console | Unique per Connector |
| Network Name | Included in Docker Compose output | Auto-populated |
| Resource IP | Local dashboard IP | Same IP used for local access |

## Gotchas
- **Token reuse is forbidden** — each Connector deployment needs freshly generated tokens
- If tokens are entered incorrectly, the Connector won't connect (check Controller/Relay status)
- Connectivity troubleshooting prerequisite: CasaOS web UI must be accessible locally before debugging Twingate issues

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- ZimaOS Setup Guide