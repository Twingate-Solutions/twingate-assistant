# Deployment Semi-Automation

## Page Title
Deployment Automation (Semi-automated Connector Deployment)

## Summary
Twingate Connectors run as `linux/amd64` Docker containers and support multiple deployment automation approaches: Terraform provider, Admin API, or semi-automated using manually retrieved tokens. Connector tokens are unique per Connector and cannot be reused across multiple Connectors.

## Key Information
- **Full automation**: Use [Terraform provider](https://www.twingate.com/docs/terraform) or Admin API
- **Semi-automation**: Retrieve tokens manually from Admin Console, then script the deployment
- Connector image: `docker.io/twingate/connector:latest` (public Docker Hub)
- Each Connector requires its own unique token pair — tokens cannot be shared

## Prerequisites
- Access to Twingate Admin Console or Admin API
- Docker-compatible environment (`linux/amd64`)
- Connector provisioned in Admin Console (generates unique tokens)

## Configuration Values

| Parameter | Type | Description |
|-----------|------|-------------|
| `TWINGATE_NETWORK` | Env var (required) | Account subdomain (e.g., `acme` for `acme.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Env var (required, secret) | Connector-specific auth token |
| `TWINGATE_REFRESH_TOKEN` | Env var (required, secret) | Connector-specific refresh token |
| `DNS_SERVER` | Env var (optional) | Private DNS server for resolving Resources |
| `--restart=unless-stopped` | Docker flag (required) | Ensures auto-restart; use equivalent in other container runtimes |
| `--name` | Docker flag (optional) | Container name; recommend matching Admin Console auto-generated name |

**Image reference:** `docker.io/twingate/connector:latest`

## Step-by-Step (Semi-automated)

1. Provision each Connector in Admin Console using the "Manual" deployment option
2. Retrieve the generated `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` for that Connector
3. Store tokens as secrets (never commit to source control)
4. Deploy container with required env vars and `--restart=unless-stopped`
5. Repeat steps 1–4 for each additional Connector (tokens cannot be reused)

## Gotchas
- **Tokens are Connector-specific** — one set of tokens per Connector, no reuse
- New Connectors must always be provisioned via Admin Console or API before deployment
- `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` must be treated as secrets
- If using a private `DNS_SERVER`, it must be network-accessible from the Connector host
- Always use `--restart=unless-stopped` (or equivalent) to prevent downtime on container restarts

## Related Docs
- [Terraform Provider](https://www.twingate.com/docs/terraform)
- [Admin API](https://www.twingate.com/docs/api)
- [Helm Charts example](https://github.com/Twingate/helm-charts)