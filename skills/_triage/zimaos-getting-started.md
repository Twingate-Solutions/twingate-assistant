<!-- triage: unassigned URL: https://www.twingate.com/docs/zimaos-getting-started -->

# Getting Started with ZimaOS and Twingate

## Summary
Deploys a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to the ZimaOS dashboard and private resources. Configuration is done through the ZimaOS app settings using environment variables.

## Key Information
- Connector is installed as an app from the ZimaOS App Store
- Tokens must be unique per Connector — never reuse token sets
- Network name = subdomain of your Twingate URL (e.g., `example` from `example.twingate.com`)
- After configuration, ZimaOS dashboard is accessible remotely via its local IP through Twingate

## Prerequisites
- Running ZimaOS instance with local web UI access
- Twingate account with Admin Console access
- An existing Remote Network in Twingate Admin Console

## Step-by-Step

1. **Generate Connector Tokens**: Admin Console → Remote Networks → select network → add/select undeployed Connector → See More → Manual → Step 2 → Generate Tokens → copy Access Token and Refresh Token
2. **Install Connector**: ZimaOS App Store → search "Twingate" → Install
3. **Configure Connector**: Dashboard → hover Twingate tile → `...` → Settings → set environment variables (tokens + network name) → Save
4. **Set Web UI link** (optional): Set to `https` + `{network_name}.twingate.com/networks/overview` for quick Admin Console access
5. **Verify**: Admin Console → Remote Networks → select Connector → confirm `Controller` and `Relay` show **Connected**
6. **Add Resource**: Admin Console → Resources → `+ Resource` → select remote network → name it → add dashboard private IP (e.g., `192.168.x.x`) → grant group access

## Configuration Values

| Field | Value |
|-------|-------|
| Access Token | Generated in Admin Console Step 2 |
| Refresh Token | Generated in Admin Console Step 2 |
| Network Name | Subdomain of `{name}.twingate.com` |
| Web UI URL format | `https://{network_name}.twingate.com/networks/overview` |

## Gotchas
- **Do not reuse tokens** — each Connector requires its own unique Access/Refresh token pair
- Install alone is insufficient — must configure environment variables before the Connector connects
- Resource IP must match the local dashboard IP used for LAN access (typically `192.168.x.x`)
- Token errors and connectivity issues are the most common failure points; verify local ZimaOS access first

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [CasaOS Setup Guide](https://www.twingate.com/docs/casaos)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)