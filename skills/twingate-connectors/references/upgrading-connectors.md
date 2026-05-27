# Updating Twingate Connectors

## Summary
Twingate releases Connector updates approximately monthly to patch CVEs, improve performance, and add features. The Twingate Controller enforces a minimum supported version and will reject Connectors below that threshold. Update methods vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Release cadence: ~monthly
- Minimum supported version is enforced by the Controller — non-compliant Connectors cannot broker connections
- Current minimum version listed in the [Connector changelog](https://twingate.com/changelog/connector)
- Kubernetes Operator automates updates; Docker/systemd require manual updates
- Admin Console shows upgrade indicators for outdated Connectors

## Prerequisites
- At least **two Connectors per Remote Network** to maintain availability during updates
- Existing Connector access and refresh tokens (must be retained through upgrade)

## Update Best Practices
1. **Update one Connector at a time** in a redundant pair to avoid downtime
2. **Retain the same tokens** — Connectors are identified by their tokens; new tokens require reprovisioning
3. **Stay current** — avoid skipping multiple releases to minimize CVE exposure window

## Deployment-Specific Instructions

| Deployment Type | Update Method |
|----------------|---------------|
| Docker container | Manual — see Docker-deployed Connectors docs |
| systemd (Linux) | Manual — see Systemd-deployed Connectors docs |
| Helm/Kubernetes | Manual or automated via Kubernetes Operator |

## Automated Updates
- **Kubernetes Operator** periodically checks for new Connector image versions and applies them automatically
- Operator repo: GitHub (twingate-kubernetes-operator)
- No automation available for Docker or systemd deployments

## Update Notifications
- **Admin email**: Weekly at 00:00 UTC Mondays listing upgradable Connectors (all admin users)
- **Admin Console**: Visual upgrade indicator per Connector
- **Changelog**: `twingate.com/changelog/connector`
- **RSS feed**: `https://twingate.com/changelog-connectors.rss.xml`

## Gotchas
- Twingate does **not** publish formal EOL dates, but the Controller will hard-block outdated Connectors
- CVE details for specific releases are not always disclosed publicly
- Generating new tokens during upgrade = new Connector identity; old one must be decommissioned
- Skipping releases widens the unpatched CVE window

## Related Docs
- Twingate Kubernetes Operator
- Docker-deployed Connectors
- Systemd-deployed Connectors
- Helm-deployed Connectors
- Connector Changelog