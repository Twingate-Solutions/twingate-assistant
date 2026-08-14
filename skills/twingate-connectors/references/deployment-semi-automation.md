---
source: https://www.twingate.com/docs/deployment-semi-automation
type: docs
fetched: 2026-08-14
source_version: a541d9458a4662161cec435b7a7c6ecb3af5c2a5d3b2702d2f7a2504ce8cc95b
---

# Deployment Semi-Automation

## Page Title
Twingate Connector Deployment Automation

## Summary
Twingate Connectors run as `linux/amd64` Docker containers supporting multiple deployment automation approaches. Tokens are Connector-specific and cannot be reused, requiring each Connector to be provisioned individually via Admin Console or API. Full automation is available via Terraform provider or Admin API.

## Key Information
- **Full automation**: Use [Terraform provider](https://www.twingate.com/docs/terraform) or Admin API
- **Semi-automation**: Manually retrieve tokens from Admin Console per Connector
- Connector tokens are **unique per Connector** — cannot be reused across multiple Connectors
- Docker image: `docker.io/twingate/connector:latest` (public on Docker Hub)
- Helm chart examples: `https://github.com/Twingate/helm-charts`

## Prerequisites
- Twingate Admin Console access
- Each Connector must be provisioned individually (Console or API) before deploying
- Docker or compatible container runtime

## Configuration Values

### Fixed Parameters (all Connectors)
| Parameter | Value | Notes |
|-----------|-------|-------|
| `TWINGATE_NETWORK` | Your account subdomain | e.g., `acme` for `acme.twingate.com` |
| Docker `--restart` | `unless-stopped` | Use equivalent in non-Docker environments |

### Connector-Specific Parameters (per Connector)
| Parameter | Description | Notes |
|-----------|-------------|-------|
| `TWINGATE_ACCESS_TOKEN` | Auth token for this Connector | **Treat as secret, never commit to source control** |
| `TWINGATE_REFRESH_TOKEN` | Auth refresh token for this Connector | **Treat as secret** |
| `--name` | Container name | Recommended to match Admin Console auto-generated name |

### Optional Parameters
| Parameter | Description |
|-----------|-------------|
| `DNS_SERVER` | Custom DNS server for resolving Resources; must be reachable from Connector host |

## Step-by-Step (Semi-Automated)

1. Provision new Connector in Admin Console (Manual deployment option)
2. Retrieve generated `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`
3. Store tokens as secrets in your secrets manager (never in source control)
4. Deploy container using tokens as environment variables per Connector
5. Repeat steps 1–4 for each additional Connector (tokens cannot be shared)

## Gotchas
- Tokens are **single-use per Connector** — spinning up multiple containers with the same token will cause conflicts
- `DNS_SERVER` must be network-accessible from the Connector host if using private DNS
- Container must have `--restart=unless-stopped` (or equivalent) to survive host reboots
- Connector name (`--name`) is cosmetic but aligning it with the Admin Console name aids troubleshooting

## Related Docs
- [Terraform Provider](https://www.twingate.com/docs/terraform)
- [Admin API](https://www.twingate.com/docs/api)
- [Helm Charts (GitHub)](https://github.com/Twingate/helm-charts)