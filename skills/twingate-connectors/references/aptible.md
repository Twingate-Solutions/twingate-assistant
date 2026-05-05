## Deploy Connector on Aptible

Two deployment methods for running Twingate Connectors on Aptible (a serverless PaaS platform with built-in security and compliance management).

**Method 1 — Automated (Twingate CLI):**
- Requirements: Twingate CLI with Read/Write/Provision API token; Aptible CLI configured
1. Run: `./tg deploy aptible app` (add `--environment NAME` for specific environment)
2. Enter Twingate account name and API token when prompted
3. Select or create a Remote Network
4. Connector deploys automatically; verify green status in Admin Console
5. For HA: run the command again and select the same Remote Network — a second Connector is provisioned automatically

**Method 2 — Manual (Aptible CLI):**
1. In Twingate Admin Console: create Remote Network → select Connector → Manual deployment → Generate Tokens → copy Access Token and Refresh Token
2. Create Aptible app: `aptible apps:create twingate-connector`
3. Set app config:
   ```
   aptible config:set --app twingate-connector      TWINGATE_NETWORK="<account>"      TWINGATE_ACCESS_TOKEN="<token>"      TWINGATE_REFRESH_TOKEN="<token>"
   ```
4. Deploy: `aptible deploy --app twingate-connector --docker-image twingate/connector:1`
5. Verify two green indicators in the Connector detail page in Admin Console

**Related Docs:**
- /docs/connector-deployment -- Full deployment method selection guide
- /docs/connector-placement-best-practices -- General Connector best practices
