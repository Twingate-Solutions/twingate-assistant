# Updating Twingate Connectors

## Summary
Twingate releases Connector updates monthly addressing CVEs, performance improvements, and new features. The Twingate Controller enforces a minimum supported version and will reject Connectors running below that threshold. Update procedures vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Monthly release cadence; specific CVEs patched are not always disclosed
- Controller enforces minimum version — Connectors below threshold cannot broker connections
- Admin Console shows upgrade indicators for outdated Connectors
- Kubernetes Operator automates updates; Docker/systemd require manual updates
- Changelog lists current minimum supported version: `twingate.com/changelog/connector`

## Prerequisites
- At least **two Connectors per Remote Network** for redundancy during updates
- Existing access and refresh tokens for the Connector being updated
- Platform-specific update access (Docker, systemd, or Helm)

## Update Best Practices
1. **Update one Connector at a time** — never update both in a redundant pair simultaneously
2. **Retain same access and refresh tokens** — tokens are the unique identifier; losing them requires reprovisioning
3. **Don't skip releases** — each skipped month widens CVE exposure window; treat as routine maintenance

## Deployment-Specific Instructions

| Deployment Type | Update Method |
|----------------|---------------|
| Docker | Manual — see Docker-deployed Connectors docs |
| systemd (Linux) | Manual — see Systemd-deployed Connectors docs |
| Helm/Kubernetes | Manual or automated via Kubernetes Operator |

## Automated Updates (Kubernetes Only)
- **Twingate Kubernetes Operator** performs scheduled checks for new Connector image versions and applies them automatically
- Repository: GitHub (Twingate Kubernetes Operator)
- No automated update mechanism exists for Docker or systemd deployments

## Update Notifications
| Method | Details |
|--------|---------|
| Admin email | Weekly, Mondays 00:00 UTC; lists all Connectors with available updates |
| Admin Console | Visual upgrade indicator per Connector |
| Changelog | `twingate.com/changelog/connector` |
| RSS feed | `https://twingate.com/changelog-connectors.rss.xml` |

## Gotchas
- Updating a Connector **requires temporary disconnection** — single-Connector networks will have downtime
- New tokens must be provisioned if existing tokens are not preserved during upgrade
- Twingate does not publish formal EOL policy, but the Controller will reject outdated Connectors without warning
- Specific CVEs patched per release are not always disclosed publicly

## Related Docs
- Connector Changelog
- Docker-deployed Connectors (update instructions)
- Systemd-deployed Connectors (update instructions)
- Helm-deployed Connectors (update instructions)
- Twingate Kubernetes Operator