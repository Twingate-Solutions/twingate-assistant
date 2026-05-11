# Updating Twingate Connectors

## Summary
Connectors can be deployed via Docker, Kubernetes (Helm), or Linux systemd, each with its own update process. Core principles apply across all platforms: update one at a time and preserve authentication tokens. Weekly email notifications alert admins when updates are available.

## Key Information
- Updates require temporary disconnection of the Connector
- Multiple Connectors in the same Remote network auto-cluster for load balancing and failover
- Admin users receive weekly update notification emails every Monday at 00:00 UTC
- Notifications list all Connectors eligible for update

## Prerequisites
- Minimum two Connectors deployed per Remote network (for redundancy during updates)
- Admin access to receive update notifications
- Existing access and refresh tokens for the Connector being updated

## Best Practices

### Update One at a Time
- Never update all Connectors in a Remote network simultaneously
- Keep at least one Connector online during updates to maintain user access

### Preserve Tokens
- Each Connector has unique access and refresh tokens
- **Must retain the same tokens** during update — using new tokens creates a new Connector identity and requires re-provisioning

## Deployment-Specific Instructions
Update procedures differ by deployment type:
- **Docker**: See Docker-deployed Connectors guide
- **Systemd**: See Systemd-deployed Connectors guide
- **Helm/Kubernetes** (GKE, EKS, MicroK8s): See Helm-deployed Connectors guide

## Update Notifications
- **Trigger**: Any Connector in the environment has an available update
- **Recipients**: All users with admin role
- **Frequency**: Weekly
- **Schedule**: Mondays at 00:00 UTC
- **Content**: List of Connectors that can be updated

## Gotchas
- Replacing tokens during update = new Connector identity; old identity is orphaned in Twingate config
- Single-Connector Remote networks will experience downtime during updates — always deploy pairs
- Update process is not automated; must be performed manually per deployment type

## Related Docs
- Docker Connector deployment
- Systemd Connector deployment
- Helm Chart deployment (Kubernetes/GKE/EKS/MicroK8s)
- Remote Networks configuration