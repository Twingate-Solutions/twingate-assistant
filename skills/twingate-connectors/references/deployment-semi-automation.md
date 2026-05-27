# Deployment Automation (Semi-Automation)

## Summary
Twingate Connectors run as `linux/amd64` Docker containers and support multiple deployment automation approaches: Terraform, Admin API, or semi-automated manual token generation. Connector tokens are unique per Connector instance and cannot be reused across multiple deployments.

## Key Information
- Full automation available via [Terraform provider](https://www.twingate.com/docs/terraform) or Admin API
- Semi-automated approach uses manually retrieved tokens from Admin Console
- Connector image: `docker.io/twingate/connector:latest` (public Docker Hub)
- Each Connector requires its own unique token pair — no token reuse

## Prerequisites
- Twingate Admin Console access
- Connectors must be provisioned via Admin Console or Twingate API (no shortcut)
- Docker or compatible container runtime

## Configuration Values

### Fixed Parameters (all Connectors)
| Parameter | Value | Notes |
|-----------|-------|-------|
| `TWINGATE_NETWORK` | Your account subdomain | e.g., `acme` for `acme.twingate.com` |
| Docker `--restart` | `unless-stopped` | Use equivalent in non-Docker environments |
| Image | `docker.io/twingate/connector:latest` | Public registry |

### Connector-Specific Parameters
| Parameter | Required | Notes |
|-----------|----------|-------|
| `TWINGATE_ACCESS_TOKEN` | Yes | Unique per Connector; treat as secret |
| `TWINGATE_REFRESH_TOKEN` | Yes | Unique per Connector; treat as secret |
| `DNS_SERVER` | No | Private DNS server for Resource resolution; must be reachable from Connector host |
| Docker `--name` | No | Recommend matching Admin Console auto-generated name |

## Step-by-Step (Semi-Automated)
1. Provision a new Connector in Admin Console (Manual deployment option)
2. Copy the generated `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`
3. Store tokens as secrets (never in source control)
4. Deploy container using the environment variables for that specific Connector
5. Repeat per Connector — tokens cannot be shared

## Gotchas
- **Token uniqueness is hard requirement**: One set of tokens per Connector, no exceptions
- **Secrets management**: Both tokens must be treated as secrets — never commit to source control
- **DNS_SERVER** must be network-accessible from the Connector host if using private DNS
- Semi-automated approach still requires manual Admin Console or API action per Connector provisioning

## Related Docs
- [Terraform Provider](https://www.twingate.com/docs/terraform)
- [Admin API](https://www.twingate.com/docs/api)
- [Helm Charts Example](https://github.com/Twingate/helm-charts)