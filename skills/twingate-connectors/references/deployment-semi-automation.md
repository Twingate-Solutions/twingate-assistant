# Deployment Automation (Semi-Automation)

## Summary
Twingate Connectors run as `linux/amd64` Docker containers and support multiple deployment automation levels: full automation via Terraform, programmatic control via Admin API, or semi-automated deployment using manually generated tokens from the Admin Console. Each Connector has unique, non-reusable tokens.

## Key Information
- Connector image: `docker.io/twingate/connector:latest` (public Docker Hub)
- Three automation tiers: Terraform provider, Admin API, manual token + scripted deployment
- Tokens are Connector-specific and **cannot be reused** across multiple Connectors
- New Connectors must be provisioned via Admin Console or API (no workaround for semi-automation)

## Prerequisites
- Twingate account with admin access
- Docker-compatible environment (linux/amd64)
- For semi-automation: manually retrieve tokens per Connector from Admin Console → "Manual" deployment option

## Configuration Values

### Fixed Parameters
| Parameter | Value/Description |
|-----------|-------------------|
| `TWINGATE_NETWORK` | Account subdomain (e.g., `acme` for `acme.twingate.com`) |
| Docker `--restart` | `unless-stopped` (or equivalent in other runtimes) |
| Image registry | `docker.io` |
| Image name | `twingate/connector` |
| Image tag | `latest` |

### Connector-Specific Parameters
| Parameter | Description |
|-----------|-------------|
| `TWINGATE_ACCESS_TOKEN` | Auth token unique to this Connector — **treat as secret, never commit to source control** |
| `TWINGATE_REFRESH_TOKEN` | Auth refresh token unique to this Connector — **treat as secret** |
| `--name` (Docker) | Container name; recommended to match auto-generated name in Admin Console |
| `DNS_SERVER` | *(Optional)* DNS server for resolving Resources; must be reachable from Connector host if private |

## Step-by-Step (Semi-Automated)
1. Log into Admin Console → create a new Connector using "Manual" deployment option
2. Capture generated `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`
3. Store tokens as secrets (e.g., in Vault, AWS Secrets Manager, CI/CD secrets)
4. Deploy container using the per-Connector environment variables
5. Repeat steps 1–4 for each additional Connector

## Gotchas
- Tokens are **single-use per Connector** — cannot template one token set for multiple deployments
- Semi-automation still requires manual provisioning step per Connector (Admin Console or API)
- `DNS_SERVER` private DNS must be network-accessible from the Connector host
- Never store `TWINGATE_ACCESS_TOKEN` or `TWINGATE_REFRESH_TOKEN` in source control

## Related Docs
- [Terraform Provider](https://www.twingate.com/docs/terraform) — full infrastructure-as-code automation
- [Admin API](https://www.twingate.com/docs/api) — programmatic Connector and token provisioning
- [Helm Charts Example](https://github.com/Twingate/helm-charts) — reference implementation for Kubernetes