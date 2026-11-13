---
source: https://www.twingate.com/docs/upgrading-connectors
type: docs
fetched: 2026-11-13
source_version: f3c5fc3565ab1578269a758a3c0676f9e6f8201ac4fc57f61c71da1190597848
trust: official
---

# Page Title
Updating Connectors (Twingate Docs)

## Summary
Twingate releases Connector updates roughly monthly, covering CVE fixes, reliability and performance improvements, and new features. The page covers update cadence, the Controller's minimum supported version, best practices, and notification channels. Per-platform update steps (Docker, systemd, Helm) are on linked sub-pages.

## Key Information
- Release cadence: about monthly. Each release is validated against multiple vulnerability scanners.
- Twingate can't always disclose which specific CVEs a release patches. The recommended approach is to stay on the latest version.
- There is no formal end-of-life policy per version. However, the **Controller enforces a minimum supported version**. Connectors below it are rejected and can't broker connections.
- The current minimum version is listed in the Connector changelog.
- Deployment types: Docker container, Kubernetes via Helm chart (GKE, EKS, MicroK8s), Linux systemd service.
- Kubernetes users can use the **Twingate Kubernetes Operator**, which periodically checks for new Connector image versions and applies them automatically.
- Docker and systemd updates are manual.

## Prerequisites
- At least two Connectors per Remote Network, for redundancy during updates.
- Access to the original access and refresh tokens for each Connector.

## Step-by-Step (general principles)
1. Check the Admin Console for the upgrade indicator, or check the changelog for the latest version.
2. Pick one Connector in a redundant pair and update it using the platform-specific instructions (Docker, systemd, or Helm).
3. Keep the same access and refresh tokens during the update.
4. Verify the Connector reconnects and shows online.
5. Repeat for the next Connector.

(Platform-specific commands are not on this page. Follow the linked Docker, systemd, and Helm guides.)

## Configuration Values
- Access token and refresh token: unique per Connector, must be retained across upgrades. Otherwise new tokens must be provisioned.
- No env vars or CLI flags are listed on this page.

## Gotchas
- Updating a Connector means briefly disconnecting it. With only one Connector in a Remote Network, users will lose access.
- Don't update all Connectors in a Remote Network at once.
- Losing the tokens means provisioning new ones.
- Falling several releases behind makes the upgrade larger and leaves known CVEs unpatched longer.
- Connectors below the minimum supported version stop working until upgraded.

## Update Notifications
- **Admin email:** weekly, Mondays at 00:00 UTC, sent to all admins and listing Connectors with available updates.
- **Admin Console:** upgrade indicator on each outdated Connector.
- **Changelog:** twingate.com/changelog/connector
- **RSS:** https://twingate.com/changelog-connectors.rss.xml

## Related Docs
- Connector changelog (minimum supported version)
- Docker, systemd, and Helm Connector update guides
- Twingate Kubernetes Operator (GitHub repository)