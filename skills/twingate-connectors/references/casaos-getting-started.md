# Getting Started with CasaOS and Twingate

## Summary
Deploys a Twingate Connector on CasaOS via the custom App Store installation using a docker-compose configuration. Enables secure remote access to CasaOS dashboard and local network resources without exposing them to the internet.

## Prerequisites
- Running CasaOS instance with web UI accessible
- Twingate account with Admin Console access
- Existing Remote Network configured in Twingate

## Step-by-Step

1. **Generate Connector Tokens** (Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens)
2. **Deploy via CasaOS App Store** → Custom Install → Import → paste docker-compose config
3. **Configure environment variables** in the Settings Panel
4. **Set Web UI** to `https://{network_name}.twingate.com/networks/overview`
5. **Verify**: Admin Console → Remote Networks → Connector shows Controller and Relay as **Connected**
6. **Add Resource**: Admin Console → Resources → + Resource → assign private IP → grant group access

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Network subdomain only (e.g., `example` from `example.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console Connector setup |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console Connector setup |
| `TWINGATE_LABEL_DEPLOYED_BY` | Set to `"casaos"` (hardcoded in compose) |
| `TWINGATE_LABEL_HOSTNAME` | Hostname label for the connector |

**Docker image:** `twingate/connector:1`  
**Memory reservation:** 500M (modify as needed)  
**Supported architectures:** amd64, arm64, arm  
**network_mode:** default  
**privileged:** false

## Gotchas
- Each Connector requires its own **unique** Access/Refresh token pair — never reuse token sets
- `TWINGATE_NETWORK` value is the subdomain only, not the full URL
- CasaOS dashboard private IP (typically `192.168.x.x`) must be added as a Twingate Resource separately for remote access
- Token errors are the most common issue — verify exact copy/paste of both tokens

## Troubleshooting
- Token errors: re-verify Access and Refresh token values
- Connectivity: confirm CasaOS web UI is accessible locally and connector container is running

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- Home Assistant Setup Guide
- Unraid Helper Script Guide
- ZimaOS Setup Guide