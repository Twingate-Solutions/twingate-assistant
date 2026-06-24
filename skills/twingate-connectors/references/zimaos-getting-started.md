# Getting Started with ZimaOS and Twingate

## Summary
Installs a Twingate Connector on ZimaOS via the ZimaOS App Store to enable secure remote access to the ZimaOS dashboard and private resources. The Connector is configured through environment variables in the ZimaOS app settings UI.

## Key Information
- Connector is installed as an app from the ZimaOS App Store (search "Twingate")
- Configuration is done post-install via the app's Settings > Environment Variables
- Each Connector requires a unique Access Token and Refresh Token pair
- Web UI shortcut can be configured to point directly to the Twingate Admin Console

## Prerequisites
- Running ZimaOS instance with local web UI access
- Twingate account with Admin Console access
- An existing Remote Network in Twingate (or create one during setup)

## Step-by-Step

1. **Generate Tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose ZimaOS option → Step 2 → Generate Tokens → copy Access Token and Refresh Token
2. **Install App**: ZimaOS App Store → search "Twingate" → Install Connector app
3. **Configure App**: Dashboard → hover Twingate tile → `...` → Settings → set Environment Variables with tokens and network name → Save
4. **Verify**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay statuses show **Connected**
5. **Add Resource**: Admin Console → Resources → `+ Resource` → select remote network → enter name and ZimaOS dashboard private IP (e.g., `192.168.x.x`) → assign group access

## Configuration Values

| Field | Value |
|-------|-------|
| `TWINGATE_NETWORK` | Subdomain of your Twingate URL (e.g., `example` from `example.twingate.com`) |
| `ACCESS_TOKEN` | Generated in Admin Console (Step 1) |
| `REFRESH_TOKEN` | Generated in Admin Console (Step 1) |
| Web UI URL | `https://{network_name}.twingate.com/networks/overview` |

## Gotchas
- **Do not reuse token sets** — each Connector must have its own unique Access/Refresh token pair
- Install does not auto-configure; must manually enter tokens via Settings after install
- Dashboard IP for the Resource must match the local LAN address used to access ZimaOS (typically `192.168.x.x`)

## Related Docs
- [CasaOS Setup Guide](https://www.twingate.com/docs/casaos-getting-started)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/home-assistant)
- [Unraid Helper Script Guide](https://www.twingate.com/docs/unraid)
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)