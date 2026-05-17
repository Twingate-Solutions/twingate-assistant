# Upgrading Twingate Connectors

## Summary
Twingate releases Connector updates approximately monthly for CVE patches, performance improvements, and new features. Connectors below the minimum supported version are rejected by the Controller and cannot broker connections. Updates vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Monthly release cadence; stay on latest version for security compliance
- Controller enforces a **minimum supported version** — Connectors below this threshold cannot broker connections
- Current minimum version listed in the [Connector changelog](https://twingate.com/changelog/connector)
- Admin Console shows upgrade indicator for any outdated Connector
- Kubernetes Operator automates updates; Docker/systemd require manual updates

## Prerequisites
- At least **two Connectors per Remote Network** (required for zero-downtime updates)
- Existing access and refresh tokens for each Connector being updated
- Deployment method identified: Docker, systemd, or Helm/Kubernetes

## Update Best Practices
1. **Update one Connector at a time** in a redundant pair to avoid downtime
2. **Retain the same access and refresh tokens** — tokens uniquely identify each Connector; new tokens require reprovisioning
3. **Don't let Connectors drift** — skipping releases widens CVE exposure window; treat as routine maintenance

## Deployment-Specific Instructions
| Deployment Type | Update Method |
|---|---|
| Docker container | Manual — see Docker update docs |
| Linux systemd service | Manual — see systemd update docs |
| Helm / Kubernetes | Manual or automated via Kubernetes Operator |

## Automated Updates (Kubernetes Only)
- [Twingate Kubernetes Operator](https://github.com/Twingate/kubernetes-operator) periodically checks for new Connector image versions and applies them automatically
- Most hands-off approach for staying current

## Update Notifications
| Channel | Details |
|---|---|
| Admin email | Weekly, Mondays at 00:00 UTC — lists updatable Connectors |
| Admin Console | Inline upgrade indicator per Connector |
| Changelog | `twingate.com/changelog/connector` |
| RSS feed | `https://twingate.com/changelog-connectors.rss.xml` |

## Gotchas
- Twingate does **not** publish specific CVEs patched per release
- No formal EOL policy, but minimum version enforcement effectively makes very old Connectors non-functional
- New tokens must be provisioned in Admin Console if tokens are lost during upgrade
- Docker and systemd deployments have **no automated update mechanism** — manual only

## Related Docs
- Docker-deployed Connectors update guide
- Systemd-deployed Connectors update guide
- Helm-deployed Connectors update guide
- Twingate Kubernetes Operator (GitHub)
- Connector Changelog