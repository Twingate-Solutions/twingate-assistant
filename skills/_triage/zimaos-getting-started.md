<!-- triage: unassigned URL: https://www.twingate.com/docs/zimaos-getting-started -->

# Getting Started with ZimaOS and Twingate

## Summary
Installs a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to the ZimaOS environment. Requires generating connector tokens from the Twingate Admin Console and configuring them as environment variables in the ZimaOS app settings.

## Prerequisites
- Running ZimaOS instance with web UI accessible locally
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Generate Connector Tokens** in Twingate Admin Console → Remote Networks → select network → add/select undeployed Connector → See More → Manual → Step 2 → Generate Tokens → copy Access Token and Refresh Token
2. **Install Connector** via ZimaOS App Store (search "Twingate" → Install)
3. **Configure Connector**: Dashboard → hover app tile → ellipsis (…) → Settings
4. **Set Web UI**: Select `https`, enter `{network_name}.twingate.com/networks/overview`
5. **Set Environment Variables** with tokens and network name → Save
6. **Verify**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay statuses show **Connected**
7. **Add Resource**: Admin Console → Resources → + Resource → select remote network → name it → enter ZimaOS private IP (192.168.x.x) → grant group access

## Configuration Values

| Field | Value |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | Access token from Step 1 |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Step 1 |
| Network name | Subdomain from `https://{network_name}.twingate.com` |
| Web UI URL | `https://{network_name}.twingate.com/networks/overview` |

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Container does not connect successfully until environment variables are saved after installation
- ZimaOS dashboard IP for Resource creation is the same local IP used to access it on-network (typically `192.168.x.x`)

## Troubleshooting
- Token errors: re-verify copied tokens match exactly
- Connectivity issues: confirm ZimaOS web UI is accessible locally and Connector container is running
- See [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting) for persistent issues

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)