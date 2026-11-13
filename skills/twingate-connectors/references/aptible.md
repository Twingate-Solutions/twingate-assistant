---
source: https://www.twingate.com/docs/aptible
type: docs
fetched: 2026-11-13
source_version: a0fac5d077141d16e5acd9fd5c13867278ae7088d587665dd8d0692e6da86e9e
trust: official
---

# How To Deploy A Connector On Aptible

## Summary
Twingate Connectors can be deployed on Aptible, a serverless application platform, to give remote users and engineers secure access to Aptible-hosted services. Deployment can be automated with the Twingate CLI or done manually with the Aptible CLI and a Docker image.

## Key Information
- Two approaches: automated (Twingate CLI) or manual (Aptible CLI).
- Peer-to-peer connections should be enabled to improve user experience and stay within the Fair Use Policy for bandwidth.
- Success is indicated by green status lights (two) on the Connector detail page in the Admin Console.
- High availability: deploy additional Connectors in the same Remote Network. They load balance and fail over automatically.

## Prerequisites
- Aptible CLI installed and configured (both methods).
- Automated method: Twingate CLI installed and configured with a **Read, Write & Provision** API token.
- Manual method: access to the Twingate Admin Console to create a Remote Network and generate tokens.

## Step-by-Step

### Automated (Twingate CLI)
1. Run `./tg deploy aptible app`. Use `--environment NAME` if you have multiple Aptible environments.
2. Enter your Twingate account name and API token when prompted.
3. Select an existing Remote Network or create a new one.
4. Deployment proceeds automatically. Verify green status indicators in the Admin Console.

For HA, re-run the same command and select the same Remote Network.

### Manual
1. In the Admin Console, go to Network, create a new Remote Network, and select a Connector.
2. Choose **Manual** as the deployment method and click **Generate Tokens**. Re-authenticate if prompted, then copy both tokens.
3. Create an Aptible app via the dashboard or `aptible apps:create [APP]` (e.g. `twingate-connector`).
4. Set the config:
   ```
   aptible config:set --app [APP] TWINGATE_NETWORK="[ACCOUNT]" \
   TWINGATE_ACCESS_TOKEN="[ACCESS_TOKEN]" \
   TWINGATE_REFRESH_TOKEN="[REFRESH_TOKEN]"
   ```
5. Deploy:
   ```
   aptible deploy --app [APP] --docker-image twingate/connector:1
   ```
6. Confirm two green lights on the Connector detail page.

## Configuration Values
| Name | Purpose |
|---|---|
| `TWINGATE_NETWORK` | Twingate account/network name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token (from Admin Console) |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token (from Admin Console) |
| `--environment NAME` | Selects the Aptible environment (Twingate CLI) |
| Docker image | `twingate/connector:1` |

## Gotchas
- Token generation requires re-authentication, and tokens must be copied immediately, since they are needed in step 4.
- Replace all bracketed placeholders (`[APP]`, `[ACCOUNT]`, tokens) with actual values.
- The Twingate CLI requires an API token with Read, Write & Provision permissions, not read-only.
- With multiple Aptible environments, specify `--environment` to target the right one.

## Related Docs
- Twingate CLI documentation
- Peer-to-peer connections
- Connector Best Practices
- Fair Use Policy