# Deployment Semi-Automation

## Page Title
Twingate Connector Deployment Automation

## Summary
Twingate Connectors run as `linux/amd64` Docker containers and support multiple deployment automation approaches: Terraform provider (full automation), Admin API (programmatic), or semi-automated manual token generation. Each Connector requires unique tokens that cannot be reused across multiple Connectors.

## Key Information
- Connector image: `docker.io/twingate/connector:latest` (public Docker Hub)
- Tokens are **Connector-specific** — one set per Connector, never reusable
- Three automation options: Terraform provider, Admin API, or manual token + scripted deployment
- Restart policy `--restart=unless-stopped` required (or equivalent in other container runtimes)

## Prerequisites
- Twingate Admin Console access (for manual token generation)
- Or Twingate Admin API access (for programmatic provisioning)
- Docker/container runtime on target host
- New Connector must be provisioned via Admin Console or API before deploying

## Step-by-Step (Semi-Automated Approach)
1. Provision new Connector in Admin Console using "Manual" deployment option
2. Retrieve the generated environment variables (tokens) for that specific Connector
3. Store `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` as secrets (never in source control)
4. Deploy container using Connector-specific variables and fixed parameters below

## Configuration Values

| Parameter | Type | Value/Notes |
|-----------|------|-------------|
| `TWINGATE_NETWORK` | Env var (fixed) | Your account subdomain (e.g., `acme` for `acme.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Env var (per-connector) | Auth token — treat as secret |
| `TWINGATE_REFRESH_TOKEN` | Env var (per-connector) | Refresh token — treat as secret |
| `DNS_SERVER` | Env var (optional) | Private DNS server IP accessible from Connector host |
| `--restart=unless-stopped` | Docker flag | Ensures auto-restart; use equivalent in other runtimes |
| `--name` | Docker flag | Container name; recommend matching Admin Console auto-generated name |
| Image registry | — | `docker.io` |
| Image name | — | `twingate/connector` |
| Image tag | — | `latest` |

## Gotchas
- Connector tokens **cannot be reused** — each new Connector deployment needs its own provisioned tokens
- Must provision Connectors via Admin Console or API first; tokens are generated at provisioning time
- `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` must never be committed to source control
- Private `DNS_SERVER` must be network-accessible from the Connector host

## Related Docs
- [Twingate Terraform Provider](https://www.twingate.com/docs/terraform)
- [Twingate Admin API](https://www.twingate.com/docs/api)
- [Helm Chart Example](https://github.com/Twingate/helm-charts)