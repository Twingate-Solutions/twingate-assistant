# Deployment Automation (Semi-Automation)

## Summary
Twingate Connectors run as `linux/amd64` Docker containers supporting multiple deployment methods. Tokens generated per-Connector are unique and non-reusable, requiring individual provisioning through the Admin Console or API for semi-automated deployments.

## Key Information
- Full automation available via [Terraform provider](https://www.twingate.com/docs/terraform)
- Programmatic provisioning available via Admin API
- Semi-automated option: manually retrieve tokens from Admin Console per Connector
- Connector image: `docker.io/twingate/connector:latest` (public Docker Hub)

## Prerequisites
- Twingate Admin Console access
- Each Connector must be individually provisioned (tokens cannot be reused across Connectors)

## Configuration Values

| Parameter | Type | Description |
|-----------|------|-------------|
| `TWINGATE_NETWORK` | Env var (fixed) | Account subdomain (e.g., `acme` for `acme.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Env var (per-Connector) | Auth token — treat as secret, never commit to source control |
| `TWINGATE_REFRESH_TOKEN` | Env var (per-Connector) | Auth refresh token — treat as secret |
| `DNS_SERVER` | Env var (optional) | DNS server for resolving Resources; must be reachable from Connector host |
| `--restart=unless-stopped` | Docker flag | Ensures auto-restart; use equivalent in other container runtimes |
| `--name` | Docker flag | Container identifier; recommended to match Admin Console auto-generated name |

**Image reference:** `docker.io/twingate/connector:latest`

## Step-by-Step (Semi-Automated)
1. Provision each Connector individually via Admin Console (Manual deployment option) or Twingate API
2. Retrieve the unique `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` for each Connector
3. Store tokens as secrets (never in source control)
4. Deploy container using the per-Connector environment variables plus the fixed `TWINGATE_NETWORK` value
5. Set restart policy equivalent to `--restart=unless-stopped`

## Gotchas
- **Tokens are per-Connector and non-reusable** — one set of tokens per Connector instance, no exceptions
- New Connectors must always be provisioned through Admin Console or API first before deployment
- `DNS_SERVER` must be network-accessible from the Connector host if specifying a private DNS server
- Use `--restart=unless-stopped` (or equivalent) — omitting this risks Connectors not recovering after host restarts

## Related Docs
- [Terraform Provider](https://www.twingate.com/docs/terraform)
- [Admin API](https://www.twingate.com/docs/api)
- [Helm Chart Example](https://github.com/Twingate/helm-charts)