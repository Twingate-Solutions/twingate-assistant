# Deploy a Connector on GCP

## Summary
Covers multiple methods for deploying Twingate Connectors on Google Cloud Platform, including Compute Engine (manual and automated), GKE, and IaC options. Subnets must have outbound internet access for image downloads and Twingate connectivity.

## Key Information
- Supported deployment methods: Compute Engine (manual/automated), GKE (Helm), Terraform/Pulumi/API
- Docker-based deployment works on any 64-bit Linux Docker supports
- systemd service supported on: Ubuntu, Fedora, Debian, CentOS
- Access/refresh tokens are **per-Connector** — cannot be shared between Connectors
- Updates run via systemd; stagger updates across Connectors to avoid downtime

## Prerequisites
- Subnet with outbound internet access (for container image pull + Twingate connectivity)
- Google Cloud CLI (for automated Compute Engine deployment)
- Twingate Admin Console access with Remote Network configured

## Step-by-Step (Automated Compute Engine)
1. Admin Console → Remote Networks → select network → **Add Connector**
2. Click new Connector → deployment page → select **Google Cloud** option
3. Scroll to step 2 → generate tokens (requires re-authentication)
4. Scroll to step 3 → fill in GCP environment details + configure optional features
5. Scroll to step 5 → copy and run the launch command in Google Cloud CLI

## Configuration Values
| Setting | Notes |
|---|---|
| `min_ports_per_vm` | Cloud NAT setting — may need tuning in small deployments sharing NAT with high-volume services |

## Gotchas
- **Cloud NAT port allocation**: GCP's default `min_ports_per_vm` is tuned for large fleets; smaller deployments sharing NAT with analytics/batch workloads may hit limits — review and tune
- Tokens generated during setup are Connector-specific; generating new tokens requires re-authentication
- Peer-to-peer connections should be enabled to improve performance and comply with Fair Use bandwidth policy

## Related Docs
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices) (includes GCP hardware recommendations)
- [GKE Helm Chart](https://www.twingate.com/docs/kubernetes)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Terraform/Pulumi/API Deployment](https://www.twingate.com/docs/deployment-automation)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-connector-update)
- GCP Docs: [Tune NAT configuration](https://cloud.google.com/nat/docs/tune-nat)