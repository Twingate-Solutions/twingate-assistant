<!-- triage: unassigned URL: https://www.twingate.com/docs/casaos-getting-started -->

# Getting Started with CasaOS and Twingate

## Summary
Deploy a Twingate Connector on CasaOS via custom App Store installation to enable secure remote access to your home network. Uses Docker Compose imported through CasaOS's Manual App Install interface. After deployment, add CasaOS dashboard as a Twingate Resource for remote access.

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Generate Connector Tokens**: Admin Console → Remote Networks → Select Network → Add/Select Connector → See More → Manual → Generate Tokens → Copy Access Token and Refresh Token
2. **Open CasaOS App Store** → Click "Custom Install" (top right)
3. **Import Config**: Click "Import" → Paste Docker Compose YAML → Submit → OK
4. **Configure Web UI**: Set dropdown to `https`, enter `{network_name}.twingate.com/networks/overview`
5. **Fill Environment Variables** with token values and network name → Install
6. **Verify**: Admin Console → Remote Networks → Select Connector → confirm Controller and Relay show **Connected**
7. **Add Resource**: Admin Console → Resources → "+ Resource" → Select Remote Network → Enter CasaOS dashboard private IP (e.g., `192.168.x.x`) → Grant Access to group

## Configuration Values

| Environment Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network subdomain (e.g., `example` from `example.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console |
| `TWINGATE_LABEL_DEPLOYED_BY` | `"casaos"` (hardcoded) |
| `TWINGATE_LABEL_HOSTNAME` | Hostname label for the Connector |

**Docker image**: `twingate/connector:1`  
**Memory reservation**: `500M` (adjustable)  
**Supported architectures**: `amd64`, `arm64`, `arm`  
**Network mode**: `default`  
**Privileged**: `false`

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Network name is the subdomain only (e.g., `example`, not `example.twingate.com`)
- CasaOS config import shows a warning popup — dismiss with OK, it's expected
- Dashboard IP for the Resource must match the local access IP (`192.168.x.x` format)

## Troubleshooting
- Token errors: Re-verify tokens are copied completely and correctly
- Connectivity issues: Confirm CasaOS web UI is locally accessible and connector container is running
- Check connector status: Controller and Relay must both show "Connected" in Admin Console

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- ZimaOS Setup Guide