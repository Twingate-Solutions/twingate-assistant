# Upgrading Twingate Connectors

## Summary
Twingate releases Connector updates approximately monthly for CVE patches, performance improvements, and new features. The Controller enforces a minimum supported version and rejects Connectors below that threshold. Update procedures vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Release cadence: ~monthly
- Controller enforces minimum version; non-compliant Connectors cannot broker connections
- Current minimum supported version listed in the [Connector changelog](https://twingate.com/changelog/connector)
- Admin Console shows upgrade indicators for outdated Connectors
- Kubernetes Operator automates updates; Docker/systemd require manual updates

## Prerequisites
- At least 2 Connectors deployed per Remote network (required for zero-downtime updates)
- Existing access and refresh tokens for each Connector (must be retained during upgrade)

## Step-by-Step (General Process)
1. Identify outdated Connectors via Admin Console or weekly admin email
2. Update **one Connector at a time** in a redundant pair
3. Temporarily disconnect the Connector being updated
4. Apply update using deployment-specific instructions (Docker / systemd / Helm)
5. Verify Connector reconnects with same tokens
6. Repeat for remaining Connectors

## Configuration Values
| Item | Value |
|------|-------|
| RSS feed | `https://twingate.com/changelog-connectors.rss.xml` |
| Admin email schedule | Weekly, Mondays at 00:00 UTC |
| Kubernetes automation | [Twingate Kubernetes Operator](https://github.com/Twingate/kubernetes-operator) |

## Deployment-Specific Instructions
- **Docker**: See Docker-deployed Connectors docs
- **systemd**: See Systemd-deployed Connectors docs
- **Helm/Kubernetes**: See Helm-deployed Connectors docs or use Kubernetes Operator for automation

## Gotchas
- **Token retention is critical**: If tokens are not preserved during upgrade, new tokens must be provisioned (new Connector identity)
- **Single-Connector networks will have downtime**: Must have 2+ Connectors per Remote network to avoid service interruption during updates
- **Minimum version is enforced server-side**: Outdated Connectors are blocked from brokering connections, not just flagged
- Specific CVEs patched are not always disclosed in release notes
- Skipping multiple releases leaves known CVEs unpatched longer

## Update Notifications
- **Admin Console**: Visual upgrade indicator per Connector
- **Email**: Weekly digest to all admin users (Mondays 00:00 UTC)
- **Changelog**: `twingate.com/changelog/connector`
- **RSS**: `https://twingate.com/changelog-connectors.rss.xml`

## Related Docs
- Connector Changelog
- Twingate Kubernetes Operator (GitHub)
- Docker-deployed Connectors
- Systemd-deployed Connectors
- Helm-deployed Connectors