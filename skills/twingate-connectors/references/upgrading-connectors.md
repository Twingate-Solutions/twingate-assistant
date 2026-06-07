# Updating Twingate Connectors

## Summary
Twingate releases Connector updates approximately monthly for CVE patches, performance improvements, and new features. The Twingate Controller enforces a minimum supported version and will reject Connectors running below that threshold. Updates vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Monthly release cadence; CVE details not always disclosed publicly
- Controller enforces minimum version — outdated Connectors cannot broker connections
- Admin Console displays upgrade prompts for Connectors with available updates
- Kubernetes Operator automates updates; Docker/systemd require manual updates

## Prerequisites
- At least **two Connectors per Remote Network** (required to avoid downtime during updates)
- Existing access and refresh tokens from the Connector being updated
- Identify deployment type: Docker, systemd, or Helm/Kubernetes

## Update Best Practices
1. **Update one Connector at a time** in a redundant pair to maintain availability
2. **Retain the same tokens** — Connectors are identified by their tokens; new tokens require reprovisioning
3. **Don't skip releases** — gaps increase unpatched CVE exposure window
4. Treat updates as routine maintenance, not a project

## Deployment-Specific Instructions

| Deployment Type | Update Method |
|---|---|
| Docker | Manual — see Docker-deployed Connectors docs |
| systemd (Linux) | Manual — see Systemd-deployed Connectors docs |
| Helm/Kubernetes | Manual or automated via Kubernetes Operator |

## Automated Updates
- **Kubernetes Operator**: Scheduled routine checks for new Connector images and applies automatically
- GitHub: `twingate/kubernetes-operator` repository
- No automation available for Docker or systemd deployments

## Update Notifications
| Channel | Details |
|---|---|
| Admin email | Weekly, Mondays 00:00 UTC; lists all updatable Connectors |
| Admin Console | Inline upgrade indicator per Connector |
| Changelog | `twingate.com/changelog/connector` |
| RSS | `https://twingate.com/changelog-connectors.rss.xml` |

## Gotchas
- Connectors below minimum supported version are **blocked entirely** — they cannot broker any connections
- Using new tokens instead of retained tokens creates a new Connector identity requiring re-provisioning
- Specific CVEs patched are not always publicly disclosed; staying current is the only reliable compliance strategy
- Single-Connector Remote Networks will experience downtime during updates

## Related Docs
- Connector Changelog: `twingate.com/changelog/connector`
- Twingate Kubernetes Operator (GitHub)
- Docker-deployed Connectors update guide
- Systemd-deployed Connectors update guide
- Helm-deployed Connectors update guide