<!-- triage: unassigned URL: https://www.twingate.com/docs/casaos-getting-started -->

# Getting Started with CasaOS and Twingate

## Summary
Deploys a Twingate Connector on CasaOS via custom App Store installation using Docker Compose. Enables secure remote access to CasaOS resources without exposing them to the internet. Connector runs as a container using the `twingate/connector:1` image.

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Generate Connector Tokens**: Admin Console → Remote Networks → select network → add/select undeployed Connector → See More → Manual → Step 2 → Generate Tokens → copy Access Token and Refresh Token
2. **Deploy via CasaOS Custom Install**: App Store → Custom Install → Import → paste docker-compose config → Submit
3. **Configure Web UI link**: Set to `https://{network_name}.twingate.com/networks/overview`
4. **Fill environment variables** with tokens and network name from step 1
5. **Install** and verify Connector shows Controller + Relay status as **Connected** in Admin Console
6. **Add Resource**: Admin Console → Resources → + Resource → select network → enter CasaOS dashboard private IP (e.g., `192.168.x.x`) → assign group access

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Network subdomain only (e.g., `example` from `example.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console |
| `TWINGATE_LABEL_DEPLOYED_BY` | Hardcode `"casaos"` |
| `TWINGATE_LABEL_HOSTNAME` | Hostname label for the Connector |

**Docker image**: `twingate/connector:1`  
**Supported architectures**: `amd64`, `arm64`, `arm`  
**Memory reservation**: 500M (adjustable)  
**Restart policy**: `unless-stopped`  
**Privileged**: `false`

## Gotchas
- **Do not reuse token sets** — each Connector requires its own unique Access/Refresh token pair
- `TWINGATE_NETWORK` takes only the subdomain portion, not the full URL
- `network_mode: default` is set in compose — required for proper connectivity
- Verify Connector shows both **Controller** and **Relay** as Connected before adding Resources

## Troubleshooting
- Token errors: re-check tokens are copied completely and correctly
- Connectivity issues: confirm CasaOS web UI is accessible locally and the container is running

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- Home Assistant Setup Guide
- ZimaOS Setup Guide
- Unraid Helper Script Guide