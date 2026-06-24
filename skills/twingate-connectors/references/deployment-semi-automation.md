# Deployment Semi-Automation

## Page Title
Deployment Automation (Semi-Automated Connector Deployment)

## Summary
Twingate Connectors run as `linux/amd64` Docker containers and support multiple deployment automation approaches: Terraform provider, Admin API, or semi-automated using manually generated tokens from the Admin Console. Each Connector requires unique tokens that cannot be reused across multiple Connectors.

## Key Information
- Full automation options: Terraform provider or Admin API
- Semi-automated approach uses manually generated tokens from Admin Console
- Connector image: `docker.io/twingate/connector:latest` (public Docker Hub)
- Each Connector token pair is unique and non-reusable
- New Connectors must be provisioned via Admin Console or Twingate API each time

## Prerequisites
- Twingate Admin Console access
- Docker environment (or compatible container runtime)
- Connector tokens retrieved per-Connector from Admin Console (Manual deployment option)

## Configuration Values

| Parameter | Type | Description |
|-----------|------|-------------|
| `TWINGATE_NETWORK` | Env var (fixed) | Account subdomain (e.g., `acme` for `acme.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Env var (per-Connector) | Auth token — treat as secret, never commit to source control |
| `TWINGATE_REFRESH_TOKEN` | Env var (per-Connector) | Auth refresh token — treat as secret |
| `DNS_SERVER` | Env var (optional) | DNS server for resolving Resources; must be reachable from Connector host |
| `--restart=unless-stopped` | Docker flag | Ensures auto-restart unless explicitly stopped; use equivalent in other runtimes |
| `--name` | Docker flag | Container identifier; recommended to match Admin Console auto-generated name |

**Image reference:**
```
docker.io/twingate/connector:latest
```

## Step-by-Step (Semi-Automated)
1. In Admin Console, create a new Connector using the "Manual" deployment option
2. Copy the generated `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`
3. Store tokens as secrets in your secrets manager (never in source control)
4. Deploy container using the fixed + Connector-specific parameters above
5. Repeat steps 1–4 for each additional Connector (tokens cannot be reused)

## Gotchas
- Tokens are **Connector-specific** — one set of tokens per Connector, no exceptions
- `--restart=unless-stopped` (or equivalent) is required for reliable operation
- Private `DNS_SERVER` must be network-accessible from the Connector host
- Automating token retrieval requires the Admin API; the semi-automated approach still requires manual Console steps per Connector

## Related Docs
- [Terraform Provider documentation](https://www.twingate.com/docs/terraform)
- [Twingate Admin API](https://www.twingate.com/docs/api)
- [Helm Chart example](https://github.com/Twingate/helm-charts)