<!-- triage: unassigned URL: https://www.twingate.com/docs/casaos-getting-started -->

# Getting Started with CasaOS and Twingate

## Summary
Deploy a Twingate Connector on CasaOS via the custom App Store to enable secure remote access to your home network resources. The Connector runs as a Docker container and connects your CasaOS instance to a Twingate Remote Network without exposing services to the internet.

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Generate Connector Tokens**: Admin Console → Remote Networks → select network → add/select Connector → See More → Manual → Generate Tokens → copy Access Token and Refresh Token
2. **Deploy via CasaOS App Store**: App Store → Custom Install → Import → paste docker-compose YAML → Submit
3. **Configure Web UI link**: Set `https://{network_name}.twingate.com/networks/overview` in Web UI dropdown
4. **Fill Environment Variables**: Enter network name and tokens from step 1
5. **Install**: Click Install button
6. **Verify**: Admin Console → Remote Networks → select Connector → confirm Controller and Relay show `Connected`
7. **Add Resource**: Admin Console → Resources → + Resource → select Remote Network → set name → add private IP (e.g., `192.168.x.x`) → grant group access

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Network subdomain only (e.g., `example` from `example.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console |
| `TWINGATE_LABEL_DEPLOYED_BY` | Set to `"casaos"` (hardcoded) |
| `TWINGATE_LABEL_HOSTNAME` | Hostname label for the Connector |

**Docker image**: `twingate/connector:1`  
**Network mode**: `default`  
**Memory reservation**: `500M` (adjustable)  
**Architectures**: amd64, arm64, arm

## Gotchas
- **Never reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- `TWINGATE_NETWORK` value is the subdomain only, not the full URL
- Container runs with `privileged: false` — ensure this is compatible with your network setup
- After clicking Submit on the docker-compose import, dismiss the warning popup before proceeding to fill environment variables

## Troubleshooting
- Token errors: Verify tokens are copied completely and correctly
- Connectivity issues: Confirm CasaOS web UI is locally accessible and Connector container is running
- Check Controller and Relay status in Admin Console; both must show `Connected`

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- ZimaOS Setup Guide