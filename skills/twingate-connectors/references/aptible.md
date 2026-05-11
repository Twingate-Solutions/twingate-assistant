# Deploy Twingate Connector on Aptible

## Summary
Aptible is a serverless platform with built-in security/compliance management. Twingate Connectors can be deployed on Aptible via two methods: automated (Twingate CLI) or manual (Aptible CLI). Peer-to-peer connections are recommended to optimize bandwidth usage.

## Key Information
- Two deployment approaches: Twingate CLI (automated) or Aptible CLI (manual)
- High Availability requires running the automated deploy command twice, selecting the same Remote Network
- HA setup provides automatic load balancing and failover
- Successful deployment shows two green status indicators in Admin Console

## Prerequisites
**Automated method:**
- Twingate CLI installed and configured
- Twingate API token with **Read, Write & Provision** permissions
- Aptible CLI installed and configured

**Manual method:**
- Aptible CLI installed and configured
- Access to Twingate Admin Console

## Step-by-Step

### Automated (Twingate CLI)
1. Run `./tg deploy aptible app` (use `--environment NAME` for multiple Aptible environments)
2. Enter Twingate account name and API token when prompted
3. Select existing Remote Network or create new one
4. Verify deployment via green status indicators in Admin Console

### Manual (Aptible CLI)
1. Create Remote Network in Twingate Admin Console → Network page → select a Connector
2. Choose **Manual** deployment method → click **Generate Tokens** → copy both tokens (requires re-authentication)
3. Create Aptible app: `aptible apps:create [APP]`
4. Set app configuration (see below)
5. Deploy: `aptible deploy --app [APP] --docker-image twingate/connector:1`
6. Verify two green lights in Connector detail page

## Configuration Values

```bash
# Set environment variables on Aptible app
aptible config:set --app [APP] \
  TWINGATE_NETWORK="[ACCOUNT]" \
  TWINGATE_ACCESS_TOKEN="[ACCESS_TOKEN]" \
  TWINGATE_REFRESH_TOKEN="[REFRESH_TOKEN]"
```

| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Twingate account name |
| `TWINGATE_ACCESS_TOKEN` | Generated Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Generated Connector refresh token |

**Docker image:** `twingate/connector:1`

**CLI flags:**
- `--environment NAME` — specify Aptible environment (automated method)
- `--app [APP]` — specify Aptible app name
- `--docker-image` — specify Connector Docker image

## Gotchas
- Token generation requires **re-authentication** in Admin Console before copying tokens
- Tokens are only shown once — copy immediately after generation
- For HA, both Connectors must be assigned to the **same** Remote Network
- Peer-to-peer connections should be configured to stay within Fair Use Policy bandwidth limits

## Related Docs
- Twingate CLI setup
- Connector Best Practices
- Peer-to-peer connections support
- Remote Network configuration
- Aptible blog post announcement