# Deployment Semi-Automation

## Page Title
Twingate Connector Deployment Automation

## Summary
Twingate Connectors run as `linux/amd64` Docker containers and support multiple deployment automation approaches: full automation via Terraform provider, programmatic control via Admin API, or semi-automated deployment using manually generated tokens from the Admin Console. Connector tokens are unique per Connector and cannot be reused.

## Key Information
- Connector image: `docker.io/twingate/connector:latest` (public Docker Hub)
- Three automation tiers: Terraform (full), Admin API (programmatic), Manual tokens (semi-automated)
- Each Connector requires its own unique token pair — tokens cannot be shared across Connectors
- New Connectors must be provisioned via Admin Console or API regardless of deployment method

## Prerequisites
- Twingate account with Admin access
- Docker-compatible environment (linux/amd64)
- Connectors provisioned individually through Admin Console or Admin API before deployment

## Configuration Values

### Fixed Parameters (same across all Connectors)
| Parameter | Description | Example |
|-----------|-------------|---------|
| `TWINGATE_NETWORK` | Account subdomain | `acme` (for `acme.twingate.com`) |
| `--restart=unless-stopped` | Docker restart policy | Required in all container environments |

### Connector-Specific Parameters (unique per Connector)
| Parameter | Description | Notes |
|-----------|-------------|-------|
| `TWINGATE_ACCESS_TOKEN` | Auth token for this Connector | **Treat as secret, never commit to source control** |
| `TWINGATE_REFRESH_TOKEN` | Auth refresh token for this Connector | **Treat as secret** |
| `--name` | Container identifier | Should match Admin Console auto-generated name |

### Optional Parameters
| Parameter | Description |
|-----------|-------------|
| `DNS_SERVER` | Custom DNS for resolving Resources; must be reachable from Connector host |

## Step-by-Step (Semi-Automated)
1. Log into Admin Console → create Connector using "Manual" deployment option
2. Copy the generated `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`
3. Store tokens as secrets (e.g., in a secrets manager, not source control)
4. Deploy container using tokens as environment variables alongside fixed parameters
5. Repeat per Connector — tokens cannot be reused

## Gotchas
- Tokens are **Connector-specific** — deploying multiple Connectors requires repeating the provisioning step for each
- `--restart=unless-stopped` equivalent **must** be configured in non-Docker environments (Kubernetes, ECS, etc.)
- Private `DNS_SERVER` must be network-accessible from the Connector host
- Access/refresh tokens should never be stored in source control

## Related Docs
- [Twingate Terraform Provider](https://www.twingate.com/docs/terraform)
- [Twingate Admin API](https://www.twingate.com/docs/api)
- [Helm Chart Example](https://github.com/Twingate/helm-charts)