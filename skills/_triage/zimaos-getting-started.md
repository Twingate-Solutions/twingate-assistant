<!-- triage: unassigned URL: https://www.twingate.com/docs/zimaos-getting-started -->

# Getting Started with ZimaOS and Twingate

## Summary
Installs a Twingate Connector on ZimaOS via the App Store to enable secure remote access to the ZimaOS environment. Configuration requires manually generating tokens from the Twingate Admin Console and entering them as environment variables in the ZimaOS app settings.

## Key Information
- Connector is deployed as a ZimaOS App Store application
- Each Connector requires its own unique Access Token + Refresh Token pair (never reuse)
- Web UI shortcut can be configured to link directly to the Twingate Admin Console
- Connector health verified via Controller and Relay status indicators in Admin Console

## Prerequisites
- Running ZimaOS instance with web UI accessible locally
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select undeployed Connector → See More → Manual → Step 2 → Generate Tokens → copy Access Token and Refresh Token
2. **Install app**: ZimaOS App Store → search "Twingate" → Install Connector app
3. **Configure app**: Dashboard → hover Connector tile → ellipsis (…) → Settings → set Environment Variables with tokens and network name → Save
4. **Set Web UI shortcut** (optional): Select `https`, enter `{network_name}.twingate.com/networks/overview`
5. **Verify**: Admin Console → Remote Networks → select Connector → confirm Controller and Relay show **Connected**
6. **Add Resource**: Admin Console → Resources → + Resource → select remote network → enter ZimaOS dashboard private IP (e.g., `192.168.x.x`) → assign group access

## Configuration Values

| Field | Value/Format |
|---|---|
| `TWINGATE_NETWORK` | Subdomain of Twingate URL (e.g., `example` from `example.twingate.com`) |
| `ACCESS_TOKEN` | Generated in Admin Console Step 2 |
| `REFRESH_TOKEN` | Generated in Admin Console Step 2 |
| Web UI URL format | `https://{network_name}.twingate.com/networks/overview` |

## Gotchas
- Tokens must be unique per Connector — do not reuse token sets across multiple Connectors
- App installs but does **not** connect until environment variables are saved in Settings
- Dashboard private IP for Resource must match the locally-accessible IP (typically `192.168.x.x`)

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)