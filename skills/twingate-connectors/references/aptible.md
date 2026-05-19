# Deploy a Twingate Connector on Aptible

## Summary
Deploy Twingate Connectors on Aptible's serverless platform to provide secure remote access to Aptible services. Two deployment methods are available: automated via Twingate CLI or manual via Aptible CLI.

## Key Information
- Aptible is a serverless platform with built-in security/compliance management
- Peer-to-peer connections recommended for better performance and Fair Use Policy compliance
- For HA setup: deploy two Connectors on the same Remote Network for automatic load balancing and failover

## Prerequisites
- **Automated method:** Twingate CLI installed + configured with Read, Write & Provision API token; Aptible CLI installed and configured
- **Manual method:** Aptible CLI installed and configured; access to Twingate Admin Console

---

## Method 1: Automated (Twingate CLI)

1. Run `./tg deploy aptible app` (add `--environment NAME` for multiple Aptible environments)
2. Enter Twingate account name and API token when prompted
3. Select existing Remote Network or create new one
4. Verify deployment via green status indicators in Admin Console Connector detail page

**HA Setup:** Repeat Step 1, select the same Remote Network — second Connector provisions automatically.

---

## Method 2: Manual (Aptible CLI)

1. Create Remote Network in Twingate Admin Console (Network page)
2. Select **Manual** deployment → click **Generate Tokens** → copy both tokens (requires re-authentication)
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
5. Deploy the app:
   ```bash
   aptible deploy --app [APP] --docker-image twingate/connector:1
   ```
6. Verify via two green lights in Admin Console Connector detail page

---

## Configuration Values

| Parameter | Description |
|---|---|
| `TWINGATE_NETWORK` | Twingate account name |
| `TWINGATE_ACCESS_TOKEN` | Generated connector access token |
| `TWINGATE_REFRESH_TOKEN` | Generated connector refresh token |
| `--docker-image` | `twingate/connector:1` |
| `--environment NAME` | Aptible environment (CLI flag, multi-env only) |

---

## Gotchas
- Tokens are shown **once** — copy immediately after generation; re-authentication is required before tokens are displayed
- Use the same Remote Network when adding a second Connector for HA (not a new network)
- Docker image tag is `1` (not `latest`)

## Related Docs
- Twingate CLI setup
- Connector Best Practices
- Peer-to-peer connections configuration
- Fair Use Policy