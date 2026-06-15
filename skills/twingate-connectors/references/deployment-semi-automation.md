# Deployment Semi-Automation

## Page Title
Twingate Connector Deployment Automation

## Summary
Twingate Connectors run as `linux/amd64` Docker containers supporting multiple deployment automation approaches. Full automation is available via Terraform provider or Admin API; semi-automated deployment uses manually generated tokens from the Admin Console. Tokens are connector-specific and cannot be reused.

## Key Information
- Connectors hosted on Docker Hub: `docker.io/twingate/connector:latest`
- Three deployment approaches: Terraform (full), Admin API (programmatic), Manual tokens (semi-automated)
- Each Connector requires unique tokens — no reuse across multiple Connectors
- Helm Chart example available at [github.com/Twingate/helm-charts](https://github.com/Twingate/helm-charts)

## Prerequisites
- Access to Twingate Admin Console or Admin API
- Docker-compatible container environment
- For semi-automated: manually provision each Connector via Admin Console to obtain tokens

## Configuration Values

| Parameter | Type | Description |
|-----------|------|-------------|
| `TWINGATE_NETWORK` | Required env var | Account subdomain (e.g., `acme` for `acme.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Required env var | Connector-specific auth token. **Treat as secret.** |
| `TWINGATE_REFRESH_TOKEN` | Required env var | Connector-specific refresh token. **Treat as secret.** |
| `DNS_SERVER` | Optional env var | Private DNS server for resolving Resources; must be reachable from Connector host |
| `--restart=unless-stopped` | Docker flag | Ensures auto-restart unless explicitly stopped |
| `--name` | Docker flag | Container identifier; recommended to match Admin Console name |

## Step-by-Step (Semi-Automated)
1. Provision new Connector in Admin Console using "Manual" deployment option
2. Copy generated `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`
3. Store tokens as secrets (never commit to source control)
4. Deploy container using fixed params + connector-specific tokens
5. Repeat for each additional Connector (tokens cannot be reused)

## Gotchas
- **Token uniqueness**: Each Connector requires its own token pair — bulk/template deployments must provision a new Connector per instance
- **Secret handling**: `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` must never be stored in source control
- **Restart policy**: Always set `--restart=unless-stopped` (or equivalent) to prevent Connector downtime
- **Private DNS**: If `DNS_SERVER` points to a private resolver, network connectivity from the Connector host to that DNS server is required

## Related Docs
- [Terraform Provider documentation](https://www.twingate.com/docs/terraform)
- [Admin API](https://www.twingate.com/docs/api)
- [Helm Charts (GitHub)](https://github.com/Twingate/helm-charts)