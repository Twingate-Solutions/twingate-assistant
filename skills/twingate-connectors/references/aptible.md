---
source: https://www.twingate.com/docs/aptible
type: docs
fetched: 2026-08-14
source_version: a26a1d39f033e1adaa90eb49e1e4bbb02de8f8561878d664e6abc97d8e207a0d
---

# Deploy a Twingate Connector on Aptible

## Summary
Aptible is a serverless platform with built-in security/compliance. Twingate Connectors can be deployed on Aptible via two methods: automated (Twingate CLI) or manual (Aptible CLI). Peer-to-peer connections are recommended for bandwidth efficiency.

## Key Information
- Two deployment approaches: Twingate CLI (automated) or Aptible CLI (manual)
- HA setup requires running the automated command twice, selecting the same Remote Network
- Green status indicators in Admin Console confirm successful deployment

## Prerequisites
**Automated method:**
- Twingate CLI installed and configured
- API token with **Read, Write & Provision** permissions
- Aptible CLI installed and configured

**Manual method:**
- Aptible CLI installed and configured
- Twingate Admin Console access to generate Connector tokens

---

## Step-by-Step

### Automated (Twingate CLI)
1. Run `./tg deploy aptible app` (add `--environment NAME` for multiple Aptible environments)
2. Enter Twingate account name and API token when prompted
3. Select existing or create new Remote Network
4. Verify deployment via green status indicators in Admin Console

**HA setup:** Repeat step 1, select the same Remote Network → second Connector auto-provisions with load balancing/failover

---

### Manual (Aptible CLI)
1. Create Remote Network in Admin Console → select a Connector
2. Choose **Manual** deployment → click **Generate Tokens** → copy both tokens (re-auth required)
3. Create Aptible app:
   ```
   aptible apps:create [APP]
   ```
4. Set app configuration:
   ```bash
   aptible config:set --app [APP] \
     TWINGATE_NETWORK="[ACCOUNT]" \
     TWINGATE_ACCESS_TOKEN="[ACCESS_TOKEN]" \
     TWINGATE_REFRESH_TOKEN="[REFRESH_TOKEN]"
   ```
5. Deploy:
   ```bash
   aptible deploy --app [APP] --docker-image twingate/connector:1
   ```
6. Verify two green lights in Admin Console

---

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `TWINGATE_NETWORK` | Twingate account name |
| `TWINGATE_ACCESS_TOKEN` | Generated Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Generated Connector refresh token |
| `--docker-image` | `twingate/connector:1` |
| `--environment NAME` | Aptible environment (CLI flag, multi-env only) |

## Gotchas
- Token generation requires **re-authentication** in the Admin Console — copy tokens immediately, they won't be shown again
- Tokens are one-time-view; losing them requires generating new ones
- HA requires selecting the **exact same Remote Network** on second deployment

## Related Docs
- Twingate CLI setup
- Connector Best Practices
- Peer-to-peer connections / Fair Use Policy
- Remote Network configuration