# Deployment Automation (Semi-Automation)

## Summary
Twingate Connectors run as `linux/amd64` Docker containers and support multiple deployment automation approaches. Tokens are Connector-specific and cannot be reused, requiring new provisioning per Connector via Admin Console or API.

## Key Information
- Full automation available via [Terraform provider](https://www.twingate.com/docs/terraform)
- Programmatic provisioning via Admin API
- Semi-automated deployments require unique tokens per Connector
- Docker image hosted publicly on Docker Hub: `docker.io/twingate/connector:latest`

## Prerequisites
- Twingate Admin Console access or Admin API credentials
- Docker or compatible container runtime
- Each Connector must be provisioned individually (no token reuse)

## Step-by-Step (Semi-Automated)
1. Provision each Connector via Admin Console (Manual deployment option) or Twingate API
2. Retrieve unique tokens generated for that specific Connector
3. Deploy container using Connector-specific environment variables
4. Apply `--restart=unless-stopped` (or equivalent) to ensure auto-restart

## Configuration Values

### Fixed Parameters
| Variable | Description | Example |
|----------|-------------|---------|
| `TWINGATE_NETWORK` | Account subdomain | `acme` (for `acme.twingate.com`) |

### Connector-Specific Parameters (treat as secrets)
| Variable | Description |
|----------|-------------|
| `TWINGATE_ACCESS_TOKEN` | Auth token unique to this Connector — never commit to source control |
| `TWINGATE_REFRESH_TOKEN` | Auth refresh token unique to this Connector — never commit to source control |

### Optional Parameters
| Variable | Description |
|----------|-------------|
| `DNS_SERVER` | Private DNS server for resolving Resources; must be reachable from Connector host |

### Docker-Specific Flags
| Flag | Purpose |
|------|---------|
| `--restart=unless-stopped` | Auto-restart unless explicitly stopped |
| `--name` | Container identifier; recommend matching Admin Console auto-generated name |

### Image Reference
```
docker.io/twingate/connector:latest
```

## Gotchas
- **Tokens are not reusable** — each Connector requires its own unique `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`
- Tokens must be provisioned before deployment; cannot batch-deploy with shared credentials
- `DNS_SERVER` must be network-accessible from the Connector host if using private DNS
- Use equivalent of `--restart=unless-stopped` in non-Docker container environments (Kubernetes, ECS, etc.)

## Related Docs
- [Terraform Provider](https://www.twingate.com/docs/terraform)
- [Admin API](https://www.twingate.com/docs/api)
- [Helm Charts Example](https://github.com/Twingate/helm-charts)