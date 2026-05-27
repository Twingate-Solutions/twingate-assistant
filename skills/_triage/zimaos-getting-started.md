<!-- triage: unassigned URL: https://www.twingate.com/docs/zimaos-getting-started -->

# Getting Started with ZimaOS and Twingate

## Summary
Deploys a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to the ZimaOS dashboard and private resources. Setup involves generating connector tokens in the Twingate Admin Console, installing the app, and configuring environment variables.

## Prerequisites
- Running ZimaOS instance
- Twingate account with Admin Console access

## Step-by-Step

1. **Generate Connector Tokens** (Admin Console)
   - Go to Remote Networks → select network → add/select undeployed Connector
   - Choose **Manual** option → scroll to Step 2 → click **Generate Tokens**
   - Copy **Access Token** and **Refresh Token** (unique per connector, do not reuse)

2. **Install Connector via ZimaOS App Store**
   - App Store → search "Twingate" → click Connector app → Install

3. **Configure Connector**
   - Dashboard → hover over Twingate tile → ellipsis (…) → Settings
   - Set Web UI: `https` + `{network_name}.twingate.com/networks/overview`
   - Fill Environment Variables with tokens and network name
   - Click Save (starts container)

4. **Verify Installation**
   - Admin Console → Remote Networks → select network → select Connector
   - Confirm **Controller** and **Relay** statuses show **Connected**

5. **Add ZimaOS Dashboard as a Resource**
   - Admin Console → Resources → + Resource
   - Select remote network, assign name (e.g., "ZimaOS")
   - Enter dashboard private IP (typically `192.168.x.x`)
   - Grant access to a group

## Configuration Values

| Field | Value |
|-------|-------|
| Access Token | Generated in Admin Console Step 2 |
| Refresh Token | Generated in Admin Console Step 2 |
| Network Name | Subdomain of `{network_name}.twingate.com` |
| Web UI URL | `https://{network_name}.twingate.com/networks/overview` |

## Gotchas
- **Do not reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Install alone is insufficient; container won't connect until environment variables are saved via Settings
- Network name = subdomain only (e.g., `example` from `https://example.twingate.com`)
- Resource IP must match the local dashboard address used for local access

## Troubleshooting
- Token errors: re-verify tokens are entered exactly as copied
- Connectivity issues: confirm ZimaOS web UI is accessible locally and Connector container is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [CasaOS Setup Guide](https://www.twingate.com/docs/casaos)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)