# Updating Twingate Connectors

## Summary
Covers best practices and deployment-specific instructions for updating Twingate Connectors. Updates require temporary disconnection, so redundancy and token preservation are critical. Notification emails alert admins weekly when updates are available.

## Key Information
- Connectors run as Docker containers, Kubernetes/Helm deployments, or Linux systemd services
- Multiple Connectors in the same Remote network auto-cluster for load balancing and failover
- Update notifications sent weekly at **00:00 UTC on Mondays** to all admin users
- Notification lists all Connectors eligible for update

## Prerequisites
- Minimum two Connectors deployed per Remote network (for redundancy during updates)
- Access to existing Connector access and refresh tokens
- Admin role to receive update notification emails

## Step-by-Step (General Process)
1. Confirm at least two Connectors exist in the target Remote network
2. Select one Connector to update first
3. Preserve existing access and refresh tokens before making changes
4. Follow deployment-specific update instructions (Docker / systemd / Helm)
5. Verify Connector reconnects successfully
6. Repeat for remaining Connectors one at a time

## Configuration Values
| Item | Value |
|------|-------|
| Notification schedule | Weekly, Mondays 00:00 UTC |
| Notification recipients | All users with admin role |

## Gotchas
- **Never update all Connectors simultaneously** — causes complete Remote network downtime
- **Token reuse is required** — generating new tokens during update creates a new Connector identity; old tokens become orphaned and must be re-provisioned
- Update process differs by deployment type; use the correct platform-specific guide

## Related Docs
- Docker Connector deployment/update guide
- Systemd Connector deployment/update guide
- Helm Connector deployment/update guide (covers GKE, EKS, MicroK8s)