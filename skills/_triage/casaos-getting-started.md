<!-- triage: unassigned URL: https://www.twingate.com/docs/casaos-getting-started -->

# Getting Started with CasaOS and Twingate

## Summary
Deploy a Twingate Connector on CasaOS via the custom App Store installation to enable secure remote access to your home network. The Connector runs as a Docker container and connects your CasaOS instance to a Twingate Remote Network without exposing resources to the internet.

## Key Information
- Uses Docker Compose via CasaOS Custom Install (not the standard App Store)
- Connector image: `twingate/connector:1`
- Supports architectures: `amd64`, `arm64`, `arm`
- Memory reservation: 500MB (adjustable)
- Runs with `network_mode: default`, `privileged: false`

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate Admin Console

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → See More → Manual → Step 2 → Generate Tokens → copy Access Token and Refresh Token
2. **Open CasaOS App Store** → Custom Install (top right) → Import button
3. **Paste Docker Compose** (see Configuration Values below) into the docker-compose section → Submit
4. **Set Web UI**: Select `https`, enter `{network_name}.twingate.com/networks/overview`
5. **Fill Environment Variables** with tokens and network name from step 1
6. Click **Install**
7. **Verify**: Admin Console → Remote Networks → select network → select Connector → confirm Controller and Relay show `Connected`
8. **Add Resource**: Admin Console → Resources → + Resource → select Remote Network → enter CasaOS dashboard private IP (e.g., `192.168.x.x`) → assign group access

## Configuration Values

| Environment Variable | Description | Example |
|---|---|---|
| `TWINGATE_NETWORK` | Network subdomain only | `example` |
| `TWINGATE_ACCESS_TOKEN` | From Admin Console token generation | — |
| `TWINGATE_REFRESH_TOKEN` | From Admin Console token generation | — |
| `TWINGATE_LABEL_DEPLOYED_BY` | Pre-set to `"casaos"` | `casaos` |
| `TWINGATE_LABEL_HOSTNAME` | Hostname label for this Connector | — |

**Network name**: subdomain portion only — if URL is `https://example.twingate.com`, use `example`

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- Network name field takes the subdomain only, not the full URL
- Dismiss the config warning popup after import before proceeding to environment variables
- CasaOS dashboard resource IP must be the local private IP (`192.168.x.x`), same address used for local access

## Troubleshooting
- Token errors: re-verify tokens are copied exactly, not reused
- Connectivity issues: confirm CasaOS web UI is locally accessible and the Connector container is running
- Reference: [Twingate troubleshooting docs](https://www.twingate.com/docs/troubleshooting)

## Related Docs
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- ZimaOS Setup Guide
- Twingate Resources configuration
- Twingate troubleshooting docs