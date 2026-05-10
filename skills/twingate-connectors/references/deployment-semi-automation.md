# Deployment Semi-Automation

## Page Title
Deployment Automation (Semi-Automated Connector Deployment)

## Summary
Twingate Connectors run as `linux/amd64` Docker containers and support multiple deployment automation approaches. For non-Terraform workflows, tokens can be retrieved manually from the Admin Console and incorporated into semi-automated pipelines. Each Connector requires unique, non-reusable tokens.

## Key Information
- Full automation available via [Terraform provider](https://www.twingate.com/docs/terraform) or Admin API
- Semi-automated approach uses manually retrieved tokens from Admin Console
- Connector image: `docker.io/twingate/connector:latest` (public Docker Hub)
- Each Connector's tokens are unique and **cannot be reused** across multiple Connectors
- Helm Chart example: https://github.com/Twingate/helm-charts

## Prerequisites
- Twingate Admin Console access
- Docker-compatible environment (linux/amd64)
- Connectors must be provisioned individually via Admin Console or API before deployment

## Configuration Values

| Parameter | Type | Description |
|-----------|------|-------------|
| `TWINGATE_NETWORK` | Env var (fixed) | Account subdomain (e.g., `acme` from `acme.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Env var (per-connector) | Auth token — treat as secret, never commit to source control |
| `TWINGATE_REFRESH_TOKEN` | Env var (per-connector) | Refresh token — treat as secret, never commit to source control |
| `DNS_SERVER` | Env var (optional) | Custom DNS server for resolving Resources; must be reachable from Connector host |
| `--restart=unless-stopped` | Docker flag | Ensures auto-restart; use equivalent in other container runtimes |
| `--name` | Docker flag | Container identifier; recommended to match Admin Console auto-generated name |

**Image reference:**
```
docker.io/twingate/connector:latest
```

## Step-by-Step (Semi-Automated)
1. In Admin Console, create a new Connector using the "Manual" deployment option
2. Capture the generated `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`
3. Store tokens as secrets (vault, CI/CD secret store — never source control)
4. Deploy container using the fixed + connector-specific parameters above
5. Repeat steps 1–4 for each additional Connector (tokens cannot be reused)

## Gotchas
- Tokens are **Connector-specific** — one set per Connector instance, no reuse
- New Connectors must always be provisioned through Admin Console or API first; you cannot clone configs
- `DNS_SERVER` must be network-accessible from the Connector host if pointing to a private resolver
- Use `--restart=unless-stopped` equivalent in non-Docker environments (Kubernetes restartPolicy, etc.)

## Related Docs
- [Terraform Provider](https://www.twingate.com/docs/terraform)
- [Admin API](https://www.twingate.com/docs/api)
- [Helm Charts (GitHub)](https://github.com/Twingate/helm-charts)