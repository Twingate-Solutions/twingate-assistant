# Updating Twingate Connectors

## Summary
Twingate releases Connector updates approximately monthly, covering CVE patches, performance improvements, and new features. Connectors below the minimum supported version are rejected by the Controller and cannot broker connections. Update procedures vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Release cadence: ~monthly
- Controller enforces a minimum supported version — outdated Connectors are blocked entirely
- Current minimum version listed in the [Connector changelog](https://twingate.com/changelog/connector)
- Admin Console shows upgrade indicators for Connectors with available updates
- Kubernetes Operator automates updates; Docker/systemd require manual updates

## Prerequisites
- At least two Connectors per Remote network (required for zero-downtime updates)
- Existing access and refresh tokens for the Connector being upgraded
- Knowledge of deployment type: Docker, systemd, or Helm/Kubernetes

## Update Best Practices
1. **Update one Connector at a time** in a redundant pair to avoid downtime
2. **Retain the same tokens** during upgrade — tokens are the unique Connector identity; new tokens require reprovisioning
3. **Don't skip multiple releases** — increases CVE exposure window and upgrade complexity

## Deployment-Specific Instructions
| Deployment Type | Update Method |
|---|---|
| Docker container | Manual — see Docker-deployed Connectors docs |
| Linux systemd service | Manual — see Systemd-deployed Connectors docs |
| Helm/Kubernetes | Manual or automated via Kubernetes Operator |

## Automated Updates
- **Kubernetes Operator**: Periodically checks for new Connector image versions and applies automatically — recommended for K8s environments
- **GitHub**: [Twingate Kubernetes Operator repository](https://github.com/Twingate/kubernetes-operator)
- Docker and systemd deployments have no automated update mechanism

## Update Notifications
| Method | Details |
|---|---|
| Admin email | Weekly, Mondays at 00:00 UTC; lists all Connectors with available updates |
| Admin Console | Upgrade indicator on outdated Connectors |
| Changelog | `twingate.com/changelog/connector` |
| RSS feed | `https://twingate.com/changelog-connectors.rss.xml` |

## Gotchas
- Specific CVEs patched per release are not always disclosed publicly
- Using new tokens during an upgrade creates a new Connector identity — old one persists as orphan unless removed
- Connectors below the minimum version **cannot broker any connections** — no graceful degradation
- Multiple Connectors in the same Remote network auto-cluster for load balancing/failover (deploy ≥2 per network)

## Related Docs
- Connector Changelog: `twingate.com/changelog/connector`
- Docker-deployed Connectors update guide
- Systemd-deployed Connectors update guide
- Helm-deployed Connectors update guide
- Twingate Kubernetes Operator