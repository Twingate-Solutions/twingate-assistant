# Deploy a Twingate Connector on Aptible

## Summary
Aptible is a serverless platform with automatic security/compliance management. Twingate Connectors can be deployed on Aptible via automated (Twingate CLI) or manual (Aptible CLI) methods to provide secure remote access to Aptible-hosted services.

## Key Information
- Two deployment methods: Twingate CLI (automated) or Aptible CLI (manual)
- HA setup requires running the automated deploy command twice, selecting the same Remote Network
- Peer-to-peer connections recommended for better performance and Fair Use Policy compliance
- Successful deployment indicated by green status lights in Admin Console Connector detail page

## Prerequisites
**Automated method:**
- Twingate CLI installed and configured
- Twingate API token with **Read, Write & Provision** permissions
- Aptible CLI installed and configured

**Manual method:**
- Aptible CLI installed and configured
- Twingate Admin Console access to create Remote Networks and generate tokens

## Step-by-Step

### Automated (Twingate CLI)
1. Run `./tg deploy aptible app` (optionally `--environment NAME` for multiple environments)
2. Enter Twingate account name and API token when prompted
3. Select existing or create new Remote Network
4. Verify green status indicators in Admin Console

**HA setup:** Repeat step 1, select the same Remote Network → second Connector auto-provisions with load balancing/failover

### Manual (Aptible CLI)
1. Create Remote Network in Admin Console → select a Connector
2. Choose **Manual** deployment → click **Generate Tokens** → copy both tokens (requires re-authentication)
3. Create Aptible app: `aptible apps:create [APP]`
4. Set configuration:
```bash
aptible config:set --app [APP] \
  TWINGATE_NETWORK="[ACCOUNT]" \
  TWINGATE_ACCESS_TOKEN="[ACCESS_TOKEN]" \
  TWINGATE_REFRESH_TOKEN="[REFRESH_TOKEN]"
```
5. Deploy: `aptible deploy --app [APP] --docker-image twingate/connector:1`
6. Verify two green lights in Connector detail page

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `TWINGATE_NETWORK` | Twingate account name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token from Admin Console |
| `--docker-image` | `twingate/connector:1` |

## Gotchas
- Connector tokens are shown **only once** during generation — copy them immediately
- Re-authentication is required before tokens can be generated in the manual flow
- Tokens are per-Connector; each HA instance needs its own token set (automated method handles this)

## Related Docs
- Twingate CLI setup
- Connector Best Practices
- Peer-to-peer connections setup
- Remote Network configuration
- Fair Use Policy