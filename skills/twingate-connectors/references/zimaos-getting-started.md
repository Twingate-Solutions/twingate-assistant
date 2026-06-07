# Getting Started with ZimaOS and Twingate

## Summary
Installs a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to the ZimaOS environment. Connector is configured through environment variables in the ZimaOS app settings UI.

## Prerequisites
- Running ZimaOS instance
- Twingate account with Admin Console access

## Step-by-Step

1. **Generate Connector Tokens** (Admin Console)
   - Go to Remote Networks → select network → add/select undeployed Connector
   - Click "See More" → choose "Manual" option
   - Scroll to Step 2 → click "Generate Tokens" → authenticate
   - Copy **Access Token** and **Refresh Token**

2. **Install Connector** (ZimaOS)
   - Open ZimaOS web UI → App Store → search "Twingate" → Install

3. **Configure Connector** (ZimaOS)
   - Hover over Twingate tile → click `…` → Settings
   - Set Web UI: `https` + `{network_name}.twingate.com/networks/overview`
   - Fill Environment Variables with tokens and network name
   - Click Save

4. **Verify** (Admin Console)
   - Remote Networks → select network → select Connector
   - Confirm **Controller** and **Relay** statuses show `Connected`

5. **Create Resource for ZimaOS Dashboard**
   - Admin Console → Resources → `+ Resource`
   - Select remote network, name resource (e.g., "ZimaOS")
   - Enter dashboard private IP (typically `192.168.x.x`)
   - Assign group access → Grant Access

## Configuration Values

| Field | Value |
|-------|-------|
| Access Token | From Connector token generation step |
| Refresh Token | From Connector token generation step |
| Network Name | Subdomain of `{network_name}.twingate.com` |
| Web UI URL | `https://{network_name}.twingate.com/networks/overview` |

## Gotchas
- **Do not reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Must configure environment variables *before* the Connector will connect successfully on first start
- Dashboard IP for resource should match the local access address (same `192.168.x.x` used locally)

## Troubleshooting
- Token errors: verify tokens are entered correctly without extra whitespace
- Connectivity issues: confirm ZimaOS web UI is accessible locally and Connector container is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [CasaOS Setup Guide](https://www.twingate.com/docs/casaos)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)