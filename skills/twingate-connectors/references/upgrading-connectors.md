---
source: https://www.twingate.com/docs/upgrading-connectors
type: docs
fetched: 2026-08-14
source_version: ec2a2343e09ce3cd68a22aa4e13b279be2a382e4c96a527531b0c968d64d2947
---

# Updating Connectors

## Summary
Twingate releases Connector updates monthly covering CVE patches, performance improvements, and new features. The Twingate Controller enforces a minimum supported version and will reject Connectors running below that threshold. Update procedures vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Monthly release cadence; stay on latest version for best security/compliance posture
- Controller enforces minimum version — Connectors below threshold cannot broker connections
- Admin Console shows upgrade indicators for outdated Connectors
- Kubernetes Operator automates updates; Docker/systemd require manual updates
- Current minimum supported version listed in the [Connector changelog](https://twingate.com/changelog/connector)

## Prerequisites
- At least **two Connectors per Remote network** (required for zero-downtime updates)
- Access to original Connector tokens (access + refresh tokens)
- Platform-specific access: Docker host, systemd host, or Kubernetes cluster

## Update Best Practices
1. **Update one Connector at a time** in a redundant pair to avoid downtime
2. **Retain the same access and refresh tokens** — tokens uniquely identify each Connector; new tokens require reprovisioning
3. **Don't skip multiple releases** — increases CVE exposure window; treat as routine maintenance

## Deployment-Specific Instructions
- **Docker**: See Docker-deployed Connectors docs
- **systemd**: See Systemd-deployed Connectors docs
- **Helm/Kubernetes**: See Helm-deployed Connectors docs
- **Kubernetes Operator**: Automates version checks and applies updates on a schedule (recommended for K8s)

## Update Notifications
| Method | Details |
|--------|---------|
| Admin email | Weekly at 00:00 UTC Mondays; lists all updatable Connectors |
| Admin Console | Upgrade indicator shown per outdated Connector |
| Changelog | `twingate.com/changelog/connector` |
| RSS feed | `https://twingate.com/changelog-connectors.rss.xml` |

## Gotchas
- Connectors running below minimum supported version are **blocked from brokering connections** (not just warned)
- New tokens must be provisioned if original tokens are lost during upgrade — losing token continuity creates a new Connector identity
- No formal EOL policy published, but minimum version is enforced dynamically by the Controller
- Specific CVEs patched are **not disclosed** in release notes

## Related Docs
- Twingate Kubernetes Operator (GitHub)
- Docker-deployed Connectors update guide
- Systemd-deployed Connectors update guide
- Helm-deployed Connectors update guide
- Connector changelog