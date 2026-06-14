# Updating Twingate Connectors

## Page Title
Upgrading Connectors

## Summary
Twingate releases Connector updates ~monthly for CVE patches, performance improvements, and new features. The Twingate Controller enforces a minimum supported version and will reject Connectors running below that threshold. Update procedures vary by deployment type (Docker, systemd, Helm/Kubernetes).

## Key Information
- Monthly release cadence; specific CVEs patched are not always disclosed
- Controller enforces minimum version; outdated Connectors cannot broker connections until upgraded
- Admin Console shows upgrade prompts for any Connector with available updates
- Kubernetes Operator automates updates; Docker/systemd require manual updates

## Prerequisites
- At least two Connectors per Remote Network (required for zero-downtime updates)
- Existing access and refresh tokens for the Connector being updated
- Identify deployment type: Docker, systemd, or Helm/Kubernetes

## Step-by-Step (General Process)
1. Confirm redundant Connector pair exists in the Remote Network
2. Update **one Connector at a time** to maintain availability
3. Retain existing access and refresh tokens during update
4. Follow deployment-specific instructions (Docker / systemd / Helm)
5. Verify updated Connector reconnects before updating the second

## Configuration Values
- RSS feed: `https://twingate.com/changelog-connectors.rss.xml`
- Changelog URL: `twingate.com/changelog/connector`
- Admin notification schedule: Weekly, Mondays at 00:00 UTC

## Gotchas
- **Token loss = new provisioning required**: If tokens are not preserved during upgrade, you must provision new tokens for that Connector
- **Controller rejection**: Connectors below minimum version cannot broker any connections—no graceful degradation
- **Single-Connector networks will have downtime**: Update requires temporary disconnection; always deploy pairs
- **Skipping releases**: Multiple skipped versions widen CVE exposure window and complicate upgrades

## Update Notification Methods
| Method | Details |
|--------|---------|
| Admin email | Weekly, Mondays 00:00 UTC, lists updatable Connectors |
| Admin Console | Inline upgrade indicator per Connector |
| Changelog | Full release history at changelog URL |
| RSS | Feed URL above |

## Related Docs
- [Twingate Kubernetes Operator (GitHub)](https://github.com/Twingate/kubernetes-operator)
- Docker-deployed Connectors (update instructions)
- Systemd-deployed Connectors (update instructions)
- Helm-deployed Connectors (update instructions)
- Connector Changelog (minimum supported version listed here)