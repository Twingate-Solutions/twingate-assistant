# Updating Twingate Connectors

## Summary
Twingate publishes Connector updates ~monthly to patch CVEs, improve performance, and add features. A minimum supported version is enforced by the Controller—Connectors below this threshold cannot broker connections. Updates vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Release cadence: ~monthly
- Controller enforces minimum supported version; non-compliant Connectors are rejected
- Current minimum version listed in [Connector changelog](https://twingate.com/changelog/connector)
- Admin Console shows upgrade indicators for outdated Connectors
- Kubernetes Operator automates updates; Docker/systemd require manual updates

## Prerequisites
- At least **2 Connectors per Remote Network** for zero-downtime upgrades
- Existing access and refresh tokens available before upgrading
- Know your deployment type: Docker, systemd, or Helm/Kubernetes

## Update Best Practices
1. **Update one Connector at a time** in a redundant pair to avoid downtime
2. **Retain the same tokens** during upgrade—tokens uniquely identify a Connector; new tokens require reprovisioning
3. **Don't skip many releases**—each skipped release widens CVE exposure window
4. Treat upgrades as routine maintenance, not a project

## Deployment-Specific Instructions
| Deployment | Update Method |
|---|---|
| Docker | Manual — see Docker-deployed Connectors docs |
| systemd (Linux) | Manual — see Systemd-deployed Connectors docs |
| Helm/Kubernetes | Manual or automated via Kubernetes Operator |

## Automated Updates
- **Kubernetes Operator**: Periodically checks for new Connector image versions and applies them automatically — recommended for K8s deployments
- Operator repo: GitHub (linked from docs)
- Docker and systemd: manual only

## Update Notifications
| Channel | Details |
|---|---|
| Admin email | Weekly, Mondays 00:00 UTC; lists all upgradeable Connectors |
| Admin Console | Upgrade indicator per Connector |
| Changelog | `twingate.com/changelog/connector` |
| RSS | `https://twingate.com/changelog-connectors.rss.xml` |

## Gotchas
- Twingate does **not** publish specific CVE details per release
- No formal EOL policy, but Controller hard-blocks outdated Connectors
- New tokens must be provisioned if old tokens are not preserved during upgrade
- Specific update steps depend on deployment platform—refer to platform-specific docs

## Related Docs
- Twingate Kubernetes Operator (GitHub)
- Docker-deployed Connectors upgrade guide
- Systemd-deployed Connectors upgrade guide
- Helm-deployed Connectors upgrade guide
- Connector changelog: `twingate.com/changelog/connector`