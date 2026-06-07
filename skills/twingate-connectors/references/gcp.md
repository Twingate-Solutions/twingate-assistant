# Deploy a Connector on GCP

## Summary
Covers deployment options for Twingate Connectors on Google Cloud Platform, including Compute Engine (manual and automated), GKE, and IaC methods. Subnet must have outbound internet access for image downloads and Twingate connectivity.

## Key Information
- Multiple deployment paths: Compute Engine (manual/automated), GKE (Helm), IaC (Terraform/Pulumi/API)
- Docker-based deployment works on any 64-bit Linux Docker supports
- systemd service supported on Ubuntu, Fedora, Debian, CentOS
- Access/refresh tokens are Connector-specific — cannot be shared between Connectors

## Prerequisites
- Subnet with outbound internet access
- Google Cloud CLI (for automated Compute Engine deployment)
- Twingate Admin Console access
- Remote Network already created in Twingate

## Step-by-Step: Automated Compute Engine Deployment
1. Admin Console → Remote Networks → select network → scroll to **Add Connector**
2. Click new Connector → deployment page → select **Google Cloud** option
3. Generate tokens (requires re-authentication)
4. Fill in GCP environment details and configure optional features
5. Copy generated launch command → run in Google Cloud CLI

## Configuration Values
| Setting | Notes |
|---|---|
| `min_ports_per_vm` | Cloud NAT setting — may need tuning if sharing NAT with high-volume workloads |
| Access token | Per-Connector, generated in Admin Console |
| Refresh token | Per-Connector, generated in Admin Console |

## Gotchas
- **Cloud NAT port allocation**: GCP default `min_ports_per_vm` is tuned for large fleets; may be insufficient in smaller deployments sharing NAT with analytics/batch workloads
- Tokens generated during setup are unique per Connector — cannot reuse across multiple Connectors
- Peer-to-peer connections required to stay within Fair Use Policy for bandwidth

## Updates
- Connectors run as systemd service on GCP
- Update manually via Linux package manager or automate with a scheduled task
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Helm Chart (GKE)](https://www.twingate.com/docs/kubernetes)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Terraform/Pulumi/API Deployment](https://www.twingate.com/docs/automation)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-connector-update)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [GCP Tune NAT Configuration](https://cloud.google.com/nat/docs/tune-nat-configuration)