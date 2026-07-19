# Deploy a Twingate Connector on Aptible

## Summary
Aptible is a serverless platform with automatic security/compliance management. Twingate Connectors can be deployed on Aptible via two methods: automated (Twingate CLI) or manual (Aptible CLI). Peer-to-peer connections are recommended for better performance and Fair Use Policy compliance.

## Key Information
- Two deployment methods: Twingate CLI (automated) or Aptible CLI (manual)
- HA setup requires running the deploy command twice, selecting the same Remote Network
- Success indicated by green status lights in the Admin Console Connector detail page

## Prerequisites
**Automated:**
- Twingate CLI installed and configured
- API token with **Read, Write & Provision** permissions
- Aptible CLI installed and configured

**Manual:**
- Aptible CLI installed and configured
- Twingate Admin Console access to generate Connector tokens

---

## Step-by-Step

### Automated (Twingate CLI)
1. Run `./tg deploy aptible app` (add `--environment NAME` for multiple Aptible environments)
2. Enter Twingate account name and API token when prompted
3. Select existing Remote Network or create new one
4. Verify green status indicators in Admin Console

**HA Setup:** Re-run step 1, select the same Remote Network — second Connector auto-provisions with load balancing/failover.

### Manual (Aptible CLI)
1. Create Remote Network in Admin Console → **Network** page, select a Connector
2. Choose **Manual** deployment → **Generate Tokens** → copy both tokens (requires re-auth)
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
| `--environment NAME` | (CLI flag) Target Aptible environment |
| `--docker-image` | `twingate/connector:1` |

---

## Gotchas
- Token generation requires **re-authentication** in the Admin Console — copy tokens immediately as they won't be shown again
- Tokens are per-Connector; each HA instance needs its own token set (automated method handles this)
- Replace `[APP]`, `[ACCOUNT]`, `[ACCESS_TOKEN]`, `[REFRESH_TOKEN]` in all commands — brackets are placeholders

---

## Related Docs
- [Twingate CLI](https://www.twingate.com/docs/cli)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)