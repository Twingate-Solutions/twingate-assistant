# Deploy a Connector on GCP

## Summary
Covers deployment options for Twingate Connectors on Google Cloud Platform, including Compute Engine (manual and automated), GKE, and IaC methods. Requires outbound internet access from the deployment subnet.

## Key Information
- Multiple deployment paths: Compute Engine (Docker or systemd), GKE (Helm), Terraform/Pulumi/API
- Docker deployment works on any 64-bit Linux distro Docker supports
- systemd service supported on: Ubuntu, Fedora, Debian, CentOS
- Access/refresh tokens are per-Connector and cannot be shared

## Prerequisites
- Subnet with outbound internet access (for image pull + Twingate connectivity)
- Google Cloud CLI (for automated Compute Engine deployment)
- Twingate Admin Console access
- Remote Network already created in Twingate

## Step-by-Step (Automated Compute Engine)
1. Admin Console → Remote Networks → select network → Add Connector
2. Click the new Connector → select **Google Cloud** option
3. Generate tokens (re-authentication required)
4. Fill in GCP environment details and configure optional features
5. Copy and run the launch command in Google Cloud CLI

## Configuration Values
| Item | Detail |
|------|--------|
| GKE deployment | Official Twingate Helm chart |
| IaC options | Terraform, Pulumi, Twingate API |
| systemd update method | Linux package manager or scheduled task |

## Gotchas
- **Cloud NAT `min_ports_per_vm`**: GCP default is tuned for large fleets; may be insufficient in smaller deployments sharing a NAT gateway with high-volume workloads — review and tune this setting
- Tokens are Connector-specific — cannot reuse tokens across multiple Connectors
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- [Best Practices for Connectors](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Kubernetes Best Practices Guide](https://www.twingate.com/docs/kubernetes-best-practices)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-connector-update)
- [Tune NAT configuration (GCP docs)](https://cloud.google.com/nat/docs/tune-nat)
- Terraform / Pulumi / Twingate API deployment guides