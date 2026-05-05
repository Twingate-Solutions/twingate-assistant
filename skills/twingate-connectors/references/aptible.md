# Deploy Twingate Connector on Aptible

## Summary
Deploy Twingate Connectors on Aptible's serverless platform via either the Twingate CLI (automated) or Aptible CLI (manual). Connectors enable secure remote access to Aptible-hosted services. Two Connectors on the same Remote Network provide HA with automatic load balancing and failover.

## Key Information
- Two deployment methods: Twingate CLI (automated) or Aptible CLI (manual)
- HA setup: run deployment twice, selecting the same Remote Network
- Success indicator: two green lights on Connector detail page in Admin Console
- Peer-to-peer connections recommended for performance and Fair Use Policy compliance

## Prerequisites
**Automated:**
- Twingate CLI installed and configured
- Twingate API token with **Read, Write & Provision** permissions
- Aptible CLI installed and configured

**Manual:**
- Aptible CLI installed and configured
- Twingate Admin Console access to generate Connector tokens

## Step-by-Step

### Automated (Twingate CLI)
1. Run `./tg deploy aptible app` (add `--environment NAME` for multiple Aptible environments)
2. Enter Twingate account name and API token when prompted
3. Select existing or create new Remote Network
4. Verify green status indicators in Admin Console

### Manual (Aptible CLI)
1. Create Remote Network in Admin Console → **Network** page
2. Select **Manual** deployment → click **Generate Tokens** → copy both tokens (requires re-auth)
3. Create Aptible app: `aptible apps:create [APP]`
4. Set configuration (see below)
5. Deploy: `aptible deploy --app [APP] --docker-image twingate/connector:1`
6. Verify two green lights in Connector detail page

## Configuration Values

### Environment Variables (set via `aptible config:set`)
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Twingate account name |
| `TWINGATE_ACCESS_TOKEN` | Generated Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Generated Connector refresh token |

### Full Config Command
```bash
aptible config:set --app [APP] \
  TWINGATE_NETWORK="[ACCOUNT]" \
  TWINGATE_ACCESS_TOKEN="[ACCESS_TOKEN]" \
  TWINGATE_REFRESH_TOKEN="[REFRESH_TOKEN]"
```

### Docker Image
```
twingate/connector:1
```

## Gotchas
- Connector tokens are displayed **once**—copy both before leaving the generation screen
- Re-authentication is required during token generation in the Admin Console
- For HA, must explicitly select the **same** Remote Network when running the second deployment
- Tokens generated per Connector; each HA instance needs its own token pair (manual method)

## Related Docs
- Twingate CLI setup
- Connector Best Practices
- Remote Network configuration
- Peer-to-peer connections support
- Fair Use Policy