# Deploy a Twingate Connector on Aptible

## Summary
Aptible is a serverless platform with built-in security/compliance. Twingate Connectors can be deployed on Aptible via two methods: automated (Twingate CLI) or manual (Aptible CLI). Supports HA deployments with multiple Connectors for load balancing and failover.

## Key Information
- Two deployment methods: Twingate CLI (automated) or Aptible CLI (manual)
- HA setup: run automated deploy command twice, selecting the same Remote Network
- Peer-to-peer connections recommended for better performance and Fair Use Policy compliance
- Docker image used: `twingate/connector:1`

## Prerequisites
**Automated method:**
- Twingate CLI installed and configured
- API token with **Read, Write & Provision** permissions
- Aptible CLI installed and configured

**Manual method:**
- Aptible CLI installed and configured
- Twingate Admin Console access to generate Connector tokens

## Step-by-Step

### Automated (Twingate CLI)
1. Run `./tg deploy aptible app` (optionally `--environment NAME` for multiple Aptible environments)
2. Enter Twingate account name and API token when prompted
3. Select existing or create new Remote Network
4. Verify green status indicators in Admin Console Connector detail page

**HA:** Repeat step 1, select the same Remote Network → second Connector auto-provisions with load balancing/failover.

### Manual (Aptible CLI)
1. Create Remote Network in Admin Console → select a Connector
2. Choose **Manual** deployment → click **Generate Tokens** → re-authenticate → copy both tokens
3. Create Aptible app: `aptible apps:create [APP]`
4. Set configuration (see below)
5. Deploy: `aptible deploy --app [APP] --docker-image twingate/connector:1`
6. Verify two green lights in Admin Console Connector detail page

## Configuration Values

```bash
# Set app configuration
aptible config:set --app [APP] \
  TWINGATE_NETWORK="[ACCOUNT]" \
  TWINGATE_ACCESS_TOKEN="[ACCESS_TOKEN]" \
  TWINGATE_REFRESH_TOKEN="[REFRESH_TOKEN]"
```

| Parameter | Description |
|-----------|-------------|
| `TWINGATE_NETWORK` | Your Twingate account name |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console |

**CLI flags:**
- `--environment NAME` — specify Aptible environment (automated method)
- `--docker-image twingate/connector:1` — Connector Docker image

## Gotchas
- Token generation requires **re-authentication** in the Admin Console before tokens are displayed
- Tokens are shown only once — copy them immediately before leaving the page
- For HA, you must select the **same Remote Network** when running the deploy command a second time

## Related Docs
- Twingate CLI setup
- Remote Networks configuration
- Peer-to-peer connections setup
- Connector Best Practices
- Fair Use Policy