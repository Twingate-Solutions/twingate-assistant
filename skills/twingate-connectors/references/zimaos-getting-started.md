# Getting Started with ZimaOS and Twingate

## Summary
Deploys a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to ZimaOS resources. The Connector bridges your ZimaOS private network to Twingate's zero-trust network access platform.

## Prerequisites
- Running ZimaOS instance
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate Admin Console

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add new Connector or select undeployed one → choose **ZimaOS** option
3. Scroll to **Step 2** → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy Connector via ZimaOS App Store
1. Open ZimaOS web UI → navigate to **App Store**
2. Search "Twingate" → click app → click **Install**
3. On dashboard, hover Twingate tile → click **…** → **Settings**
4. Set **Web UI** dropdown to `https`, enter: `{network_name}.twingate.com/networks/overview`
5. Fill **Environment Variables** (see below)
6. Click **Save** — container starts automatically

### 3. Verify Installation
- Admin Console → Remote Networks → select network → select Connector
- Confirm **Controller** and **Relay** statuses show **Connected**

### 4. Expose ZimaOS Dashboard as Resource
1. Admin Console → **Resources** → **+ Resource**
2. Select remote network, name resource (e.g., "ZimaOS")
3. Enter dashboard private IP (format: `192.168.x.x`)
4. Assign group and click **Grant Access**

## Configuration Values

| Environment Variable | Value |
|---|---|
| Access Token | Token from Step 1 |
| Refresh Token | Token from Step 1 |
| Network Name | Subdomain of Twingate URL (e.g., `example` from `example.twingate.com`) |

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Network name is the subdomain only (not the full URL)
- Connector must be configured before first connection attempt — install alone is insufficient
- Access ZimaOS remotely using the same private IP as local access (once Twingate client is connected)

## Troubleshooting
- Token errors: verify exact copy-paste of Access/Refresh tokens into env vars
- Connectivity issues: confirm ZimaOS web UI is locally accessible and Connector container is running
- Reference: [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [CasaOS Setup Guide](https://www.twingate.com/docs/casaos)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Twingate Resources configuration](https://www.twingate.com/docs/resources)