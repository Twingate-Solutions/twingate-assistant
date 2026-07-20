# Getting Started with ZimaOS and Twingate

## Summary
Deploys a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to the ZimaOS environment. The Connector bridges your private ZimaOS network to Twingate's zero-trust access layer.

## Key Information
- Connector is installed via ZimaOS App Store (search "Twingate")
- Each Connector requires its own unique Access/Refresh token pair — never reuse tokens
- After install, Connector must be configured via Settings before it connects
- Verification: Check Controller and Relay statuses show "Connected" in Admin Console
- Web UI shortcut can be configured to point to Twingate Admin Console from ZimaOS dashboard

## Prerequisites
- Running ZimaOS instance
- Twingate account with Admin Console access
- Existing Remote Network in Twingate (or ability to create one)

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose ZimaOS option → Step 2 → Generate Tokens → copy Access Token and Refresh Token
2. **Install app**: ZimaOS web UI → App Store → search "Twingate" → Install Connector app
3. **Configure app**: Dashboard → hover Twingate tile → ellipsis (…) → Settings
4. **Set Web UI** (optional): Select `https`, enter `{network_name}.twingate.com/networks/overview`
5. **Set environment variables**: Enter tokens and network name from step 1 → Save
6. **Verify**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay = Connected
7. **Add Resource**: Admin Console → Resources → + Resource → select remote network → name it → enter ZimaOS dashboard private IP (e.g., `192.168.x.x`) → assign group access

## Configuration Values

| Variable | Description |
|---|---|
| Access Token | Generated in Admin Console per-Connector |
| Refresh Token | Generated in Admin Console per-Connector |
| Network Name | Subdomain of Twingate URL (e.g., `example` from `example.twingate.com`) |

## Gotchas
- **Do not reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- App installs but does **not** connect until environment variables are saved in Settings
- ZimaOS dashboard IP for Resource configuration is the same local IP used for local access (typically `192.168.x.x`)
- Network name is the subdomain only, not the full URL

## Troubleshooting
- Token errors: Re-verify tokens are copied correctly with no extra whitespace
- Connectivity issues: Confirm ZimaOS web UI is locally accessible and Connector container is running
- Reference: [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- [CasaOS Setup Guide](https://www.twingate.com/docs/casaos)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)