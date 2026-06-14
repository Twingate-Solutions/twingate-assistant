# Getting Started with ZimaOS and Twingate

## Summary
Deploys a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to ZimaOS resources. The Connector is configured through the ZimaOS app settings UI using tokens generated from the Twingate Admin Console.

## Prerequisites
- Running ZimaOS instance
- Twingate account with Admin Console access
- Access to ZimaOS App Store

## Step-by-Step

### 1. Generate Connector Tokens
1. Admin Console → **Remote Networks** → select target network
2. Add or select an undeployed Connector → **See More** → **Manual** option
3. Scroll to **Step 2** → click **Generate Tokens** → authenticate
4. Copy **Access Token** and **Refresh Token**

### 2. Deploy Connector via ZimaOS App Store
1. Open ZimaOS web UI → App Store → search "Twingate" → Install
2. On dashboard, hover Twingate tile → click **…** → **Settings**
3. Set **Web UI** dropdown to `https` and enter: `{network_name}.twingate.com/networks/overview`
4. Fill **Environment Variables** with tokens and network name
5. Click **Save** — container starts automatically

### 3. Verify Installation
- Admin Console → Remote Networks → select network → select Connector
- Confirm **Controller** and **Relay** statuses show **Connected**

### 4. Add ZimaOS as a Resource
1. Admin Console → **Resources** → **+ Resource**
2. Select remote network, name the resource (e.g., "ZimaOS")
3. Enter dashboard private IP (format: `192.168.x.x`)
4. Assign to a group via **Grant Access**

## Configuration Values

| Field | Value |
|-------|-------|
| Network name | Subdomain from `https://{network_name}.twingate.com` |
| Access Token | Generated in Admin Console (Step 2 of Connector setup) |
| Refresh Token | Generated alongside Access Token |
| Web UI URL | `{network_name}.twingate.com/networks/overview` |
| Resource IP | Local dashboard IP, typically `192.168.x.x` |

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Connector must be installed before configuring; initial install will not connect until environment variables are saved
- Network name is the subdomain only (e.g., `example` from `example.twingate.com`)

## Troubleshooting
- Token errors: re-verify tokens were copied correctly and are not reused
- Connectivity issues: confirm ZimaOS web UI is accessible locally and the Connector container is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [CasaOS Setup Guide](https://www.twingate.com/docs/casaos)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)