# Deploy Twingate Connector on Aptible

## Summary
Guide for deploying Twingate Connectors on Aptible's serverless platform using either the Twingate CLI (automated) or Aptible CLI (manual). Supports High Availability via multiple Connector instances on the same Remote Network.

## Key Information
- Two deployment methods: automated (Twingate CLI) or manual (Aptible CLI)
- HA setup requires running the automated command twice against the same Remote Network
- Successful deployment shows two green status indicators in Admin Console
- Peer-to-peer connections recommended for better performance and Fair Use Policy compliance

## Prerequisites
**Automated method:**
- Twingate CLI installed and configured
- API token with Read, Write & Provision permissions
- Aptible CLI installed and configured

**Manual method:**
- Aptible CLI installed and configured
- Remote Network created in Twingate Admin Console
- Connector tokens generated (Manual deployment method)

## Step-by-Step

### Automated (Twingate CLI)
1. Run `./tg deploy aptible app` (add `--environment NAME` for multiple Aptible environments)
2. Enter Twingate account name and API token when prompted
3. Select existing or create new Remote Network
4. Verify deployment via green indicators in Admin Console

### Manual (Aptible CLI)
1. Create Remote Network in Admin Console → select Connector
2. Choose Manual deployment → click **Generate Tokens** → copy both tokens
3. Create Aptible app: `aptible apps:create [APP]`
4. Set app configuration:
```bash
aptible config:set --app [APP] \
  TWINGATE_NETWORK="[ACCOUNT]" \
  TWINGATE_ACCESS_TOKEN="[ACCESS_TOKEN]" \
  TWINGATE_REFRESH_TOKEN="[REFRESH_TOKEN]"
```
5. Deploy: `aptible deploy --app [APP] --docker-image twingate/connector:1`
6. Verify two green indicators in Admin Console

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `TWINGATE_NETWORK` | Twingate account name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |
| `--environment NAME` | Aptible environment (CLI flag, optional) |
| `--docker-image` | `twingate/connector:1` |

## Gotchas
- Token generation requires re-authentication in Admin Console — copy tokens immediately, they won't be shown again
- HA setup: must select the **same** Remote Network for both Connector instances
- Token generation step during manual setup triggers a re-auth request before tokens are displayed

## Related Docs
- Twingate CLI setup
- Connector Best Practices
- Remote Network configuration
- Peer-to-peer connections / Fair Use Policy